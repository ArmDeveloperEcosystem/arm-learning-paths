---
title: Optimize with SPE profiling
weight: 7

### FIXED, DO NOT MODIFY

layout: learningpathall

---

## What is SPE?
SPE (Statistical Profiling Extension) is an Arm hardware profiling unit that collects statistical samples of program execution with very low runtime overhead.
SPE periodically samples microarchitectural events such as instruction execution, memory accesses, and branches. The processor records information about the sampled event in a trace buffer, which profiling tools later decode.

For BOLT, SPE branch samples are the relevant input as they provide an edge-based control-flow profile.
Unlike [BRBE](../brbe), SPE does not record sequences of taken branches. Instead, each sample describes only a single branch transition between two program locations, representing a single edge in the control-flow graph. Because of this limited context, SPE typically produces less detailed control-flow profiles than BRBE.

Some processors also support the Previous Branch Target (PBT) feature. PBT records the target of the most recently taken branch in addition to the sampled edge. This provides a depth-1 branch history, which slightly improves the quality of the reconstructed control-flow profile.

Even with PBT, SPE provides less branch history than BRBE, but it remains a useful profiling option when BRBE is not available.

## When to use SPE
SPE provides less detailed control-flow information than BRBE because it samples individual branch events rather than recording full branch histories. Despite this limitation, SPE can still capture useful branch behavior and guide code layout decisions.
Use SPE when BRBE is unavailable or when instrumentation overhead is too high for the workload. In these cases, SPE offers a practical compromise between profiling overhead and profile quality.

## Check SPE availability
SPE is an optional processor feature called **FEAT_SPE (Statistical Profiling Extension)**, introduced in the [Armv8.1 architecture](https://developer.arm.com/documentation/109697/2025_12/Feature-descriptions/The-Armv8-2-architecture-extension#md447-the-armv82-architecture-extension__feat_FEAT_SPE).
To check whether your system supports SPE, attempt to record an SPE trace using `perf`.

If SPE is available, the command records the trace successfully:

```bash { command_line="user@host | 2-5"}
perf record -e arm_spe/branch_filter=1/u -o prof/spe.data -- ./out/bsort
Bubble sorting 10000 elements
454 ms (first=100669 last=2147469841)
[ perf record: Woken up 7 times to write data ]
[ perf record: Captured and wrote 13.458 MB prof/spe.data ]
```

If the processor or kernel does not support SPE, perf reports an error similar to the following:
```bash { command_line="user@host | 2-12"}
perf record -e arm_spe/branch_filter=1/u -o prof/spe.data -- ./out/bsort

event syntax error: 'arm_spe/branch_filter=1/u'
                     \___ Bad event or PMU

Unable to find PMU or event on a PMU of 'arm_spe'
Run 'perf list' for a list of valid events

 Usage: perf record [<options>] [<command>]
    or: perf record [<options>] -- <command> [<options>]

    -e, --event <event>   event selector. use 'perf list' to list available events
```
This error indicates that the system does not expose the arm_spe PMU, which usually means that the processor or kernel does not support SPE profiling.

Recording SPE traces requires a Linux kernel version 6.14 or later. Check the kernel version with:
```bash
uname -r
```
## Optimize with SPE
Next, collect an SPE profile by running the workload under `perf`. Then convert the recorded trace into a format that BOLT can use and run the BOLT optimizer.
The process consists of three steps:
* Record an SPE profile using perf
* Convert the profile into BOLT’s .fdata format
* Run BOLT to generate an optimized binary.

```bash { line_numbers=true }
mkdir -p prof
perf record -e arm_spe/branch_filter=1/u -o prof/spe.data -- ./out/bsort
perf2bolt -p prof/spe.data -o prof/spe.fdata ./out/bsort --spe
llvm-bolt out/bsort -o out/bsort.opt.spe --data prof/spe.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

The `perf record` command collects branch samples using the SPE hardware profiler.
The `perf2bolt` tool converts the SPE trace into BOLT’s .fdata profile format, using the --spe option to interpret the samples correctly.
Finally, `llvm-bolt` uses the generated profile to reorganize functions and basic blocks in the binary, producing an optimized binary named `out/bsort.opt.spe`.


