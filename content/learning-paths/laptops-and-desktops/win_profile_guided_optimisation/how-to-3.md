---
title: Create a baseline benchmark
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you'll create a baseline benchmark to measure the performance of a division operation. This baseline allows you to measure the improvement when you apply profile-guided optimization in the next section.

Integer division is ideal for benchmarking because it's significantly more expensive than operations like addition, subtraction, or multiplication. On most CPU architectures, including Arm, division instructions have higher latency and lower throughput compared to other arithmetic operations. By applying Profile-Guided Optimization to code containing division operations, you can achieve significant performance improvements.

For this example, you'll use an Arm computer running Windows.

## Set up Google Benchmark on Windows on Arm

Before you can run benchmarks, you need to install vcpkg (a C++ package manager) and Google Benchmark. This is a one-time setup step.

### Install vcpkg and Google Benchmark

The following commands download and initialize vcpkg, create a project directory, and install Google Benchmark for Windows on Arm:

```console
iex (iwr -useb https://aka.ms/vcpkg-init.ps1)
cd $HOME
mkdir pgo-benchmark
cd pgo-benchmark
& "$HOME\.vcpkg\vcpkg.exe" new --application
& "$HOME\.vcpkg\vcpkg.exe" add port benchmark
& "$HOME\.vcpkg\vcpkg.exe" install
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

## Compile the baseline benchmark with MSVC

Open an **ARM64 Native Tools Command Prompt** from the Windows Start menu and start PowerShell:

```console
powershell
```

Set an environment variable to refer to the vcpkg-installed package directory for the ARM64 Windows target. This simplifies the compiler commands that follow:

```console
$VCPKG="$HOME\pgo-benchmark\vcpkg_installed\arm64-windows"
```

Compile the benchmark. This command uses the MSVC compiler and links with the Google Benchmark libraries:

```console
cl /I"$VCPKG\include" /D BENCHMARK_STATIC_DEFINE div_bench.cpp /link /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

## Run the benchmark

Add the vcpkg binary directory to your PATH so the program can find required DLLs, then run the benchmark:

```console
$env:PATH += ";$HOME\pgo-benchmark\vcpkg_installed\arm64-windows\bin"
.\div_bench.exe
```

The output is similar to:

```output
Running ./div_bench.exe
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

The warning appears because the Google Benchmark library was built in debug mode, but it doesn't affect the validity of the measurements for this example.

## What you've accomplished and what's next

You've set up Google Benchmark on Windows on Arm, created a division-heavy benchmark, and established a baseline performance measurement of 7.90 microseconds. This baseline gives you a clear reference point to measure the impact of Profile-Guided Optimization. In the next section, you'll apply PGO to this code and measure the performance improvement.