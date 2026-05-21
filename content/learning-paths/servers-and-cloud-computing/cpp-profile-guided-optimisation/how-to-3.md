---
title: Example operation
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimizing costly division operations with Google Benchmark and PGO

In this section, you'll learn how to use Google Benchmark and Profile-Guided Optimization to improve the performance of a simple division operation. This example demonstrates how even seemingly straightforward operations can benefit from optimization techniques.

Integer division is ideal for benchmarking because it's significantly more expensive than operations like addition, subtraction, or multiplication. On most CPU architectures, including Arm, division instructions have higher latency and lower throughput compared to other arithmetic operations. By applying Profile-Guided Optimization to code containing division operations, we can potentially achieve significant performance improvements.

## What tools are needed to run a Google Benchmark example?

For this example, you can use any Arm Linux computer. For example, the 1st generation Arm AGI CPU running Ubuntu 24.04 LTS.

Run the following commands to install the prerequisite packages:

```bash
sudo apt update
sudo apt install gcc g++ make libbenchmark-dev -y
```

## Division example

Use an editor to copy and paste the C++ source code below into a file named `div_bench.cpp`.

This trivial example takes in a vector of 4096 32-bit integers and divides each element by a number. Importantly, the use of `benchmark/benchmark.h` introduces indirection since the divisor value is unknown at compile time, although it is visible in the source code as 1500.

```cpp
#include <benchmark/benchmark.h>
#include <vector>

// Benchmark division instruction
static void baseDiv(benchmark::State &s) {
  std::vector<int> v_in(4096);
  std::vector<int> v_out(4096);

  for (auto _ : s) {
    for (size_t i = 0; i < v_in.size(); i++) v_out[i] = v_in[i] / s.range(0);
    // s.range(0) is unknown at compile time, cannot be reduced
  }
}

BENCHMARK(baseDiv)->Arg(1500)->Unit(benchmark::kMicrosecond); // value of 1500 is passed through as an argument so strength reduction cannot be applied

BENCHMARK_MAIN();
```

To compile and run the microbenchmark on this function, you need to link with the `pthreads` and `benchmark` libraries.

Compile with the command:

```bash
g++ -O3 -std=c++17 div_bench.cpp -lbenchmark -lpthread -o div_bench.base
```

{{% notice Please Note %}}

Since the command above does not specify `-mcpu` or `-march`, GCC targets a generic baseline architecture. If you want to apply PGO specifically for the 1st generation Arm AGI CPU, the `-mcpu=armagicpu` was added in [GCC 16.1.0](https://github.com/gcc-mirror/gcc/commit/0f5f728854d2ea93e6806a8632c04383502b0386). As of May 2026, it enables the same architectural features as `-march=neoverse-v3ae` from [GCC 15](https://gcc.gnu.org/gcc-15/changes.html). However in the future there may be differences.

As such, we recommend installing the latest version of GCC/G++ if you are targeting the Arm AGI CPU. Use the `-mcpu=native` flag if compiling on the target machine or `-mcpu=armagicpu` if cross compiling.

{{% /notice %}}

Run the program:

```bash { command_line="user@localhost | 2-16" }
./div_bench.base 
2026-05-21T08:12:08+00:00
Running ./div_bench.base
Run on (128 X 2800 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x128)
  L1 Instruction 64 KiB (x128)
  L2 Unified 2048 KiB (x128)
  L3 Unified 131072 KiB (x1)
Load Average: 0.13, 0.05, 0.02
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
***WARNING*** Library was built as DEBUG. Timings may be affected.
-------------------------------------------------------
Benchmark             Time             CPU   Iterations
-------------------------------------------------------
baseDiv/1500       7.37 us         7.37 us        79910
```

{{% notice Please Note%}}

Since we are not interested in exact timings but the relative change we can ignore the warnings about CPU scaling and library debug. We expect the speed up from PGO to be beyond the reasonable margin or error caused by said affects.

{{% /notice %}}

### Inspect assembly

To inspect what assembly instructions are being executed most frequently, you can use the `perf` command. This is useful for identifying bottlenecks and understanding the performance characteristics of your code.

Install Perf using the [install guide](/install-guides/perf/) before proceeding.

{{% notice Please Note %}}
You may need to set the `perf_event_paranoid` value to -1 with the `sudo sysctl kernel.perf_event_paranoid=-1` command to run the commands below.
{{% /notice %}}

Run the following commands to record `perf` data and create a report in the terminal:

```bash
sudo perf record -o perf-division-base ./div_bench.base 
sudo perf report --input=perf-division-base
```

As the `perf report` graphic below shows, the program spends a significant amount of time in the short loops with no loop unrolling. There is also an expensive `sdiv` operation, and most of the execution time is spent storing the result of the operation.

![before-pgo](./before-pgo.gif)
