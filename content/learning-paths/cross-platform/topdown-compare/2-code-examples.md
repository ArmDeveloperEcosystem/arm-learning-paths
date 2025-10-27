---
title: "Measure cross-platform performance with topdown-tool and Perf PMU counters"
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

##  Cross-platform performance analysis example

To compare x86 and Arm Neoverse top-down methodologies, you can run a backend-bound benchmark that demonstrates PMU counter differences between architectures.

You can prepare the application and test it on both x86 and Arm Neoverse Linux systems. You will need a C compiler installed, [GCC](/install-guides/gcc/native/) or Clang, and [Perf](/install-guides/perf/) installed on each system. For Arm systems, you'll also need [topdown-tool](/install-guides/topdown-tool/). Refer to the package manager for your Linux distribution for installation information. 

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

This program demonstrates a backend-bound workload that will show high `STALL_SLOT_BACKEND` on Arm Neoverse and high `Backend_Bound` percentage on x86. It takes a single command-line argument specifying the number of iterations to run. The sequential floating-point divisions create a dependency chain of high-latency operations, simulating a core-bound workload where each iteration must wait for the previous division to complete.

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

## Collect x86 top-down Level 1 metrics with Perf

Linux Perf computes 4-level hierarchical top-down breakdown using PMU counters like `UOPS_RETIRED.RETIRE_SLOTS`, `IDQ_UOPS_NOT_DELIVERED.CORE`, and `CPU_CLK_UNHALTED.THREAD` for the four categories: Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

Use `perf stat` on the pinned core to collect Level 1 metrics: 

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

You can also run with the `-M topdownl1` argument with Perf. 

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

Again, showing a `Backend_Bound` value that is very high (0.96). Notice the x86-specific PMU counters:
- `uops_issued.any` and `uops_retired.retire_slots` for micro-operation accounting
- `idq_uops_not_delivered.core` for frontend delivery failures
- `cpu_clk_unhalted.thread` for cycle normalization

If you want to learn more, you can continue with the Level 2 and Level 3 hierarchical analysis.


## Use the Arm Neoverse top-down methodology

Arm's approach uses a methodology with PMU counters like `STALL_SLOT_BACKEND`, `STALL_SLOT_FRONTEND`, `OP_RETIRED`, and `OP_SPEC` for Stage 1 analysis, followed by resource effectiveness groups in Stage 2.

Make sure you install the Arm topdown-tool using the [Telemetry Solution install guide](/install-guides/topdown-tool/).

Collect general metrics including Instructions Per Cycle (IPC):

```console
taskset -c 1 topdown-tool -m General ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── General (General)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
            ┃ Metric                 ┃ Value ┃ Unit      ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
            │ Instructions Per Cycle │ 0.324 │ per cycle │
            └────────────────────────┴───────┴───────────┘
```

Collect the Stage 1 topdown metrics using Arm's cycle accounting:

```console
taskset -c 1 topdown-tool -m Cycle_Accounting ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── Cycle Accounting (Cycle_Accounting)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
            ┃ Metric                  ┃ Value ┃ Unit ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
            │ Backend Stalled Cycles  │ 93.22 │ %    │
            │ Frontend Stalled Cycles │ 0.03  │ %    │
            └─────────────────────────┴───────┴──────┘
```

This confirms the example has high backend stalls, equivalent to x86's Backend_Bound category. Notice how Arm's Stage 1 uses percentage of cycles rather than Intel's slot-based accounting. 

You can continue to use the `topdown-tool` for additional microarchitecture exploration.

For L1 data cache:

```console
taskset -c 1 topdown-tool -m L1D_Cache_Effectiveness ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── L1 Data Cache Effectiveness (L1D_Cache_Effectiveness)
        ├── Follows
        │   └── Backend Bound (backend_bound)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃ Metric               ┃ Value ┃ Unit                          ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
            │ L1D Cache Miss Ratio │ 0.000 │ per cache access              │
            │ L1D Cache MPKI       │ 0.129 │ misses per 1,000 instructions │
            └──────────────────────┴───────┴───────────────────────────────┘
```

For L1 instruction cache effectiveness:

```console
taskset -c 1 topdown-tool -m L1I_Cache_Effectiveness  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── L1 Instruction Cache Effectiveness (L1I_Cache_Effectiveness)
        ├── Follows
        │   └── Frontend Bound (frontend_bound)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃ Metric               ┃ Value ┃ Unit                          ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
            │ L1I Cache Miss Ratio │ 0.003 │ per cache access              │
            │ L1I Cache MPKI       │ 0.474 │ misses per 1,000 instructions │
            └──────────────────────┴───────┴───────────────────────────────┘
```

For last level cache: 

```console
taskset -c 1 topdown-tool -m LL_Cache_Effectiveness  ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── Last Level Cache Effectiveness (LL_Cache_Effectiveness)
        ├── Follows
        │   ├── Backend Bound (backend_bound)
        │   └── Frontend Bound (frontend_bound)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            ┃ Metric                   ┃ Value ┃ Unit                          ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
            │ LL Cache Read Hit Ratio  │ nan   │ per cache access              │
            │ LL Cache Read Miss Ratio │ nan   │ per cache access              │
            │ LL Cache Read MPKI       │ 0.000 │ misses per 1,000 instructions │
            └──────────────────────────┴───────┴───────────────────────────────┘
```

For operation mix:

```console
taskset -c 1 topdown-tool -m Operation_Mix ./test 1000000000
```

The output is similar to:

```output
Performing 1000000000 dependent floating-point divisions...
Monitoring command: test. Hit Ctrl-C to stop.
Run 1
Done. Final result: 0.000056
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── Speculative Operation Mix (Operation_Mix)
        ├── Follows
        │   ├── Backend Bound (backend_bound)
        │   └── Retiring (retiring)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
            ┃ Metric                                           ┃ Value ┃ Unit ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
            │ Barrier Operations Percentage                    │ ❌    │ %    │
            │ Branch Operations Percentage                     │ ❌    │ %    │
            │ Crypto Operations Percentage                     │ 0.00  │ %    │
            │ Integer Operations Percentage                    │ 33.52 │ %    │
            │ Load Operations Percentage                       │ 16.69 │ %    │
            │ Floating Point Operations Percentage             │ 16.51 │ %    │
            │ Advanced SIMD Operations Percentage              │ 0.00  │ %    │
            │ Store Operations Percentage                      │ 16.58 │ %    │
            │ SVE Operations (Load/Store Inclusive) Percentage │ 0.00  │ %    │
            └──────────────────────────────────────────────────┴───────┴──────┘
```


## Cross-architecture performance analysis summary

Both Arm Neoverse and modern x86 cores expose hardware PMU events that enable equivalent top-down analysis, despite different counter names and calculation methods. 

Intel x86 processors use a four-level hierarchical methodology based on slot-based pipeline accounting, relying on PMU counters such as `UOPS_RETIRED.RETIRE_SLOTS`, `IDQ_UOPS_NOT_DELIVERED.CORE`, and `CPU_CLK_UNHALTED.THREAD` to break down performance into retiring, bad speculation, frontend bound, and backend bound categories. Linux Perf serves as the standard collection tool, using commands like `perf stat --topdown` and the `-M topdownl1` option for detailed breakdowns.

Arm Neoverse platforms implement a complementary two-stage methodology where Stage 1 focuses on topdown categories using counters such as `STALL_SLOT_BACKEND`, `STALL_SLOT_FRONTEND`, `OP_RETIRED`, and `OP_SPEC` to analyze pipeline stalls and instruction retirement. Stage 2 evaluates resource effectiveness, including cache and operation mix metrics through `topdown-tool`, which accepts the desired metric group via the `-m` argument.

Both architectures identify the same performance bottleneck categories, enabling similar optimization strategies across Intel and Arm platforms while accounting for methodological differences in measurement depth and analysis approach.

