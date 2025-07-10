---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is BOLT?

[BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) is a post-link binary optimizer that uses uses profiling data from [Linux Perf](/install-guides/perf/) to identify frequently executed functions and basic blocks. Based on this data, BOLT reorders code to improve instruction cache locality, reduce branch mispredictions, and shorten critical execution paths.

This often results in faster startup times, lower CPU cycles per instruction (CPI), and improved throughput - especially for large, performance-sensitive applications like databases, web servers, or system daemons.

{{% notice Note %}}
BOLT complements compile-time optimizations like LTO (Link-Time Optimization) and PGO (Profile-Guided Optimization). It applies after linking, giving it visibility into the final binary layout, which traditional compiler optimizations do not.
{{% /notice %}}

Before you begin, ensure that you have the following installed:

- [BOLT](/install-guides/bolt/) 
- [Linux Perf](/install-guides/perf/)

You should use an Arm-based Linux system with at least 8 CPUs and 16 GB of RAM. This Learning Path was tested on Ubuntu 24.04, but other Linux distributions are also supported.

## What will I do in this Learning Path?

In this Learning Path, you'll learn how to use BOLT to optimize both applications and shared libraries. You'll walk through a real-world example using MySQL and two of its dependent libraries: 

- `libssl.so` 
- `libcrypto.so`

You will:

- **Collect and merge BOLT profiles from multiple workloads, such as read-only and write-only** - a read-only workload typically involves operations that only retrieve or query data, such as running SELECT statements in a database without modifying any records. In contrast, a write-only workload focuses on operations that modify data, such as INSERT, UPDATE, or DELETE statements. Profiling both types ensures that the optimized binary performs well under different usage patterns.

- **Independently optimize application binaries and external user-space libraries, such as `libssl.so` and `libcrypto.so`** - this means that you can apply BOLT optimizations to not just your main application, but also to shared libraries it depends on, resulting in a more comprehensive performance improvement across your entire stack.

- **Merge profile data for broader code coverage** - by combining the profile data collected from different workloads and libraries, you create a single, comprehensive profile that represents a wide range of application behaviors. This merged profile allows BOLT to optimize code paths that are exercised under different scenarios, leading to better overall performance and coverage than optimizing for a single workload.

- **Run BOLT on each binary application and library** - with the merged profile, you apply BOLT optimizations separately to each binary and shared library. This step ensures that both your main application and its dependencies are optimized based on real-world usage patterns, resulting in a more efficient and responsive software stack.

- **Link the final optimized binary with the separately optimized libraries to deploy a fully optimized runtime stack** - after optimizing each component, you combine them to create a deployment where both the application and its libraries benefit from BOLT's enhancements.

## What is BOLT profile merging?

BOLT profile merging combines profiling data from multiple runs into one unified profile. This merged profile enables BOLT to optimize binaries for a broader set of real-world behaviors, ensuring that the final optimized application or library performs well across diverse workloads, not just a single use case. By merging profiles, you capture a wider range of code paths and execution patterns, leading to more robust and effective optimizations.

![Diagram showing how BOLT profile merging combines multiple runtime profiles into a single optimized view#center](bolt-merge.png "Why BOLT profile merging improves optimization coverage")

## What types of applications benefit from BOLT?

Although this Learning Path uses MySQL and Sysbench as examples, you can apply the same method to any feature-rich application that:

- **Exhibits multiple runtime paths** - applications often have different code paths depending on the workload or user actions. Optimizing for just one path can leave performance gains untapped in others. By profiling and merging data from various workloads, you ensure broader optimization coverage.

- **Uses dynamic libraries** - most modern applications rely on shared libraries for functionality. + Optimizing shared libraries alongside the main binary ensures consistent performance across your stack.

- **Requires full-stack binary optimization for performance-critical deployment** - in scenarios where every bit of performance matters, such as high-throughput servers or latency-sensitive applications, optimizing the entire binary stack can yield significant benefits.


