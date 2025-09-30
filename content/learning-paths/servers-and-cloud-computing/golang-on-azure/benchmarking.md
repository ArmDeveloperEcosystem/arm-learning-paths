---
title: Perform Benchmark using go test -bench
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run performance tests using go test -bench

`go test -bench` is Go’s built-in benchmark runner. It repeatedly executes benchmark functions and reports latency (ns/op). With the `-benchmem` flag, it also reports memory usage (B/op) and allocations (allocs/op). It’s simple, reliable, and requires only writing benchmark functions in the standard Golang testing package.

## Create a project folder

Create a directory for your benchmark project and navigate to it:
```console
mkdir gosort-bench
cd gosort-bench
```

## Initialize a Go module

Initialize a new module:
```console
go mod init gosort-bench
```
This creates a `go.mod` file, which defines the module path (gosort-bench in this case) and marks the directory as a Go project. The `go.mod` file also allows Go to manage dependencies (external libraries) automatically, ensuring your project remains reproducible and easy to maintain.

## Add sorting functions

Create a file named `sorting.go`:
```console
nano sorting.go
```

Paste the following implementation into `sorting.go`:
```go
package sorting 
func BubbleSort(arr []int) {
    n := len(arr)
    for i := 0; i < n-1; i++ {
        for j := 0; j < n-i-1; j++ {
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
}

func QuickSort(arr []int) {
    quickSort(arr, 0, len(arr)-1)
}

func quickSort(arr []int, low, high int) {
    if low < high {
        pivot := partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)
    }
}

func partition(arr []int, low, high int) int {
    pivot := arr[high]
    i := low - 1
    for j := low; j < high; j++ {
        if arr[j] < pivot {
            i++
            arr[i], arr[j] = arr[j], arr[i]
        }
    }
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
}
```
The code contains two sorting methods, Bubble Sort and Quick Sort, which arrange numbers in order from smallest to largest:

- Bubble Sort works by repeatedly comparing two numbers side by side and swapping them if they are in the wrong order. It keeps doing this until the whole list is sorted.
- Quick Sort is faster. It picks a pivot number and splits the list into two groups. Numbers smaller than the pivot and numbers bigger than it. Then it sorts each group separately. The function partition helps Quick Sort decide where to split the list based on the pivot number.

To summarize, Bubble Sort is simple but slow, while Quick Sort is more efficient and usually much faster for big lists of numbers. 

At this point, you have defined two sorting algorithms ready to be benchmarked.

To keep your project modular and maintainable, it’s best practice to place implementation code inside its own package folder. This allows benchmarks and other Go files to import it cleanly.

```console
mkdir sorting
mv sorting.go sorting/
```

### Add benchmark tests

Create a benchmark file named `sorting_benchmark_test.go` in the project root:
```console
nano sorting_benchmark_test.go
```

Paste the following code:
```go
package sorting_test
import (
    "math/rand"
    "testing"
    "gosort-bench/sorting"
)
const LENGTH = 10000
func makeRandomNumberSlice(n int) []int {
    numbers := make([]int, n)
    for i := range numbers {
        numbers[i] = rand.Intn(n)
    }
    return numbers
}
func BenchmarkBubbleSort(b *testing.B) {
    for i := 0; i < b.N; i++ {
        b.StopTimer()
        numbers := makeRandomNumberSlice(LENGTH)
        b.StartTimer()
        sorting.BubbleSort(numbers)
    }
}

func BenchmarkQuickSort(b *testing.B) {
    for i := 0; i < b.N; i++ {
        b.StopTimer()
        numbers := makeRandomNumberSlice(LENGTH)
        b.StartTimer()
        sorting.QuickSort(numbers)
    }
}
```
The code implements a benchmark that measures the performance of Bubble Sort and Quick Sort in Go by generating a new list of 10,000 random numbers before each run to keep the test fair and consistent. The BenchmarkBubbleSort() function evaluates the slower Bubble Sort algorithm, while the BenchmarkQuickSort() function evaluates the faster Quick Sort algorithm, allowing you to compare their relative speeds and efficiency.

When you run the benchmark, Go will show you how long each sort takes and how much memory it uses, so you can compare the two sorting techniques.

### Run the Benchmark

Execute the benchmark suite using the following command:
```console
go test -bench=. -benchmem
```
`-bench=.` runs every function whose name starts with `Benchmark`. `-benchmem` adds memory metrics (B/op, allocs/op) to the report.

Expected output:
```output
goos: linux
goarch: arm64
pkg: gosort-bench
BenchmarkBubbleSort-4                 32          36616759 ns/op               0 B/op          0 allocs/op
BenchmarkQuickSort-4                3506            340873 ns/op               0 B/op          0 allocs/op
PASS
ok      gosort-bench    2.905s
```

## Metrics explained

The metrics reported by go test -bench include ns/op, which measures nanoseconds per operation and reflects latency where lower values are better, B/op, which shows the number of bytes allocated per operation and helps identify memory efficiency, and allocs/op, which indicates the number of heap allocations per operation and highlights how often memory is being allocated, with lower values preferred in all cases.

### Benchmark summary on Arm64

Results collected on an Arm64 **D4ps_v6** Ubuntu Pro 24.04 LTS virtual machine:

| Benchmark            | Value |
|----------------------|-------|
| BubbleSort (ns/op)   | 36,616,759 |
| QuickSort (ns/op)    | 340,873 |
| BubbleSort runs      | 32 |
| QuickSort runs       | 3,506 |
| Allocations/op       | 0 |
| Bytes/op             | 0 |
| Total time (s)       | 2.905 |

## Benchmark summary on x86-64

Results collected on an x86-64 **D4s_v6** Ubuntu Pro 24.04 LTS virtual machine:

| Benchmark          | Value on Virtual Machine |
|-------------------|--------------------------|
| BubbleSort (ns/op) | 42,801,947              |
| QuickSort (ns/op)  |    512,726              |
| BubbleSort runs    | 27                      |
| QuickSort runs     | 2,332                   |
| Allocations/op     | 0                       |
| Bytes/op           | 0                       |
| Total time (s)     | 2.716                   |


## Benchmarking comparison summary

On Azure Cobalt 100 (Arm64), both BubbleSort and QuickSort run faster, with a larger advantage for QuickSort. The observed performance delta (~15–33%) highlights how Arm Neoverse cores excel at CPU-bound, integer-heavy workloads common in Go services.

For real-world Go applications, such as sorting, JSON processing, and other recursive or data-processing tasks, Azure Cobalt 100 Arm64 VMs can provide higher throughput and lower execution time than similarly sized x86-64 VMs. These results validate the benefits of running Go on Cobalt 100 and establish a baseline for extending benchmarks beyond simple sorting.
