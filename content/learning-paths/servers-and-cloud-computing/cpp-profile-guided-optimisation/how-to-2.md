---
title: Introduction to Google Benchmark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Google Benchmark

Google Benchmark is a C++ library specifically designed for microbenchmarking – measuring the performance of small code snippets with high accuracy. Microbenchmarking is essential for identifying bottlenecks and optimizing critical sections of code, especially in performance-sensitive applications. Google Benchmark simplifies this process by providing a framework that handles common tasks like managing iterations, timing execution, and performing statistical analysis. This allows you to focus on the code being measured rather than writing boilerplate code for testing scenarios or trying to prevent unwanted compiler optimizations.

To use Google Benchmark, you define a function that contains the code you want to measure. This function should accept a `benchmark::State&` parameter and iterate over it to perform the benchmarking. You then register this function using the `BENCHMARK` macro and include `BENCHMARK_MAIN()` to create the main function for the benchmark executable.

Here's a basic example:

```cpp
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
BENCHMARK(BM_StringCreation);

BENCHMARK_MAIN();
```

### Filtering and Preventing Compiler Optimizations

Google Benchmark provides tools to ensure accurate measurements by preventing the compiler from optimizing away parts of your benchmarked code:

1. **Preventing Optimizations**: Use `benchmark::DoNotOptimize(value);` to force the compiler to read and store a variable or expression, ensuring it is not optimized away.
   
2. **Filtering Benchmarks**: To run a specific subset of benchmarks, use the `--benchmark_filter` command-line option with a regular expression. For example:

   ```bash
   ./benchmark_binary --benchmark_filter=BM_String.*
   ```
   This eliminates the need to repeatedly comment out lines of source code.

For more detailed information and advanced usage, refer to the [official documentation](https://github.com/google/benchmark).