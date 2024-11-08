---
title: Use BOLT with SPE
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with SPE

{{% notice Important Note %}}
Currently, BOLT may not generate a faster binary when using Perf SPE due to limitations within `perf` and BOLT itself.
For more information and the latest updates see: [[AArch64] BOLT does not support SPE branch data](https://github.com/llvm/llvm-project/issues/115333).
{{% /notice %}}

The steps to use BOLT with Perf SPE are listed below.

### Collect Perf data with SPE 

Run your executable in the normal use case and collect a SPE performance profile. This will output a `perf.data` file containing the profile and will be used to optimize the executable.

Record samples while running your application. Substitute the actual name of your application for `executable`:

```bash { target="ubuntu:latest" }
perf record -e arm_spe/branch_filter=1/u -o perf.data-- ./executable
```

Perf prints the size of the `perf.data` file:

```output
[ perf record: Woken up 79 times to write data ]
[ perf record: Captured and wrote 4.910 MB perf.data ]
```

### Convert the Profile into BOLT format

`perf2bolt` converts the profile into a BOLT data format. For the given sample data, `perf2bolt` finds all instruction pointers in the profile, maps them back to the assembly instructions, and outputs a count of how many times each assembly instruction was sampled.

If you application is named `executable`, run the commend below to convert the profile data:

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata -nl ./executable
```

Below is example output from `perf2bolt`, it has read all samples and created the file `perf.fdata`.

```output
BOLT-INFO: shared object or position-independent executable detected
PERF2BOLT: Starting data aggregation job for perf.data
PERF2BOLT: spawning perf job to read events without LBR
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
PERF2BOLT: parsing basic events (without LBR)...
PERF2BOLT: waiting for perf mem events collection to finish...
PERF2BOLT: parsing memory events...
PERF2BOLT: processing basic events (without LBR)...
PERF2BOLT: read 79 samples
PERF2BOLT: out of range samples recorded in unknown regions: 5 (6.3%)
PERF2BOLT: wrote 14 objects and 0 memory objects to perf.fdata
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
