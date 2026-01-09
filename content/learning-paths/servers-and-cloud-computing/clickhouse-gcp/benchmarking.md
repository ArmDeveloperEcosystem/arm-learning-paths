---
title: Benchmark ClickHouse on Google Axion processors
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## ClickHouse benchmarking on Axion processors

In this section you'll benchmark query latency on ClickHouse running on Google Axion (Arm64). The goal is to measure repeatable query latency with a focus on p95 latency, using data ingested with the real-time Dataflow pipeline.

## Prepare ClickHouse for Accurate Latency Measurement

### Disable Query Cache
ClickHouse may serve repeated queries from its query cache, which can artificially reduce latency numbers. To ensure that every query is fully executed, the query cache is disabled.

Run this **inside the ClickHouse client**:

```sql
SET use_query_cache = 0;
```
This ensures every query is executed fully and not served from cache.

### Validate dataset size

Ensure enough data is present to produce meaningful latency results by checking the current row count.

```console
SELECT count(*) FROM realtime.logs;
```

The output is similar to:

```output
   ┌─count()─┐
1. │ 5000013 │ -- 5.00 million
   └─────────┘
```

If data volume is low, generate additional rows (optional):

```sql
INSERT INTO realtime.logs
SELECT
    now() - number,
    concat('service-', toString(number % 10)),
    'INFO',
    'benchmark message'
FROM numbers(1000000);
```

The output is similar to:

```output
Query id: 8fcbefab-fa40-4124-8f23-516fca2b8fdd
Ok.
1000000 rows in set. Elapsed: 0.058 sec. Processed 1.00 million rows, 8.00 MB (17.15 million rows/s., 137.20 MB/s.)
Peak memory usage: 106.54 MiB.
```

### Define benchmark queries

These queries represent common real-time analytics patterns:

- Filtered count: service-level analytics
- Time-windowed count: recent activity
- Aggregation by service: grouped analytics

Each query scans and processes millions of rows to stress the execution engine.

**Query 1 – Filtered Count (Service-level analytics)**

```sql
SELECT count(*)
FROM realtime.logs
WHERE service = 'service-5';
```

The output is similar to:
```output
Query id: cfbab386-7168-42ce-a752-2d5146f68b48

   ┌─count()─┐
1. │  350000 │
   └─────────┘
1 row in set. Elapsed: 0.013 sec. Processed 6.00 million rows, 74.50 MB (466.81 million rows/s., 5.80 GB/s.)
Peak memory usage: 3.25 MiB.
```

**Query 2 – Time-windowed Count (Recent activity)**

```sql
SELECT count(*)
FROM realtime.logs
WHERE event_time >= now() - INTERVAL 10 MINUTE;
```

The output is similar to:

```output
Query id: 7654746b-3068-4663-a5c6-6944d9c2d2b9
   ┌─count()─┐
1. │     572 │
   └─────────┘
1 row in set. Elapsed: 0.003 sec.
```

**Query 3 – Aggregation by Service**

```sql
SELECT
    service,
    count(*) AS total
FROM realtime.logs
GROUP BY service
ORDER BY total DESC;
```

The output is similar to:

```output
Query id: c48c0d30-0ef6-4fb9-bbb9-815a509a5f91

    ┌─service────┬──total─┐
 1. │ service-6  │ 350000 │
 2. │ service-1  │ 350000 │
 3. │ service-0  │ 350000 │
 4. │ service-7  │ 350000 │
 5. │ service-3  │ 350000 │
 6. │ service-4  │ 350000 │
 7. │ service-5  │ 350000 │
 8. │ service-2  │ 350000 │
 9. │ service-9  │ 350000 │
10. │ service-8  │ 350000 │
11. │ service-10 │ 250000 │
12. │ service-15 │ 250000 │
13. │ service-16 │ 250000 │
14. │ service-13 │ 250000 │
15. │ service-18 │ 250000 │
16. │ service-17 │ 250000 │
17. │ service-19 │ 250000 │
18. │ service-12 │ 250000 │
19. │ service-11 │ 250000 │
20. │ service-14 │ 250000 │
21. │ api        │     12 │
22. │ local      │      1 │
    └────────────┴────────┘
22 rows in set. Elapsed: 0.011 sec. Processed 6.00 million rows, 74.50 MB (527.10 million rows/s., 6.54 GB/s.)
Peak memory usage: 7.18 MiB.
```

### Run repeatable latency measurements

To calculate reliable latency metrics, execute the same query multiple times (10 iterations) using `clickhouse-client --time`.

```sql
clickhouse-client --time --query "
SELECT count(*)
FROM realtime.logs
WHERE service = 'service-5';
"
```

You should see an output similar to:
```output
350000
0.009
350000
0.009
350000
0.009
350000
0.011
350000
0.010
350000
0.0011
350000
0.009
350000
0.009
350000
0.009
350000
0.011
```
**Each run prints:**

- Query result (row count)
- Execution time (seconds)
- Output has row count + time mixed. We only need the time values.

Edit your file:

```console
vi latency-results.txt
```

Only the latency values are required for statistical analysis. Row counts are removed.

```txt
0.009
0.009
0.009
0.011
0.010
0.011
0.009
0.009
0.009
0.011
```

- Clean input for sorting and percentile calculation.
- Remove 350000 lines if they exist.

**Sort the latency values:**
Latency values are sorted in ascending order to compute percentiles.

```console
sort -n latency-results.txt
```
```output
0.009
0.009
0.009
0.009
0.009
0.009
0.010
0.011
0.011
0.011
```

**Calculate p95 latency (manual):**

The p95 latency represents the value under which 95% of query executions complete.

**Formula:**

```
p95 index = ceil(0.95 × N)
```

For 10 samples:

```
ceil(0.95 × 10) = ceil(9.5) = 10
```

The 10th value in the sorted list is your p95 latency.

**p95 result**

```txt
p95 latency = 0.011 seconds ≈ 11 ms
```

After executing the ClickHouse query 10 times on the GCP Axion (Arm) VM, the observed p95 query latency was ~11 ms, demonstrating consistently low-latency analytical performance on Arm-based infrastructure.

## What you've accomplished

You've successfully completed a comprehensive ClickHouse benchmarking exercise on Google Axion (Arm64) processors. Key results from the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM running SUSE:

- ClickHouse on Google Axion (Arm64) delivered consistently low query latency, even while scanning ~6 million rows per query.
- Across 10 repeat executions, the p95 latency was ~11 ms, indicating stable and predictable performance.
- Disabling the query cache ensured true execution latency, not cache-assisted results.
- Analytical queries sustained 500M+ rows/sec throughput with minimal memory usage.

Throughout this Learning Path, you provisioned an Arm-based VM on Google Cloud, deployed ClickHouse, configured a real-time streaming pipeline with Pub/Sub and Dataflow, and validated end-to-end analytical performance. You can now deploy, optimize, and benchmark ClickHouse workloads on Google Cloud Arm infrastructure.
