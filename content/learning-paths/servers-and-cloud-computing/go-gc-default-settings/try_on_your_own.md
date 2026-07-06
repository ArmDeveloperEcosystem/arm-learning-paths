---
title: Experiment with garbage collection optimization 
description: Apply controlled Go code changes to the benchmark and compare results with benchstat to evaluate effects on GC behavior.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Make code changes to influence garbage collection

Now that you have a baseline, you can experiment with code changes that influence garbage collection (GC) behavior. Apply one suggested change at a time to `parsebench/parsebench_test.go`, then re-run the benchmark and compare the results with Benchstat:

```bash
go test ./parsebench \
    -run '^$' \
    -bench BenchmarkParseAndAllocate \
    -benchmem \
    -count 10 \
    -benchtime=5s | tee modified_gc_benchmark.txt

benchstat default_gc_benchmark.txt modified_gc_benchmark.txt
```

Benchstat produces a side-by-side comparison. A negative percentage in `sec/op`, `B/op`, `allocs/op`, or `stw-sec/op` means the change reduced cost. A `~` means the difference is not statistically significant. 

For example, a successful reduction in allocation rate is similar to:

```output
                   │ default_gc_benchmark.txt │    modified_gc_benchmark.txt    │
                   │          sec/op          │   sec/op     vs base            │
ParseAndAllocate-4               169.5µ ± 0%   142.3µ ± 1%  -16.05% (p=0.000)

                   │ default_gc_benchmark.txt │    modified_gc_benchmark.txt    │
                   │           B/op           │    B/op      vs base            │
ParseAndAllocate-4               160.0Ki ± 0%   80.0Ki ± 0%  -50.00% (p=0.000)
```

### Reduce the payload size

Assume that the payload size this benchmark is intended to represent is only 512 records instead of 2048. 

To test whether a smaller workload affects GC frequency, pause times, and overall application performance, reduce the payload size from the following:

```go
payload := strings.Repeat(
    "name=arm&runtime=go&gc=default&value=12345;",
    2048,
)
```

To the following:

```go
payload := strings.Repeat(
    "name=arm&runtime=go&gc=default&value=12345;",
    512,
)
```

Reducing the payload size creates fewer temporary objects and less garbage each iteration, improving application performance.

### Move payload split logic outside the benchmark loop

Assume that after profiling the application, you discover that the input payload rarely changes between requests. 

To reuse preprocessing work, update split logic from the following:

```go
for i := 0; i < b.N; i++ {
    parts := strings.Split(payload, ";")

    out := make([]string, 0, len(parts))

    ...
}
```

To the following:

```go
parts := strings.Split(payload, ";")

for i := 0; i < b.N; i++ {
    out := make([]string, 0, len(parts))

    ...
}
```

By making this change, you can avoid repeatedly allocating the same slice of records on every iteration. Reducing repeated allocations improves GC behavior and throughput. 

### Reuse the output slice

The benchmark currently creates a new output buffer for every operation, but production code processes millions of requests using the same worker. 

To evaluate the impact on GC activity and memory consumption, update the code from the following:

```go
for i := 0; i < b.N; i++ {
    out := make([]string, 0, len(parts))

    ...
}
```

To the following:

```go
out := make([]string, 0, len(parts))

for i := 0; i < b.N; i++ {
    out = out[:0]

    ...
}
```

By modifying the benchmark to reuse the backing array, you can reduce allocations and GC pressure.

### Replace SplitN() with IndexByte()

Assume a CPU profile shows that string parsing is one of the hottest code paths in the application. 

To reduce temporary allocations during parsing, update the code from the following:

```go
fields := strings.SplitN(part, "=", 2)

if len(fields) == 2 {
    out = append(
        out,
        fields[0]+":"+strconv.Itoa(len(fields[1])),
    )
}
```

To the following:

```go
idx := strings.IndexByte(part, '=')

if idx >= 0 {
    key := part[:idx]
    value := part[idx+1:]

    out = append(
        out,
        key+":"+strconv.Itoa(len(value)),
    )
}
```

By making this update, you can avoid allocating a temporary `[]string` for every record processed.

### Avoid creating new strings in the hot loop

Assume product requirements change and the application no longer needs to generate derived `"key:length"` strings. 

To avoid unnecessary string allocations in such a scenario, update the code from the following:

```go
out = append(
    out,
    fields[0]+":"+strconv.Itoa(len(fields[1])),
)
```

To the following:

```go
out = append(
    out,
    fields[0],
)
```

By storing existing strings or simple values instead of building `"key:length"` strings, you can reduce allocations.

## What you've accomplished

You've now experimented with changing payload size, split logic, slice reuse, and string parsing to influence GC behavior.

You can continue experimenting with code changes to optimize GC behavior for your Go applications on Arm-based compute.
