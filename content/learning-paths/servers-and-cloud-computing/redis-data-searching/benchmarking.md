---
title: Redis Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Redis Benchmarking by redis-benchmark
The `redis-benchmark` tool is an official performance testing utility for Redis. It helps measure to throughput (requests per second) and latency (response delay) across different workloads.

### Prerequisites
Ensure Redis server is running and accessible:

```console
redis-cli ping
```

If you do not see a "PONG" response, please start redis:

```console
redis-server &
redis-cli ping
```

### Benchmark SET (Write Performance)
The `SET` benchmark helps validate Redis’s ability to handle high insertion rates efficiently on Arm-based servers.

The following command benchmarks data insertion performance:

```console
redis-benchmark -t set -n 100000 -c 50
```
**Explanation:**

- `-t set`: Runs the benchmark only for **SET** operations.  
- `-n 100000`: Performs **100,000 total requests**.  
- `-c 50`: Simulates **50 concurrent clients**.

You should see an output similar to:

```output
====== SET ======
  100000 requests completed in 0.67 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.063 milliseconds (cumulative count 1)
50.000% <= 0.167 milliseconds (cumulative count 54147)
75.000% <= 0.175 milliseconds (cumulative count 94619)
96.875% <= 0.183 milliseconds (cumulative count 98788)
99.219% <= 0.231 milliseconds (cumulative count 99222)
99.609% <= 0.415 milliseconds (cumulative count 99617)
99.805% <= 0.543 milliseconds (cumulative count 99817)
99.902% <= 0.671 milliseconds (cumulative count 99909)
99.951% <= 0.775 milliseconds (cumulative count 99965)
99.976% <= 0.983 milliseconds (cumulative count 99978)
99.988% <= 1.087 milliseconds (cumulative count 99993)
99.994% <= 1.095 milliseconds (cumulative count 100000)
100.000% <= 1.095 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.035% <= 0.103 milliseconds (cumulative count 35)
99.166% <= 0.207 milliseconds (cumulative count 99166)
99.465% <= 0.303 milliseconds (cumulative count 99465)
99.577% <= 0.407 milliseconds (cumulative count 99577)
99.743% <= 0.503 milliseconds (cumulative count 99743)
99.869% <= 0.607 milliseconds (cumulative count 99869)
99.932% <= 0.703 milliseconds (cumulative count 99932)
99.968% <= 0.807 milliseconds (cumulative count 99968)
99.975% <= 0.903 milliseconds (cumulative count 99975)
99.983% <= 1.007 milliseconds (cumulative count 99983)
100.000% <= 1.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 149700.61 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.170     0.056     0.167     0.183     0.191     1.095
```

### Benchmark GET (Read/Search Performance)
Now test data retrieval performance separately.

```console
redis-benchmark -t get -n 100000 -c 50
```
**Explanation:**

- `-t get`: Runs the benchmark only for **GET** operations.  
- `-n 100000`: Executes **100,000 total requests**.  
- `-c 50`: Simulates **50 concurrent clients** performing reads.

You should see an output similar to:

```output
====== GET ======
  100000 requests completed in 0.67 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.055 milliseconds (cumulative count 2)
50.000% <= 0.167 milliseconds (cumulative count 55781)
75.000% <= 0.175 milliseconds (cumulative count 94250)
96.875% <= 0.183 milliseconds (cumulative count 98794)
99.219% <= 0.239 milliseconds (cumulative count 99222)
99.609% <= 0.431 milliseconds (cumulative count 99618)
99.805% <= 0.575 milliseconds (cumulative count 99822)
99.902% <= 0.663 milliseconds (cumulative count 99906)
99.951% <= 0.759 milliseconds (cumulative count 99953)
99.976% <= 0.783 milliseconds (cumulative count 99976)
99.988% <= 0.799 milliseconds (cumulative count 99995)
99.997% <= 0.807 milliseconds (cumulative count 100000)
100.000% <= 0.807 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.034% <= 0.103 milliseconds (cumulative count 34)
99.141% <= 0.207 milliseconds (cumulative count 99141)
99.478% <= 0.303 milliseconds (cumulative count 99478)
99.558% <= 0.407 milliseconds (cumulative count 99558)
99.718% <= 0.503 milliseconds (cumulative count 99718)
99.866% <= 0.607 milliseconds (cumulative count 99866)
99.951% <= 0.703 milliseconds (cumulative count 99951)
100.000% <= 0.807 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 150375.94 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.169     0.048     0.167     0.183     0.191     0.807
```

### Benchmark Metrics Explanation

- **Throughput:** Number of operations (requests) Redis can process per second.
- **Latency:** Latency reflects the time it takes for Redis to complete a single request, measured in milliseconds (ms).  
- **avg:** Average time taken to process a request across the entire test.
- **min:** Fastest observed response time (best case).
- **p50:** Median latency — 50% of requests completed faster than this value.
- **p95:** 95th percentile — 95% of requests completed faster than this value.
- **p99:** 99th percentile — shows near worst-case latency, key for reliability analysis.
- **max:** Slowest observed response time (worst case).

### Benchmark summary
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE Enterprise Server):

| Operation | Total Requests | Concurrent Clients | Avg Latency (ms) | Min (ms) | P50 (ms) | P95 (ms) | P99 (ms) | Max (ms) | Throughput (req/sec) | Description |
|------------|----------------|--------------------|------------------|-----------|-----------|-----------|-----------|-----------|-----------------------|--------------|
| SET        | 100,000        | 50                 | 0.170            | 0.056     | 0.167     | 0.183     | 0.191     | 1.095     | 149,700.61            | Measures Redis write performance using SET command |
| GET        | 100,000        | 50                 | 0.169            | 0.048     | 0.167     | 0.183     | 0.191     | 0.807     | 150,375.94            | Measures Redis read performance using GET command |

 - **High Efficiency:** Redis achieved over **150K ops/sec** on both read and write workloads, showcasing strong throughput on **Arm64 (C4A)** architecture.
- **Low Latency:** Average latency remained around **0.17 ms**, demonstrating consistent response times under concurrency.
- **Balanced Performance:** Both **SET** and **GET** operations showed nearly identical performance, indicating excellent CPU and memory optimization on **Arm64**.
- **Energy-Efficient Compute:** The **Arm-based C4A VM** delivers competitive performance-per-watt efficiency, ideal for scalable, sustainable Redis deployments.
