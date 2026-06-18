---
title: Create a Go garbage collection benchmark
description: Create and verify a Go benchmark that generates allocation pressure and reports garbage collection metrics on Arm Linux.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a benchmark module

Create a small Go benchmark module called `parsebench_test.go`. The high-level flow of the benchmark is:

1. Generate a large input string.
2. Repeatedly parse it and create new objects and strings.
3. Force memory allocations so the garbage collector has work to do.
4. Measure how long the workload takes.
5. Measure how much garbage collection (GC) activity occurred during the benchmark.
6. Report both performance metrics and GC metrics.

First, create the module directory and initialize it:

```bash
mkdir -p $HOME/go-gc-default/parsebench
cd $HOME/go-gc-default
go mod init example.com/go-gc-default
```

Then, create `parsebench_test.go`:

```bash
cat > parsebench/parsebench_test.go <<'EOF'
package parsebench

import (

	"runtime"
	"strconv"
	"strings"
	"testing"

)

// Global variable used to store benchmark results.

var sink []string

func BenchmarkParseAndAllocate(b *testing.B) {

	// Simulates a large payload by creating a large test string by
	// repeating the same key=value data many times.
	//
	// Example:
	// name=arm&runtime=go&gc=default&value=12345;
	//
	
	payload := strings.Repeat("name=arm&runtime=go&gc=default&value=12345;",2048)
	
	// Tells the benchmark framework to track memory allocations.
	//
	// This will show metrics such as allocations per operation, and bytes allocated per operation
	
	b.ReportAllocs()
	
	// Captures runtime memory statistics before the benchmark starts.  You'll later compare these values to see:
	// - how many GCs occurred
	// - how much pause time was spent in GC
	
	var before runtime.MemStats
	runtime.ReadMemStats(&before)
	
	// Resets benchmark timing so that any setup work performed won't be included in the benchmark measurements.
	
	b.ResetTimer()
	
	// Benchmark loop where the actual work is done.  The number of times this loop is
	// executed is controlled by the b.N variable.  The value of b.N is automatically chosen by the Go benchmark framework to obtain stable and statistically useful measurements.
	
	// The reason for this design is that timing a single operation is often unreliable. Running it many times reduces noise from:
	// - OS scheduling
	// - CPU frequency changes
	// - background processes

	for i := 0; i < b.N; i++ {
		// splits the large payload into individual records.
		// Example: "a=1;b=2;c=3;" becomes: ["a=1", "b=2", "c=3", ""]
		parts := strings.Split(payload, ";")
		// Creates a new slice to store parsed output.  This allocation is intentional for the benchmark to generate memory pressure and trigger GC activity.
		
		out := make([]string, 0, len(parts))
		
		// Processes each record.
		
		for _, part := range parts {
			// Ignores the empty string created by the trailing semicolon.
			if part == "" {
				continue
			}
			// Splits the string into key and value.
			
			fields := strings.SplitN(part, "=", 2)
			
			// Makes sure both key and value exist.
			if len(fields) == 2 {
				// Builds a new string containing: key:length_of_value. This creates additional allocations and string objects, increasing GC activity.
				out = append(out,fields[0]+":"+strconv.Itoa(len(fields[1])),)
			}
		}
		// Saves the result so the compiler can't eliminate the work as unused.
		sink = out
	}
	// Stops benchmark timing.
	// Everything that follows is measurement or reporting logic and shouldn't affect benchmark performance results.
	b.StopTimer()
	
	// Captures memory statistics after the benchmark completes.
	
	var after runtime.MemStats
	runtime.ReadMemStats(&after)
	
	// Number of benchmark operations executed.
	ops := float64(b.N)
	
	// Total number of GC cycles that occurred while the benchmark was running:
	
	gcCycles := after.NumGC - before.NumGC
	
	// Total "stop-the-world" pause time spent in GC. During these pauses, application execution is temporarily halted while the runtime performs parts of GC.
	
	pauseNs := after.PauseTotalNs - before.PauseTotalNs
	
	// Reports GC events per benchmark operation.  Example: 0.002 gc/op means one GC cycle every 500 operations.
	
	if ops > 0 {
		b.ReportMetric(float64(gcCycles)/ops, "gc/op")
	
		// Reports average GC pause time per operation.
		b.ReportMetric(float64(pauseNs)/ops, "stw-ns/op")
	}
	// Reports the average stop-the-world pause duration for each GC cycle if at least one GC occurred.
	if gcCycles > 0 {
		b.ReportMetric(
			float64(pauseNs)/float64(gcCycles),
			"stw-ns/GC",
		)
	}

}
EOF
```

The benchmark code is now ready. 

Run the following command to verify it executes without errors:

```bash
cd $HOME/go-gc-default
go test ./parsebench -run '^$' -bench BenchmarkParseAndAllocate -benchmem -count 1 -benchtime=2s
```

The output is similar to:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
BenchmarkParseAndAllocate-4    14014    170814 ns/op    0.04553 gc/op    102956 stw-ns/GC    4687 stw-ns/op    163840 B/op    4098 allocs/op
PASS
ok      example.com/go-gc-default/parsebench    4.127s
```

Your exact numbers will differ by instance type, Go version, operating system, and system load.  If this test run yields results with no errors, you're ready to move to the next section.

## What you've accomplished and what's next

You've now created a Go GC benchmark module.

Next, you'll run the benchmark with default GC settings. 

