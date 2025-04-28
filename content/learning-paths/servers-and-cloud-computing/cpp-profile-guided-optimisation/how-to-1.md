---
title: Introduction to Profile-Guided Optimisation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction of Profile Guided Optimisation

### What is Profile-Guided Optimization (PGO) and How Does It Work?

Profile-Guided Optimization (PGO) is a compiler optimization technique that enhances program performance by utilizing real-world execution data. In GCC/G++, PGO involves a two-step process: first, compiling the program with the -fprofile-generate flag to produce an instrumented binary that collects profiling data during execution; and second, recompiling the program with the -fprofile-use flag, allowing the compiler to leverage the collected data to make informed optimization decisions. This approach enables the compiler to identify frequently executed paths—known as “hot” paths—and optimize them more aggressively, while potentially reducing the emphasis on less critical code paths.

### When to Use Profile-Guided Optimization

PGO is particularly beneficial in the later stages of development, once the codebase has stabilized. It’s most effective for applications where performance is critical and runtime behavior is complex or data-dependent. For instance, optimizing “hot” functions—those that are executed frequently—can lead to significant performance improvements. By focusing on these critical sections, PGO ensures that the most impactful parts of the code are optimized based on actual usage patterns.

### Limitations of Profile-Guided Optimization and When Not to Use

While PGO offers substantial performance benefits, it has certain limitations. The profiling data must accurately represent typical usage scenarios; otherwise, the optimizations may not yield the desired performance improvements and could even degrade performance in some cases. 

Additionally, the process requires additional build steps which will inevitably increase compile time which can be an issue for large code bases. As such, PGO is not suitable for all sections of code. We recommend only using PGO only sections of code which are heavily influenced by run-time behaviour and are performance critical. Therefore, PGO might not be ideal for early-stage development or for applications with highly variable or unpredictable usage patterns.

