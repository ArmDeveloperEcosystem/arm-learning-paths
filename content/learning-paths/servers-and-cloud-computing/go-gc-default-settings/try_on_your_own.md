---
title: Experiment with optimization ideas
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Experiment with GC optimizations

Now that you have a baseline, you can experiment with code changes that influence GC behavior. For each challenge, apply the suggested change to `parsebench/parsebench_test.go`, then re-run the benchmark and compare the results with Benchstat:

```bash
go test ./parsebench \
    -run '^$' \
    -bench BenchmarkParseAndAllocate \
    -benchmem \
    -count 10 \
    -benchtime=5s | tee modified_gc_benchmark.txt

benchstat default_gc_benchmark.txt modified_gc_benchmark.txt
```

Benchstat produces a side-by-side comparison. A negative percentage in `sec/op`, `B/op`, `allocs/op`, or `stw-sec/op` means the change reduced cost. A `~` means the difference is not statistically significant. For example, a successful reduction in allocation rate looks similar to this:

```output
                   │ default_gc_benchmark.txt │    modified_gc_benchmark.txt    │
                   │          sec/op          │   sec/op     vs base            │
ParseAndAllocate-4               169.5µ ± 0%   142.3µ ± 1%  -16.05% (p=0.000)

                   │ default_gc_benchmark.txt │    modified_gc_benchmark.txt    │
                   │           B/op           │    B/op      vs base            │
ParseAndAllocate-4               160.0Ki ± 0%   80.0Ki ± 0%  -50.00% (p=0.000)
```

## Challenge 1

You just found out that the payload size this benchmark is intended to represent is actually only 128 records instead of 2048. What changes can you make to test whether a smaller workload affects GC frequency, pause times, and overall application performance?

### Idea: Reduce the payload size

### How

**Before**

```go
payload := strings.Repeat(
    "name=arm&runtime=go&gc=default&value=12345;",
    2048,
)
```

**After**

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

After profiling the application, you discover that the input payload rarely changes between requests. What modifications can you make to reuse preprocessing work and determine whether reducing repeated allocations improves GC behavior and throughput?

### Idea: Move payload split logic outside the benchmark loop

### How

**Before**

```go
for i := 0; i < b.N; i++ {
    parts := strings.Split(payload, ";")

    out := make([]string, 0, len(parts))

    ...
}
```

**After**

```go
parts := strings.Split(payload, ";")

for i := 0; i < b.N; i++ {
    out := make([]string, 0, len(parts))

    ...
}
```

### Why

This avoids repeatedly allocating the same slice of records on every iteration.

---

## Challenge 3

The benchmark currently creates a new output buffer for every operation, but production code processes millions of requests using the same worker. How can you modify the benchmark to reuse memory and evaluate the impact on GC activity and memory consumption?

### Idea: Reuse the output slice

### How

**Before**

```go
for i := 0; i < b.N; i++ {
    out := make([]string, 0, len(parts))

    ...
}
```

**After**

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

A CPU profile shows that string parsing is one of the hottest code paths in the application. What changes can you make to reduce temporary allocations during parsing and measure whether this reduces GC overhead?

### Idea: Replace SplitN() with IndexByte()

### How

**Before**

```go
fields := strings.SplitN(part, "=", 2)

if len(fields) == 2 {
    out = append(
        out,
        fields[0]+":"+strconv.Itoa(len(fields[1])),
    )
}
```

**After**

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

### Why

This avoids allocating a temporary `[]string` for every record processed.

---

## Challenge 5

Product requirements change and the application no longer needs to generate derived `"key:length"` strings. What modifications can you make to avoid unnecessary string allocations and test their effect on garbage collection performance?

### Idea: Avoid creating new strings in the hot loop

### How

**Before**

```go
out = append(
    out,
    fields[0]+":"+strconv.Itoa(len(fields[1])),
)
```

**After**

```go
out = append(
    out,
    fields[0],
)
```

### Why

Instead of building `"key:length"` strings, store existing strings or simpler values to reduce allocations.

