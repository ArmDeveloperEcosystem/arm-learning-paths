---
title: Optimize with ETM profiling
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is ETM?

ETM (Embedded Trace Macrocell) is an Arm trace unit that can record instruction flow from a running program. Linux perf can collect ETM trace data and store it in a `perf.data` file, such as `prof/etm.data`.

For BOLT, ETM can provide detailed branch information that helps reconstruct control flow. This makes ETM useful for profile-guided code layout optimization, especially when you need richer trace information than basic PMU sampling provides.

ETM traces can be large, so this section also shows ETM AutoFDO, which uses trace strobing to collect smaller trace samples.

{{% notice Note %}}
The ETM commands in this section require hardware, kernel, and perf support for CoreSight ETM. Validate the workflow on your ETM-capable system before using it for performance conclusions.
{{% /notice %}}

## When to use ETM

Use ETM when your system exposes CoreSight ETM through Linux perf and you want detailed trace-based profile data for BOLT.

ETM can provide high-quality control-flow information, but it may generate large profile files and depends on CoreSight support in the hardware, kernel, and perf tools.

## Check ETM availability

ETM is exposed through Linux perf as a CoreSight event. Check whether your system supports ETM by running:

```bash
perf list | grep cs_etm
```

If ETM is available, the output is similar to:

```output
cs_etm//           [Kernel PMU event]
cs_etm/autofdo/    [Kernel PMU event]
```

If `cs_etm` is not listed, your system or perf installation might not expose CoreSight ETM tracing.
You might need to build a version of perf with Arm CoreSight enabled. For more information, see the [CoreSight perf documentation](https://docs.kernel.org/trace/coresight/coresight-perf.html).

AutoFDO is an alternative way to collect ETM data with small data sizes.
If `cs_etm/autofdo/` is not listed, update the Linux kernel and perf to 5.15 or later before using AutoFDO.

To confirm AutoFDO is working, run:

```bash
perf record -e cs_etm/autofdo/u -- echo "Hello World"
perf report -D | grep "CoreSight ETM"
```

The output should contain text similar to:

```output
. ... CoreSight ETMV4I Trace data: size 0x30 bytes
```

## Optimize with ETM

After confirming ETM availability, collect an ETM profile by running the workload under `perf`. Then convert the collected trace into the format that BOLT expects and run the BOLT optimizer.

```bash { line_numbers=true }
mkdir -p prof
perf record -e cs_etm//u -o prof/etm.data -- ./out/bsort
perf2bolt -p prof/etm.data -o prof/etm.fdata --itrace=l64i1us ./out/bsort
llvm-bolt ./out/bsort -o ./out/bsort.opt.etm --data prof/etm.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

The `perf record` command collects ETM trace data while running the workload.
The `perf2bolt` tool decodes the trace and converts it into BOLT's `.fdata` profile format.
Finally, `llvm-bolt` uses the generated profile to produce an optimized binary named `out/bsort.opt.etm`.

Example `perf2bolt` output is similar to:

```output
BOLT-INFO: shared object or position-independent executable detected
PERF2BOLT: Starting data aggregation job for prof/etm.data
PERF2BOLT: spawning perf job to read branch events with itrace
PERF2BOLT: spawning perf job to read mem events
PERF2BOLT: spawning perf job to read process events
PERF2BOLT: spawning perf job to read task events
BOLT-INFO: Target architecture: aarch64
BOLT-INFO: BOLT version: c66c15a76dc7b021c29479a54aa1785928e9d1bf
BOLT-INFO: first alloc address is 0x0
BOLT-INFO: creating new program header table at address 0x200000, offset 0x200000
BOLT-INFO: enabling relocation mode
BOLT-INFO: disabling -align-macro-fusion on non-x86 platform
BOLT-INFO: enabling strict relocation mode for aggregation purposes
BOLT-INFO: pre-processing profile using perf data aggregator
BOLT-INFO: binary build-id is:     21dbca691155f1e57825e6381d727842f3d43039
PERF2BOLT: spawning perf job to read buildid list
PERF2BOLT: matched build-id and file name
PERF2BOLT: waiting for perf mmap events collection to finish...
PERF2BOLT: parsing perf-script mmap events output
PERF2BOLT: waiting for perf task events collection to finish...
PERF2BOLT: parsing perf-script task events output
PERF2BOLT: input binary is associated with 1 PID(s)
PERF2BOLT: waiting for perf events collection to finish...
PERF2BOLT: parse branch events...
PERF2BOLT: read 2366 samples and 151118 LBR entries
PERF2BOLT: 0 samples (0.0%) were ignored
PERF2BOLT: traces mismatching disassembled function contents: 0 (0.0%)
PERF2BOLT: out of range traces involving unknown regions: 2325 (1.6%)
PERF2BOLT: waiting for perf mem events collection to finish...
PERF2BOLT: parsing memory events...
PERF2BOLT: processing branch events...
PERF2BOLT: wrote 401 objects and 0 memory objects to prof/etm.fdata
```

Example `llvm-bolt` output is similar to:

```output
BOLT-INFO: shared object or position-independent executable detected
BOLT-INFO: Target architecture: aarch64
BOLT-INFO: BOLT version: c66c15a76dc7b021c29479a54aa1785928e9d1bf
BOLT-INFO: first alloc address is 0x0
BOLT-INFO: creating new program header table at address 0x200000, offset 0x200000
BOLT-INFO: enabling relocation mode
BOLT-INFO: disabling -align-macro-fusion on non-x86 platform
BOLT-INFO: pre-processing profile using branch profile reader
BOLT-INFO: number of removed linker-inserted veneers: 0
BOLT-INFO: 24 out of 52 functions in the binary (46.2%) have non-empty execution profile
BOLT-INFO: 1 function with profile could not be optimized
BOLT-INFO: profile for 1 objects was ignored
BOLT-INFO: removed 1 empty block
BOLT-INFO: basic block reordering modified layout of 11 functions (45.83% of profiled, 17.46% of total)
BOLT-INFO: 0 Functions were reordered by LoopInversionPass
BOLT-INFO: program-wide dynostats after all optimizations before SCTC and FOP:

               88011 : executed forward branches
               20526 : taken forward branches
              130161 : executed backward branches
              101876 : taken backward branches
                8905 : executed unconditional branches
                9352 : all function calls
                1150 : indirect calls
                   8 : PLT calls
             1250176 : executed instructions
              184599 : executed load instructions
                   0 : executed store instructions
                   0 : taken jump table branches
                   0 : taken unknown indirect branches
              227077 : total branches
              131307 : taken branches
               95770 : non-taken conditional branches
              122402 : taken conditional branches
              218172 : all conditional branches
                   0 : linker-inserted veneer calls

               95483 : executed forward branches (+8.5%)
                8373 : taken forward branches (-59.2%)
              122689 : executed backward branches (-5.7%)
              100437 : taken backward branches (-1.4%)
                4144 : executed unconditional branches (-53.5%)
                9352 : all function calls (=)
                1150 : indirect calls (=)
                   8 : PLT calls (=)
             1241230 : executed instructions (-0.7%)
              184599 : executed load instructions (=)
                   0 : executed store instructions (=)
                   0 : taken jump table branches (=)
                   0 : taken unknown indirect branches (=)
              222316 : total branches (-2.1%)
              112954 : taken branches (-14.0%)
              109362 : non-taken conditional branches (+14.2%)
              108810 : taken conditional branches (-11.1%)
              218172 : all conditional branches (=)
                   0 : linker-inserted veneer calls (=)

BOLT-INFO: Starting stub-insertion pass
BOLT-INFO: Inserted 0 stubs in the hot area and 0 stubs in the cold area. Shared 0 times, iterated 1 times.
BOLT-INFO: padding code to 0x600000 to accommodate hot text
BOLT-INFO: setting _end to 0x600f98
BOLT-INFO: setting __hot_start to 0x400000
BOLT-INFO: setting __hot_end to 0x4014b0
BOLT-INFO: patched build-id (flipped last bit)
```

## Optimize with ETM AutoFDO

ETM AutoFDO performs trace strobing to collect small slices of ETM trace. This reduces the amount of data recorded per second, which can make longer profile collection runs more practical.

Record with AutoFDO while running the workload:

```bash
perf record -e cs_etm/autofdo/u -o prof/etm-autofdo.data -- ./out/bsort
```

Perf prints the size of the `prof/etm-autofdo.data` file:

```output
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.021 MB prof/etm-autofdo.data ]
```

The output shows that much less data was written for the same workload. The BOLT conversion and optimization steps are the same as the ETM flow:

```bash { line_numbers=true }
perf2bolt -p prof/etm-autofdo.data -o prof/etm-autofdo.fdata --itrace=l64i1us ./out/bsort
llvm-bolt ./out/bsort -o ./out/bsort.opt.etm-autofdo --data prof/etm-autofdo.fdata \
        -reorder-blocks=ext-tsp -reorder-functions=cdsort -split-functions \
        --dyno-stats
```

## What you've learned and what's next

You've collected an ETM trace and used it to optimize the binary with BOLT. ETM provides detailed trace-based profile information, while ETM AutoFDO can reduce profile data size by collecting smaller trace slices.

You can explore lower-overhead sampling methods or move on to verify the optimization results.
