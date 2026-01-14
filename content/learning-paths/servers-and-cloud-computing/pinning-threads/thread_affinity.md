---
title: CPU Affinity
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Pinning Threads at Source-Code Level

Another way to set CPU affinity is at the source code level, this allows developers to be more expressive as to which thread goes where at specific points during the runtime. For example, in a hot path that repeatedly updates shared state with a read-modify-write style, a pinned thread could avoids excessive cache invalidations due to other threads modifying data. 

To demonstrate this we have an example program below. Copy and paste the code below into a new file named `default_os_scheduling.cpp`.

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

`default_os_scheduling.cpp` has 2 atomic variables that are aligned on different cache lines to avoid thrashing. We spawn 4 threads, with 2 threads performing a read-modify-wite operation on the first atomic variable, and the final 2 threads performing the same operation on the second atomic variable. 

Now, copy the code block below into a file named `thread_affinity.cpp`.

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

`Thread_affinity.cpp` uses the `pthread_set_affinity_np` function from the `pthread.h` header file to pin the 2 threads operating on atomic variable, `a`, to a specific CPU set and the other threads operating on atomic variable, `b`, to a different CPU.

Compile both programs with the following command.

```bash
g++ default_os_scheduling.cpp -O3 -march=native -lbenchmark -lpthread -o default-os-scheduling
g++ thread_affinity.cpp -O3 -march=native -lbenchmark -lpthread -o thread-affinity
```

We will use the `perf` tool to print statistic for the program. 

```bash
perf stat -e L1-dcache-loads,L1-dcache-load-misses ./default-os-scheduling
perf stat -e L1-dcache-loads,L1-dcache-load-misses ./thread-affinity
```

Inspecting the output below we see that the `L1-dcache-load-misses` which occur when the the CPU core does not have a up-to-date version of the data in the L1 Data cache and must perform an expensive operation to fetch data from a different location, reduces from ~7.84% to ~0.6% as a result of the thread pinning. 

```outputRunning ./default-os-scheduling
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

### Conclusion

In this tutorial, we introduced thread pinning (CPU affinity) through a pair of worked examples. By comparing default OS thread scheduling against explicitly pinned threads, we showed how controlling where threads run can reduce cache disruption in contention-heavy paths and improve runtime stability and performance.

We also highlighted the tradeoffs, pinning can boost locality and predictability, but it can hurt performance of other running processes, espec. Finally, we showed how to implement affinity quickly using common system utilities for inspection and measurement, and how to be more expressive directly in code using APIs like `pthread_setaffinity_np` from `pthread.h`.