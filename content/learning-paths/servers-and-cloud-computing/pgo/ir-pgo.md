---
title: Optimize with IR-PGO
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is IR-PGO?

IR-PGO uses instrumentation at the LLVM IR level to collect execution counts by adding counters before LLVM optimizes the IR.

Compared to FE-PGO, it usually has lower instrumentation overhead, generates smaller profiles, and is generally the better choice for optimization.

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

After the program exits, the raw profiles are written to:

```bash
ls prof/ir/*.profraw
```

## Merge, Convert, and Inspect the profile data

When profile filename patterns are used, Clang can write multiple raw `.profraw` files. This is useful when profiling multiple processes, collecting profiles on different hosts, running the program multiple times, or avoiding profile file overwrites in parallel runs. For more information, see [Clang profile filename patterns](https://clang.llvm.org/docs/UsersManual.html#profiling-with-instrumentation).

Before Clang can use the profile during an optimized build, merge the raw profiles with `llvm-profdata`. This step also converts them to the `.profdata` format used during optimization.


```bash
llvm-profdata merge  prof/ir -output=prof/ir.profdata
```

You can inspect the merged profile to see block counts. In the example below, the function `sort_array` has 6 counters with several recorded hits. You can inspect all functions with `--all-functions`, but the output can be extensive for large applications.

```bash { command_line="user@host | 2-8" }
llvm-profdata show --counts --function=sort_array prof/ir.profdata
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

## Build with IR-PGO and LTO

Build the optimized binary using the merged profile:

```bash
clang++ -O3 -flto -fuse-ld=lld -fprofile-use=prof/ir.profdata \
        bsort.cpp -o out/bsort.irpgo.opt
```

Run the optimized binary:

```bash
./out/bsort.irpgo.opt
```


## What you've learned and what's next

You've collected an IR-PGO profile, merged it with `llvm-profdata`, and used it with Thin-LTO to build an optimized binary.

Next, you'll extend the IR-PGO workflow with a context-sensitive profiling pass.
