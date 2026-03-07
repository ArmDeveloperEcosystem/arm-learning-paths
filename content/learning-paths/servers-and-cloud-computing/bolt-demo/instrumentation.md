---
title: "BOLT with Instrumentation"
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What is instrumentation

Instrumentation is a profiling method, not specific to BOLT, that augments code with counters to record exact execution counts.

For BOLT, Instrumentation provides complete execution counts for the paths that run. This gives a near-optimal profile for code-layout optimization and therefore the highest optimization potential, without requiring special hardware.

Instrumentation can increase binary size and add significant runtime overhead, making it less attractive for production use. It is mainly used when other profiling methods, such as BRBE, are unavailable, or for comparison to understand the maximum optimization potential.

### Optimizing with instrumentation
We first build an instrumented binary and then execute the workload to generate a profile.
By default, BOLT writes the profile to `/tmp/prof.fdata`, unless a path is specified using the `--instrumentation-file` flag.
Finally, we use the generated profile to optimize the binary with BOLT.

```bash
llvm-bolt --instrument out/bsort -o out/bsort.instr
./out/bsort.instr
llvm-bolt out/bsort -o out/bsort.opt.instr --data /tmp/prof.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```
