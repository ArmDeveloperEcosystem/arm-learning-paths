---
title: Understand Google Benchmark basics
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before you start working with Profile-Guided Optimization, you need to understand how to measure performance. This section introduces Google Benchmark, the tool you'll use to measure the impact of your optimizations. Don't worry about installing anything yet. You'll set up your environment and run your first benchmark in the next section.

Google Benchmark is a C++ library specifically designed for microbenchmarking, which means measuring the performance of small code snippets with high accuracy. Microbenchmarking helps you identify bottlenecks and optimize critical sections, especially in performance-sensitive applications. 

Google Benchmark simplifies this process by providing a framework that manages iterations, times execution, and performs statistical analysis. This lets you focus on the code being measured, rather than writing boilerplate or trying to prevent unwanted compiler optimizations manually.

To use Google Benchmark, you define a function that accepts a `benchmark::State&` parameter and iterate over it to perform the benchmarking. You register the function using the `BENCHMARK` macro and include `BENCHMARK_MAIN()` to generate the benchmark's entry point.

This example shows a basic benchmark that measures the time it takes to create an empty string:

```cpp
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
BENCHMARK(BM_StringCreation);

BENCHMARK_MAIN();
```

## Filter benchmarks and prevent compiler optimizations

Google Benchmark provides tools to ensure accurate measurements by preventing unintended compiler optimizations and allowing flexible benchmark selection.

To prevent the compiler from optimizing away your code, use `benchmark::DoNotOptimize(value);` to force the compiler to read and store a variable or expression. This ensures your benchmark actually measures what you intend to measure.

When you have multiple benchmarks, you can run a specific subset using the `--benchmark_filter` command-line option with a regular expression. This example runs all benchmarks that start with "BM_String":

```console
.\benchmark_binary --benchmark_filter=BM_String.*
```

This approach eliminates the need to repeatedly comment out lines of source code when you want to focus on specific benchmarks.

Now that you understand how Google Benchmark works, you're ready to install it and run your first benchmark. In the next section, you'll set up your environment and use Google Benchmark with Profile-Guided Optimization to measure and improve performance.
