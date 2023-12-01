---
title: BOLT with ETM
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## BOLT with ETM

Steps to optimise executable with BOLT using Perf ETM

### Collect Perf Samples

Run your executable in the normal use case and collect a ETM performance profile. This will output a `perf.data` file containing the profile and will be used to optimise the executable.

Record ETM while running executable

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0/u -o perf.data -- ./executable
```

Perf writes records to `perf.data`

```output
[ perf record: Woken up 10 times to write data ]
[ perf record: Captured and wrote 1.254 MB perf.data ]
```

### Convert Profile into BOLT format

`perf2bolt` converts the profile into a BOLT data format. For ETM data `perf2bolt` finds all branches pointers in the profile, maps them back to the executable assembly and keeps outputs a count of how many times each assembly branch was taken.

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata --itrace=l64i1us ./executable
```

Output from `perf2bolt`, it has read 2366 samples and 151118 Last Branch Records and created `perf.fdata`.

```output
BOLT-INFO: shared object or position-independent executable detected
PERF2BOLT: Starting data aggregation job for perf.data
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
PERF2BOLT: wrote 401 objects and 0 memory objects to perf.fdata
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

This outputs the new optimised executable `new_executable`.

### Using ETM AutoFDO

ETM AutoFDO is an perf record method similar to ETM that performs trace strobing to collect small slices of trace. This reduces the amount of data recorded per second and that allows it to be run for longer periods compared to ETM and creates much smaller files. 

```bash { target="ubuntu:latest" }
perf record -e cs_etm/@tmc_etr0,autofdo/u -o perf.data -- ./executable
```

```output
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.021 MB perf.data ]
```

The output shows that much less data was written to `perf.data` for the same executable

The BOLT steps are the same as ETM above.

```bash { target="ubuntu:latest" }
perf2bolt -p perf.data -o perf.fdata --itrace=l64i1us ./executable
llvm-bolt ./executable -o ./new_executable -data perf.fdata -reorder-blocks=ext-tsp -reorder-functions=hfsort -split-functions -split-all-cold -split-eh -dyno-stats
```
