---
title: Set CPU affinity in source code
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Pin threads at the source code level

Another way to set CPU affinity is at the source code level. This allows you to be more expressive about which thread goes where at specific points during runtime. 

For example, in a hot path that repeatedly updates shared state with a read-modify-write pattern, a pinned thread can avoid excessive cache invalidations caused by other threads modifying data.

## Create a baseline program without thread pinning

To demonstrate this, you'll create two example programs. The first uses the default OS scheduling without thread pinning.

Copy and paste the code below into a new file named `default_os_scheduling.cpp`:

```cpp
#include <benchmark/benchmark.h>
#include <atomic>
#include <thread>
#include <vector>

using namespace std;

// Places each atomic float on a separate 64-byte cache line
struct AlignedAtomic {
  alignas(64) std::atomic<float> val = 0;
};

void os_scheduler() {

  const int NUM_THREADS = 4;

  AlignedAtomic a;
  AlignedAtomic b;

  // Lambda Work Function
  auto task = [](AlignedAtomic &atomic){
      for(int i = 0; i < (1 << 18); i++){
        atomic.val = atomic.val + 1.0f;
      }  
  };

  std::vector<thread> threads;
  threads.reserve(NUM_THREADS);
  
  // Launch NUM_THREADS threads
  for (int i = 0; i < NUM_THREADS; i++){
    if (i%2 == 0){
          threads.emplace_back(task, ref(a));
    }
    else{
          threads.emplace_back(task, ref(b));

    }
  }

  // wait for all threads to join before exiting
  for (auto& thread : threads){
    thread.join();
  }
}

// Google Benchmark Framework
static void default_os_scheduling(benchmark::State& s) {
  while (s.KeepRunning()) {
    os_scheduler();
  }
}
BENCHMARK(default_os_scheduling)->UseRealTime()->Unit(benchmark::kMillisecond);

BENCHMARK_MAIN();
```

This program has two atomic variables that are aligned on different cache lines to avoid thrashing. You spawn four threads: two threads perform a read-modify-write operation on the first atomic variable, and two threads perform the same operation on the second atomic variable.

## Create a program with explicit thread pinning

Create a file named `thread_affinity.cpp` with the code below. This program uses `pthread_setaffinity_np` to pin threads to specific CPU cores:

```cpp
#include <benchmark/benchmark.h>
#include <pthread.h>
#include <vector>
#include <atomic>
#include <cassert>
#include <thread>


using namespace std;

// Places each atomic float on a separate 64-byte cache line
struct AlignedAtomic {
  alignas(64) std::atomic<float> val = 0;
};

void thread_affinity() {
  
  const int NUM_THREADS = 4;

  AlignedAtomic a;
  AlignedAtomic b;

  // Lambda Work Function
  auto task = [](AlignedAtomic &atomic){
      for(int i = 0; i < (1 << 18); i++){
        atomic.val = atomic.val + 1.0f;
      }  
  };

  std::vector<thread> threads;
  threads.reserve(NUM_THREADS);

  // Create cpu sets
  cpu_set_t cpu_set_0;
  cpu_set_t cpu_set_1;

  // Zero them out
  CPU_ZERO(&cpu_set_0);
  CPU_ZERO(&cpu_set_1);

  // And set the CPU cores we want to pin the threads too
  CPU_SET(0, &cpu_set_0);
  CPU_SET(1, &cpu_set_1);

    // Launch threads and pin variables a and b to the same CPU cores. 
  for (int i = 0; i < NUM_THREADS; i++){
    if (i%2 == 0){
          threads.emplace_back(task, ref(a));
          assert(pthread_setaffinity_np(threads[i].native_handle(), sizeof(cpu_set_t), &cpu_set_0) == 0);

    }
    else{
          threads.emplace_back(task, ref(b));
          assert(pthread_setaffinity_np(threads[i].native_handle(), sizeof(cpu_set_t),  &cpu_set_1) == 0);
    }
  }


  // wait for all threads to join before exiting
  for (auto& thread : threads){
    thread.join();
  }
}

// Thread affinity benchmark
static void thread_affinity(benchmark::State& s) {
  for(auto _ : s) {
    thread_affinity();
  }
}
BENCHMARK(thread_affinity)->UseRealTime()->Unit(benchmark::kMillisecond);

BENCHMARK_MAIN();
```

This program uses the `pthread_setaffinity_np` function from the `pthread.h` header file to pin threads. The two threads operating on atomic variable `a` are pinned to a specific CPU set, and the other threads operating on atomic variable `b` are pinned to a different CPU.

## Compile and benchmark the programs

Compile both programs with the following commands:

```bash
g++ default_os_scheduling.cpp -O3 -march=native -lbenchmark -lpthread -o default-os-scheduling
g++ thread_affinity.cpp -O3 -march=native -lbenchmark -lpthread -o thread-affinity
```

Use Perf to print statistics for both programs:

```bash
perf stat -e L1-dcache-loads,L1-dcache-load-misses ./default-os-scheduling
perf stat -e L1-dcache-loads,L1-dcache-load-misses ./thread-affinity
```

## Analyze the performance results

The output shows the `L1-dcache-load-misses` metric reduces from approximately 7.84% to approximately 0.6% as a result of thread pinning. This metric measures how often the CPU core doesn't have an up-to-date version of data in the L1 data cache and must perform an expensive operation to fetch data from a different location. 

This results in a significant reduction in function execution time, dropping from 10.7 ms to 3.53 ms:

```output
Running ./default-os-scheduling
Run on (16 X 2100 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x16)
  L1 Instruction 64 KiB (x16)
  L2 Unified 1024 KiB (x16)
  L3 Unified 32768 KiB (x1)
Load Average: 0.37, 0.40, 0.20
--------------------------------------------------------------------------
Benchmark                                Time             CPU   Iterations
--------------------------------------------------------------------------
default_os_scheduling/real_time       10.7 ms        0.118 ms           64

 Performance counter stats for './default-os-scheduling':

         391719695      L1-dcache-loads                                                       
          30726569      L1-dcache-load-misses            #    7.84% of all L1-dcache accesses 

       0.808460086 seconds time elapsed

       3.059934000 seconds user
       0.030958000 seconds sys


2026-01-14T09:46:00+00:00
Running ./thread-affinity
Run on (16 X 2100 MHz CPU s)
CPU Caches:
  L1 Data 64 KiB (x16)
  L1 Instruction 64 KiB (x16)
  L2 Unified 1024 KiB (x16)
  L3 Unified 32768 KiB (x1)
Load Average: 0.66, 0.46, 0.22
--------------------------------------------------------------------
Benchmark                          Time             CPU   Iterations
--------------------------------------------------------------------
thread_affinity/real_time       3.53 ms        0.343 ms          198

 Performance counter stats for './thread-affinity':

         699781841      L1-dcache-loads                                                       
           3154506      L1-dcache-load-misses            #    0.45% of all L1-dcache accesses 

       1.094879115 seconds time elapsed

       2.044792000 seconds user
       0.169065000 seconds sys
```

The results demonstrate that thread pinning can significantly improve performance when threads operate on separate data structures. By keeping threads on specific cores, you reduce cache coherency traffic and improve data locality.

## What you've accomplished and what's next

In this section, you've:
- Created two programs to compare default OS scheduling against explicit thread pinning
- Used the `pthread_setaffinity_np` API to control CPU affinity at the source code level
- Measured cache performance using Perf to quantify the impact of thread pinning
- Observed a performance improvement and a reduction in cache misses through strategic thread placement

You've seen how controlling where threads run can reduce cache disruption in contention-heavy paths and improve runtime stability and performance. You've also learned about the trade-offs: pinning can boost locality and predictability, but it can hurt performance of other running processes, especially if the workload characteristics change or if you over-constrain the scheduler.

Thread pinning is most effective when you have well-understood workload patterns and clear separation between data structures accessed by different threads. Use it as a fine-tuning technique after establishing baseline performance with default OS scheduling.