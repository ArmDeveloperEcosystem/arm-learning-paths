---
title: Profile-Guided Optimization
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What is Profile-Guided Optimization (PGO) and how does it work?

Profile-Guided Optimization (PGO) is a compiler optimization technique that enhances program performance by utilizing real-world execution data. PGO typically involves a two-step process: 

- First, compile the program to produce an instrumented binary that collects profiling data during execution; 
- Second, recompile the program with an optimization profile, allowing the compiler to leverage the collected data to make informed optimization decisions. This approach identifies frequently executed paths — known as “hot” paths — and optimizes them more aggressively, while potentially reducing emphasis on less critical code paths.

### When should I use Profile-Guided Optimization?

PGO is particularly beneficial in the later stages of development when real-world workloads are available. It is especially useful for applications where performance is critical and runtime behavior is complex or data-dependent. For instance, consider optimizing “hot” functions that execute frequently. Doing so ensures that the most impactful parts of your code are optimized based on actual usage patterns.

### What are the limitations of Profile-Guided Optimization and when should I avoid it?

While PGO offers substantial performance benefits, it has limitations. The profiling data must accurately represent typical usage scenarios; otherwise, the optimizations may not deliver the desired performance improvements and could even degrade performance.

Additionally, the process requires extra build steps, potentially increasing compile times for large codebases. Therefore, use PGO only on performance-critical sections that are heavily influenced by actual runtime behavior. PGO might not be ideal for early-stage development or applications with highly variable or unpredictable usage patterns.

For further information, see the [GCC documentation](https://gcc.gnu.org/onlinedocs/gcc-13.3.0/gcc/Instrumentation-Options.html) on enabling and using PGO.
