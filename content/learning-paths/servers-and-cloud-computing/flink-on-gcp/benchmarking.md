---
title: Benchmark Flink performance
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark Apache Flink performance

This section walks you through running Apache Flink microbenchmarks on a Google Cloud Axion C4A (Arm64) SUSE VM. You will clone the official Flink-benchmarks repository, build the benchmark suite, and run the Remote Channel Throughput Benchmark.

## Clone the repository
Clone the official Flink microbenchmarks repository:

```console
cd ~
git clone https://github.com/apache/flink-benchmarks.git
cd flink-benchmarks
```
This repository contains microbenchmarks built using JMH (Java Microbenchmark Harness), widely used for JVM-level performance testing.

## Build the benchmarks with Maven
Compile the benchmarks and create the executable JAR:

```console
mvn clean package -DskipTests
```
What this does:
  * `clean` removes previous build artifacts
  * `package` compiles the code and produces benchmark JARs
  * -DskipTests speeds up the build since unit tests aren’t needed for benchmarking
    
After building, the compiled benchmarks.jar files appear under:

```output
flink-benchmarks/target/
```

## Explore the JAR contents
Verify that benchmarks.jar was generated:

```console
cd target
ls
```

The output is similar to:

```output
benchmark-0.1.jar  classes            generated-test-sources  maven-status         protoc-plugins
benchmarks.jar     generated-sources  maven-archiver          protoc-dependencies  test-classes
```

`benchmarks.jar` contains all Flink microbenchmarks packaged with JMH.

## List available benchmarks
View all benchmarks included in the JAR:

```console
java -jar benchmarks.jar -l
```
- `-l` → Lists all benchmarks packaged in the JAR.
- This helps you identify which benchmarks you want to execute on your VM.

## Run the Remote Channel Throughput benchmark
While the Flink benchmarking project includes multiple suites for state backends, windowing, checkpointing, and scheduler performance, in this Learning path you will run the Remote Channel Throughput benchmark to evaluate network and I/O performance.

Remote Channel Throughput: This benchmark measures the data transfer rate between remote channels in Flink, helping to evaluate network and I/O performance.

Run the benchmark:
```console
java -jar benchmarks.jar org.apache.flink.benchmark.RemoteChannelThroughputBenchmark.remoteRebalance
```

The output is similar to:

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

## Understand benchmark metrics

The output from the Remote Channel Throughput benchmark includes several statistical measures that help you interpret Flink's performance on Arm64. Understanding these metrics enables you to assess both the average performance and the consistency of results across multiple iterations.

- Run Count: total benchmark iterations executed, higher count improves reliability.  
- Average Throughput: mean operations per second across all iterations.  
- Standard Deviation: variation from average throughput, smaller means more consistent.  
- Confidence Interval (99.9%): range where the true average throughput lies with 99.9% certainty.  
- Min Throughput: the lowest throughput was observed, and it shows worst-case performance.  
- Max Throughput: highest throughput observed, shows best-case performance.

## Benchmark summary for Arm64
Results from the run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE) are summarized below:

| Benchmark                                          | Mode     | Count | Score (ops/ms) | Error (±) | Min       | Max       | Stdev   | CI (99.9%)             | Units  |
|---------------------------------------------------|---------|-------|----------------|-----------|-----------|-----------|---------|------------------------|--------|
| RemoteChannelThroughputBenchmark.remoteRebalance | ALIGNED | 30    | 17445.341      | 153.256   | 10289.593 | 10687.736 | 89.987  | [10476.390, 10596.633] | ops/ms |
| RemoteChannelThroughputBenchmark.remoteRebalance | DEBLOAT | 30    | 10536.511      | 60.121    | 10289.593 | 10687.736 | 89.987  | [10476.390, 10596.633] | ops/ms |

## What you've accomplished and what's next

You've successfully deployed Apache Flink on a Google Axion C4A Arm-based virtual machine, validated its functionality, and measured its performance using JMH-based microbenchmarks.
The benchmark results confirm that Google Axion C4A Arm-based instances deliver strong throughput in both ALIGNED and DEBLOAT modes, demonstrating that Arm64 architecture efficiently handles Flink's remote channel throughput workloads.

Arm64 VMs are highly suitable for real-time Flink workloads, including streaming analytics, ETL pipelines, and JVM-based microbenchmarks. The consistent performance across different modes demonstrates that Arm-based infrastructure can effectively handle Flink's demanding real-time processing requirements.
