---
title: Benchmarking via go test -bench
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run Performance Tests Using go test -bench

`go test -bench` (the benchmarking mode of go test) is Golang’s built-in benchmarking framework that measures the performance of functions by running them repeatedly and reporting execution time (**ns/op**), memory usage, and allocations. With the `-benchmem flag`, it also shows memory usage and allocations. It’s simple, reliable, and requires only writing benchmark functions in the standard Golang testing package.

1. Create a Project Folder

In your terminal, create a directory for your benchmark project and navigate into it:

```console
mkdir gosort-bench
cd gosort-bench
```

2. Initialize a Go Module
   
Inside your project directory, initialize a new Go module by running:

```console
go mod init gosort-bench
```
This creates a `go.mod` file, which defines the module path (gosort-bench in this case) and marks the directory as a Go project. The `go.mod` file also allows Go to manage dependencies (external libraries) automatically, ensuring your project remains reproducible and easy to maintain.

3. Add Sorting Functions

Create a file called `sorting.go`:

```console
nano sorting.go
```
Paste the following code in `sorting.go`:

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
The code contains two sorting methods, Bubble Sort and Quick Sort, which arrange numbers in order from smallest to largest.
  * Bubble Sort works by repeatedly comparing two numbers side by side and swapping them if they are in the wrong order. It keeps doing this until the whole list is sorted.
  * Quick Sort is faster. It picks a pivot number and splits the list into two groups — numbers smaller than the pivot and numbers bigger than it. Then it sorts each group separately. The function partition helps Quick Sort decide where to split the list based on the pivot number.

To summarize, Bubble Sort is simple but slow, while Quick Sort is more efficient and usually much faster for big lists of numbers. 

At this point, you have defined two sorting algorithms ready to be benchmarked.

To keep your project modular and maintainable, it’s best practice to place implementation code inside its own package folder. This allows benchmarks and other Go files to import it cleanly.

```console
mkdir sorting
mv sorting.go sorting/
```

4. Add Benchmark Tests

Next, create a benchmark test file named `sorting_benchmark_test.go` in your project’s root directory (not inside the sorting/ folder, so it can import the sorting package cleanly):

```console
nano sorting_benchmark_test.go
````

Paste the following code into it:

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
The code implements a benchmark that checks how fast Bubble Sort and Quick Sort run in Go.
- It first creates a list of 10,000 random numbers each time before running a sort, so the test is fair and consistent.
- The BenchmarkBubbleSort() function measures the speed of sorting using the slower Bubble Sort method.
- The BenchmarkQuickSort() function measures the speed of sorting using the faster Quick Sort method.

When you run the benchmark, Go will show you how long each sort takes and how much memory it uses, so you can compare the two sorting techniques.

### Run the Benchmark

Execute the benchmark suite using the following command:
```console
go test -bench=. -benchmem
```
-bench=. runs every function whose name starts with Benchmark.
-benchmem adds memory metrics (B/op, allocs/op) to the report.

You should see output similar to:

```output
goos: linux
goarch: arm64
pkg: gosort-bench
BenchmarkBubbleSort-4                 32          36616759 ns/op               0 B/op          0 allocs/op
BenchmarkQuickSort-4                3506            340873 ns/op               0 B/op          0 allocs/op
PASS
ok      gosort-bench    2.905s
```
### Metrics Explained

  * ns/op – nanoseconds per operation (lower is better). This is the primary latency metric.
  * B/op – bytes allocated per operation (lower is better). This is useful for spotting hidden allocations.
  * allocs/op – number of heap allocations per operation (lower is better). Zero here means the algorithm itself didn’t allocate.
    
### Benchmark summary on Arm64
Here is a summary of benchmark results collected on an Arm64 D4ps_v6 Ubuntu Pro 24.04 LTS virtual machine.

| Benchmark          | Value on Virtual Machine |
|-------------------|--------------------------|
| BubbleSort (ns/op) | 36,616,759              |
| QuickSort (ns/op)  | 340,873                 |
| BubbleSort runs    | 32                      |
| QuickSort runs     | 3,506                   |
| Allocations/op     | 0                       |
| Bytes/op           | 0                       |
| Total time (s)     | 2.905                   |

### Benchmark summary on x86_64
Here is a summary of the benchmark results collected on x86_64 D4s_v6 Ubuntu Pro 24.04 LTS virtual machine.

| Benchmark          | Value on Virtual Machine |
|-------------------|--------------------------|
| BubbleSort (ns/op) | 42,801,947              |
| QuickSort (ns/op)  |    512,726              |
| BubbleSort runs    | 27                      |
| QuickSort runs     | 2,332                   |
| Allocations/op     | 0                       |
| Bytes/op           | 0                       |
| Total time (s)     | 2.716                   |


### Benchmarking comparison summary

When you compare the benchmarking results you will notice that on the Azure Cobalt 100:

- **Arm64 maintains consistency** – the virtual machine delivered stable and predictable results, showing that Arm64 optimizations are effective for compute workloads.
- **BubbleSort (CPU-heavy, O(n²))** – runs in **~36.6M ns/op**, proving that raw CPU performance on Arm64 is consistent and unaffected by environmental factors.
- **QuickSort (efficient O(n log n))** – execution is very fast (**~341K ns/op**), demonstrating that Arm64 handles algorithmic workloads efficiently.
- **No memory overhead** – the benchmark shows **0 B/op and 0 allocs/op**, confirming Golang’s memory efficiency is preserved on Arm64.
- **Run counts align closely** – **BubbleSort (32 runs)** and **QuickSort (3,506 runs)** indicate Arm64 delivers repeatable and reliable performance.
