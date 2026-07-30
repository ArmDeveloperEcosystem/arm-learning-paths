---
title: Optimize with CSIR-PGO
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is CSIR-PGO?

CSIR-PGO extends IR-PGO by adding a second, context-sensitive profiling pass.
The first pass is the standard IR-PGO instrumentation pass. The second pass instruments the program after inlining, which enables LLVM to distinguish execution counts from different calling contexts.
The additional context can improve optimization when function behavior depends on the call site, but it does not guarantee better performance for every program.

Use CSIR-PGO when you want to provide LLVM with more detailed profile information and can afford an extra build and training run.

## Build the context-sensitive instrumented binary

First, generate a standard IR-PGO profile as described in the [previous section](/learning-paths/servers-and-cloud-computing/pgo/ir-pgo/).
We reuse the resulting `prof/ir.profdata` profile to build a second instrumented binary with `-fcs-profile-generate`, which adds context-sensitive instrumentation after inlining.

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-use=prof/ir.profdata \
    -fcs-profile-generate=prof/csir \
    bsort.cpp -o out/bsort.csirpgo.instr
```

Run the context-sensitive instrumented binary:

```bash
./out/bsort.csirpgo.instr
```

After the program exits, the raw profiles are written to:

```bash
ls prof/csir/*.profraw
```

## Merge, Convert, and Inspect the profile

As with IR-PGO, the context-sensitive training run can produce one or more raw `.profraw` files. Merge those files together with the existing `prof/ir.profdata` profile using `llvm-profdata` before using the merged profile during the final optimized build.


```bash
llvm-profdata merge prof/ir.profdata prof/csir -output=prof/csir.profdata
```

You can inspect the merged profile to see block counts. In the example below, the function `sort_array` has 6 context-sensitive counters with several recorded hits. You can inspect all functions with `--all-functions`, but the output can be extensive for large applications.

```bash { command_line="user@host | 2-13" }
llvm-profdata show --showcs --counts --function=sort_array prof/csir.profdata
Counters:
  ld-temp.o;_Z10sort_arrayPi:
    Hash: 0x18c2aba34f0cfff9
    Counters: 6
    Block counts: [24763682, 25224415, 9999, 9882, 1, 9881]
Instrumentation level: IR  entry_first = 0  instrument_loop_entries = 0
Functions shown: 1
Total functions: 12
Maximum function count: 24763682
Maximum internal block count: 25224415
Total number of blocks: 32
Total count: 75242276
```

## Build with CSIR-PGO and LTO

Build the optimized binary using the merged CS-IR profile:


```bash
clang++ -O3 -flto -fuse-ld=lld -fprofile-use=prof/csir.profdata \
        bsort.cpp -o out/bsort.csirpgo.opt
```

Run the optimized binary:

```bash { command_line="user@host | 2-3" }
./out/bsort.opt.csir
```

## What you've learned and what's next

You've added a second context-sensitive profiling pass on top of IR-PGO and built a CSIR-PGO optimized binary with LTO.
