---
title: Optimize AArch64 code with S-PGO
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What S-PGO is

{{% notice Note %}}
Sample-based Profile-Guided Optimization (S-PGO) is also called SamplePGO, AutoFDO, or AFDO in LLVM documentation and related tools.
{{% /notice %}}

Instead of adding software counters, S-PGO records hardware events while an optimized binary runs. This workflow uses Linux `perf` to collect branch-stack samples from the Arm Branch Record Buffer Extension (BRBE). The `llvm-profgen` tool converts the raw `perf` data into an LLVM sample profile. Clang then consumes that profile through `-fprofile-sample-use` during another optimized build.

This workflow needs a processor that implements BRBE and Linux kernel 6.17 or later. It also uses debug information and pseudo-probes to map sampled instructions back to functions and source locations.

## When to use S-PGO

Use S-PGO when you need lower profiling overhead than instrumentation-based PGO. It's suitable for long-running or production-like workloads where an instrumented binary would add too much overhead. Sample accuracy depends on collecting enough data from representative inputs.


## Build a binary for sampling

Build the binary with optimization enabled and add the metadata that LLVM needs to map samples back to the program. This example uses DWARF line tables, profiling-specific debug information, unique names for internal-linkage functions, and pseudo-probes.
For more information about these options, see the [Clang profile-guided optimization guide](https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization).

Build the binary for sampling:

```bash
clang++ -O3 -flto=thin -fuse-ld=lld \
  -gline-tables-only \
  -fdebug-info-for-profiling \
  -funique-internal-linkage-names \
  -fpseudo-probe-for-profiling \
  bsort.cpp -o out/bsort.spgo
```

{{% notice Note %}}
Clang derives unique internal-linkage names from the source path. If your build system uses an absolute source path that changes between the profiling and optimized builds, omit `-funique-internal-linkage-names` from both builds. Otherwise, the generated function names won't match the profile.
{{% /notice %}}

Check that the binary contains line-table information and pseudo-probe sections:

```bash
llvm-readelf --sections out/bsort.spgo | grep -E 'debug_line|pseudo_probe'
```

The output is similar to:

```output
  [28] .pseudo_probe_desc PROGBITS       0000000000000000 01cdce 000464 00      0   0  1
  [35] .debug_line       PROGBITS        0000000000000000 01da48 00049d 00      0   0  1
  [36] .debug_line_str   PROGBITS        0000000000000000 01dee5 000043 01  MS  0   0  1
  [37] .pseudo_probe     PROGBITS        0000000000000000 01df28 000199 00   L 13   0  1
```


## Collect a sampling profile

Collect a `perf` profile with user-space branch-stack data. The `-j any,u` option requests any branch type at privilege level `u`, which means user space:

```bash
perf record -j any,u -o prof/brbe.data -- ./out/bsort.spgo
```

The output is similar to:

```output
Bubble sorting 10000 elements
140 ms (first=100669 last=2147469841)
[ perf record: Woken up 2 times to write data ]
[ perf record: Captured and wrote 0.438 MB prof/brbe.data (566 samples) ]
```

The sample count and runtime are illustrative. They depend on the processor, sampling configuration, system load, and LLVM build.

{{% notice Note %}}
If `perf` reports that branch-stack sampling isn't supported or permitted, confirm the following:
 
  - Your processor implements BRBE
  - The kernel is version 6.17 or later
  - Your account can access performance events
{{% /notice %}}

## Convert the sampling profile

Convert the raw `perf` data into an LLVM sample profile:


```bash
llvm-profgen \
    --binary=out/bsort.spgo \
    --perfdata=prof/brbe.data \
    --output=prof/brbe.data.prof
```

Inspect the generated sample profile:

```bash
llvm-profdata show --sample --all-functions prof/brbe.data.prof | grep -E 'Function:|inlined callee:'
```

The output is similar to:

```output
Function: main: CFG checksum 1688854155231231
  4: inlined callee: _ZL11start_timerv.__uniq.184325335692493633500970462303439801414: CFG checksum 281479271677951
  5: inlined callee: _Z10sort_arrayPi: CFG checksum 563057241526008
      8: inlined callee: _Z11bubble_sortPii: CFG checksum 281822477581176
  6: inlined callee: _ZL10stop_timerv.__uniq.184325335692493633500970462303439801414: CFG checksum 562954248388607
  7: inlined callee: _ZL16print_first_lastPKii.__uniq.184325335692493633500970462303439801414: CFG checksum 281546317938031
Function: _ZL5swap4PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap3PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap1PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap2PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap5PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
```

The output lists functions and inlined call sites that received samples. Exact names, checksums, and counts can vary with the LLVM version and training workload. For large applications, the complete output can be extensive.

## Build with S-PGO and LTO

Build the optimized binary using the sample profile. Use the same pseudo-probe and internal-linkage-name options as the profiling build so Clang can correlate the profile with the program:

```bash
clang++ -O3 -flto=thin -fuse-ld=lld \
    -fsample-profile-use-profi \
    -fdebug-info-for-profiling -funique-internal-linkage-names \
    -fpseudo-probe-for-profiling \
    -fprofile-sample-use=prof/brbe.data.prof \
    -Rpass=sample-profile-inline -fdiagnostics-show-hotness \
    bsort.cpp -o out/bsort.spgo.opt
```
The `-fsample-profile-use-profi` option infers missing block and edge counts.

The `-Rpass=sample-profile-inline` and `-fdiagnostics-show-hotness` options emit optimization remarks. These remarks verify that Clang used the sample profile for inlining decisions.

The output is similar to:

```output
bsort.cpp:107:5: remark: '_ZL11start_timerv.__uniq.184325335692493633500970462303439801414' inlined into 'main' to match profiling context with (cost=-14990, threshold=45)
      at callsite main:5:5; [-Rpass=sample-profile-inline]
  107 |     start_timer();
      |     ^

bsort.cpp:108:5: remark: '_Z10sort_arrayPi' inlined into 'main' to match profiling context with (cost=-14945, threshold=45) at callsite main:6:5; (hotness: 1)
```

Run the optimized binary to confirm that it completes successfully:

```bash
./out/bsort.spgo.opt
```


## What you've accomplished and what's next

You've collected a sampled profile, converted it with `llvm-profgen`, and used it with Thin-LTO to build an optimized binary.

Next, you'll try FE-PGO with Thin-LTO.
