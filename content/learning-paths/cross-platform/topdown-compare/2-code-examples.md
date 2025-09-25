---
title: Performance analysis code example
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

##  Example code

To compare top-down on Arm and x86 you can run a small example to gain some practical experience. 

You can prepare the application and test it on both x86 and Arm Linux systems. You will need a C compiler installed, [GCC](/install-guides/gcc/native/) or Clang, and [Perf](/install-guides/perf/) installed on each system. Refer to the package manager for your Linux distribution for installation information. 

Use a text editor to copy the code below to a file named `test.c`

```C
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number_of_iterations>\n", argv[0]);
        return 1;
    }

    long long num_iterations = atoll(argv[1]);
    if (num_iterations <= 0) {
        fprintf(stderr, "Number of iterations must be a positive integer.\n");
        return 1;
    }

    // Using volatile tells the compiler not to optimize this variable away.
    // We initialize it to a non-trivial value.
    volatile double result = 1.23456789;

    printf("Performing %lld dependent floating-point divisions...\n", num_iterations);

    // This loop creates a long dependency chain of floating-point divisions.
    // Division is a high-latency operation. The dependency between iterations
    // means the CPU backend will be stalled waiting for the result of the
    // previous division before it can start the next one. This creates a
    // classic backend-bound scenario, specifically core-bound.
    for (long long i = 0; i < num_iterations; ++i) {
        result /= 1.00000001;
    }

    printf("Done. Final result: %f\n", (double)result);

    return 0;
}
```

This  program takes a single command-line argument specifying the number of iterations to run. It performs that many sequential floating-point divisions in a loop, using a volatile variable to prevent compiler optimization, and prints the final result. 

It's a contrived example used to create a dependency chain of high-latency operations (divisions), simulating a CPU-bound workload where each iteration must wait for the previous one to finish.

Build the application using GCC:

```console
gcc -O3 -march=native -o test test.c
```

You can also use Clang by substituting `clang` instead of `gcc` in the command above.

Run the application and pin it to one core to make the numbers more consistent:

```console
taskset -c 1 ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
```

## Collect x86 top-down level 1 metrics 

Linux Perf computes top-down level 1 breakdown as described in the previous section for Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

Use `perf stat` to on the pinned core to collect the metrics. 

```console
taskset -c 1 perf stat -C 1 --topdown ./test 1000000000 
```

The output will be similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056

 Performance counter stats for 'CPU(s) 1':

                                    retiring      bad speculation       frontend bound        backend bound 
S0-D0-C1           1                 8.5%                 0.0%                 0.1%                91.4% 

       6.052117775 seconds time elapsed
```

You see a very large `backend bound` component for this program. 

You can also run with the `-M topdownl1` argument on Perf. 

```console
taskset -c 1 perf stat -C 1 -M topdownl1  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056

 Performance counter stats for 'CPU(s) 1':

     3,278,902,619      uops_issued.any           #     0.00 Bad_Speculation          (14.30%)
    19,185,808,092      cpu_clk_unhalted.thread   #     0.04 Retiring                 (14.30%)
     3,275,536,897      uops_retired.retire_slots                                     (14.30%)
         1,065,517      int_misc.recovery_cycles                                      (14.30%)
     3,263,874,383      uops_issued.any           #     0.96 Backend_Bound            (14.33%)
        28,107,558      idq_uops_not_delivered.core                                     (28.64%)
           631,768      int_misc.recovery_cycles                                      (42.90%)
    19,173,526,414      cpu_clk_unhalted.thread                                       (57.17%)
    19,176,373,078      cpu_clk_unhalted.thread   #     0.00 Frontend_Bound           (42.79%)
        25,090,380      idq_uops_not_delivered.core                                     (42.79%)
     <not counted>      cpu_clk_unhalted.thread                                     

       6.029283206 seconds time elapsed
```

Again, showing `Backend_Bound` value very high (0.96). 

If you want to learn more, you can continue with the level 2 and level 3 analysis.


## Use the Arm top-down methodology

Make sure you install the Arm top-down tool.

Use the [Telemetry Solution install guide](/install-guides/topdown-tool/) for information about installing `topdown-tool`. 

Collect instructions per cycle (IPC):

```console
taskset -c 1 topdown-tool -m General ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 2 (uarch metrics)
=======================
[General]
Instructions Per Cycle 0.355 per cycle
```

Connect the stage 1 metrics:

```console
taskset -c 1 topdown-tool -m Cycle_Accounting ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 1 (Topdown metrics)
=========================
[Cycle Accounting]
Frontend Stalled Cycles 0.04% cycles
Backend Stalled Cycles. 88.15% cycles
```

This confirms the example has high backend stalls as on x86. 

You can continue to use the `topdown-tool` for additional microarchitecture exploration.

For L1 data cache:

```console
taskset -c 1 topdown-tool -m L1D_Cache_Effectiveness  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 2 (uarch metrics)
=======================
[L1 Data Cache Effectiveness]
L1D Cache MPKI............... 0.023 misses per 1,000 instructions
L1D Cache Miss Ratio......... 0.000 per cache access
```

For L1 instruction cache:

```console
taskset -c 1 topdown-tool -m L1D_Cache_Effectiveness  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 2 (uarch metrics)
=======================
[L1 Data Cache Effectiveness]
L1D Cache MPKI............... 0.022 misses per 1,000 instructions
L1D Cache Miss Ratio......... 0.000 per cache access
```

For last level cache: 

```console
taskset -c 1 topdown-tool -m LL_Cache_Effectiveness  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 2 (uarch metrics)
=======================
[Last Level Cache Effectiveness]
LL Cache Read MPKI.............. 0.017 misses per 1,000 instructions
LL Cache Read Miss Ratio........ 0.802 per cache access
LL Cache Read Hit Ratio......... 0.198 per cache access
```

For operation mix:

```console
taskset -c 1 topdown-tool -m Operation_Mix ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Done. Final result: 0.000056
Stage 2 (uarch metrics)
=======================
[Speculative Operation Mix]
Load Operations Percentage.......... 16.70% operations
Store Operations Percentage......... 16.59% operations
Integer Operations Percentage....... 33.61% operations
Advanced SIMD Operations Percentage. 0.00% operations
Floating Point Operations Percentage 16.45% operations
Branch Operations Percentage........ 16.65% operations
Crypto Operations Percentage........ 0.00% operations
```


## Summary

Both Arm Neoverse and modern x86 cores expose hardware events that Perf aggregates into the same top-down categories. Names of the PMU counters differ, but the level 1 categories are the same. 

If you are working on both architectures you can use the same framework with minor differences between Intel's hierarchical structure and Arm's two-stage resource groups to systematically identify and resolve performance bottlenecks. 

