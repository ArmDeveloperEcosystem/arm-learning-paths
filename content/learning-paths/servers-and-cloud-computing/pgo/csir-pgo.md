---
title: Optimize AArch64 code with CSIR-PGO
description: Build a context-sensitive IR-PGO profile from an existing IR-PGO profile, inspect its counters, and optimize AArch64 code with Clang and LTO.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What CSIR-PGO is

Context-sensitive Intermediate Representation-level Profile-Guided Optimization (CSIR-PGO) extends IR-PGO by adding a second, context-sensitive profiling pass.

The first pass is the standard IR-PGO instrumentation pass. The second pass instruments the program after inlining, enabling LLVM to distinguish execution counts from different calling contexts.

{{% notice Note %}}
The additional context can improve optimization when a function's behavior depends on its call site. It doesn't guarantee better performance for every program.
{{% /notice %}}

Use CSIR-PGO when you want to provide LLVM with more detailed profile information and can afford an extra build and training run.

## Build the context-sensitive instrumented binary

First, generate `prof/ir.profdata` by completing the [IR-PGO workflow](/learning-paths/servers-and-cloud-computing/pgo/ir-pgo/). Use that profile to guide Clang's usual PGO-driven optimization decisions while it builds a second instrumented binary:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-use=prof/ir.profdata \
    -fcs-profile-generate=prof/csir \
    bsort.cpp -o out/bsort.csirpgo.instr
```
The `-fcs-profile-generate` option then adds context-sensitive counters after inlining.

Run the context-sensitive instrumented binary:

```bash
./out/bsort.csirpgo.instr
```

Confirm that the training run created at least one context-sensitive raw profile:

```bash
ls prof/csir/*.profraw
```

## Merge and inspect the profiles

Merge the context-sensitive raw profiles with the existing `prof/ir.profdata` profile:

{{% notice Important %}}
Don't merge only the `.profraw` files: the final CSIR-PGO profile needs counts from both instrumentation passes.
{{% /notice %}}

```bash
llvm-profdata merge prof/ir.profdata prof/csir -output=prof/csir.profdata
```

Inspect the context-sensitive execution counts recorded for `sort_array`. For this example, `sort_array` should have six context-sensitive counters:

```bash
llvm-profdata show --showcs --counts --function=sort_array prof/csir.profdata
```

The output is similar to:

```output
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

{{% notice Note %}}
The `--showcs` option selects context-sensitive records from the merged profile. Exact hashes and individual counter values can vary with the LLVM version and training workload.
{{% /notice %}}

## Build with CSIR-PGO and LTO

Build the optimized binary using the merged CSIR-PGO profile:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-use=prof/csir.profdata \
    bsort.cpp -o out/bsort.csirpgo.opt
```

Run the optimized binary:

```bash
./out/bsort.csirpgo.opt
```

## What you've accomplished and what's next

You've added a second context-sensitive profiling pass on top of IR-PGO and built a CSIR-PGO optimized binary with LTO.

You can now apply the workflow that best matches your profiling environment to a representative workload from your own application.
