---
title: Apache Flink Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Apache Flink Benchmarking
This section walks you through running Apache Flink microbenchmarks on a Google Cloud Axion C4A (Arm64) SUSE VM. You will clone the official Flink-benchmarks repository, build the benchmark suite, explore available tests, and run the Remote Channel Throughput Benchmark, one of the key indicators of Flink’s communication and data-transfer performance.

### Clone the Repository
Clone the official Flink microbenchmarks repository:

```console
cd ~
git clone https://github.com/apache/flink-benchmarks.git
cd flink-benchmarks
```
This repository contains microbenchmarks built using JMH (Java Microbenchmark Harness), widely used for JVM-level performance testing.

### Build the Benchmarks with Maven
Compile the benchmarks and create the executable JAR:

```console
mvn clean package -DskipTests
```
What this does:
  * clean removes previous build artifacts
  * package compiles the code and produces benchmark JARs
  * -DskipTests speeds up the build since unit tests aren’t needed for benchmarking
    
After building, the compiled **benchmarks.jar** files appear under:

```output
flink-benchmarks/target/
```

### Explore the JAR Contents
Verify that benchmarks.jar was generated:

```console
cd target
ls
```
You should see:

```output
benchmark-0.1.jar  classes            generated-test-sources  maven-status         protoc-plugins
benchmarks.jar     generated-sources  maven-archiver          protoc-dependencies  test-classes
```
benchmarks.jar — Contains all Flink microbenchmarks packaged with JMH.

### List Available Benchmarks
View all benchmarks included in the JAR:

```console
java -jar benchmarks.jar -l
```
- `-l` → Lists all benchmarks packaged in the JAR.
- This helps you identify which benchmarks you want to execute on your VM.

### Run Selected Benchmarks
While the Flink benchmarking project includes multiple suites for state backends, windowing, checkpointing, and scheduler performance, in this Learning path you will run the Remote Channel Throughput benchmark to evaluate network and I/O performance.

**Remote Channel Throughput**: This benchmark measures the data transfer rate between remote channels in Flink, helping to evaluate network and I/O performance.

Run the benchmark:
```console
java -jar benchmarks.jar org.apache.flink.benchmark.RemoteChannelThroughputBenchmark.remoteRebalance
```
You should see output similar to:
```output

Result "org.apache.flink.benchmark.RemoteChannelThroughputBenchmark.remoteRebalance":
  10536.511 ±(99.9%) 60.121 ops/ms [Average]
  (min, avg, max) = (10289.593, 10536.511, 10687.736), stdev = 89.987
  CI (99.9%): [10476.390, 10596.633] (assumes normal distribution)

# Run complete. Total time: 00:25:14
Benchmark                                          (mode)   Mode  Cnt      Score     Error   Units
RemoteChannelThroughputBenchmark.remoteRebalance  ALIGNED  thrpt   30  17445.341 ± 153.256  ops/ms
RemoteChannelThroughputBenchmark.remoteRebalance  DEBLOAT  thrpt   30  10536.511 ±  60.121  ops/ms
```

### Flink Benchmark Metrics Explained  

- **Run Count**: Total benchmark iterations executed, higher count improves reliability.  
- **Average Throughput**: Mean operations per second across all iterations.  
- **Standard Deviation**: Variation from average throughput, smaller means more consistent.  
- **Confidence Interval (99.9%)**: Range where the true average throughput lies with 99.9% certainty.  
- **Min Throughput**: The lowest throughput was observed, and it shows worst-case performance.  
- **Max Throughput**: Highest throughput observed, shows best-case performance.

### Benchmark summary on Arm64
Results from the run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE) are summarized below:

| Benchmark                                          | Mode     | Count | Score (ops/ms) | Error (±) | Min       | Max       | Stdev   | CI (99.9%)             | Units  |
|---------------------------------------------------|---------|-------|----------------|-----------|-----------|-----------|---------|------------------------|--------|
| RemoteChannelThroughputBenchmark.remoteRebalance | ALIGNED | 30    | 17445.341      | 153.256   | 10289.593 | 10687.736 | 89.987  | [10476.390, 10596.633] | ops/ms |
| RemoteChannelThroughputBenchmark.remoteRebalance | DEBLOAT | 30    | 10536.511      | 60.121    | 10289.593 | 10687.736 | 89.987  | [10476.390, 10596.633] | ops/ms |

### Apache Flink performance benchmarking observations on Arm64

- Both the ALIGNED mode and DEBLOAT modes demonstrate a strong throughput on the Arm64 VM.  
- The benchmark confirms that the Arm64 architecture efficiently handles Flink's remote channel throughput workloads.  

Overall, Arm64 VMs have shown that they are highly suitable for real-time Flink workloads, especially streaming analytics, ETL pipelines, and JVM-based microbenchmarks.
