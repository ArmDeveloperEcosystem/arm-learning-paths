---
title: Create a Go GC benchmark
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a benchmark module

Create a small Go module for the benchmark:

```console
mkdir -p $HOME/go-gc-default/parsebench
cd $HOME/go-gc-default
go mod init example.com/go-gc-default
```

Create the benchmark file:

```console
cat > parsebench/parsebench_test.go <<'EOF'
package parsebench

import (
	"runtime"
	"strconv"
	"strings"
	"testing"
)

var sink []string

func BenchmarkParseAndAllocate(b *testing.B) {
	payload := strings.Repeat("name=arm&runtime=go&gc=default&value=12345;", 2048)

	b.ReportAllocs()

	var before runtime.MemStats
	runtime.ReadMemStats(&before)

	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		parts := strings.Split(payload, ";")
		out := make([]string, 0, len(parts))

		for _, part := range parts {
			if part == "" {
				continue
			}
			fields := strings.SplitN(part, "=", 2)
			if len(fields) == 2 {
				out = append(out, fields[0]+":"+strconv.Itoa(len(fields[1])))
			}
		}

		sink = out
	}
	b.StopTimer()

	var after runtime.MemStats
	runtime.ReadMemStats(&after)

	ops := float64(b.N)
	gcCycles := after.NumGC - before.NumGC
	pauseNs := after.PauseTotalNs - before.PauseTotalNs

	if ops > 0 {
		b.ReportMetric(float64(gcCycles)/ops, "gc/op")
		b.ReportMetric(float64(pauseNs)/ops, "stw-ns/op")
	}
	if gcCycles > 0 {
		b.ReportMetric(float64(pauseNs)/float64(gcCycles), "stw-ns/GC")
	}
}
EOF
```

This benchmark repeatedly parses and allocates strings. It reports the default Go benchmark metrics plus three GC-specific metrics:

| Metric | Meaning |
| --- | --- |
| `gc/op` | GC cycles per completed benchmark operation |
| `stw-ns/op` | GC stop-the-world pause nanoseconds per completed operation |
| `stw-ns/GC` | GC stop-the-world pause nanoseconds per GC cycle |

The benchmark reads `runtime.MemStats` before and after the timed loop. It does not set Go runtime tuning variables.

## Confirm the benchmark builds

Run one short benchmark pass:

```console
cd $HOME/go-gc-default
go test ./parsebench -run '^$' -bench BenchmarkParseAndAllocate -benchmem -count 1 -benchtime=2s
```

You should see output with `ns/op`, `B/op`, `allocs/op`, and the GC-specific metrics:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
BenchmarkParseAndAllocate-4    14014    170814 ns/op    0.04553 gc/op    102956 stw-ns/GC    4687 stw-ns/op    163840 B/op    4098 allocs/op
PASS
ok      example.com/go-gc-default/parsebench    4.127s
```

Your exact numbers will differ by instance type, Go version, operating system, and system load.
