---
title: Benchmark using Java Microbenchmark Harness
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Measure response construction with JMH

Use Java Microbenchmark Harness (JMH) to measure repeated construction of an HTTP response string on your Cobalt 200 VM. JMH provides warmup, measurement iterations, and separate JVM forks. This example measures in-memory string construction; it does not start Tomcat or measure HTTP server throughput.

JMH is a Java benchmarking framework developed by the JVM team at Oracle to measure the performance of small code snippets with high precision. It accounts for JVM optimizations like JIT and warmup to ensure accurate and reproducible results. You can measure throughput (ops/sec), average execution time, or percentiles for latency. 
## Install Maven

Install Maven to generate and build the benchmark project:

```console
sudo apt update
sudo apt install -y maven
mvn -version
```

## Create a benchmark project

From your VM terminal, create a project with the OpenJDK JMH 1.37 archetype:

```console
mvn archetype:generate \
  -DinteractiveMode=false \
  -DarchetypeGroupId=org.openjdk.jmh \
  -DarchetypeArtifactId=jmh-java-benchmark-archetype \
  -DarchetypeVersion=1.37 \
  -DgroupId=com.example \
  -DartifactId=jmh-benchmark \
  -Dversion=1.0
cd jmh-benchmark
```

The output includes:

```output
[INFO] Project created from Archetype in dir: /home/azureuser/java-cobalt-validation/jmh-benchmark
[INFO] BUILD SUCCESS
[INFO] Total time:  7.405 s
[INFO] Finished at: 2026-11-10T20:13:55Z
```

If you already have a `jmh-benchmark` directory from an earlier run, use a new working directory before generating the project again.

## Define the benchmark

Replace the entire contents of `src/main/java/com/example/MyBenchmark.java` with:

```java
package com.example;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.Param;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;

@State(Scope.Thread)
public class MyBenchmark {
    @Param({"Benchmarking a Tomcat-like operation"})
    public String body;

    @Benchmark
    public String benchmarkHttpResponse() {
        StringBuilder sb = new StringBuilder();
        sb.append("HTTP/1.1 200 OK\r\n");
        sb.append("Content-Type: text/plain\r\n");
        sb.append("Content-Length: ").append(body.length()).append("\r\n\r\n");
        sb.append(body);
        return sb.toString();
    }
}
```

The benchmark returns the response so JMH consumes the result and limits dead-code elimination. The body is a JMH parameter rather than a local constant. See the OpenJDK [dead-code elimination sample](https://github.com/openjdk/jmh/blob/master/jmh-samples/src/main/java/org/openjdk/jmh/samples/JMHSample_08_DeadCode.java) for the reason to return benchmark results.

## Build the benchmark JAR

Build the project:

```console
mvn clean package
```

The output includes:

```output
[INFO] BUILD SUCCESS
[INFO] Total time:  10.919 s
[INFO] Finished at: 2026-11-10T20:14:07Z
```

Confirm that the executable benchmark JAR exists:

```console
ls target/benchmarks.jar
```

The output is:

```output
target/benchmarks.jar
```

## Run the benchmark

Use a single benchmark thread, two JVM forks, three five-second warmup iterations per fork, and three five-second measurement iterations per fork. Fix the forked JVM heap size and save results as JSON:

```console
java -jar target/benchmarks.jar benchmarkHttpResponse \
  -bm thrpt -tu s -t 1 -f 2 -wi 3 -i 3 -w 5s -r 5s \
  -jvmArgs "-Xms256m -Xmx256m" \
  -rf json -rff results.json
```

The run takes about one minute plus JVM startup overhead. The output is similar to the following excerpt:

```output
# JMH version: 1.37
# VM version: JDK 21.0.13.0.3, OpenJDK 64-Bit Server VM, 21.0.13.0.3+1-1-24.04.1-Ubuntu
# VM invoker: /usr/lib/jvm/java-21-openjdk-arm64/bin/java
# VM options: -Xms256m -Xmx256m
# Blackhole mode: compiler (auto-detected, use -Djmh.blackhole.autoDetect=false to disable)
# Warmup: 3 iterations, 5 s each
# Measurement: 3 iterations, 5 s each
# Timeout: 10 min per iteration
# Threads: 1 thread, will synchronize iterations
# Benchmark mode: Throughput, ops/time
# Benchmark: com.example.MyBenchmark.benchmarkHttpResponse
# Parameters: (body = Benchmarking a Tomcat-like operation)

# Run progress: 0.00% complete, ETA 00:01:00
# Fork: 1 of 2
# Warmup Iteration   1: 20753271.619 ops/s
# Warmup Iteration   2: 21280631.634 ops/s
# Warmup Iteration   3: 21518491.639 ops/s
Iteration   1: 21535221.845 ops/s
Iteration   2: 21503000.952 ops/s
Iteration   3: 21550180.005 ops/s

# Run progress: 50.00% complete, ETA 00:00:30
# Fork: 2 of 2
# Warmup Iteration   1: 19908356.298 ops/s
# Warmup Iteration   2: 20051778.703 ops/s
# Warmup Iteration   3: 20298498.049 ops/s
Iteration   1: 20311476.788 ops/s
Iteration   2: 20316584.871 ops/s
Iteration   3: 20288439.476 ops/s


Result "com.example.MyBenchmark.benchmarkHttpResponse":
  20917483.989 ±(99.9%) 1880585.508 ops/s [Average]
  (min, avg, max) = (20288439.476, 20917483.989, 21550180.005), stdev = 670634.908
  CI (99.9%): [19036898.482, 22798069.497] (assumes normal distribution)


# Run complete. Total time: 00:01:00

Benchmark                                                        (body)   Mode  Cnt         Score         Error  Units
MyBenchmark.benchmarkHttpResponse  Benchmarking a Tomcat-like operation  thrpt    6  20917483.989 ± 1880585.508  ops/s

Benchmark result is saved to results.json
```

These results were collected on a **Standard_D4ps_v7** Cobalt 200 VM (4 vCPUs, 16 GiB) in **West US 2**, running **Ubuntu 24.04 LTS** and the OpenJDK version shown above. The benchmark uses one thread; it does not measure throughput across all four vCPUs.

## Interpret the results

- **Mode (`thrpt`)** measures operations per unit of time. Here, one operation constructs and returns one response string.
- **Cnt** is the number of measured iterations across all forks: two forks with three measurements each give six samples.
- **Score** is the mean measured throughput in operations per second.
- **Error** is the half-width of JMH’s reported confidence interval; it is not the standard deviation.
- **Warmup** lets the JVM compile and optimize code before collecting measurements.

Use `results.json` to inspect the per-iteration results and reported uncertainty. Longer measurements and additional forks can help investigate variability, but do not guarantee repeatability.

## Use this baseline

This small, allocation-heavy microbenchmark establishes a baseline for the selected code, JVM, and heap settings. It does not measure web-server capacity, request latency, or production application performance. Results can change with JDK versions, garbage collection, background services, and benchmark design.

For comparisons, keep the code, JDK, JVM flags, JMH settings, and workload consistent. The Arm-based Azure `D4ps_v7` VM provides stable and efficient performance for Java workloads, even in microbenchmark scenarios. These results establish a baseline you can now compare directly against x86_64 instances to evaluate relative performance. 

