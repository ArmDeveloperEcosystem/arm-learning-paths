---
title: Optimize with CSIR-PGO
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is CSIR-PGO?

Context-sensitive IR PGO (CSIR-PGO) extends IR-PGO by adding a second, context-sensitive profiling pass.
The first pass is the standard IR-PGO instrumentation pass. The second pass instruments the program after inlining, which enables LLVM to distinguish execution counts from different calling contexts.

The additional context can improve optimization when a function's behavior depends on its call site. It does not guarantee better performance for every program.

Use CSIR-PGO when you want to provide LLVM with more detailed profile information and can afford an extra build and training run.

## Build the context-sensitive instrumented binary

First, generate `prof/ir.profdata` by completing the [IR-PGO workflow](/learning-paths/servers-and-cloud-computing/pgo/ir-pgo/). Use that profile to guide inlining while Clang builds a second instrumented binary. The `-fcs-profile-generate` option adds context-sensitive counters after inlining:

```bash
clang++ -O3 -flto=thin -fuse-ld=lld \
    -fprofile-use=prof/ir.profdata \
    -fcs-profile-generate=prof/csir \
    bsort.cpp -o out/bsort.csirpgo.instr
```

Run the context-sensitive instrumented binary:

```bash
./out/bsort.csirpgo.instr
```

Confirm that the training run created at least one context-sensitive raw profile:

```bash
ls prof/csir/*.profraw
```

## Merge and inspect the profiles

Merge the context-sensitive raw profiles with the original IR-PGO profile. The result contains counts from both instrumentation passes:

```bash
llvm-profdata merge prof/ir.profdata prof/csir -output=prof/csir.profdata
```

Inspect the context-sensitive execution counts recorded for `sort_array`:

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

The `--showcs` option selects context-sensitive records from the merged profile. Exact hashes and counts can vary with the LLVM version and training workload.

## Build with CSIR-PGO and LTO

Build the optimized binary using the merged CS-IR profile:


```bash
clang++ -O3 -flto=thin -fuse-ld=lld \
    -fprofile-use=prof/csir.profdata \
    bsort.cpp -o out/bsort.csirpgo.opt
```

If the profile doesn't match the source or build configuration, Clang emits a profile mismatch warning. A build without that warning confirms that Clang accepted the merged profile.

Run the optimized binary:

```bash
./out/bsort.csirpgo.opt
```

## What you've accomplished and what's next

You've added a second context-sensitive profiling pass on top of IR-PGO and built a CSIR-PGO optimized binary with LTO.

You can now apply the workflow that best matches your profiling environment to a representative workload from your own application.
