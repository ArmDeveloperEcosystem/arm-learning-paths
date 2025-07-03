---
title: Benchmarking via JMH 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test the Java application for Performance 
Now that you’ve built and run the Tomcat-like response, you can use it to test the JVM performance using JMH. You can also use it to test the performance difference between Cobalt 100 instances and other similar D series x86_64 based instances. 

## Run the performance tests using JMH

JMH (Java Microbenchmark Harness) is a Java benchmarking framework developed by the JVM team at Oracle to measure the performance of small code snippets with high precision. It accounts for JVM optimizations like JIT and warm-up to ensure accurate and reproducible results. It measures the throughput, average latency, or execution time. Below steps help benchmark the Tomcat-like operation: 

Install Maven: 

```console 
$ tdnf install maven -y 
```
Create Benchmark Project: 

```console
$ mvn archetype:generate \ 
  -DinteractiveMode=false \ 
  -DarchetypeGroupId=org.openjdk.jmh \ 
  -DarchetypeArtifactId=jmh-java-benchmark-archetype \ 
  -DarchetypeVersion=1.37 \ 
  -DgroupId=com.example \ 
  -DartifactId=jmh-benchmark \ 
  -Dversion=1.0
$ cd jmh-benchmark
```

Edit the `src/main/java/com/example/MyBenchmark.java` file and add the below code on it: 

```java
package com.example; 
import org.openjdk.jmh.annotations.Benchmark; 
public class MyBenchmark { 
 
    @Benchmarkpublic void benchmarkHttpResponse() { 
        String body = "Benchmarking a Tomcat-like operation"; 
        StringBuilder sb = new StringBuilder(); 
        sb.append("HTTP/1.1 200 OK\r\n"); 
        sb.append("Content-Type: text/plain\r\n"); 
        sb.append("Content-Length: ").append(body.length()).append("\r\n\r\n"); 
        sb.append(body); 
        if (sb.length() == 0) throw new RuntimeException(); // avoid DCE    } 
} 
```
This simulates HTTP response generation similar to Tomcat. 

Build the Benchmark:

```console
$ mvn clean install
```

After the build is complete, the JMH benchmark jar will be in the target/ directory.

Run the Benchmark: 

```console 
$ java -jar target/benchmarks.jar    
```
 
Output: 

```output 
Result "com.example.MyBenchmark.benchmarkHttpResponse": 
35600560.283 ?(99.9%) 121215.695 ops/s [Average] 
(min, avg, max) = (35293153.787, 35600560.283, 35831841.216), stdev = 161819.485
CI (99.9%): [35479344.588, 35721775.978] (assumes normal distribution) 
# Run complete. Total time: 00:08:21 
```

## Benchmark summary on x86_64 based D4s_v6 general purpose Azure VM (JDK 11.0.27) 

The benchmark was executed inside an Azure Linux 3.0 Docker container on an x86_64 VM using the default Microsoft OpenJDK 11.0.27. 
- Average Throughput: 21.88 million operations per second 
- Standard Deviation: ±76941.944 ops/sec 
- Confidence Interval (99.9%): [21.82M, 21.94M] ops/sec 
- Run Count: 25 iterations

## Benchmark summary on Arm64 based D4ps_v6 general purpose Azure VM (JDK 11.0.27): 

The benchmark was run using JMH inside an Azure Linux 3.0 Docker container on an Arm64 VM 
with the default Microsoft OpenJDK 11.0.27. 
- Average Throughput: 35.60 million operations per second
- Standard Deviation: ±161819.485 ops/sec
- Confidence Interval (99.9%): [35.48M, 35.72M] ops/sec
- Run Count: 25 iterations

## Highlights from Azure Linux Arm64 Benchmarking (JDK 11.0.27)

- **Superior Throughput:** Achieved an average of 35.60 million ops/sec.
- **Stable Performance:** Low standard deviation (±161819.485 ops/sec) and a tight confidence interval suggest consistent benchmarking results.
- **Efficient Execution:** Demonstrates the efficiency of the Arm64 architecture for handling high-throughput Java workloads, even within a containerized Azure Linux environment.
- **Container Feasibility:** Confirms that Azure Linux 3.0 containers on Arm64 are a viable option for performance-sensitive Java applications, even in the absence of native Arm64 VM images.

