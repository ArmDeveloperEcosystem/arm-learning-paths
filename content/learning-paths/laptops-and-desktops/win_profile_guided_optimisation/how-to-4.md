---
title: Apply Profile-Guided Optimization
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Now that you have a baseline benchmark, you're ready to apply Profile-Guided Optimization. The PGO process involves three steps: build an instrumented binary, run it to collect profile data, and rebuild with optimizations based on that data.

## Build instrumented binary with MSVC

Open an **ARM64 Native Tools Command Prompt** from the Windows Start menu and start PowerShell if it's not already open. If you're starting a new session, navigate to your project directory and set the `$VCPKG` environment variable again:

```console
powershell
cd $HOME\pgo-benchmark
$VCPKG="$HOME\pgo-benchmark\vcpkg_installed\arm64-windows"
```

Build the instrumented binary with the `/GENPROFILE` flag. This creates a version of your program that records how it executes:

```console
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench.exe div_bench.cpp /link /LTCG /GENPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

This command uses several important compiler and linker options. The `/O2` flag creates fast code, while `/GL` enables whole program optimization. The `/GENPROFILE` linker option generates a `.pgd` file for PGO, and `/LTCG` specifies link time code generation. The `/PGD` option specifies the database file where profile data will be stored.

## Collect PGO profile data on Windows on Arm

Run the instrumented binary to generate profile data:

```console
.\div_bench.exe
```

This execution creates profile data files (typically with a `.pgc` extension) in the same directory. The profile data captures information about which code paths execute most frequently and how the program behaves at runtime.

## Rebuild with PGO optimizations

Now recompile the program using the `/USEPROFILE` flag to apply optimizations based on the collected data:

```console
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench_opt.exe div_bench.cpp /link /LTCG:PGOptimize /USEPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

The `/USEPROFILE` linker option instructs the linker to enable PGO with the profile generated during the previous run. The compiler can now make informed decisions about code layout, inlining, and other optimizations based on actual runtime behavior.

## Measure PGO performance gains

Run the optimized binary to see the performance improvement:

```console
.\div_bench_opt.exe
```

The output is similar to:

```output
Running ./div_bench.opt
Run on (4 X 2100 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x4)
  L1 Instruction 64 KiB (x4)
  L2 Unified 1024 KiB (x4)
  L3 Unified 32768 KiB (x1)
Load Average: 0.10, 0.03, 0.01
***WARNING*** Library was built as DEBUG. Timings may be affected.
-------------------------------------------------------
Benchmark             Time             CPU   Iterations
-------------------------------------------------------
baseDiv/1500       2.86 us         2.86 us       244429
```

The warning appears because the Google Benchmark library was built in debug mode, but it doesn't affect the validity of the measurements.

The average execution time is reduced from 7.90 to 2.86 microseconds, which is a 64% improvement. This result was measured on a Windows on Arm device with Visual Studio 2022 (MSVC 17.0) using the division benchmark with a constant divisor of 1500. Your results may vary depending on your specific hardware and workload.

The compiler used the profile data to determine that the divisor was consistently 1500, enabling optimizations that wouldn't be possible with static analysis alone.

## What you've accomplished

You've applied PGO to reduce execution time by 64% on a division-heavy benchmark. You completed the full PGO workflow: instrument, profile, and optimize. Apply this same technique to performance-critical sections of your own code to achieve similar gains on Windows on Arm.