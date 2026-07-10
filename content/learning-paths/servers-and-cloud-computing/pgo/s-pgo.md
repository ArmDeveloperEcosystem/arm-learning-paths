---
title: Optimize with S-PGO (AFDO)
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is S-PGO?

{{% notice Note %}}
S-PGO is also called Sample-PGO, AFDO, or AutoFDO in LLVM documentation and related tools.
{{% /notice %}}

S-PGO is sample-based profile-guided optimization.
Instead of adding software counters to the program, you run an optimized binary with a profiler such as Linux `perf`, which records hardware events while the program executes.
`llvm-profgen` converts the raw sample data into an LLVM sample profile. Clang then uses that profile during an optimized build with `-fprofile-sample-use`.

S-PGO requires hardware and operating system support for sampling.
It also uses debug information to map the collected samples back to functions and source locations.

## When to use S-PGO

Use S-PGO when you want lower profiling overhead than instrumentation-based PGO. A typical use case is collecting profile data in production environments, where instrumentation-based profiling can introduce too much overhead.


## Build a binary for sampling


Build the binary with optimization enabled and add the information needed to match the collected samples to the program.
This guide uses line-table debug information, profiling-specific debug information, unique internal names, and pseudo-probes.
For more information about these options, see the [Clang profile-guided optimization guide](https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization).

To generate the binary for sampling, run:

```
clang++ -O3 -flto=thin -fuse-ld=lld \
  -gline-tables-only \
  -fdebug-info-for-profiling \
  -funique-internal-linkage-names \
  -fpseudo-probe-for-profiling \
  bsort.cpp -o out/bsort.spgo
```

If your build system changes source paths between the profiling build and the optimized build, omit `-funique-internal-linkage-names` from both builds.

Check that the binary contains line-table information and pseudo-probe sections:

```bash { command_line="user@host | 2-5" }
llvm-readelf --sections out/bsort.spgo | grep -E 'debug_line|pseudo_probe'
  [28] .pseudo_probe_desc PROGBITS       0000000000000000 01cdce 000464 00      0   0  1
  [35] .debug_line       PROGBITS        0000000000000000 01da48 00049d 00      0   0  1
  [36] .debug_line_str   PROGBITS        0000000000000000 01dee5 000043 01  MS  0   0  1
  [37] .pseudo_probe     PROGBITS        0000000000000000 01df28 000199 00   L 13   0  1
```


## Collect a sampling profile

Collect a `perf` profile with branch stack data:

```bash { command_line="user@host | 2-5" }
perf record -j any,u -o prof/brbe.data -- ./out/bsort.spgo
Bubble sorting 10000 elements
140 ms (first=100669 last=2147469841)
[ perf record: Woken up 2 times to write data ]
[ perf record: Captured and wrote 0.438 MB prof/brbe.data (566 samples) ]
```

## Convert the sampling profile

Convert the raw `perf` data into an LLVM sample profile:


```
llvm-profgen \
    --binary=out/bsort.spgo \
    --perfdata=prof/brbe.data \
    --output=prof/brbe.data.prof
```

Inspect the generated sample profile:

```bash { command_line="user@host | 2-12" }
llvm-profdata show --sample --all-functions prof/brbe.data.prof | grep -E 'Function:|inlined callee:'
Function: main: CFG checksum 1688854155231231
  4: inlined callee: _ZL11start_timerv.__uniq.184325335692493633500970462303439801414: CFG checksum 281479271677951
  5: inlined callee: _Z10sort_arrayPi: CFG checksum 563057241526008
      8: inlined callee: _Z11bubble_sortPii: CFG checksum 281822477581176
  6: inlined callee: _ZL10stop_timerv.__uniq.184325335692493633500970462303439801414: CFG checksum 562954248388607
  7: inlined callee: _ZL16print_first_lastPKii.__uniq.184325335692493633500970462303439801414: CFG checksum 281546317938031
Function: _ZL5swap4PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap3PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap1PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap2PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
Function: _ZL5swap5PiS_.__uniq.184325335692493633500970462303439801414: CFG checksum 844617033839767
```

The output should show sample data for the workload. For large applications, the output can be extensive.


## Build with S-PGO and LTO

Build the optimized binary using the sample profile.

The `-fsample-profile-use-profi` option infers missing block and edge counts to improve profile quality.


```bash
clang++ -O3 -flto=thin -fuse-ld=lld \
    -fsample-profile-use-profi \
    -fdebug-info-for-profiling -funique-internal-linkage-names \
    -fpseudo-probe-for-profiling \
    -fprofile-sample-use=prof/brbe.data.prof \
    -Rpass=sample-profile-inline -fdiagnostics-show-hotness \
    bsort.cpp -o out/bsort.spgo.opt
```

Use `-Rpass=sample-profile-inline` and `-fdiagnostics-show-hotness` to emit optimization remarks and verify that Clang used the sample profile during optimization.

Example output:

```
bsort.cpp:107:5: remark: '_ZL11start_timerv.__uniq.184325335692493633500970462303439801414' inlined into 'main' to match profiling context with (cost=-14990, threshold=45)
      at callsite main:5:5; [-Rpass=sample-profile-inline]
  107 |     start_timer();
      |     ^

bsort.cpp:108:5: '_Z10sort_arrayPi' inlined into 'main' to match profiling context with (cost=-14945, threshold=45) at callsite main:6:5; (hotness: 1)
```

Finally, run the optimized binary:
```
./out/bsort.spgo.opt
```


## What you've learned and what's next

You've collected a sampled profile, converted it with `llvm-profgen`, and used it with Thin-LTO to build an optimized binary.

Next, you'll try FE-PGO with Thin-LTO.
