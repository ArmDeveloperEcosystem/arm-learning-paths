---
title: Optimize with BRBE profiling
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is BRBE?
BRBE stands for Branch Record Buffer Extension. It is an Arm hardware unit with a circular buffer that captures the most recent 32 or 64 taken branches. The exact size depends on the hardware implementation.

For BOLT, BRBE provides an efficient and low-overhead way to collect profiling data. The hardware records taken branches directly without requiring frequent interrupts or instrumentation. Each recorded taken branch represents a control-flow edge, which makes BRBE an edge-based profiling method.

Taken branches are continuously added to the circular buffer, and the buffer is periodically sampled to keep overheads low.
Recording only taken branches is an efficient use of the buffer, since fall-through paths do not need to be captured at runtime.
During post-processing, fall-through edges between the recorded taken branches are reconstructed, extending the effective branch history beyond what is stored in the buffer. BOLT performs this reconstruction automatically.

## When to use BRBE
When available, BRBE is the preferred profiling option for BOLT.
It is expected to have the lowest runtime overhead while still providing near-optimal profiles, close to those obtained with instrumentation.

## Check BRBE availability
BRBE is an optional processor feature called **FEAT_BRBE** (Branch Record Buffer Extension), introduced in the [Armv9.1 architecture](https://developer.arm.com/documentation/109697/2025_09/Feature-descriptions/The-Armv9-2-architecture-extension#extension__feat_FEAT_BRBE). 
To check whether your system supports BRBE, attempt to record a branch profile using `perf`.

If BRBE is available, the command records the branch samples successfully:

```bash { command_line="user@host | 2-5"}
perf record -j any,u -o prof/brbe.data -- ./out/bsort
Bubble sorting 10000 elements
421 ms (first=100669 last=2147469841)
[ perf record: Woken up 161 times to write data ]
[ perf record: Captured and wrote 40.244 MB brbe.data (26662 samples) ]
```

If the processor or kernel does not support BRBE, perf reports an error similar to the following:

```bash { command_line="user@host | 2-3"}
perf record -j any,u -o prof/brbe.data -- ./out/bsort
Error:
cycles:P: PMU Hardware or event type doesn't support branch stack sampling.
```

Recording BRBE profiles requires a Linux kernel version 6.17 or later.
Check your kernel version with:
```bash
uname -r
```
## Optimize with BRBE
After confirming the availability of BRBE on your system, you can now collect a BRBE profile by running the workload under `perf`. Then convert the collected profile into the format that BOLT expects and run the BOLT optimizer.

```bash { line_numbers=true }
mkdir -p prof
perf record -j any,u -o prof/brbe.data -- ./out/bsort
perf2bolt -p prof/brbe.data -o prof/brbe.fdata out/bsort
llvm-bolt out/bsort -o out/bsort.opt.brbe --data prof/brbe.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

## What you've learned and what's next

You've collected a BRBE profile and used it to optimize the binary with BOLT. BRBE provides high-quality control-flow profiles with minimal runtime overhead.

You can now explore alternative profiling methods (instrumentation, SPE, or PMU) or proceed directly to verify the optimization results.
