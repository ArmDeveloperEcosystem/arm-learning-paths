---
title: Optimize with instrumentation profiling
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is instrumentation?

Instrumentation is a profiling technique that inserts counters into a program to record how often different parts of the code execute. Unlike sampling-based methods, instrumentation collects exact execution counts.

BOLT can instrument a binary to record control-flow behavior such as how often basic blocks and edges execute. This produces a complete execution profile, which allows BOLT to make highly accurate code layout decisions.

Because instrumentation records exact execution counts, it often produces near-optimal profiles for code layout optimization. It does not require specialized hardware support.

However, instrumentation increases the size of the binary and adds extra instructions that update profiling counters. These changes can introduce significant runtime overhead, which makes instrumentation less suitable for production workloads.

Developers typically use instrumentation when other profiling methods, such as BRBE, are unavailable or when they want to measure the maximum optimization potential of BOLT.

## Optimize with instrumentation
First, generate an instrumented version of the binary. BOLT inserts counters into the program to record how often different code paths execute.
Next, run the instrumented program to collect the execution profile.
By default, BOLT writes the profile to `/tmp/prof.fdata`. You can specify a different location using the `--instrumentation-file` option.
Finally, run BOLT again and provide the collected profile to produce an optimized binary.

```bash
llvm-bolt --instrument out/bsort -o out/bsort.instr
./out/bsort.instr
llvm-bolt out/bsort -o out/bsort.opt.instr --data /tmp/prof.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```
This process produces an optimized binary named out/bsort.opt.instr, which uses the collected execution profile to improve code layout.
