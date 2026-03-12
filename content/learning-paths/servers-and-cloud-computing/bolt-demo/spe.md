---

title: "BOLT with SPE"

weight: 7

### FIXED, DO NOT MODIFY

layout: learningpathall

---

### What is SPE
SPE stands for Statistical Profiling Extension. It is an Arm hardware unit that provides low-overhead, statistical sampling of program execution.
SPE samples microarchitectural events such as instruction execution, memory accesses, and branches.

For BOLT, SPE branch samples are the relevant input as they provide an edge-based control-flow profile.
Unlike [BRBE](../brbe), SPE does not record sequences of taken branches.
Each sample captures only a single transition between two program locations, representing a single edge in the control-flow graph.

Some implementations also support the Previous Branch Target (PBT) feature.
This feature records 1 taken branch in addition to the edge.
This provides a depth-1 branch history. It extends standard SPE sampling but remains shallower than BRBE.

### When to use SPE
SPE provides less detailed control-flow information than BRBE. It can still capture useful branch behavior and guide code layout decisions, making it a good alternative when BRBE is unavailable or instrumentation overhead is prohibitive.

### Optimizing with SPE
We check [SPE availability](#availability) before recording a profile.
We then record an SPE profile by running our workload under perf, convert it into a format that BOLT understands, and run the BOLT optimization.

```bash { line_numbers=true }
mkdir -p prof
perf record -e arm_spe/branch_filter=1/u -o prof/spe.data -- ./out/bsort
perf2bolt -p prof/spe.data -o prof/spe.fdata ./out/bsort --spe
llvm-bolt out/bsort -o out/bsort.opt.spe --data prof/spe.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```


### Availability
SPE is an optional feature in processors that implement [Armv8.1](https://developer.arm.com/documentation/109697/2025_12/Feature-descriptions/The-Armv8-2-architecture-extension#md447-the-armv82-architecture-extension__feat_FEAT_SPE) or later. To check availability, we record a trace.

On a successful recording we see:
```bash { command_line="user@host | 2-5"}
perf record -e arm_spe/branch_filter=1/u -o prof/spe.data -- ./out/bsort
Bubble sorting 10000 elements
454 ms (first=100669 last=2147469841)
[ perf record: Woken up 7 times to write data ]
[ perf record: Captured and wrote 13.458 MB prof/spe.data ]
```

When unavailable:
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

To record an SPE trace we need a Linux system that is version 6.14 or later. We can check the version using:
```bash
perf --version
```


### Further Reading
- [Arm Statistical Profiling Extension: Performance Analysis Methodology White Paper](https://developer.arm.com/documentation/109429/latest/)
