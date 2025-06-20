---
title: Use BOLT with SPE
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with SPE
The steps to use BOLT with Perf SPE are listed below.

### Collect Perf data with SPE

First, make sure you are using Linux Perf version v6.14 or later, which supports the 'brstack' field and captures all branch information.

```bash { output_lines = "2" }
perf --version
perf version 6.14
```

Next, run your executable in the normal use case to collect an SPE performance profile. This generates a `perf.data` file containing the profile, which will be used to optimize the executable.

Record samples while running your application, replacing `executable`  below:

```bash { target="ubuntu:latest" }
perf record -e 'arm_spe/branch_filter=1/u' -o perf.data -- ./executable
```
Once the execution is complete, perf will print a summary that includes the size of the `perf.data` file:

```bash { target="ubuntu:latest" }
[ perf record: Woken up 79 times to write data ]
[ perf record: Captured and wrote 4.910 MB perf.data ]
```

The `-jitter=1` flag can help avoid resonance, while `-c`/`--count` controls the sampling period.

### Convert the Profile to BOLT format

`perf2bolt` converts the profile into BOLT's data format. It maps branch events from the profile to assembly instructions and outputs branch execution traces with sample counts.

If you application is named `executable`, run the command below to convert the profile data:

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata --spe ./executable
```

Below is example output from `perf2bolt`, it has read all samples from `perf.data` and created the converted profile `perf.fdata`.

```output
BOLT-INFO: shared object or position-independent executable detected
PERF2BOLT: Starting data aggregation job for perf.data
PERF2BOLT: spawning perf job to read SPE brstack events
PERF2BOLT: spawning perf job to read mem events
PERF2BOLT: spawning perf job to read process events
PERF2BOLT: spawning perf job to read task events
BOLT-INFO: Target architecture: aarch64
BOLT-INFO: BOLT version: b1516a9d688fed835dce5efc614302649c3baf0e
BOLT-INFO: first alloc address is 0x0
BOLT-INFO: creating new program header table at address 0x4600000, offset 0x4600000
BOLT-INFO: enabling relocation mode
BOLT-INFO: enabling strict relocation mode for aggregation purposes
BOLT-INFO: pre-processing profile using perf data aggregator
BOLT-INFO: binary build-id is:     8bb7beda9bae10bc546eace62775dd2958a9c940
PERF2BOLT: spawning perf job to read buildid list
PERF2BOLT: matched build-id and file name
PERF2BOLT: waiting for perf mmap events collection to finish...
PERF2BOLT: parsing perf-script mmap events output
PERF2BOLT: waiting for perf task events collection to finish...
PERF2BOLT: parsing perf-script task events output
PERF2BOLT: input binary is associated with 1 PID(s)
PERF2BOLT: waiting for perf events collection to finish...
PERF2BOLT: SPE branch events in LBR-format...
PERF2BOLT: read 3592267 samples and 3046129 LBR entries
PERF2BOLT: ignored samples: 0 (0.0%)
PERF2BOLT: waiting for perf mem events collection to finish...
PERF2BOLT: parsing memory events...
PERF2BOLT: processing branch events...
PERF2BOLT: traces mismatching disassembled function contents: 0
PERF2BOLT: out of range traces involving unknown regions: 0
PERF2BOLT: wrote 21027 objects and 0 memory objects to perf.fdata
BOLT-INFO: 2178 out of 72028 functions in the binary (3.0%) have non-empty execution profile
BOLT-INFO: 12 functions with profile could not be optimized
BOLT-INFO: Functions with density >= 0.0 account for 99.00% total sample counts
```

### Run BOLT to generate the optimized executable

The final step is to generate a new executable using `perf.fdata`.

To run BOLT use the command below and substitute the name of your application:

```bash { target="ubuntu:latest" }
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

The output from `llvm-bolt` describes the executable stats before and after optimization:

```output
BOLT-INFO: shared object or position-independent executable detected
BOLT-INFO: Target architecture: aarch64
BOLT-INFO: BOLT version: c66c15a76dc7b021c29479a54aa1785928e9d1bf
BOLT-INFO: first alloc address is 0x0
BOLT-INFO: creating new program header table at address 0x200000, offset 0x200000
BOLT-INFO: enabling relocation mode
BOLT-INFO: disabling -align-macro-fusion on non-x86 platform
BOLT-INFO: pre-processing profile using branch profile reader
BOLT-INFO: operating with basic samples profiling data (no LBR).
BOLT-INFO: number of removed linker-inserted veneers: 0
BOLT-INFO: 7 out of 52 functions in the binary (13.5%) have non-empty execution profile
BOLT-INFO: removed 1 empty block
BOLT-INFO: basic block reordering modified layout of 7 functions (100.00% of profiled, 11.11% of total)
BOLT-INFO: 1 Functions were reordered by LoopInversionPass
BOLT-INFO: program-wide dynostats after all optimizations before SCTC and FOP:

               19000 : executed forward branches
                   0 : taken forward branches
               55000 : executed backward branches
               17000 : taken backward branches
                   0 : executed unconditional branches
               22000 : all function calls
                2000 : indirect calls
                   0 : PLT calls
              310000 : executed instructions
               75000 : executed load instructions
                   0 : executed store instructions
                   0 : taken jump table branches
                   0 : taken unknown indirect branches
               74000 : total branches
               17000 : taken branches
               57000 : non-taken conditional branches
               17000 : taken conditional branches
               74000 : all conditional branches
                   0 : linker-inserted veneer calls

               57000 : executed forward branches (+200.0%)
                   0 : taken forward branches (=)
               17000 : executed backward branches (-69.1%)
               17000 : taken backward branches (=)
                   0 : executed unconditional branches (=)
               22000 : all function calls (=)
                2000 : indirect calls (=)
                   0 : PLT calls (=)
              384000 : executed instructions (+23.9%)
               75000 : executed load instructions (=)
                   0 : executed store instructions (=)
                   0 : taken jump table branches (=)
                   0 : taken unknown indirect branches (=)
               74000 : total branches (=)
               17000 : taken branches (=)
               57000 : non-taken conditional branches (=)
               17000 : taken conditional branches (=)
               74000 : all conditional branches (=)
                   0 : linker-inserted veneer calls (=)

BOLT-INFO: Starting stub-insertion pass
BOLT-INFO: Inserted 0 stubs in the hot area and 0 stubs in the cold area. Shared 0 times, iterated 1 times.
BOLT-INFO: padding code to 0x600000 to accommodate hot text
BOLT-INFO: setting _end to 0x600f20
BOLT-INFO: setting __hot_start to 0x400000
BOLT-INFO: setting __hot_end to 0x4002b0
BOLT-INFO: patched build-id (flipped last bit)
```

The optimized executable is now available as `new_executable`.
