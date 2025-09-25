
---
title: Benchmark using Java Microbenchmark Harness
weight: 6 

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

Now that you have built and run a Tomcat-like response in Java, the next step is to benchmark it using a reliable, JVM-aware framework.

## Run performance tests using JMH

JMH (Java Microbenchmark Harness) is a Java benchmarking framework developed by the JVM team at Oracle to measure the performance of small code snippets with high precision. It accounts for JVM optimizations like JIT and warmup to ensure accurate and reproducible results. You can measure throughput (ops/sec), average execution time, or percentiles for latency. 

Follow the steps to help benchmark the Tomcat-like operation with JMH:


Install Maven:

```console
sudo apt update
sudo apt install -y maven
```
Once Maven is installed, create a JMH benchmark project using the official archetype provided by OpenJDK:

```console
mvn archetype:generate   -DinteractiveMode=false   -DarchetypeGroupId=org.openjdk.jmh   -DarchetypeArtifactId=jmh-java-benchmark-archetype   -DarchetypeVersion=1.37   -DgroupId=com.example   -DartifactId=jmh-benchmark   -Dversion=1.0
cd jmh-benchmark
```
The output should look like:

```output
[INFO] ----------------------------------------------------------------------------
[INFO] Using following parameters for creating project from Archetype: jmh-java-benchmark-archetype:1.37
[INFO] ----------------------------------------------------------------------------
[INFO] Parameter: groupId, Value: com.example
[INFO] Parameter: artifactId, Value: jmh-benchmark
[INFO] Parameter: version, Value: 1.0
[INFO] Parameter: package, Value: com.example
[INFO] Parameter: packageInPathFormat, Value: com/example
[INFO] Parameter: package, Value: com.example
[INFO] Parameter: groupId, Value: com.example
[INFO] Parameter: artifactId, Value: jmh-benchmark
[INFO] Parameter: version, Value: 1.0
[INFO] Project created from Archetype in dir: /home/azureuser/jmh-benchmark
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  3.474 s
[INFO] Finished at: 2025-09-15T18:28:15Z
[INFO] ------------------------------------------------------------------------
```

Now edit the `src/main/java/com/example/MyBenchmark.java` file in the generated project. Replace the placeholder `TestMethod()` function with the following code:

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
This mirrors the Tomcat-like simulation you created earlier but now runs under JMH.

## Build the benchmark JAR

Build the project to produce the benchmark JAR:

```console
mvn clean install -q
```

The output from this command should look like:

```output
[INFO] Installing /home/azureuser/jmh-benchmark/target/jmh-benchmark-1.0.jar to /home/azureuser/.m2/repository/com/example/jmh-benchmark/1.0/jmh-benchmark-1.0.jar
[INFO] Installing /home/azureuser/jmh-benchmark/pom.xml to /home/azureuser/.m2/repository/com/example/jmh-benchmark/1.0/jmh-benchmark-1.0.pom
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  5.420 s
[INFO] Finished at: 2025-09-15T18:31:32Z
```

After the build is complete, the JMH benchmark JAR will be located in the target directory.

Run the benchmark:

```console
java -jar target/benchmarks.jar
```
This will execute the benchmarkHttpResponse() method under JMH, showing average time per operation.

You should see output similar to:
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

JMH runs warmup iterations so the JVM has a chance to JIT-compile and optimize the code before the real measurement begins.
Each iteration shows how many times per second your `benchmarkHttpResponse()` method ran. You get an aggregate summary of the result at the end. In this example, on average the JVM executed ~35.6 million response constructions per second.

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

## Benchmark metrics explained  

- **Run count** - the total number of benchmark iterations that JMH executed. More runs improve statistical reliability and help smooth out anomalies caused by the JVM or OS. 
- **Average throughput** - the mean number of operations completed per second across all measured iterations. This is the primary indicator of sustained performance for the benchmarked code.
- **Standard deviation** - indicates the amount of variation or dispersion from the average throughput. A smaller standard deviation means more consistent performance.  
- **Confidence interval (99.9%)** - the statistical range in which the true average throughput is expected to fall with 99.9% certainty. Narrow confidence intervals suggest more reliable and repeatable measurements. 
- **Min throughput** - the lowest observed throughput across all iterations, representing a worst-case scenario under the current test conditions.
- **Max throughput** - the highest observed throughput across all iterations, representing the best-case performance under the current test conditions. 

## Benchmark summary on Arm64

Here is a summary of benchmark results collected on an Arm64 **D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine**.
| Metric                        | Value |
|--------------------------------|---------------------------|
| **Java version**               | OpenJDK 21.0.8            |
| **Run count**                  | 25 iterations             |
| **Average throughput**         | 35.66M ops/sec            |
| **Standard deviation**         | ±0.92M ops/sec            |
| **Confidence interval (99.9%)**| [34.97M, 36.34M] ops/sec  |
| **Min throughput**             | 33.53M ops/sec            |
| **Max throughput**             | 36.99M ops/sec            |


## Key insights from the results

- **Strong throughput performance** - the benchmark sustained around 35.6 million operations per second, demonstrating efficient string construction and memory handling on the Arm64 JVM.
- **Consistency across runs** - with a standard deviation under 1 million ops/sec, results were tightly clustered. This suggests stable system performance without significant noise from background processes.
- **High statistical confidence** - the narrow 99.9% confidence interval ([34.97M, 36.34M]) indicates reliable, repeatable results. 
- **Predictable performance envelope** - the difference between min (33.5M) and max (37.0M) throughput is modest (~10%), suggests the workload performed consistently without extreme slowdowns or spikes.

The Arm-based Azure `D4ps_v6` VM provides stable and efficient performance for Java workloads, even in microbenchmark scenarios. These results establish a baseline you can now compare directly against x86_64 instances to evaluate relative performance. 
