---
title: Create a baseline benchmark
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you'll create a baseline benchmark to measure the performance of a division operation. This baseline will help you see the improvement when you apply Profile-Guided Optimization in the next section. This example demonstrates how even seemingly straightforward operations can benefit from optimization techniques.

Integer division is ideal for benchmarking because it's significantly more expensive than operations like addition, subtraction, or multiplication. On most CPU architectures, including Arm, division instructions have higher latency and lower throughput compared to other arithmetic operations. By applying Profile-Guided Optimization to code containing division operations, you can achieve significant performance improvements.

For this example, you'll use an Arm computer running Windows.

## Install the required tools

First, you need to install Google Benchmark for Arm64 via vcpkg. Run the following commands in PowerShell as Administrator:

```console
cd C:\git
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
.\vcpkg install benchmark:arm64-windows-static
```

## Create the division benchmark

Use an editor to copy and paste the C++ source code below into a file named `div_bench.cpp`.

This example takes a vector of 4096 32-bit integers and divides each element by a number. The key detail here is that the divisor value is passed through `s.range(0)`, making it unknown at compile time. This prevents the compiler from applying optimizations like strength reduction, which means PGO will have an opportunity to make a real difference.

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

## Compile and run the baseline benchmark

Before compiling, set an environment variable to refer to the vcpkg installation directory:

```console
$VCPKG="C:\git\vcpkg\installed\arm64-windows-static"
```

Now compile the benchmark. This command uses the MSVC compiler and links with the Google Benchmark libraries:

```console
cl /D BENCHMARK_STATIC_DEFINE div_bench.cpp /link /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

Run the program to establish your baseline performance:

```console
.\div_bench.exe
```

The output is similar to:

```output
Running ./div_bench.base
Run on (4 X 2100 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x4)
  L1 Instruction 64 KiB (x4)
  L2 Unified 1024 KiB (x4)
  L3 Unified 32768 KiB (x1)
Load Average: 0.00, 0.00, 0.00
***WARNING*** Library was built as DEBUG. Timings may be affected.
-------------------------------------------------------
Benchmark             Time             CPU   Iterations
-------------------------------------------------------
baseDiv/1500       7.90 us         7.90 us        88512
```

The baseline shows an average execution time of 7.90 microseconds. This gives you a clear starting point to measure improvement. Now that you have this baseline measurement, you're ready to apply Profile-Guided Optimization. In the next section, you'll use PGO to optimize this code and see how much faster it can run.
