---
title: Optimize with PMU profiling
weight: 8

### FIXED, DO NOT MODIFY

layout: learningpathall

---

## What is PMU?
The PMU (Performance Monitoring Unit) is a hardware component that records microarchitectural events during program execution. It supports event-based sampling of events such as instructions, cycles, cache accesses, and branches. Most Arm processors provide a PMU, which makes this profiling method widely available.

For BOLT, PMU provides samples that capture coarse hotness information. Samples are associated with instruction addresses and therefore with basic blocks, which are straight-line sequences of instructions that always execute in full once entered. This indicates how often those blocks run, rather than how control flows between them.
For this reason, PMU profiling is often referred to as *basic sampling* rather than *edge sampling*. While it is possible to sample branch events using the PMU, these samples do not include branch target information and therefore do not provide control-flow edge information.

Because functions consist of many basic blocks, PMU sampling can provide useful information at the function level. This makes it suitable for coarse-grained optimizations such as function reordering, but can be less effective for fine-grained block layout. Increasing the sampling frequency can improve coverage, but at the cost of higher profile collection overhead.

## When to use PMU
Use PMU profiling when BRBE and SPE are unavailable and instrumentation is not practical for the workload.
PMU provides the least detailed control-flow information among the profiling methods described here. Because it samples instruction addresses rather than control-flow edges, it mainly reveals which parts of the program execute frequently.
For this reason, PMU profiling typically serves as a fallback option for BOLT when more informative profiling methods are not available.

## Check PMU availability
All Arm systems that support the Linux perf tool provide access to PMU events. PMU profiling does not require any additional hardware features beyond standard performance monitoring support.

## Optimize with PMU
Record a PMU profile by running the workload under `perf`. Then convert the recorded profile into a format that BOLT understands and run the BOLT optimizer.
The example uses instruction sampling, which attributes samples to the instructions that were executing when the sampling event occurred.
The process consists of three steps:
  * Record a PMU profile using perf
  * Convert the profile into BOLT’s .fdata format
  * Run BOLT to generate an optimized binary

```bash { line_numbers=true }
mkdir -p prof
perf record -e instructions:u -o prof/pmu.data -- ./out/bsort
perf2bolt out/bsort -p prof/pmu.data -o prof/pmu.fdata --ba
llvm-bolt out/bsort -o out/bsort.opt.pmu --data prof/pmu.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

The `perf record` command collects samples of the instructions event in user space.
The `perf2bolt` tool converts the collected samples into BOLT’s .fdata profile format using the --ba option, which interprets the samples as basic-block counts.
Finally, `llvm-bolt` uses the generated profile to reorganize functions and basic blocks in the binary, producing an optimized binary named `out/bsort.opt.pmu`.
## What you've learned and what's next

You've collected a PMU profile and generated an optimized binary using basic sampling. While PMU provides less detailed control-flow information than BRBE or SPE, it's available on all Arm systems.

Now you're ready to verify how effective the BOLT optimization was by measuring performance improvements.