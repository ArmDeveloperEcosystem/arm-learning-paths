---
title: Interpret the default garbage collection benchmark results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the benchmark metrics

To understand what the benchmark results are showing, first open the Benchstat summary:

```bash
cat default_gc_benchstat.txt
```

The metrics you see explain the following:

| Metric | Read |
| --- | --- |
| `ns/op` | Time per completed operation. Lower is better for throughput. |
| `B/op` | Heap bytes allocated per operation. Lower usually reduces garbage collection (GC) pressure. |
| `allocs/op` | Heap allocation count per operation. Lower usually reduces GC pressure. |
| `gc/op` | GC cycles per operation. Lower means GC runs less often per completed operation. |
| `stw-ns/op` or `stw-sec/op` | GC pause cost per operation. Lower means less stop-the-world pause time is paid per completed operation. |
| `stw-ns/GC` or `stw-sec/GC` | Pause cost per GC cycle. Lower means each GC cycle pauses for less time. |

These metrics answer different questions. For example, `stw-ns/GC` can increase while `stw-ns/op` stays flat or decreases if GC runs less often per completed operation.

## Read the profiles

 Next, open the CPU profile summary:

```bash
cat cpu_default_top.txt
```

Look for functions that dominate CPU time. In an allocation-heavy benchmark, you can expect to see time in string handling, allocation paths, and some runtime or GC support functions.

The `flat` column shows CPU time spent directly in that function. The `cum` (cumulative) column includes time spent in the function and all functions it called. A function with low `flat` but high `cum` is spending most of its time in callees, which can point to allocation chains or deep call stacks.

On the validated `m8g.xlarge` instance, the top CPU profile entries included string scanning, string concatenation, split handling, and allocation paths:

```output
      flat  flat%   sum%        cum   cum%
     2.45s 15.53% 15.53%      2.45s 15.53%  internal/bytealg.IndexByteString
     2.37s 15.02% 30.54%      4.65s 29.47%  runtime.concatstrings
     1.28s  8.11% 38.66%      8.07s 51.14%  strings.genSplit
     0.85s  5.39% 44.04%      1.35s  8.56%  runtime.mallocgcTiny
     0.72s  4.56% 53.36%      5.17s 32.76%  runtime.mallocgc
```

`IndexByteString` and `concatstrings` dominate because the benchmark splits the payload with `strings.Split`, which scans for `;` byte-by-byte, and builds `key:length` strings with `+` concatenation on every iteration. These operations create a large volume of short-lived strings, giving the GC constant work to do. On Graviton, `pprof` makes these allocation chains directly visible because the Arm64 stack unwinder captures the full call path without frame pointer ambiguity.

Open the heap allocation profile summary and look for application functions that allocate the most heap memory. Reducing allocation volume in those functions usually gives the Go garbage collector less work to do.

On the validated `m8g.xlarge` instance, the allocation profile showed that `strings.genSplit` and the benchmark function accounted for nearly all allocated bytes:

```output
      flat  flat%   sum%        cum   cum%
    7.57GB 64.49% 64.49%     7.57GB 64.49%  strings.genSplit
    4.16GB 35.45% 99.94%    11.74GB 99.94%  example.com/go-gc-default/parsebench.BenchmarkParseAndAllocate
         0     0% 99.94%     2.90GB 24.70%  strings.Split (inline)
         0     0% 99.94%     4.67GB 39.79%  strings.SplitN (inline)
```

## Keep a baseline to compare to future changes

These results show your default Go GC baseline for this benchmarking app on AWS Graviton. By keeping the following files together — for example, in a versioned folder or archive — you can see how code changes affect overall performance:

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

## What you've accomplished and what's next

You've now interpreted a documented default GC baseline showing operation time, allocation rate, GC frequency, and stop-the-world pause costs on AWS Graviton.

Next, you'll apply code changes to the benchmark and measure how each change affects these metrics.
