---
title: Benchmarking via go test -bench
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the performance tests using go test -bench

`go test -bench` (the benchmarking mode of go test) is Golang’s built-in benchmarking framework that measures the performance of functions by running them repeatedly and reporting execution time (**ns/op**), memory usage, and allocations. With the `-benchmem flag`, it also shows memory usage and allocations. It’s simple, reliable, and requires only writing benchmark functions in the standard Golang testing package.

This guide walks you through **benchmarking sorting algorithms** in Golang using the built-in **go test -bench framework**. You will learn how to set up a project, write sorting and benchmark functions, run performance tests, and compare results across **VMs and Docker containers on both x86_64 and Arm64 environments**.

1. Create a Project Folder

Open your terminal and create a new folder for this project:

```console
mkdir gosort-bench
cd gosort-bench
```

2. Initialize a Go Module

Inside the folder, run:

```console
go mod init gosort-bench
```
This creates a go.mod file which tells Go, “this is my project, and its name is gosort-bench”.
It helps Go manage dependencies (libraries) automatically.

3. Add Sorting Functions

Create a file called **sorting.go**:

```console
nano sorting.go
```
Paste this code in **sorting.go** file:

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
- The code contains **two sorting methods**, Bubble Sort and Quick Sort, which arrange numbers in order from smallest to largest.
- **Bubble Sort** works by repeatedly comparing two numbers side by side and swapping them if they are in the wrong order. It keeps doing this until the whole list is sorted.
- **Quick Sor**t is faster. It picks a "pivot" number and splits the list into two groups — numbers smaller than the pivot and numbers bigger than it. Then it sorts each group separately.
- The **function** partition helps Quick Sort decide where to split the list based on the pivot number.
- In short, **Bubble Sort is simple but slow,** while **Quick Sort is smarter and usually much faster for big lists of numbers**.

4. Add Benchmark Tests

Create another file called s**orting_benchmark_test.go**:

```console
nano sorting_benchmark_test.go
````

Paste the below code:

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

- The code is a **benchmark test** that checks how fast Bubble Sort and Quick Sort run in Go.
- It first creates a **list of 10,000 random numbers** each time before running a sort, so the test is fair and consistent.
- **BenchmarkBubbleSort** measures the speed of sorting using the slower Bubble Sort method.
- **BenchmarkQuickSort** measures the speed of sorting using the faster Quick Sort method.

When you run **go test -bench=. -benchmem**, Go will show you how long each sort takes and how much memory it uses, so you can compare the two sorting techniques.

### Run the Benchmark

Execute the benchmark suite using the following command:
```console
go test -bench=. -benchmem
```
- **-bench=.** - runs all functions starting with Benchmark.
- **-benchmem** - also shows memory usage (allocations per operation).

You should see the output similar to this:

```output
goos: linux
goarch: arm64
pkg: gosort-bench
BenchmarkBubbleSort-4                 26          44857916 ns/op               0 B/op          0 allocs/op
BenchmarkQuickSort-4                3526            338550 ns/op               0 B/op          0 allocs/op
PASS
ok      gosort-bench    2.903s

```
### Matrics Explanation

- **ns/op** - nanoseconds per operation (lower is better).
- **B/op** - bytes of memory used per operation.
- **allocs/op** - how many memory allocations happened per operation.

### Benchmark summary on x86_64

The following benchmark results are collected on two different x86_64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4s_v6 Ubuntu-based Azure virtual machine**, and a **D4s_v4 Azure virtual machine created from the Azure Linux 3.0 image published by Ntegral Inc**.

| Benchmark          | Value on Docker Container | Value on Virtual Machine |
|--------------------|----------------------------|---------------------------|
| BubbleSort (ns/op) | 44,242,116                 | 107,821,267               |
| QuickSort (ns/op)  |    530,817                 |    587,150                |
| BubbleSort runs    | 26                         | 10                        |
| QuickSort runs     | 2,214                      | 2,032                     |
| Allocations/op     | 0                          | 0                         |
| Bytes/op           | 0                          | 0                         |
| Total time (s)     | 2.692                      | 2.886                     |

### Benchmark summary on Arm64

The following benchmark results are collected on two different Arm64 environments: a **Docker container running Azure Linux 3.0 hosted on a D4ps_v6 Ubuntu-based Azure virtual machine**, and a **D4ps_v6 Azure virtual machine created from the Azure Linux 3.0 custom image using the AArch64 ISO**.

| Benchmark          | Value on Docker Container | Value on Virtual Machine |
|--------------------|----------------------------|---------------------------|
| BubbleSort (ns/op) | 44,288,850                 | 44,857,916                |
| QuickSort (ns/op)  |    339,310                 |    338,550                |
| BubbleSort runs    | 26                         | 26                        |
| QuickSort runs     | 3,496                      | 3,526                     |
| Allocations/op     | 0                          | 0                         |
| Bytes/op           | 0                          | 0                         |
| Total time (s)     | 2.882                      | 2.903                     |

### Benchmarking comparison summary

When you compare the benchmarking results you will notice that on the Azure Cobalt 100:

- **Arm64 maintains consistency** – both Docker container and virtual machine delivered nearly identical results, showing that Arm64 optimizations are working well across environments.
- **BubbleSort (CPU-heavy, O(n²))** – runs in **~44M ns/op** on both setups, proving that raw CPU compute on Arm64 is stable and unaffected by containerization.
- **QuickSort (efficient O(n log n))** – execution is very fast (**~339K ns/op**), showing Arm handles algorithmic workloads efficiently.
- **No memory overhead** – both container and virtual machine show **0 B/op and 0 allocs/op**, confirming Golang’s memory efficiency is preserved on Arm64.
- **Run counts align closely** – **BubbleSort (26 runs each) and QuickSort (~3.5K runs)** indicate Arm64 delivers repeatable and predictable performance.
