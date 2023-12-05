---
title: BOLT with Samples
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with Samples

Steps to optimise executable with BOLT using Perf Samples

### Collect Perf Samples

Run your executable in the normal use case and collect a samples performance profile. This will output a `perf.data` file containing the profile and will be used to optimise the executable.

Record samples while running executable

```bash { target="ubuntu:latest" }
perf record -e cycles:u -o perf.data -- ./executable
```

Perf outputs total samples taken and the size of the `perf.data` file

```output
[ perf record: Woken up 2 times to write data ]
[ perf record: Captured and wrote 0.381 MB perf.data (9957 samples) ]
```

### Convert Profile into BOLT format

`perf2bolt` converts the profile into a BOLT data format. For sample data `perf2bolt` finds all instruction pointers in the profile, maps them back to the executable assembly and keeps outputs a count of how many times each assembly instruction was sampled.

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata -nl ./executable
```

Output from `perf2bolt`, it has read all 9957 samples and created `perf.fdata`.

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
PERF2BOLT: processing basic events (without LBR)...
PERF2BOLT: read 9957 samples
PERF2BOLT: out of range samples recorded in unknown regions: 7 (0.1%)
PERF2BOLT: wrote 321 objects and 0 memory objects to perf.fdata
```

### Generate Optimised Executable

The final step is to generate a new executable using the `perf.fdata`.

```bash { target="ubuntu:latest" }
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```

Output from `llvm-bolt`, it describes the executable stats before & after optimisation.

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
BOLT-INFO: normalizing samples by instruction count.
BOLT-INFO: number of removed linker-inserted veneers: 0
BOLT-INFO: 15 out of 52 functions in the binary (28.8%) have non-empty execution profile
BOLT-INFO: removed 1 empty block
BOLT-INFO: basic block reordering modified layout of 11 functions (73.33% of profiled, 17.46% of total)
BOLT-INFO: 1 Functions were reordered by LoopInversionPass
BOLT-INFO: program-wide dynostats after all optimizations before SCTC and FOP:

              806550 : executed forward branches
              211117 : taken forward branches
             1302786 : executed backward branches
             1218161 : taken backward branches
               69927 : executed unconditional branches
               52487 : all function calls
               11166 : indirect calls
                   0 : PLT calls
             9949829 : executed instructions
             2116267 : executed load instructions
                   0 : executed store instructions
                   0 : taken jump table branches
                   0 : taken unknown indirect branches
             2179263 : total branches
             1499205 : taken branches
              680058 : non-taken conditional branches
             1429278 : taken conditional branches
             2109336 : all conditional branches
                   0 : linker-inserted veneer calls

             1094891 : executed forward branches (+35.7%)
               81610 : taken forward branches (-61.3%)
             1014445 : executed backward branches (-22.1%)
              877658 : taken backward branches (-28.0%)
              269990 : executed unconditional branches (+286.1%)
               52487 : all function calls (=)
               11166 : indirect calls (=)
                   0 : PLT calls (=)
            10514250 : executed instructions (+5.7%)
             2116267 : executed load instructions (=)
                   0 : executed store instructions (=)
                   0 : taken jump table branches (=)
                   0 : taken unknown indirect branches (=)
             2379326 : total branches (+9.2%)
             1229258 : taken branches (-18.0%)
             1150068 : non-taken conditional branches (+69.1%)
              959268 : taken conditional branches (-32.9%)
             2109336 : all conditional branches (=)
                   0 : linker-inserted veneer calls (=)

BOLT-INFO: Starting stub-insertion pass
BOLT-INFO: Inserted 0 stubs in the hot area and 0 stubs in the cold area. Shared 0 times, iterated 1 times.
BOLT-INFO: padding code to 0x600000 to accommodate hot text
BOLT-INFO: setting _end to 0x600fb0
BOLT-INFO: setting __hot_start to 0x400000
BOLT-INFO: setting __hot_end to 0x400d88
BOLT-INFO: patched build-id (flipped last bit)
```

This outputs the new optimised executable `new_executable`.
