---
title: Interpret the default GC results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Read the benchmark metrics

Open the Benchstat summary:

```console
cat default_gc_benchstat.txt
```

Use the metrics as follows:

| Metric | Read |
| --- | --- |
| `ns/op` | Time per completed operation. Lower is better for throughput. |
| `B/op` | Heap bytes allocated per operation. Lower usually reduces GC pressure. |
| `allocs/op` | Heap allocation count per operation. Lower usually reduces GC pressure. |
| `gc/op` | GC cycles per operation. Lower means GC runs less often per completed operation. |
| `stw-ns/op` or `stw-sec/op` | GC pause cost per operation. Lower means less stop-the-world pause time is paid per completed operation. |
| `stw-ns/GC` or `stw-sec/GC` | Pause cost per GC cycle. Lower means each GC cycle pauses for less time. |

These metrics answer different questions. For example, `stw-ns/GC` can increase while `stw-ns/op` stays flat or decreases if GC runs less often per completed operation.

## Read the profiles

Open the CPU profile summary:

```console
cat cpu_default_top.txt
```

Look for functions that dominate CPU time. In an allocation-heavy benchmark, you can expect to see time in string handling, allocation paths, and some runtime or GC support functions.

On the validated `m8g.xlarge` instance, the top CPU profile entries included string scanning, string concatenation, split handling, and allocation paths:

```output
      flat  flat%   sum%        cum   cum%
     2.45s 15.53% 15.53%      2.45s 15.53%  internal/bytealg.IndexByteString
     2.37s 15.02% 30.54%      4.65s 29.47%  runtime.concatstrings
     1.28s  8.11% 38.66%      8.07s 51.14%  strings.genSplit
     0.85s  5.39% 44.04%      1.35s  8.56%  runtime.mallocgcTiny
     0.72s  4.56% 53.36%      5.17s 32.76%  runtime.mallocgc
```

Open the heap allocation profile summary:

```console
cat mem_default_alloc_top.txt
```

Look for application functions that allocate the most heap memory. Reducing allocation volume in those functions usually gives the Go GC less work to do.

On the validated `m8g.xlarge` instance, the allocation profile showed that `strings.genSplit` and the benchmark function accounted for nearly all allocated bytes:

```output
      flat  flat%   sum%        cum   cum%
    7.57GB 64.49% 64.49%     7.57GB 64.49%  strings.genSplit
    4.16GB 35.45% 99.94%    11.74GB 99.94%  example.com/go-gc-default/parsebench.BenchmarkParseAndAllocate
         0     0% 99.94%     2.90GB 24.70%  strings.Split (inline)
         0     0% 99.94%     4.67GB 39.79%  strings.SplitN (inline)
```

## Keep this result as the baseline

This result is your default Go GC baseline on AWS Graviton. Keep the following files together when you compare future changes:

```output
default_runtime_baseline.txt
default_gc_benchmark.txt
default_gc_benchstat.txt
default_gc_profile_run.txt
cpu_default.out
cpu_default_top.txt
mem_default.out
mem_default_alloc_top.txt
```

When you test code changes, compare against this baseline before changing Go runtime settings. If you later tune `GOGC`, `GOMEMLIMIT`, `GODEBUG`, or `GOMAXPROCS`, treat that as a separate experiment because it changes the runtime operating mode.
