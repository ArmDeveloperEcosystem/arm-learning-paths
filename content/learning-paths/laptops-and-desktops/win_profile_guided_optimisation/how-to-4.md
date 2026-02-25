---
title: Apply Profile-Guided Optimization
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Now that you have a baseline benchmark, you're ready to apply Profile-Guided Optimization. The PGO process involves three steps: build an instrumented binary, run it to collect profile data, and rebuild with optimizations based on that data.

## Build the instrumented binary

You should already have an ARM64 Native Tools Command Prompt open with PowerShell running from the previous section.

Set the environment variable to refer to the vcpkg installation directory:

```console
$VCPKG="$HOME\pgo-benchmark\vcpkg_installed\arm64-windows"
```

Build the instrumented binary with the `/GENPROFILE` flag. This creates a version of your program that records how it executes:

```console
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench.exe div_bench.cpp /link /LTCG /GENPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

This command uses several important compiler and linker options. The `/O2` flag creates fast code, while `/GL` enables whole program optimization. The `/GENPROFILE` linker option generates a `.pgd` file for PGO, and `/LTCG` specifies link time code generation. The `/PGD` option specifies the database file where profile data will be stored.

## Collect profile data

Run the instrumented binary to generate profile data:

```console
.\div_bench.exe
```

This execution creates profile data files (typically with a `.pgc` extension) in the same directory. The profile data captures information about which code paths execute most frequently and how the program behaves at runtime.

## Rebuild with optimizations

Now recompile the program using the `/USEPROFILE` flag to apply optimizations based on the collected data:

```console
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench_opt.exe div_bench.cpp /link /LTCG:PGOptimize /USEPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

The `/USEPROFILE` linker option instructs the linker to enable PGO with the profile generated during the previous run. The compiler can now make informed decisions about code layout, inlining, and other optimizations based on actual runtime behavior.

## Measure the improvement

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

The average execution time is reduced from 7.90 to 2.86 microseconds, which is a 64% improvement. This significant gain occurs because the profile data informed the compiler that the input divisor was consistently 1500 during the profiled runs, allowing it to apply specific optimizations that wouldn't be possible with static analysis alone.

You've successfully used Profile-Guided Optimization to improve performance on Windows on Arm. This same technique can be applied to your own performance-critical code to achieve similar improvements.
