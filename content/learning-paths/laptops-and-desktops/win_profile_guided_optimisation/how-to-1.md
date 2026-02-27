---
title: Understand Profile-Guided Optimization
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Profile-Guided Optimization?

Profile-Guided Optimization (PGO) is a compiler optimization technique that enhances your program's performance by using real-world execution data. PGO works in two steps: 

First, you compile your program to produce an instrumented binary that collects profiling data during execution. Second, you recompile the program with this optimization profile, allowing the compiler to make informed optimization decisions based on the collected data.

This approach identifies frequently executed paths (known as "hot" paths) and optimizes them more aggressively, while reducing emphasis on less critical code paths.

## How PGO improves performance on Windows on Arm

PGO enables several compiler optimizations that aren't possible with static analysis alone.

Code layout optimization arranges frequently executed code together in memory, improving instruction cache utilization and reducing branch mispredictions. Instead of using heuristics for inlining decisions, the compiler inlines functions based on actual call frequency and execution patterns from your profiling data.

For C++ virtual functions, PGO can identify the most common call targets and optimize or devirtualize those paths. The compiler can also eliminate dead code by optimizing differently or removing code paths that never execute in your profiling runs.

If your application has an error handling path that rarely executes, PGO ensures the compiler doesn't optimize for that path at the expense of your main execution flow. Performance improvements typically range from 5-15%, though results vary by workload and architecture.

## When to use PGO on Arm

You'll find PGO particularly beneficial in the later stages of development when real-world workloads are available. It's especially useful for applications where performance is critical and runtime behavior is complex or data-dependent.

For example, consider optimizing "hot" functions that execute frequently. By doing so, you ensure that the most impactful parts of your code are optimized based on actual usage patterns.

## Limitations of Profile-Guided Optimization

While PGO offers substantial performance benefits, it has some limitations to keep in mind.

Your profiling data must accurately represent typical usage scenarios. If it doesn't, the optimizations might not deliver the desired performance improvements and could even degrade performance.

Additionally, the process requires extra build steps, which can increase compile times for large codebases. Use PGO on performance-critical sections that are heavily influenced by actual runtime behavior.

PGO might not be ideal for early-stage development or applications with highly variable or unpredictable usage patterns.

## What you've accomplished and what's next

You now understand what PGO is, how it improves performance through code layout and inlining optimizations, and when to apply it. In the next section, you'll learn about Google Benchmark, the tool you'll use to measure these performance improvements.
