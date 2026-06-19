---
title: Run the benchmark with default Go garbage collection settings
description: Run repeated Go benchmark samples with default GC settings, save runtime baselines, and capture CPU and heap profiles for analysis.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Confirm runtime tuning variables are unset

Before you run the benchmark, confirm that the shell isn't setting Go runtime tuning variables:

```bash
env | grep -E '^(GOGC|GOMEMLIMIT|GODEBUG|GOMAXPROCS)=' || true
```

The command shouldn't print any matching variables.

If it prints one or more variables, unset them:

```bash
unset GOGC
unset GOMEMLIMIT
unset GODEBUG
unset GOMAXPROCS
```

## Record the runtime baseline

Before running the benchmark, record the Go version, architecture, CPU count, and memory size:

```bash
cd $HOME/go-gc-default
{
    go version
    go env GOOS GOARCH
    nproc
    free -h
} | tee default_runtime_baseline.txt
```

The output is similar to:

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

Run the benchmark with repeated samples and save the output.  In this example, the benchmark runs for five seconds and repeats 10 times:

```bash
go test ./parsebench \
    -run '^$' \
    -bench BenchmarkParseAndAllocate \
    -benchmem \
    -count 10 \
    -benchtime=5s | tee default_gc_benchmark.txt
```

The output includes 10 lines of benchmark output, and is similar to:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
BenchmarkParseAndAllocate-4    29803    169823 ns/op    0.04553 gc/op    99843 stw-ns/GC    4544 stw-ns/op    163840 B/op    4098 allocs/op
BenchmarkParseAndAllocate-4    29912    170104 ns/op    0.04601 gc/op    98762 stw-ns/GC    4541 stw-ns/op    163840 B/op    4098 allocs/op
BenchmarkParseAndAllocate-4    29887    170211 ns/op    0.04578 gc/op    99102 stw-ns/GC    4538 stw-ns/op    163840 B/op    4098 allocs/op
...
PASS
ok      example.com/go-gc-default/parsebench    58.243s
```

The output is saved to a file that includes the following benchmark measurements: 
- operation time
- allocation rate
- allocation count
- GC cycles per operation
- pause time per operation
- pause time per GC cycle.

With the output saved, you can now aggregate the repeated samples with Benchstat:

```bash
benchstat default_gc_benchmark.txt | tee default_gc_benchstat.txt
```

Benchstat might scale nanosecond metrics to seconds in the summary. For example, raw `stw-ns/op` benchmark output can appear as `stw-sec/op` in the Benchstat table.

The output is similar to:

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

```bash
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

The output is similar to:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
BenchmarkParseAndAllocate-4        66757            179173 ns/op                 0.06936 gc/op       75968 stw-ns/GC          5269 stw-ns/op      163840 B/op           4098 allocs/op
PASS
```

Inspect the CPU profile to list the functions that consumed the most CPU time during benchmark execution, ranked from highest to lowest:

```bash
go tool pprof -top ./parsebench.test cpu_default.out | tee cpu_default_top.txt
```

The output is similar to:

```output
File: parsebench.test
Build ID: dda39872c1dff6ff2f22c39246cb2d89979b90e0
Type: cpu
Time: 2026-06-17 20:09:37 UTC
Duration: 13.78s, Total samples = 15.74s (114.21%)
Showing nodes accounting for 14.49s, 92.06% of 15.74s total
Dropped 162 nodes (cum <= 0.08s)
      flat  flat%   sum%        cum   cum%
     2.42s 15.37% 15.37%         5s 31.77%  runtime.concatstrings
     2.40s 15.25% 30.62%      2.40s 15.25%  internal/bytealg.IndexByteString
     1.05s  6.67% 37.29%      7.72s 49.05%  strings.genSplit
     0.86s  5.46% 42.76%      1.46s  9.28%  runtime.mallocgcTiny
     0.80s  5.08% 47.84%      2.71s 17.22%  runtime.mallocgcSmallScanNoHeader
```

Inspect the heap allocation profile to list the functions responsible for allocating the most total memory over the lifetime of the benchmark, ranked from highest to lowest:

```bash
go tool pprof -top -alloc_space ./parsebench.test mem_default.out | tee mem_default_alloc_top.txt
```

The output is similar to:

```output
File: parsebench.test
Build ID: dda39872c1dff6ff2f22c39246cb2d89979b90e0
Type: alloc_space
Time: 2026-06-17 20:09:50 UTC
Showing nodes accounting for 11.69GB, 99.94% of 11.69GB total
Dropped 37 nodes (cum <= 0.06GB)
      flat  flat%   sum%        cum   cum%
    7.60GB 65.03% 65.03%     7.60GB 65.03%  strings.genSplit
    4.08GB 34.91% 99.94%    11.69GB 99.94%  example.com/go-gc-default/parsebench.BenchmarkParseAndAllocate
         0     0% 99.94%     2.90GB 24.80%  strings.Split (inline)
         0     0% 99.94%     4.70GB 40.22%  strings.SplitN (inline)
         0     0% 99.94%    11.69GB 99.94%  testing.(*B).launch
         0     0% 99.94%    11.69GB 99.95%  testing.(*B).runN
```

## What you've accomplished and what's next

You've now captured a default-GC benchmark result, a Benchstat summary, and CPU and heap profiles from the same workload. 

Next, you'll analyze the benchmark results.



