---
title: BOLT overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) is a post-link binary optimizer that uses Linux Perf data to re-order the executable code layout to reduce memory overhead and improve performance.

Make sure you have [BOLT](/install-guides/bolt/) and [Linux Perf](/install-guides/perf/) installed. 

You should use an Arm Linux system with at least 8 CPUs and 16 Gb of RAM. Ubuntu 24.04 is used for testing, but other Linux distributions are possible. 

## What will I do in this Learning Path?

In this Learning Path you learn how to use BOLT to optimize applications and shared libraries. MySQL is used as the application and two share libraries which are used by MySQL are also optimized using BOLT.

Here is an outline of the steps:

1. Collect and merge BOLT profiles from multiple workloads, such as read-only and write-only  

    A read-only workload typically involves operations that only retrieve or query data, such as running SELECT statements in a database without modifying any records. In contrast, a write-only workload focuses on operations that modify data, such as INSERT, UPDATE, or DELETE statements. Profiling both types ensures that the optimized binary performs well under different usage patterns.

2. Independently optimize application binaries and external user-space libraries, such as `libssl.so` and `libcrypto.so`

    This means you can apply BOLT optimizations not just to your main application, but also to shared libraries it depends on, resulting in a more comprehensive performance improvement across your entire stack.

3. Merge profile data for broader code coverage

    By combining the profile data collected from different workloads and libraries, you create a single, comprehensive profile that represents a wide range of application behaviors. This merged profile allows BOLT to optimize code paths that are exercised under different scenarios, leading to better overall performance and coverage than optimizing for a single workload.

4. Run BOLT on each binary application and library

    With the merged profile, you apply BOLT optimizations separately to each binary and shared library. This step ensures that both your main application and its dependencies are optimized based on real-world usage patterns, resulting in a more efficient and responsive software stack.

5. Link the final optimized binary with the separately bolted libraries to deploy a fully optimized runtime stack  

    After optimizing each component, you combine them to create a deployment where both the application and its libraries benefit from BOLT's enhancements.

## What is BOLT profile merging?

BOLT profile merging is the process of combining profiling from multiple runs into a single profile. This merged profile enables BOLT to optimize binaries for a broader set of real-world behaviors, ensuring that the final optimized application or library performs well across diverse workloads, not just a single use case. By merging profiles, you capture a wider range of code paths and execution patterns, leading to more robust and effective optimizations.

![Why BOLT Profile Merging?](Bolt-merge.png)

## What are good applications for BOLT?

MySQL and Sysbench are used as example applications, but you can use this method for any feature-rich application that:

1. Exhibits multiple runtime paths  

    Applications often have different code paths depending on the workload or user actions. Optimizing for just one path can leave performance gains untapped in others. By profiling and merging data from various workloads, you ensure broader optimization coverage.

2. Uses dynamic libraries  

    Most modern applications rely on shared libraries for functionality. Optimizing these libraries alongside the main binary ensures consistent performance improvements throughout the application.

3. Requires full-stack binary optimization for performance-critical deployment  

    In scenarios where every bit of performance matters, such as high-throughput servers or latency-sensitive applications, optimizing the entire binary stack can yield significant benefits.


