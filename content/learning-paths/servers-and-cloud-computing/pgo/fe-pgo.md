---
title: Optimize with FE-PGO
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is FE-PGO?

FE-PGO uses Clang frontend instrumentation to collect execution counts while the program runs. Clang adds the counters before lowering the program to LLVM IR, so the profile data maps closely to the source code. After the training run, Clang uses the collected profile during an optimized build.

Use FE-PGO when source-level profile information is important. For performance-focused PGO, IR-PGO and CSIR-PGO are usually better defaults and are covered next.

## Build the instrumented binary

Build an instrumented binary. The `-fprofile-instr-generate` option tells Clang to add frontend counters and write the raw profile.


```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-instr-generate=prof/fe.profraw \
    bsort.cpp -o out/bsort.fepgo.instr
```

Run the instrumented binary:

```bash
./out/bsort.fepgo.instr
```

After the program exits, the raw profile should be written to:

```bash
ls prof/fe.profraw
```


## Convert and Inspect the profile data

Before Clang can use the profile during an optimized build, convert it to the `.profdata` format.

```bash
llvm-profdata merge prof/fe.profraw -output=prof/fe.profdata
```
You can inspect the merged profile to see block counts. In the example below we see that the function `sort_array` had 2 counters with hits matching our problem size. You can observe every function using `--all-functions` but can generate a large output on big binaries.

```bash { command_line="user@host | 2-14" }
llvm-profdata show --counts --function=sort_array prof/fe.profdata
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

## Build with FE-PGO and LTO

Build the optimized binary using the converted profile:

```bash
clang++ -O3 -flto -fuse-ld=lld \
    -fprofile-instr-use=prof/fe.profdata \
    bsort.cpp -o out/bsort.fepgo.opt
```

Run the optimized binary:

```bash { command_line="user@host | 2-3" }
./out/bsort.fepgo.opt
```

## What you've learned and what's next


You've collected an FE-PGO profile, converted it with `llvm-profdata`, and used it with Thin-LTO to build an optimized binary.

Next, you'll build the same example with IR-PGO and Thin-LTO.
