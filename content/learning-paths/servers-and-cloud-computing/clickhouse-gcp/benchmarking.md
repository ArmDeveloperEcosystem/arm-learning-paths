---
title: ClickHouse Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


##  ClickHouse Benchmark on GCP SUSE Arm64 VM
ClickHouse provides an official benchmarking utility called **`clickhouse-benchmark`**, which is included **by default** in the ClickHouse installation.
This tool measures **query throughput and latency**.

### Verify the benchmarking tool exists
Confirm that `clickhouse-benchmark` is installed and available on the system before running performance tests.

```console
which clickhouse-benchmark
```
You should see an output similar to:

```output
/usr/bin/clickhouse-benchmark
```

### Prepare benchmark database and table
Create a test database and table structure where sample data will be stored for benchmarking.

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
You should see an output similar to:
```output
Query id: 83485bc4-ad93-4dfc-bafe-c0e2a45c1b34
Ok.
0 rows in set. Elapsed: 0.005 sec.
```

Exit client:

```console
exit;
```
### Load benchmark data
Insert 1 million sample records into the table to simulate a realistic workload for testing query performance.

```sql
clickhouse-client --query "
INSERT INTO bench.hits
SELECT
    now() - number,
    number,
    concat('/page/', toString(number % 100))
FROM numbers(1000000)"
```

This inserts 1 million rows.

**Verify:**

Check that the data load was successful by counting the total number of rows in the table.

```sql
clickhouse-client --query "SELECT count(*) FROM bench.hits"
```

You should see an output similar to:
```output
1000000
```

### Read query benchmark
Measures how fast ClickHouse can scan and count rows using a simple filter, showing basic read performance and low latency.

```sql
clickhouse-benchmark \
  --host localhost \
  --port 9000 \
  --iterations 10 \
  --concurrency 1 \
  --query "SELECT count(*) FROM bench.hits WHERE url LIKE '/page/%'"
```

You should see an output similar to:
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


### Benchmark aggregation query
Test the performance of grouping and aggregation operations, demonstrating analytical query efficiency.

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

You should see an output similar to:
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

### Benchmark concurrent read workload
Run multiple queries at the same time to evaluate how well ClickHouse handles higher user load and parallel processing.

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

You should see an output similar to:
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

### Measuring insert performance
Measures bulk data ingestion speed and write latency under concurrent insert operations.

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

You should see an output similar to:
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
### Benchmark Metrics Explanation

- **QPS (Queries Per Second):** Indicates how many complete queries ClickHouse can execute per second. Higher QPS reflects stronger overall query execution capacity.
- **RPS (Rows Per Second):** Shows the number of rows processed every second. Very high RPS values demonstrate ClickHouse's efficiency in scanning large datasets.
- **MiB/s (Throughput):** Represents data processed per second in mebibytes. High throughput highlights effective CPU, memory, and disk utilization during analytics workloads.
- **Latency Percentiles (p50, p95, p99):** Measure query response times. p50 is the median latency, while p95 and p99 show tail latency under heavier load—critical for understanding performance consistency.
- **Iterations:** Number of times the same query is executed. More iterations improve measurement accuracy and stability.
- **Concurrency:** Number of parallel query clients. Higher concurrency tests ClickHouse's ability to scale under concurrent workloads.
- **Result RPS / Result MiB/s:** Reflects the size and rate of returned query results. Low values are expected for aggregate queries like `COUNT(*)`.
- **Insert Benchmark Metrics:** Write tests measure ingestion speed and stability, where consistent latency indicates reliable bulk insert performance.

### Benchmark summary
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Test Category           | Test Case      | Query / Operation                      | Iterations | Concurrency |   QPS | Rows / sec (RPS) | Throughput (MiB/s) | p50 Latency | p95 Latency | p99 Latency |
| ----------------------- | -------------- | -------------------------------------- | ---------: | ----------: | ----: | ---------------: | -----------------: | ----------: | ----------: | ----------: |
| Read                    | Filtered COUNT | `COUNT(*) WHERE url LIKE '/page/%'`    |         10 |           1 | 63.17 |          63.17 M |             957.83 |        4 ms |        5 ms |        5 ms |
| Read / Aggregate        | GROUP BY       | `GROUP BY url`                         |         10 |           2 | 67.15 |          67.15 M |            1018.25 |        7 ms |        8 ms |        8 ms |
| Read (High Concurrency) | Filtered COUNT | `COUNT(*) WHERE user_id % 10 = 0`      |         20 |           8 | 99.72 |          99.72 M |             760.83 |       29 ms |       63 ms |       78 ms |
| Write                   | Bulk Insert    | `INSERT SELECT … FROM numbers(500000)` |          5 |           4 | 20.94 |          10.47 M |              79.86 |       68 ms |       73 ms |       73 ms |

- **High Read Throughput:** Simple filtered reads and aggregations achieved over **63–67 million rows/sec**, demonstrating strong scan and aggregation performance on Arm64.
- **Scales Under Concurrency:** At higher concurrency (8 clients), the system sustained nearly **100 million rows/sec**, showing efficient parallel execution and CPU utilization.
- **Fast Aggregations:** `GROUP BY` workloads delivered over **1 GiB/s throughput** with low single-digit millisecond latency at moderate concurrency.
- **Stable Write Performance:** Bulk inserts maintained consistent throughput with predictable latency, indicating reliable ingestion performance on C4A Arm cores.
