---
title: "BOLT with BRBE"
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### What is BRBE
BRBE stands for Branch Record Buffer Extension. It is an Arm hardware unit with a circular buffer that captures the most recent 32 or 64 taken branches. The exact size depends on the hardware implementation.

For BOLT, BRBE provides an effective, low-overhead sampling mechanism that records taken branches directly in hardware without frequent interruptions. Each recorded taken branch represents a control-flow edge, which makes BRBE an edge-based profiling method.

Taken branches are continuously added to the circular buffer, and the buffer is periodically sampled to keep overheads low.
Recording only taken branches is an efficient use of the buffer, since fall-through paths do not need to be captured at runtime.
During post-processing, fall-through edges between the recorded taken branches are reconstructed, extending the effective branch history beyond what is stored in the buffer. BOLT performs this reconstruction automatically.

### When to use BRBE
When available, BRBE is the preferred profiling option for BOLT.
It is expected to have the lowest runtime overhead while still providing near-optimal profiles, close to those obtained with instrumentation.

### Optimizing with BRBE
We check [BRBE availability](#availability) before recording a profile.
We then record a BRBE profile by running our workload under perf, convert it into a format that BOLT understands, and run the BOLT optimization.

```bash { line_numbers=true }
mkdir -p prof
perf record -j any,u -o prof/brbe.data -- ./out/bsort
perf2bolt -p prof/brbe.data -o prof/brbe.fdata out/bsort
llvm-bolt out/bsort -o out/bsort.opt.brbe --data prof/brbe.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```


### Availability
BRBE is an optional feature in processors that implement [Armv9.1](https://developer.arm.com/documentation/109697/2025_09/Feature-descriptions/The-Armv9-2-architecture-extension#extension__feat_FEAT_BRBE) or later. To check availability, we record a trace.

On a successful recording we see:
```bash { command_line="user@host | 2-5"}
perf record -j any,u -o prof/brbe.data -- ./out/bsort
Bubble sorting 10000 elements
421 ms (first=100669 last=2147469841)
[ perf record: Woken up 161 times to write data ]
[ perf record: Captured and wrote 40.244 MB brbe.data (26662 samples) ]
```

When unavailable:
```bash { command_line="user@host | 2-3"}
perf record -j any,u -o prof/brbe.data -- ./out/bsort
Error:
cycles:P: PMU Hardware or event type doesn't support branch stack sampling.
```

To record a BRBE trace we need a Linux system that is version 6.17 or later. We can check the version using:
```bash
perf --version
```


### Further Reading
- [Arm Architecture Reference Manual for A-profile architecture](https://developer.arm.com/documentation/ddi0487/latest)
