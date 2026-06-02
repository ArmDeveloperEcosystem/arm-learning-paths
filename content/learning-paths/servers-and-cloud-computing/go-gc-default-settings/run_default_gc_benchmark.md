---
title: Run the benchmark with default Go GC settings
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Confirm runtime tuning variables are unset

Before you run the benchmark, confirm that the shell is not setting Go runtime tuning variables:

```console
env | grep -E '^(GOGC|GOMEMLIMIT|GODEBUG|GOMAXPROCS)=' || true
```

The command should not print any matching variables.

If it prints one or more variables, unset them:

```console
unset GOGC
unset GOMEMLIMIT
unset GODEBUG
unset GOMAXPROCS
```

This keeps GC pacing, memory-limit behavior, debug behavior, and CPU parallelism at the Go runtime defaults.

## Record the runtime baseline

Record the Go version, architecture, CPU count, and memory size before the benchmark:

```console
cd $HOME/go-gc-default
{
    go version
    go env GOOS GOARCH
    nproc
    free -h
} | tee default_runtime_baseline.txt
```

On the validated `m8g.xlarge` instance, the output was:

```output
go version go1.26.3 linux/arm64
linux
arm64
4
               total        used        free      shared  buff/cache   available
Mem:            15Gi       841Mi        13Gi       1.1Mi       921Mi        14Gi
Swap:             0B          0B          0B
```

## Run repeated benchmark samples

Run the benchmark with repeated samples and save the output:

```console
go test ./parsebench \
    -run '^$' \
    -bench BenchmarkParseAndAllocate \
    -benchmem \
    -count 10 \
    -benchtime=5s | tee default_gc_benchmark.txt
```

The benchmark output includes operation time, allocation rate, allocation count, GC cycles per operation, pause time per operation, and pause time per GC cycle.

Summarize the repeated samples with Benchstat:

```console
benchstat default_gc_benchmark.txt | tee default_gc_benchstat.txt
```

Benchstat may scale nanosecond metrics to seconds in the summary. For example, raw `stw-ns/op` benchmark output can appear as `stw-sec/op` in the Benchstat table.

On the validated `m8g.xlarge` instance, the Benchstat summary was:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
                   │ default_gc_benchmark.txt │
                   │          sec/op          │
ParseAndAllocate-4                169.5µ ± 0%

                   │ default_gc_benchmark.txt │
                   │          gc/op           │
ParseAndAllocate-4                45.59m ± 0%

                   │ default_gc_benchmark.txt │
                   │        stw-sec/GC        │
ParseAndAllocate-4                99.55µ ± 3%

                   │ default_gc_benchmark.txt │
                   │        stw-sec/op        │
ParseAndAllocate-4                4.538µ ± 3%

                   │ default_gc_benchmark.txt │
                   │           B/op           │
ParseAndAllocate-4               160.0Ki ± 0%

                   │ default_gc_benchmark.txt │
                   │        allocs/op         │
ParseAndAllocate-4                4.098k ± 0%
```

## Capture CPU and heap profiles

Create a test binary and run one longer benchmark pass with CPU and heap profiles enabled:

```console
go test -c -o parsebench.test ./parsebench

./parsebench.test \
    -test.run '^$' \
    -test.bench BenchmarkParseAndAllocate \
    -test.benchmem \
    -test.count 1 \
    -test.benchtime 10s \
    -test.cpuprofile cpu_default.out \
    -test.memprofile mem_default.out | tee default_gc_profile_run.txt
```

Inspect the CPU profile:

```console
go tool pprof -top ./parsebench.test cpu_default.out | tee cpu_default_top.txt
```

Inspect the heap allocation profile:

```console
go tool pprof -top -alloc_space ./parsebench.test mem_default.out | tee mem_default_alloc_top.txt
```

You now have a default-GC benchmark result, a Benchstat summary, and CPU and heap profiles from the same workload.
