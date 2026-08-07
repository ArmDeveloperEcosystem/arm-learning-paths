---
title: Optimize with FE-PGO
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is FE-PGO?

Frontend PGO (FE-PGO) adds counters before Clang lowers the source code to LLVM intermediate representation (IR). The counters collect execution frequencies while the instrumented program runs, and the resulting profile maps closely to source-level constructs.

Use FE-PGO when source-level profile information is important. For performance-focused PGO, IR-PGO and CSIR-PGO are usually better defaults and are covered next.

## Build the instrumented binary

Build an instrumented binary. The `-fprofile-instr-generate` option tells Clang to add frontend counters and write the raw profile to `prof/fe.profraw`:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-instr-generate=prof/fe.profraw \
    bsort.cpp -o out/bsort.fepgo.instr
```

Run the instrumented binary:

```bash
./out/bsort.fepgo.instr
```

Confirm that the training run created the raw profile:

```bash
ls prof/fe.profraw
```


## Convert and inspect the profile data

Before Clang can use the profile during an optimized build, convert it to the `.profdata` format.

```bash
llvm-profdata merge prof/fe.profraw -output=prof/fe.profdata
```

Inspect the execution counts recorded for `sort_array`:

```bash
llvm-profdata show --counts --function=sort_array prof/fe.profdata
```

The output is similar to:

```output
Counters:
  _Z10sort_arrayPi:
    Hash: 0x00000000000046d1
    Counters: 2
    Function count: 1
    Block counts: [10000]
Instrumentation level: Front-end
Functions shown: 1
Total functions: 16
Maximum function count: 5044883
Maximum internal block count: 49988097
Total number of blocks: 39
Total count: 100476579
```

The profile contains two frontend counters for `sort_array`. Exact hashes and counts can vary with the LLVM version and training workload. Use `--all-functions` to inspect the complete profile, but expect much more output for a large application.

## Build with FE-PGO and LTO

Build the optimized binary using the converted profile:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-instr-use=prof/fe.profdata \
    bsort.cpp -o out/bsort.fepgo.opt
```

If the profile doesn't match the source or build configuration, Clang emits a profile mismatch warning. A build without that warning confirms that Clang accepted the profile.

Run the optimized binary:

```bash
./out/bsort.fepgo.opt
```

## What you've accomplished and what's next

You've collected an FE-PGO profile, converted it with `llvm-profdata`, and used it with LTO to build an optimized binary.

Next, you'll build the same example with IR-PGO and LTO.
