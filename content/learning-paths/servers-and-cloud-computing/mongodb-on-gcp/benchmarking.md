---
title: MongoDB Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark MongoDB with YCSB

YCSB (Yahoo! Cloud Serving Benchmark) is an open-source tool for evaluating NoSQL databases under various workloads. It simulates operations such as writes, updates, and scans to mimic production traffic.

## Install YCSB from source

Install build tools and clone YCSB, then build the MongoDB binding:

```console
sudo dnf install -y git maven java-11-openjdk-devel
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB
mvn -pl site.ycsb:mongodb-binding -am clean package


## Load initial data 

Load a starter dataset (defaults to 1,000 records) into MongoDB:
```console
./bin/ycsb load mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```

This prepares the database for the performance test.

## Run a mixed workload

Run Workload A (50% reads, 50% updates) and collect metrics:

```console
./bin/ycsb run mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```

**Workload A** is a balanced workload:
- 50% reads
- 50% updates

This simulates common real-world applications like session stores or shopping carts.

Sample output:

```output
[READ], Operations, 534
[READ], AverageLatency(us), 312.96
[READ], MinLatency(us), 156
[READ], MaxLatency(us), 8279
...
[UPDATE], Operations, 466
[UPDATE], AverageLatency(us), 384.45
[UPDATE], MinLatency(us), 186
[UPDATE], MaxLatency(us), 26543
...
[OVERALL], RunTime(ms), 512
[OVERALL], Throughput(ops/sec), 1953.125
```

## Understand YCSB metrics

- **Operations Count**: Total operations performed for each type (for example, READ, UPDATE).
- **Average Latency (us)**: The average time to complete each operation, measured in microseconds.
- **Min Latency / Max Latency (us)**: The fastest and slowest observed times for any single operation of that type.

With YCSB installed and benchmark results captured, you now have a baseline for MongoDB's performance under mixed workloads.

## Benchmark summary on x86_64

To better understand how MongoDB behaves across architectures, YCSB benchmark workloads were run on both an **x86_64 (C3 Standard)** and an **Arm64 (C4A Standard)** virtual machine, each with 4 vCPUs and 16 GB of memory, running RHEL 9.

Results from a c3-standard-4 instance (4 vCPUs, 16 GB RAM) on RHEL 9:

| Operation | Count | Avg Latency (us) | Min Latency (us) | Max Latency (us) | 50th Percentile (us) | 95th Percentile (us) | 99th Percentile (us) |
|-----------|-------|------------------|------------------|------------------|-----------------------|----------------------|-----------------------|
| READ      | 472   | 672.27           | 177              | 56703            | 514                   | 903                  | 1331                  |
| UPDATE    | 528   | 621.27           | 214              | 12855            | 554                   | 971                  | 1224                  |
| CLEANUP   | 1     | 4702             | 4700             | 4703             | 4703                  | 4703                 | 4703                  |

## Benchmark summary on Arm64 (Google Axion C4A):
Results from a c4a-standard-4 instance (4 vCPUs, 16 GB RAM) on RHEL 9:

| Operation | Count | Avg Latency (us) | Min Latency (us) | Max Latency (us) | 50th Percentile (us) | 95th Percentile (us) | 99th Percentile (us) |
|----------|------------------|------------------|------------------|------------------|----------------------|----------------------|----------------------|
| READ      |               534 |           312.96  |               156 |              8279 |                   261 |                   524 |                   758 |
| UPDATE    |               466 |           384.45  |               186 |             26543 |                   296 |                   498 |                   821 |
| CLEANUP   |                 1 |          4138     |              4136 |              4139 |                  4139 |                  4139 |                  4139 |

## Highlights from the C4A Arm VM

- Lower average latencies on Arm: ~313 µs (READ) and ~384 µs (UPDATE).

- Stable p50–p99 latencies indicate consistent performance.

- Occasional max-latency outliers suggest transient spikes common in mixed workloads.

With YCSB built and results captured, you now have a baseline for MongoDB performance on Arm-based Google Axion C4A. You can iterate on dataset size, thread counts, and workloads (A–F) to profile additional scenarios and compare cost-performance across architectures.