---
title: Benchmarking via JMH
weight: 6 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you’ve built and run the Tomcat-like response, you can use it to test the JVM performance using JMH. You can also use it to test the performance difference between Cobalt 100 instances and other similar D series x86_64 based instances.
## Run the performance tests using JMH

JMH (Java Microbenchmark Harness) is a Java benchmarking framework developed by the JVM team at Oracle to measure the performance of small code snippets with high precision. It accounts for JVM optimizations like JIT and warm-up to ensure accurate and reproducible results. It measures the throughput, average latency, or execution time. Below steps help benchmark the Tomcat-like operation:


Install Maven:

```console
sudo apt install maven -y
```
Create Benchmark Project:

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

Edit the `src/main/java/com/example/MyBenchmark.java` file and add the below code on it:

```java
package com.example;

import org.openjdk.jmh.annotations.Benchmark;

public class MyBenchmark {

    @Benchmark
    public void benchmarkHttpResponse() {
        String body = "Benchmarking a Tomcat-like operation";
        StringBuilder sb = new StringBuilder();
        sb.append("HTTP/1.1 200 OK\r\n");
        sb.append("Content-Type: text/plain\r\n");
        sb.append("Content-Length: ").append(body.length()).append("\r\n\r\n");
        sb.append(body);

        // Prevent dead-code elimination
        if (sb.length() == 0) {
            throw new RuntimeException();
        }
    }
}
```
This simulates HTTP response generation similar to Tomcat.

Build the Benchmark:

```console
mvn clean install
```

After the build is complete, the JMH benchmark jar will be in the target/ directory.

Run the Benchmark:

```console
java -jar target/benchmarks.jar
```

You should see an output similar to:
```output
# JMH version: 1.37
# VM version: JDK 21.0.8, OpenJDK 64-Bit Server VM, 21.0.8+9-Ubuntu-0ubuntu124.04.1
# VM invoker: /usr/lib/jvm/java-21-openjdk-arm64/bin/java
# VM options: <none>
# Blackhole mode: compiler (auto-detected, use -Djmh.blackhole.autoDetect=false to disable)
# Warmup: 5 iterations, 10 s each
# Measurement: 5 iterations, 10 s each
# Timeout: 10 min per iteration
# Threads: 1 thread, will synchronize iterations
# Benchmark mode: Throughput, ops/time
# Benchmark: com.example.MyBenchmark.benchmarkHttpResponse

# Run progress: 0.00% complete, ETA 00:08:20
# Fork: 1 of 5
# Warmup Iteration   1: 33509694.060 ops/s
# Warmup Iteration   2: 36783933.354 ops/s
# Warmup Iteration   3: 35202103.615 ops/s
# Warmup Iteration   4: 36493073.361 ops/s
# Warmup Iteration   5: 36470050.153 ops/s
Iteration   1: 35188405.658 ops/s
Iteration   2: 35011856.616 ops/s
Iteration   3: 36282916.441 ops/s
Iteration   4: 34558682.952 ops/s
Iteration   5: 34878375.325 ops/s

# Run progress: 20.00% complete, ETA 00:06:41
# Fork: 2 of 5
# Warmup Iteration   1: 33055148.091 ops/s
# Warmup Iteration   2: 36374390.556 ops/s
# Warmup Iteration   3: 35020852.850 ops/s
# Warmup Iteration   4: 36463924.398 ops/s
# Warmup Iteration   5: 35116009.523 ops/s
Iteration   1: 36604427.854 ops/s
Iteration   2: 35151064.855 ops/s
Iteration   3: 35171529.012 ops/s
Iteration   4: 35092144.416 ops/s
Iteration   5: 36670199.634 ops/s

# Run progress: 40.00% complete, ETA 00:05:00
# Fork: 3 of 5
# Warmup Iteration   1: 34021525.130 ops/s
# Warmup Iteration   2: 35796028.914 ops/s
# Warmup Iteration   3: 36813541.649 ops/s
# Warmup Iteration   4: 34424554.094 ops/s
# Warmup Iteration   5: 35100074.155 ops/s
Iteration   1: 33533209.090 ops/s
Iteration   2: 34755031.947 ops/s
Iteration   3: 36463135.748 ops/s
Iteration   4: 34961009.997 ops/s
Iteration   5: 36496001.612 ops/s

# Run progress: 60.00% complete, ETA 00:03:20
# Fork: 4 of 5
# Warmup Iteration   1: 33393091.940 ops/s
# Warmup Iteration   2: 35235407.288 ops/s
# Warmup Iteration   3: 36203077.665 ops/s
# Warmup Iteration   4: 34580888.238 ops/s
# Warmup Iteration   5: 35984836.776 ops/s
Iteration   1: 34896194.779 ops/s
Iteration   2: 36479405.215 ops/s
Iteration   3: 35010049.135 ops/s
Iteration   4: 36277296.075 ops/s
Iteration   5: 36340953.266 ops/s

# Run progress: 80.00% complete, ETA 00:01:40
# Fork: 5 of 5
# Warmup Iteration   1: 35482444.435 ops/s
# Warmup Iteration   2: 37116032.766 ops/s
# Warmup Iteration   3: 35389871.716 ops/s
# Warmup Iteration   4: 36814888.849 ops/s
# Warmup Iteration   5: 35462220.484 ops/s
Iteration   1: 36896452.473 ops/s
Iteration   2: 35362724.405 ops/s
Iteration   3: 36992383.389 ops/s
Iteration   4: 35535471.437 ops/s
Iteration   5: 36881529.760 ops/s


Result "com.example.MyBenchmark.benchmarkHttpResponse":
  35659618.044 ±(99.9%) 686946.011 ops/s [Average]
  (min, avg, max) = (33533209.090, 35659618.044, 36992383.389), stdev = 917053.272
  CI (99.9%): [34972672.032, 36346564.055] (assumes normal distribution)


# Run complete. Total time: 00:08:21

REMEMBER: The numbers below are just data. To gain reusable insights, you need to follow up on
why the numbers are the way they are. Use profilers (see -prof, -lprof), design factorial
experiments, perform baseline and negative tests that provide experimental control, make sure
the benchmarking environment is safe on JVM/OS/HW level, ask for reviews from the domain experts.
Do not assume the numbers tell you what you want them to tell.

NOTE: Current JVM experimentally supports Compiler Blackholes, and they are in use. Please exercise
extra caution when trusting the results, look into the generated code to check the benchmark still
works, and factor in a small probability of new VM bugs. Additionally, while comparisons between
different JVMs are already problematic, the performance difference caused by different Blackhole
modes can be very significant. Please make sure you use the consistent Blackhole mode for comparisons.

Benchmark                           Mode  Cnt         Score        Error  Units
MyBenchmark.benchmarkHttpResponse  thrpt   25  35659618.044 ± 686946.011  ops/s
```

### Benchmark Metrics Explained  

- **Run Count**: The total number of benchmark iterations executed. A higher run count increases statistical reliability and reduces the effect of outliers.  
- **Average Throughput**: The mean number of operations executed per second across all iterations. This metric represents the overall sustained performance of the benchmarked workload.
- **Standard Deviation**: Indicates the amount of variation or dispersion from the average throughput. A smaller standard deviation means more consistent performance.  
- **Confidence Interval (99.9%)**: The statistical range within which the true average throughput is expected to fall, with 99.9% certainty. Narrow intervals imply more reliable results.  
- **Min Throughput**: The lowest throughput observed across all iterations, reflecting the worst-case performance scenario.  
- **Max Throughput**: The highest throughput observed across all iterations, reflecting the best-case performance scenario.  

### Benchmark summary on Arm64

Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.
| Metric                        | Value |
|--------------------------------|---------------------------|
| **Java Version**               | OpenJDK 21.0.8            |
| **Run Count**                  | 25 iterations             |
| **Average Throughput**         | 35.66M ops/sec            |
| **Standard Deviation**         | ±0.92M ops/sec            |
| **Confidence Interval (99.9%)**| [34.97M, 36.34M] ops/sec  |
| **Min Throughput**             | 33.53M ops/sec            |
| **Max Throughput**             | 36.99M ops/sec            |

### Benchmark summary on x86

Here is a summary of benchmark results collected on x86 **D4s_v6 Ubuntu Pro 24.04 LTS virtual machine**.

| Metric                        | Value |
|--------------------------------|---------------------------|
| **Java Version**               | OpenJDK 21.0.8            |
| **Run Count**                  | 25 iterations             |
| **Average Throughput**         | 16.78M ops/sec            |
| **Standard Deviation**         | ±0.06M ops/sec            |
| **Confidence Interval (99.9%)**| [16.74M, 16.83M] ops/sec  |
| **Min Throughput**             | 16.64M ops/sec            |
| **Max Throughput**             | 16.88M ops/sec            |


### Benchmark comparison insights
When comparing the results on Arm64 vs x86_64 virtual machines:

- **High Throughput:** Achieved an average of **35.66M ops/sec**, with peak performance reaching **36.99M ops/sec**.  
- **Stable Performance:** Standard deviation of **±0.92M ops/sec**, with results tightly bounded within the 99.9% confidence interval **[34.97M, 36.34M]**.  
- **Consistent Efficiency:** Demonstrates the reliability of Arm64 architecture for sustaining high-throughput Java workloads on Azure Ubuntu Pro environments.

You have now benchmarked Java on an Azure Cobalt 100 Arm64 virtual machine and compared results with x86_64.
