---
title: Create a Go GC benchmark
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating a benchmark module

You'll first create a small Go benchmark module.  The high-level flow is:

1. Generate a large input string.
2. Repeatedly parse it and create new objects/strings.
3. Force memory allocations so the garbage collector has work to do.
4. Measure how long the workload takes.
5. Measure how much GC activity occurred during the benchmark.
6. Report both performance metrics and GC-related metrics.

Pasting the code below will create the module and benchmark file:

```bash

# Create the module directory and initialize it.

mkdir -p $HOME/go-gc-default/parsebench
cd $HOME/go-gc-default
go mod init example.com/go-gc-default

# Create the benchmark file:

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

	// This simulates a large payload by creating a large test string by
	// repeating the same key=value data many times.
	//
	// Example:
	// name=arm&runtime=go&gc=default&value=12345;
	//
	
	payload := strings.Repeat("name=arm&runtime=go&gc=default&value=12345;",2048)
	
	// Next, we tell the benchmark framework to track memory allocations.
	//
	// This will show metrics such as allocations per operation, and bytes allocated per operation
	
	b.ReportAllocs()
	
	// Capture runtime memory statistics before the benchmark starts.  We will later compare these
	// values to see:
	// - how many garbage collections occurred
	// - how much pause time was spent in GC
	
	var before runtime.MemStats
	runtime.ReadMemStats(&before)
	
	// Reset benchmark timing so that any setup work performed above will not be included
	// in the benchmark measurements.
	
	b.ResetTimer()
	
	// The benchmark loop is where the actual work is done.  The number of times this loop is
	// executed is controlled by the b.N variable.  The value of b.N is automatically chosen by
	// the Go benchmark framework to obtain stable and statistically useful measurements.
	
	// The reason for this design is that timing a single operation is often unreliable; running 
	// it many times reduces noise from:
	// * OS scheduling
	// * CPU frequency changes
	// * background processes

	for i := 0; i < b.N; i++ {
		// split the large payload into individual records.
		// Example:
		// "a=1;b=2;c=3;" becomes: ["a=1", "b=2", "c=3", ""]
		parts := strings.Split(payload, ";")
		// Create a new slice to store parsed output.  This allocation is intentional because we want
		// the benchmark to generate memory pressure and trigger garbage collection activity.
		
		out := make([]string, 0, len(parts))
		
		// Process each record.
		
		for _, part := range parts {
			// Ignore the empty string created by the trailing semicolon.
			if part == "" {
				continue
			}
			// Split the string into key and value.
			
			fields := strings.SplitN(part, "=", 2)
			
			// Make sure both key and value exist.
			if len(fields) == 2 {
				// Build a new string containing: key:length_of_value
				// This creates additional allocations and string objects, increasing GC activity.
				out = append(out,fields[0]+":"+strconv.Itoa(len(fields[1])),)
			}
		}
		// Save the result so the compiler cannot eliminate the work as unused.
		sink = out
	}
	// Stop benchmark timing.
	//
	// Everything below is measurement/reporting logic and should not affect benchmark performance results.
	b.StopTimer()
	
	// Capture memory statistics after the benchmark completes.
	
	var after runtime.MemStats
	runtime.ReadMemStats(&after)
	
	// Number of benchmark operations executed.
	ops := float64(b.N)
	
	// Total number of garbage collection cycles that occurred while the benchmark was running:
	
	gcCycles := after.NumGC - before.NumGC
	
	// Total "stop-the-world" pause time spent in GC. During these pauses, application execution
	// is temporarily halted while the runtime performs parts of garbage collection.
	
	pauseNs := after.PauseTotalNs - before.PauseTotalNs
	
	// Report GC events per benchmark operation.  Example: 0.002 gc/op means one GC cycle
	// every 500 operations.
	
	if ops > 0 {
		b.ReportMetric(float64(gcCycles)/ops, "gc/op")
	
		// Report average GC pause time per operation.
		b.ReportMetric(float64(pauseNs)/ops, "stw-ns/op")
	}
	// If at least one GC occurred, report the average stop-the-world pause duration for each GC cycle.
	if gcCycles > 0 {
		b.ReportMetric(
			float64(pauseNs)/float64(gcCycles),
			"stw-ns/GC",
		)
	}

}
EOF
```

The benchmark code is now ready to run!  Give it a try by running the following command:

```bash
cd $HOME/go-gc-default
go test ./parsebench -run '^$' -bench BenchmarkParseAndAllocate -benchmem -count 1 -benchtime=2s
```

You should see output similar to below:

```output
goos: linux
goarch: arm64
pkg: example.com/go-gc-default/parsebench
BenchmarkParseAndAllocate-4    14014    170814 ns/op    0.04553 gc/op    102956 stw-ns/GC    4687 stw-ns/op    163840 B/op    4098 allocs/op
PASS
ok      example.com/go-gc-default/parsebench    4.127s
```

Your exact numbers will differ by instance type, Go version, operating system, and system load.  If this test run yields results with no errors, you're ready to move on to the next step.



