---
title: Using Profile Guided Optimization (Windows)
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Build with PGO

To generate a binary optimized using runtime profile data, first build an instrumented binary that records usage data. Before building, open the Arm dev shell so that the compiler is in your PATH:

```bash
& "C:\Program Files\Microsoft Visual Studio\18\Community\Common7\Tools\Launch-VsDevShell.ps1" -Arch arm64
```

(**note:** you may need to change the version number in your Visual Studio path, depending on which Visual Studio version you've installed.)

Next, set an environment variable to refer to the installed packages directory:

```bash
$VCPKG="C:\git\vcpkg\installed\arm64-windows-static"
```

Next, run the following command, which includes the `/GENPROFILE` flag, to build the instrumented binary:

```bash
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench.exe div_bench.cpp /link /LTCG /GENPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

The compiler options used in this command are:

* **/O2**: Creates [fast code](https://learn.microsoft.com/en-us/cpp/build/reference/o1-o2-minimize-size-maximize-speed?view=msvc-170)
* **/GL**: Enables [whole program optimization](https://learn.microsoft.com/en-us/cpp/build/reference/gl-whole-program-optimization?view=msvc-170).
* **/D**: Enables the Benchmark [static preprocessor definition](https://learn.microsoft.com/en-us/cpp/build/reference/d-preprocessor-definitions?view=msvc-170).
* **/I**: Adds the arm64 includes to the [list of include directories](https://learn.microsoft.com/en-us/cpp/build/reference/i-additional-include-directories?view=msvc-170).
* **/Fe**: Specifies a name for the [executable file output](https://learn.microsoft.com/en-us/cpp/build/reference/fe-name-exe-file?view=msvc-170).
* **/link**: Specifies [options to pass to linker](https://learn.microsoft.com/en-us/cpp/build/reference/link-pass-options-to-linker?view=msvc-170).

The linker options used in this command are:

* **/LTCG**: Specifies [link time code generation](https://learn.microsoft.com/en-us/cpp/build/reference/ltcg-link-time-code-generation?view=msvc-170).
* **/GENPROFILE**: Specifies [generation of a .pgd file for PGO](https://learn.microsoft.com/en-us/cpp/build/reference/genprofile-fastgenprofile-generate-profiling-instrumented-build?view=msvc-170).
* **/PGD**: Specifies a [database for PGO](https://learn.microsoft.com/en-us/cpp/build/reference/pgd-specify-database-for-profile-guided-optimizations?view=msvc-170).
* **/LIBPATH**: Specifies the [additional library path](https://learn.microsoft.com/en-us/cpp/build/reference/libpath-additional-libpath?view=msvc-170).

Next, run the instrumented binary to generate the profile data:

```bash
.\div_bench.exe
```

This execution creates profile data files (typically with a `.pgc` extension) in the same directory. 

Now recompile the program using the `/USEPROFILE` flag to apply optimizations based on the collected data: 

```bash
cl /O2 /GL /D BENCHMARK_STATIC_DEFINE /I "$VCPKG\include" /Fe:div_bench_opt.exe div_bench.cpp /link /LTCG:PGOptimize /USEPROFILE /PGD:div_bench.pgd /LIBPATH:"$VCPKG\lib" benchmark.lib benchmark_main.lib shlwapi.lib
```

In this command, the [USEPROFILE linker option](https://learn.microsoft.com/en-us/cpp/build/reference/useprofile?view=msvc-170) instructs the linker to enable PGO with the profile generated during the previous run of the executable. 

### Run the optimized binary 

Now run the optimized binary:

```bash
.\div_bench_opt.exe
```

The following output shows the performance improvement:

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

As the terminal output above shows, the average execution time is reduced from 7.90 to 2.86 microseconds. This improvement occurs because the profile data informed the compiler that the input divisor was consistently 1500 during the profiled runs, allowing it to apply specific optimizations.
