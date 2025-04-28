---
title: Introduction to Google Benchmark
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Google Benchmark

Google Benchmark is a C++ library designed to expedite the microbenchmarking of code. It simplifies the process of writing microbenchmarks by providing a structured framework that automatically handles iterations, timing, and statistical analysis. This allows developers to focus on optimizing their code rather than writing  main functions, refactoring source code to run in a testing scenario and trying to anticipate any unwanted compiler optimisations.

To use Google Benchmark, you define a function that contains the code you want to measure. This function should accept a `benchmark::State&` parameter and iterate over it to perform the benchmarking. You then register this function using the `BENCHMARK` macro and include `BENCHMARK_MAIN()` to create the main function for the benchmark executable. Here's a basic example:

```cpp
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
BENCHMARK(BM_StringCreation);

BENCHMARK_MAIN();
```

Filtering and preventing Compiler Optimisations

To ensure that the compiler does not optimize away parts of your benchmarked code, Google Benchmark provides the function `benchmark::DoNotOptimize(value);`. This Prevents the compiler from optimizing away a variable or expression by forcing it to be read and stored. 

Additionally, to run a specific subset of benchmarks, you can use the `--benchmark_filter` command-line option with a regular expression. For example `./benchmark_binary --benchmark_filter=BM_String.*` so you don't need to repeatedly comment out lines of source code.  


For more detailed information and advanced usage, refer to the [official Google documentation](https://github.com/google/benchmark).