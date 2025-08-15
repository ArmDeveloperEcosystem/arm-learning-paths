---
title: MongoDB Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## MongoDB Benchmarking with YCSB (Yahoo! Cloud Serving Benchmark)

**YCSB (Yahoo! Cloud Serving Benchmark)** is an open-source benchmarking tool for evaluating the performance of NoSQL databases under different workloads. It supports operations like read, write, update, and scan to simulate real-world usage patterns.

### Install YCSB (Build from Source)

```console
sudo dnf install -y git maven java-11-openjdk-devel
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB
mvn -pl site.ycsb:mongodb-binding -am clean package
```

### Load Phase – Insert Initial Dataset

This phase inserts documents into MongoDB to simulate a typical workload.

```console
./bin/ycsb load mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```
The core purpose of this phase is to prepare the database with initial records (default: 1,000) for benchmarking.

### Execute Benchmark Workload

This phase performs actual read/write operations and reports performance metrics.
```console
./bin/ycsb run mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```
Workload A (from workloads/workloada) simulates a balanced read/write workload:

- 50% reads
- 50% updates/writes

This is designed to mimic many real-world systems where reads and writes are equally important (e.g., session stores, shopping carts, etc.).
The above command measures latency and throughput of mixed read/write operations.


You should see an output similar to:

```output
Loading workload...
Starting test.
2025-08-06 06:05:50:378 0 sec: 0 operations; est completion in 0 second
mongo client connection created with mongodb://127.0.0.1:27017/ycsb
DBWrapper: report latency for each error is false and specific error codes to track for latency are: []
2025-08-06 06:05:50:874 0 sec: 1000 operations; 1953.12 current ops/sec; [READ: Count=534, Max=8279, Min=156, Avg=312.96, 50=261, 90=436, 99=758, 99.9=8279, 99.99=8279] [CLEANUP: Count=1, Max=4139, Min=4136, Avg=4138, 50=4139, 90=4139, 99=4139, 99.9=4139, 99.99=4139] [UPDATE: Count=466, Max=26543, Min=186, Avg=384.45, 50=296, 90=444, 99=821, 99.9=26543, 99.99=26543]
[OVERALL], RunTime(ms), 512
[OVERALL], Throughput(ops/sec), 1953.125
[TOTAL_GCS_G1_Young_Generation], Count, 2
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 3
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 0.5859375
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 2
[TOTAL_GC_TIME], Time(ms), 3
[TOTAL_GC_TIME_%], Time(%), 0.5859375
[READ], Operations, 534
[READ], AverageLatency(us), 312.96067415730334
[READ], MinLatency(us), 156
[READ], MaxLatency(us), 8279
[READ], 50thPercentileLatency(us), 261
[READ], 95thPercentileLatency(us), 524
[READ], 99thPercentileLatency(us), 758
[READ], Return=OK, 534
[CLEANUP], Operations, 1
[CLEANUP], AverageLatency(us), 4138.0
[CLEANUP], MinLatency(us), 4136
[CLEANUP], MaxLatency(us), 4139
[CLEANUP], 50thPercentileLatency(us), 4139
[CLEANUP], 95thPercentileLatency(us), 4139
[CLEANUP], 99thPercentileLatency(us), 4139
[UPDATE], Operations, 466
[UPDATE], AverageLatency(us), 384.4527896995708
[UPDATE], MinLatency(us), 186
[UPDATE], MaxLatency(us), 26543
[UPDATE], 50thPercentileLatency(us), 296
[UPDATE], 95thPercentileLatency(us), 498
[UPDATE], 99thPercentileLatency(us), 821
[UPDATE], Return=OK, 466
```

### YCSB Operations & Latency Metrics

- **Operations Count**: Total number of operations performed by YCSB for each type.
- **Average Latency (us**):	The average time (in microseconds) it took to complete each operation type.
- **Min Latency (us)**: The fastest (minimum) time observed for any single operation of that type.
- **Max Latency (us)**: The slowest (maximum) time recorded for any single operation of that type.

### Benchmark summary on x86_64:
The following  benchmark results are collected on a c3-standard-4 (4 vCPU, 2 core, 16 GB Memory) x86_64 environment, running RHEL 9.

| Operation | Count | Avg Latency (us) | Min Latency (us) | Max Latency (us) | 50th Percentile (us) | 95th Percentile (us) | 99th Percentile (us) |
|-----------|-------|------------------|------------------|------------------|-----------------------|----------------------|-----------------------|
| READ      | 472   | 672.27           | 177              | 56703            | 514                   | 903                  | 1331                  |
| UPDATE    | 528   | 621.27           | 214              | 12855            | 554                   | 971                  | 1224                  |
| CLEANUP   | 1     | 4702             | 4700             | 4703             | 4703                  | 4703                 | 4703                  |

### Benchmark summary on Arm64:
The following  benchmark results are collected on a c4a-standard-4 (4 vCPU, 16 GB Memory) Arm64 environment, running RHEL 9.

| Operation | Count | Avg Latency (us) | Min Latency (us) | Max Latency (us) | 50th Percentile (us) | 95th Percentile (us) | 99th Percentile (us) |
|----------|------------------|------------------|------------------|------------------|----------------------|----------------------|----------------------|
| READ      |               534 |           312.96  |               156 |              8279 |                   261 |                   524 |                   758 |
| UPDATE    |               466 |           384.45  |               186 |             26543 |                   296 |                   498 |                   821 |
| CLEANUP   |                 1 |          4138     |              4136 |              4139 |                  4139 |                  4139 |                  4139 |

### **Highlights from GCP C4A Arm virtual machine**

- Arm results show low **average latencies**, **READ** at **313 us** and **UPDATE** at **384 us**.
- **50th** to **99th percentile** latencies remain stable, indicating consistent performance.
- **Max latency** spikes (**8279 us READ**, **26543 us UPDAT**E) suggest rare outliers.
