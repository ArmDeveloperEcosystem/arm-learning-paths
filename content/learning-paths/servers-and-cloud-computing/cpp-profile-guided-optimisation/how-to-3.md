---
title: Division Example
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install prerequisites 

In this example I am connecting to an AWS-based, `c7g.xlarge` instance running Ubuntu 24.04 LTS. Run the following commands to install the prerequisite packages. 


```bash
sudo apt update
sudo apt install gcc g++ make libbenchmark-dev -y
```

## Division example

Copy and paste the `C++` source code below into a file named `div_bench.cpp`. This example takes in a vector of 4096 32-bit integers and divides each element by a number. Importantly, the `benchmark/benchmark.h` results in indirection so that the value is unknown compile time, although it is visible in our source code as 1500. 

```cpp
#include <benchmark/benchmark.h>
#include <vector>

// Benchmark division instruction
static void baseDiv(benchmark::State &s) {
  std::vector<int> v_in(4096);
  std::vector<int> v_out(4096);

  for (auto _ : s) {
    for (size_t i = 0; i < v_in.size(); i++) v_out[i] = v_in[i] / s.range(0);
    // s.range(0) is unknown at compile time, cannot be reduced
  }
}

BENCHMARK(baseDiv)->Arg(1500)->Unit(benchmark::kMicrosecond); // value of 1500 is passed through as an argument so strength reduction cannot be applied

BENCHMARK_MAIN();
```

To compile as run the microbenchmark on this function we need to link against `pthreads` and `benchmark` with the following commands. 

```bash
g++ -O3 -std=c++17 div_bench.cpp -lbenchmark -lpthread -o div_bench.base
```

Running the output, `div_bench.base` results in the following output. 

```output
Running ./div_bench.base
Run on (4 X 2100 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x4)
  L1 Instruction 64 KiB (x4)
  L2 Unified 1024 KiB (x4)
  L3 Unified 32768 KiB (x1)
Load Average: 0.00, 0.00, 0.00
***WARNING*** Library was built as DEBUG. Timings may be affected.
-------------------------------------------------------
Benchmark             Time             CPU   Iterations
-------------------------------------------------------
baseDiv/1500       7.90 us         7.90 us        88512
```


### Inspect Assembly 

To inspect what assembly instructions are being executed the most frequently, we can use the `perf` command. Please install `perf` using the [installation instructions](https://learn.arm.com/install-guides/perf/) before proceeding. 

{{% notice Please Note %}}
You may need to set the `perf_event_paranoid` value to 0 with the `sudo sysctl kernel.perf_event_paranoid=0` command
{{% /notice %}}


Run the following command to record `perf` data and create a report in the terminal

```bash
sudo perf record -o perf-division-base ./div_bench.base 
sudo perf report --input=perf-division-base
```
![before-pgo](./before-pgo.gif)

