---

title: "BOLT with PMU"

weight: 8

### FIXED, DO NOT MODIFY

layout: learningpathall

---

### What is PMU
PMU stands for Performance Monitoring Unit. It is an Arm hardware unit that provides event-based sampling of program execution.
PMU samples microarchitectural events such as instructions, cycles, branches, and other hardware events. This form of profiling is widely available across Arm systems.

For BOLT, PMU provides samples that capture coarse hotness information. Samples are associated with instruction addresses and therefore with *basic blocks*, which are straight-line sequences of instructions that always execute in full once entered. This indicates how often those blocks run, rather than how control flows between them.
For this reason, PMU profiling is often referred to as *basic sampling* rather than *edge sampling*. While it is possible to sample branch events using the PMU, these samples do not include branch target information and therefore still do not provide control-flow edge information.

Because functions consist of many basic blocks, PMU sampling can provide useful information at the function level. This makes it suitable for coarse-grained optimizations such as function reordering, but can be less effective for fine-grained block layout. Increasing the sampling frequency can improve coverage, but at the cost of higher profile collection overhead.

### When to use PMU
PMU is most useful when BRBE and SPE are unavailable and instrumentation is not feasible.
It provides the least detailed control-flow information among the available methods, so it is typically used as a fallback option.

### Optimizing with PMU
We record a PMU profile by running our workload under perf, convert it into a format that BOLT understands, and then run the BOLT optimization.
This tutorial uses instruction sampling.


```bash { line_numbers=true }
mkdir -p prof
perf record -e instructions:u -o prof/pmu.data -- ./out/bsort
perf2bolt out/bsort -p prof/pmu.data -o prof/pmu.fdata --ba
llvm-bolt out/bsort -o out/bsort.opt.pmu --data prof/pmu.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

### Availability
PMU events are available on all Arm systems that support perf. No additional hardware features are required.
