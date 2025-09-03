---
title: MongoDB Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## MongoDB Benchmarking with YCSB (Yahoo! Cloud Serving Benchmark)

**YCSB (Yahoo! Cloud Serving Benchmark)** is an open-source tool for evaluating the performance of NoSQL databases under various workloads. It simulates operations such as reads, writes, updates, and scans to mimic real-world usage patterns.

### Install YCSB (Build from Source)

First, install the required build tools and clone the YCSB repository:

```console
sudo dnf install -y git maven java-11-openjdk-devel
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB
mvn -pl site.ycsb:mongodb-binding -am clean package
```

### Load Phase – Insert Initial Dataset

This phase inserts a set of documents into MongoDB to simulate a typical starting workload. By default, it inserts 1,000 records.

```console
./bin/ycsb load mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```

This prepares the database for the actual performance test.

### Execute Benchmark Workload

Run the actual benchmark with the predefined workload. This command performs mixed read/write operations and collects performance metrics.

```console
./bin/ycsb run mongodb -s \
  -P workloads/workloada \
  -p mongodb.url=mongodb://127.0.0.1:27017/ycsb
```

**Workload A** is a balanced workload:
- 50% reads
- 50% updates

This simulates common real-world applications like session stores or shopping carts.

You’ll see performance output that looks like this:

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

### YCSB Operations & Latency Metrics Explained

- **Operations Count**: Total operations performed for each type (e.g., READ, UPDATE).
- **Average Latency (us)**: The average time to complete each operation, measured in microseconds.
- **Min Latency / Max Latency (us)**: The fastest and slowest observed times for any single operation of that type.

With YCSB installed and benchmark results captured, you now have a baseline for MongoDB's performance under mixed workloads.

### Benchmark summary on x86_64

To better understand how MongoDB behaves across architectures, YCSB benchmark workloads were run on both an **x86_64 (C3 Standard)** and an **Arm64 (C4A Standard)** virtual machine, each with 4 vCPUs and 16 GB of memory, running RHEL 9.

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
- **Max latency** spikes (**8279 us READ**, **26543 us UPDATE**) suggest rare outliers.

This Learning Path walked you through setting up and benchmarking MongoDB on an Arm-based GCP instance, highlighting how to run core operations, validate performance, and interpret benchmarking results with YCSB. Alongside, you explored some performance numbers, showing that Arm is a powerful and cost-efficient alternative for modern data-serving workloads like MongoDB.