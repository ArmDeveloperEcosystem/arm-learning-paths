---
title: Understand Google Benchmark basics
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Before you start working with Profile-Guided Optimization, you need to understand how to measure performance. This section introduces Google Benchmark, the tool you'll use to measure the impact of your optimizations. Don't worry about installing anything yet. You'll set up your environment and run your first benchmark in the next section.

## What is Google Benchmark?

Google Benchmark is a C++ library specifically designed for microbenchmarking, which means measuring the performance of small code snippets with high accuracy. Microbenchmarking helps you identify bottlenecks and optimize critical sections, especially in performance-sensitive applications. 

Google Benchmark simplifies this process by providing a framework that manages iterations, times execution, and performs statistical analysis. You can focus on the code being measured, rather than writing test code or trying to prevent unwanted compiler optimizations manually.

## Write a simple benchmark

To use Google Benchmark, define a function that accepts a benchmark::State& parameter and use it to run the benchmark in a loop. You register the function using the `BENCHMARK` macro and include `BENCHMARK_MAIN()` to generate the benchmark's entry point.

The following example shows a basic benchmark that measures the time it takes to create an empty string. A minimal benchmark looks like this:

```cpp
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
BENCHMARK(BM_StringCreation);

BENCHMARK_MAIN();
```

## Control benchmarks with Google Benchmark filters

Google Benchmark provides tools to ensure accurate measurements by preventing unintended compiler optimizations and allowing flexible benchmark selection.

To prevent the compiler from optimizing away your code, use `benchmark::DoNotOptimize(value);` to force the compiler to read and store a variable or expression. This ensures your benchmark actually measures what you intend to measure.

When you have multiple benchmarks, you can run a specific subset using the `--benchmark_filter` command-line option with a regular expression. This example runs all benchmarks that start with "BM_String":

```console
.\benchmark_binary --benchmark_filter=BM_String.*
```

Filtering eliminates the need to repeatedly comment out lines of source code when you want to focus on specific benchmarks.

## What you've learned

You now understand how to write basic benchmarks with Google Benchmark, use `benchmark::DoNotOptimize` to prevent unwanted compiler optimizations, and filter benchmark execution with command-line options. In the next section, you'll install Google Benchmark and create a baseline benchmark to measure division performance on Windows on Arm.
