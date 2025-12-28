---
title: Benchmark ClickHouse performance
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare for benchmarking

ClickHouse provides an official benchmarking utility called `clickhouse-benchmark`, which is included in the ClickHouse installation. This tool measures query throughput and latency.


## Run benchmark tests

You can benchmark different aspects of ClickHouse performance, including read queries, aggregations, concurrent workloads, and insert operations.


### Verify the benchmarking tool exists

Confirm that `clickhouse-benchmark` is installed:

```console
which clickhouse-benchmark
```

The output is similar to:

```output
/usr/bin/clickhouse-benchmark
```

### Prepare benchmark database and table

Create a test database and table:

```console
clickhouse client
```

```sql
CREATE DATABASE IF NOT EXISTS bench;
USE bench;

CREATE TABLE IF NOT EXISTS hits
(
  event_time DateTime,
  user_id UInt64,
  url String
)
ENGINE = MergeTree
ORDER BY (event_time, user_id);
```

The output is similar to:
```output
Query id: 83485bc4-ad93-4dfc-bafe-c0e2a45c1b34
Ok.
0 rows in set. Elapsed: 0.005 sec.
```

Exit the client:

```console
exit
```

### Load benchmark data

Insert one million sample records into the table:

```sql
clickhouse-client --query "
INSERT INTO bench.hits
SELECT
  now() - number,
  number,
  concat('/page/', toString(number % 100))
FROM numbers(1000000)"
```

Verify the data load:

```sql
clickhouse-client --query "SELECT count(*) FROM bench.hits"
```

The output is similar to:
```output
1000000
```

### Run read query benchmark

Measure how fast ClickHouse can scan and count rows using a filter:

```sql
clickhouse-benchmark \
  --host localhost \
  --port 9000 \
  --iterations 10 \
  --concurrency 1 \
  --query "SELECT count(*) FROM bench.hits WHERE url LIKE '/page/%'"
```

The output is similar to:
```output
Loaded 1 queries.

Queries executed: 10 (100%).

localhost:9000, queries: 10, QPS: 63.167, RPS: 63167346.434, MiB/s: 957.833, result RPS: 63.167, result MiB/s: 0.000.

0%              0.003 sec.
10%             0.003 sec.
20%             0.003 sec.
30%             0.004 sec.
40%             0.004 sec.
50%             0.004 sec.
60%             0.004 sec.
70%             0.004 sec.
80%             0.004 sec.
90%             0.004 sec.
95%             0.005 sec.
99%             0.005 sec.
99.9%           0.005 sec.
99.99%          0.005 sec.
```

### Run aggregation query benchmark

Test the performance of grouping and aggregation operations:

```sql
clickhouse-benchmark \
  --host localhost \
  --port 9000 \
  --iterations 10 \
  --concurrency 2 \
  --query "
  SELECT
    url,
    count(*) AS total
  FROM bench.hits
  GROUP BY url
  "
```

The output is similar to:
```output
Queries executed: 10 (100%).

localhost:9000, queries: 10, QPS: 67.152, RPS: 67151788.647, MiB/s: 1018.251, result RPS: 6715.179, result MiB/s: 0.153.

0%              0.005 sec.
10%             0.005 sec.
20%             0.005 sec.
30%             0.007 sec.
40%             0.007 sec.
50%             0.007 sec.
60%             0.007 sec.
70%             0.007 sec.
80%             0.007 sec.
90%             0.007 sec.
95%             0.008 sec.
99%             0.008 sec.
99.9%           0.008 sec.
99.99%          0.008 sec.
```

### Run concurrent read workload benchmark

Run multiple queries simultaneously to evaluate how ClickHouse handles higher user load:

```sql
clickhouse-benchmark \
  --host localhost \
  --port 9000 \
  --iterations 20 \
  --concurrency 8 \
  --query "
  SELECT count(*)
  FROM bench.hits
  WHERE user_id % 10 = 0
  "
```

The output is similar to:
```output
Loaded 1 queries.

Queries executed: 20 (100%).

localhost:9000, queries: 20, QPS: 99.723, RPS: 99723096.882, MiB/s: 760.827, result RPS: 99.723, result MiB/s: 0.001.

0%              0.012 sec.
10%             0.012 sec.
20%             0.013 sec.
30%             0.017 sec.
40%             0.020 sec.
50%             0.029 sec.
60%             0.029 sec.
70%             0.038 sec.
80%             0.051 sec.
90%             0.062 sec.
95%             0.063 sec.
99%             0.078 sec.
99.9%           0.078 sec.
99.99%          0.078 sec.
```

### Measure insert performance

Measure bulk data ingestion speed and write latency:

```sql
clickhouse-benchmark \
  --iterations 5 \
  --concurrency 4 \
  --query "
  INSERT INTO bench.hits
  SELECT
    now(),
    rand64(),
    '/benchmark'
  FROM numbers(500000)
  "
```

The output is similar to:
```output
Queries executed: 5 (100%).

localhost:9000, queries: 5, QPS: 20.935, RPS: 10467305.309, MiB/s: 79.859, result RPS: 0.000, result MiB/s: 0.000.

0%              0.060 sec.
10%             0.060 sec.
20%             0.060 sec.
30%             0.060 sec.
40%             0.068 sec.
50%             0.068 sec.
60%             0.068 sec.
70%             0.069 sec.
80%             0.069 sec.
90%             0.073 sec.
95%             0.073 sec.
99%             0.073 sec.
99.9%           0.073 sec.
99.99%          0.073 sec.
```

## Understand benchmark metrics

The benchmarking output includes several key metrics:

- QPS (Queries Per Second): number of complete queries ClickHouse can execute per second. Higher QPS reflects stronger overall query execution capacity.
- RPS (Rows Per Second): number of rows processed every second. Very high RPS values demonstrate ClickHouse's efficiency in scanning large datasets.
- MiB/s (Throughput): data processed per second in mebibytes. High throughput indicates effective CPU, memory, and disk utilization during analytics workloads.
- Latency Percentiles (p50, p95, p99): query response times. p50 is the median latency, while p95 and p99 show tail latency under heavier load, which is critical for understanding performance consistency.
- Iterations: number of times the same query is executed. More iterations improve measurement accuracy and stability.
- Concurrency: number of parallel query clients. Higher concurrency tests ClickHouse's ability to scale under concurrent workloads.
- Result RPS / Result MiB/s: size and rate of returned query results. Low values are expected for aggregate queries like `COUNT(*)`.
- Insert Benchmark Metrics: write tests measure ingestion speed and stability. Consistent latency indicates reliable bulk insert performance.

## Review benchmark results

Results from the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 virtual machine:

| Test Category           | Test Case      | Query / Operation                      | Iterations | Concurrency |   QPS | Rows / sec (RPS) | Throughput (MiB/s) | p50 Latency | p95 Latency | p99 Latency |
| ----------------------- | -------------- | -------------------------------------- | ---------: | ----------: | ----: | ---------------: | -----------------: | ----------: | ----------: | ----------: |
| Read                    | Filtered COUNT | `COUNT(*) WHERE url LIKE '/page/%'`    |         10 |           1 | 63.17 |          63.17 M |             957.83 |        4 ms |        5 ms |        5 ms |
| Read / Aggregate        | GROUP BY       | `GROUP BY url`                         |         10 |           2 | 67.15 |          67.15 M |            1018.25 |        7 ms |        8 ms |        8 ms |
| Read (High Concurrency) | Filtered COUNT | `COUNT(*) WHERE user_id % 10 = 0`      |         20 |           8 | 99.72 |          99.72 M |             760.83 |       29 ms |       63 ms |       78 ms |
| Write                   | Bulk Insert    | `INSERT SELECT … FROM numbers(500000)` |          5 |           4 | 20.94 |          10.47 M |              79.86 |       68 ms |       73 ms |       73 ms |
## Interpret the results

The benchmark results demonstrate strong analytical and ingestion performance on the Arm-based C4A instance:

- High read throughput: filtered reads and aggregations achieved over 63–67 million rows/sec, demonstrating strong scan and aggregation performance on Arm64.
- Scales under concurrency: at higher concurrency (8 clients), the system sustained nearly 100 million rows/sec, showing efficient parallel execution and CPU utilization.
- Fast aggregations: `GROUP BY` workloads delivered over 1 GiB/s throughput with low single-digit millisecond latency at moderate concurrency.
- Stable write performance: bulk inserts maintained consistent throughput with predictable latency, indicating reliable ingestion performance on C4A Arm cores.
