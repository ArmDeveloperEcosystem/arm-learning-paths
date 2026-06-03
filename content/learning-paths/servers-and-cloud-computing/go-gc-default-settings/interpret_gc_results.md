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

## Experiment with Code Changes that influence GC Behavior
Now that you have a baseline, you can experiment with code changes that influence GC behavior. For example, you could try:

## Challenge 1

You just found out that the payload size this benchmark is intended to represent is actually only 128 records instead of 2048. What changes can we make from the baseline to test whether optimizing for this smaller workload affects GC frequency, pause times, and overall application performance?

### Idea: Reduce the payload size

### How

```go
payload := strings.Repeat(
    "name=arm&runtime=go&gc=default&value=12345;",
    512,
)
```

### Why

A smaller payload creates fewer temporary objects and less garbage each iteration.

---

## Challenge 2

After profiling the application, you discover that the input payload rarely changes between requests. What modifications can we make to reuse preprocessing work and determine whether reducing repeated allocations improves GC behavior and throughput?

### Idea: Move `strings.Split(payload, ";")` outside the benchmark loop

### How

```go
parts := strings.Split(payload, ";")

b.ResetTimer()

for i := 0; i < b.N; i++ {
    ...
}
```

### Why

This avoids repeatedly allocating the same slice of records on every iteration.

---

## Challenge 3

The benchmark currently creates a new output buffer for every operation, but production code processes millions of requests using the same worker. How can we modify the benchmark to reuse memory and evaluate the impact on GC activity and memory consumption?

### Idea: Reuse the output slice

### How

```go
out := make([]string, 0, len(parts))

for i := 0; i < b.N; i++ {
    out = out[:0]
    ...
}
```

### Why

Reusing the backing array reduces allocations and GC pressure.

---

## Challenge 4

A CPU profile shows that string parsing is one of the hottest code paths in the application. What changes can we make to reduce temporary allocations during parsing and measure whether this reduces GC overhead?

### Idea: Replace `strings.SplitN()` with `strings.IndexByte()`

### How

```go
idx := strings.IndexByte(part, '=')
if idx >= 0 {
    key := part[:idx]
    value := part[idx+1:]
    ...
}
```

### Why

This avoids allocating a temporary `[]string` for every record processed.

---

## Challenge 5

Product requirements change and the application no longer needs to generate derived `"key:length"` strings. What modifications can we make to avoid unnecessary string allocations and test their effect on garbage collection performance?

### Idea: Avoid creating new strings in the hot loop

### How

```go
out = append(out, fields[0])
```

### Why

Instead of building `"key:length"` strings, store existing strings or simpler values to reduce allocations.

---

## Challenge 6

Usage analytics show that most customers send payloads that are half the size represented by the current benchmark. How can we adjust the workload to better reflect real-world traffic and evaluate whether the resulting reduction in allocations improves GC efficiency?

### Idea: Reduce the number of records processed

### How

```go
payload := strings.Repeat(
    "name=arm&runtime=go&gc=default&value=12345;",
    1024,
)
```

### Why

Fewer records means less allocation work and fewer GC cycles.