---
title: Example operation
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optimizing costly division operations with Google Benchmark and PGO

In this section, you'll learn how to use Google Benchmark and Profile-Guided Optimization to improve the performance of a simple division operation. This example demonstrates how even seemingly straightforward operations can benefit from optimization techniques.

Integer division is ideal for benchmarking because it's significantly more expensive than operations like addition, subtraction, or multiplication. On most CPU architectures, including Arm, division instructions have higher latency and lower throughput compared to other arithmetic operations. By applying Profile-Guided Optimization to code containing division operations, we can potentially achieve significant performance improvements.

For this example, you can use an Arm computer (Linux or Windows).

## What tools are needed to run a Google Benchmark example on Linux?

Run the following commands to install the prerequisite packages:

```bash
sudo apt update
sudo apt install gcc g++ make libbenchmark-dev -y
```

## What tools are needed to run a Google Benchmark example on Windows?

Download the [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) to install the prerequisite packages.

Next, install the static version of Google Benchmark for Arm64 via vcpkg. Run the following commands in Powershell as Administrator:

```console
cd C:\git
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
.\vcpkg install benchmark:arm64-windows-static
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

To compile and run the microbenchmark on this function, you need to link with the correct libraries:

**(Linux)** Compile with the command:

```bash
g++ -O3 -std=c++17 div_bench.cpp -lbenchmark -lpthread -o div_bench.base
```

**(Windows)** Compile with the command:

```console
cl /D BENCHMARK_STATIC_DEFINE div_bench.cpp /link /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

**(Linux)** Run the program:

```bash
./div_bench.base
```

**(Windows)** Run the program:

```console
.\div_bench.exe
```

### Example output

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
