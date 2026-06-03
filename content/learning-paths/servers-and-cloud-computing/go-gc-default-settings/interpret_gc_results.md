---
title: Interpret the default GC results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding the benchmark metrics

To understand better what these benchmarks results are showing, firt open the Benchstat summary:

```bash
cat default_gc_benchstat.txt
```

The the metrics you see explain the following:

| Metric | Read |
| --- | --- |
| `ns/op` | Time per completed operation. Lower is better for throughput. |
| `B/op` | Heap bytes allocated per operation. Lower usually reduces GC pressure. |
| `allocs/op` | Heap allocation count per operation. Lower usually reduces GC pressure. |
| `gc/op` | GC cycles per operation. Lower means GC runs less often per completed operation. |
| `stw-ns/op` or `stw-sec/op` | GC pause cost per operation. Lower means less stop-the-world pause time is paid per completed operation. |
| `stw-ns/GC` or `stw-sec/GC` | Pause cost per GC cycle. Lower means each GC cycle pauses for less time. |

These metrics answer different questions. For example, `stw-ns/GC` can increase while `stw-ns/op` stays flat or decreases if GC runs less often per completed operation.

## Reading the profiles

 Next, open the CPU profile summary:

```bash
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

```bash
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

## Keeping a baseline to compare to future changes

These results show your default Go GC baseline stats for this benchmarking app on AWS Graviton. By keeping the following files together (eg, each stored in their own zip file, folder, etc) you can easily see how making code changes affects your apps overall performance:

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

Example of changes you can experiment with include:

### Simple changes that can improve GC performance

1. **Reduce the payload size**
   ```go
   payload := strings.Repeat(
       "name=arm&runtime=go&gc=default&value=12345;",
       512,
   )
   ```
   A smaller payload creates fewer temporary objects and less garbage each iteration.

2. **Move `strings.Split(payload, ";")` outside the benchmark loop**
   ```go
   parts := strings.Split(payload, ";")

   b.ResetTimer()

   for i := 0; i < b.N; i++ {
       ...
   }
   ```
   This avoids repeatedly allocating the same slice of records on every iteration.

3. **Reuse the output slice**
   ```go
   out := make([]string, 0, len(parts))

   for i := 0; i < b.N; i++ {
       out = out[:0]
       ...
   }
   ```
   Reusing the backing array reduces allocations and GC pressure.

4. **Replace `strings.SplitN()` with `strings.IndexByte()`**
   ```go
   idx := strings.IndexByte(part, '=')
   if idx >= 0 {
       key := part[:idx]
       value := part[idx+1:]
       ...
   }
   ```
   This avoids allocating a temporary `[]string` for every record processed.

5. **Avoid creating new strings in the hot loop**
   ```go
   out = append(out, fields[0])
   ```
   Instead of building `"key:length"` strings, store existing strings or simpler values to reduce allocations.

6. **Reduce the number of records processed**
   ```go
   payload := strings.Repeat(
       "name=arm&runtime=go&gc=default&value=12345;",
       1024, // instead of 2048
   )
   ```
   Fewer records means less allocation work and fewer GC cycles.

### Biggest GC wins

For this benchmark, the largest improvements typically come from:

- Moving `strings.Split(payload, ";")` outside the benchmark loop.
- Reusing the `out` slice instead of allocating a new one every iteration.
- Replacing `strings.SplitN()` with `strings.IndexByte()`.

When you test code changes, compare against this baseline before changing Go runtime settings. If you later tune `GOGC`, `GOMEMLIMIT`, `GODEBUG`, or `GOMAXPROCS`, treat that as a separate experiment because it changes the runtime operating mode.
