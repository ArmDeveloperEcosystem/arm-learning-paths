---
title: Optimize AArch64 code with IR-PGO
description: Instrument an AArch64 binary at the LLVM IR level, merge and inspect its profile, and build an optimized binary with IR-PGO and LTO.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What IR-PGO is

Intermediate Representation-level Profile-Guided Optimization (IR-PGO) adds counters to LLVM IR before LLVM runs its optimization passes. The counters collect execution frequencies during the training run.

Compared with FE-PGO, IR-PGO usually has lower instrumentation overhead and creates smaller raw profiles. IR-PGO is generally the better instrumentation-based choice for optimization.

## Build the instrumented binary

Build an instrumented binary. The `-fprofile-generate` option tells LLVM to add IR-level counters and write raw profiles to the specified directory.

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-generate=prof/ir \
    bsort.cpp -o out/bsort.irpgo.instr
```

Run the instrumented binary:

```bash
./out/bsort.irpgo.instr
```

Confirm that the training run created at least one raw profile:

```bash
ls prof/ir/*.profraw
```

## Merge and inspect the profile data

With `-fprofile-generate=prof/ir`, Clang writes a uniquely named raw profile in the specified directory. Multiple training runs or processes can create or update profiles there without clobbering unrelated profile data. For more information, see [Clang profile filename patterns](https://clang.llvm.org/docs/UsersManual.html#profiling-with-instrumentation).

Before Clang can use the profile during an optimized build, merge the raw profiles with `llvm-profdata`:

```bash
llvm-profdata merge prof/ir -output=prof/ir.profdata
```
The merge step also converts the profiles to the `.profdata` format used during optimization.

Inspect the execution counts recorded for `sort_array`:

```bash
llvm-profdata show --counts --function=sort_array prof/ir.profdata
```

The output is similar to:

```output
Counters:
  _Z10sort_arrayPi:
    Hash: 0x08380d8f3e6d4c88
    Counters: 6
    Block counts: [9882, 49988097, 25224415, 10000, 1, 9882]
Instrumentation level: IR  entry_first = 0  instrument_loop_entries = 0
Functions shown: 1
Total functions: 13
Maximum function count: 9882
Maximum internal block count: 49988097
Total number of blocks: 38
Total count: 150915523
```

The profile contains six IR-level counters for `sort_array`. Exact hashes and counts can vary with the LLVM version and training workload. Use `--all-functions` to inspect the complete profile, but expect much more output for a large application.

## Build with IR-PGO and LTO

Build the optimized binary using the merged profile:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-use=prof/ir.profdata \
    bsort.cpp -o out/bsort.irpgo.opt
```

Run the optimized binary:

```bash
./out/bsort.irpgo.opt
```

## What you've accomplished and what's next

You've collected an IR-PGO profile, merged it with `llvm-profdata`, and used it with LTO to build an optimized binary.

Next, you'll extend the IR-PGO workflow with a context-sensitive profiling pass.
