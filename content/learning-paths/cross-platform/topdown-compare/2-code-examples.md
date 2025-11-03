---
title: "Measure cross-platform performance with topdown-tool and Perf PMU counters"
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-platform performance analysis example

To compare x86 and Arm Neoverse top-down methodologies, you can run a backend-bound benchmark that demonstrates PMU counter differences between architectures.

You need a C compiler installed, [GCC](/install-guides/gcc/native/) or Clang, and [Perf](/install-guides/perf/) installed on each system. For Arm systems, you also need [topdown-tool](/install-guides/topdown-tool/). Refer to the package manager for your Linux distribution for installation information. 

Use a text editor to copy the code below to a file named `core-bound-div-chain.c`:

```C
// Usage: ./core-bound-div-chain <iterations>
// Intention: Backend/Core-bound via FP64 divide dependency chain.

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number_of_iterations>\n", argv[0]);
        return 1;
    }

    long long iters = atoll(argv[1]);
    if (iters <= 0) {
        fprintf(stderr, "Number of iterations must be a positive integer.\n");
        return 1;
    }

    volatile double result = 1.23456789;   // keep it live between iterations
    volatile double divisor = 1.00000001;  // volatile thwarts constant folding & reciprocal

    // Optional warmup: helps get steady-state frequency/thermal behavior
    for (int w = 0; w < 1000000; ++w) { result /= divisor; }

    printf("Running %lld dependent FP64 divisions...\n", iters);
    for (long long i = 0; i < iters; ++i) {
        // True dependency chain: next division waits for previous to complete
        result /= divisor;

        // Tiny perturbation keeps the compiler cautious while having negligible impact
        if ((i & 0x3FFFFF) == 0) { asm volatile("" ::: "memory"); }
    }

    // Print result to keep operations observable
    printf("Done. Final result: %.9f\n", (double)result);
    return 0;
}
```

The example code performs one floating-point divide per iteration. The next divide depends on the previous result (result is reused). Divides are high-latency, low-throughput and generally take about 20–40 cycles on Intel x86 and Neoverse V2. Because each iteration depends on the last, the CPU can't overlap operations (no instruction-level parallelism). The backend's execution resources, specifically the FP divide unit, become the bottleneck. The frontend and speculation engines have no problem supplying work. 

This example is not a realistic application, but creates a controlled environment where the CPU's backend execution become the bottleneck. While such tight loops of dependent divides rarely exist in production code, similar patterns occur in scientific, financial, and engineering applications that perform iterative numerical calculations. In those cases, limited instruction-level parallelism and high operation latency lead to the same core-bound behavior.

By isolating the pipeline dynamics the top-down performance metrics are easy to observe and interpret. By removing noise from memory access, control flow, and cache effects, the program highlights how the top-down methodology identifies backend stalls and distinguishes execution-resource bottlenecks from frontend or memory limitations.

The program takes a single command-line argument specifying the number of iterations to run. The sequential floating-point divisions create a dependency chain of high-latency operations, simulating a core-bound workload where each iteration must wait for the previous division to complete.

Build the application using GCC:

```console
gcc -O3 -march=native -o core-bound-div-chain core-bound-div-chain.c
```

You can also use Clang by substituting `clang` instead of `gcc` in the command above.

{{% notice Note %}}
If you use GCC 13 and newer for Arm compilation, using `-march=native` is recommended. For older versions you should use `-mcpu=neoverse-v2`.
{{% /notice %}}

Run the application using `taskset` to pin it to one core to make the numbers more consistent:

```console
taskset -c 1 ./core-bound-div-chain 1000000000
```

The output is:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492
```

You can now try top-down on Intel x86 and Arm Neoverse V2.

## Collect Intel x86 top-down Level 1 metrics with Perf

Linux Perf collects level 1 top-down information using PMU counters like `UOPS_RETIRED.RETIRE_SLOTS`, `IDQ_UOPS_NOT_DELIVERED.CORE`, and `CPU_CLK_UNHALTED.THREAD` for the four categories: Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

Use `perf stat` on the pinned core to collect Level 1 metrics: 

```console
taskset -c 1 perf stat -C 1 --topdown ./core-bound-div-chain 1000000000 
```

The expected output is similar to:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492

 Performance counter stats for 'CPU(s) 1':

                                    retiring      bad speculation       frontend bound        backend bound 
S0-D0-C1           1                18.3%                 0.0%                 0.1%                81.6% 

       6.119817329 seconds time elapsed

```

Here's a summary of the results:

| Metric                   | Result                                                                                          | Interpretation |
| :----------------------- | :---------------------------------------------------------------------------------------------- | :------------- |
| Retiring is 18.3%      | Roughly one-fifth of available issue slots were used for useful µops that successfully retired. |                |
| Bad Speculation is 0%  | The program executed without branch mispredictions or pipeline flushes.                         |                |
| Frontend Bound is 0.1% | The instruction fetch and decode stages easily kept the backend supplied with µops.             |                |
| Backend Bound is 81.6% | The vast majority of slots were stalled in the backend, waiting for execution resources.        |                |

This pattern is expected from the dependent floating-point division chain: each divide must wait for the previous result, and the FP-divide unit has a latency of roughly 20–40 cycles.

The high Backend Bound and low Frontend/Speculation percentages confirm that performance is limited by execution-unit latency, not instruction supply, memory access, or branching.

In real applications, similar backend/core-bound behavior appears in compute-intensive numerical kernels that contain long dependency chains or high-latency math operations.

You can also use the `-M topdownl1` argument with Perf: 

```console
taskset -c 1 perf stat -C 1 -M topdownl1 ./core-bound-div-chain 1000000000
```

The expected output is similar to:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492

 Performance counter stats for 'CPU(s) 1':

     7,030,153,262      uops_issued.any           #     0.00 Bad_Speculation          (14.30%)
    19,206,823,557      cpu_clk_unhalted.thread   #     0.09 Retiring                 (14.30%)
     7,026,625,438      uops_retired.retire_slots                                     (14.30%)
         1,111,503      int_misc.recovery_cycles                                      (14.30%)
     7,017,115,812      uops_issued.any           #     0.91 Backend_Bound            (14.33%)
        31,942,584      idq_uops_not_delivered.core                                     (28.60%)
           704,834      int_misc.recovery_cycles                                      (42.87%)
    19,201,754,818      cpu_clk_unhalted.thread                                       (57.15%)
    19,203,260,401      cpu_clk_unhalted.thread   #     0.00 Frontend_Bound           (42.82%)
        26,956,040      idq_uops_not_delivered.core                                     (42.82%)
     <not counted>      cpu_clk_unhalted.thread                                     

       6.052936784 seconds time elapsed

```

This output provides the raw event counts and derived Top-Down Level 1 metrics for a single core running the dependent floating-point divide workload.

| Metric                  |Interpretation                                                                                              | 
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------ | 
| Retiring is 9%        | This is expected because each iteration performs one divide dependent on the previous result. |
| Bad Speculation is 0% | No wasted work from mispredicted branches or pipeline flushes.                                                                                    |
| Frontend Bound is 0%  | The frontend easily supplied µops; instruction delivery was not a limiting factor.                                                                |
| Backend Bound is 91%  | The majority of slots were stalled waiting for execution resources, specifically the floating-point divide unit.       |

You can continue with the Level 2 and Level 3 hierarchical analysis if you want to learn more.

## Use the Arm Neoverse top-down methodology

Arm's approach uses a methodology with PMU counters like `STALL_SLOT_BACKEND`, `STALL_SLOT_FRONTEND`, `OP_RETIRED`, and `OP_SPEC` for Stage 1 analysis, followed by resource effectiveness groups in Stage 2.

Make sure you install the Arm topdown-tool using the [Telemetry Solution install guide](/install-guides/topdown-tool/).

Collect general metrics including Instructions Per Cycle (IPC):

```console
taskset -c 1 topdown-tool -m General ./core-bound-div-chain 1000000000
```

The expected output is similar to:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── General (General)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
            ┃ Metric                 ┃ Value ┃ Unit      ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
            │ Instructions Per Cycle │ 0.485 │ per cycle │
            └────────────────────────┴───────┴───────────┘
```

The reported Instructions Per Cycle (IPC) of 0.485 means that, on average, the Neoverse V2 core retired about 0.5 instructions every clock cycle while running the workload.

Neoverse V2 can theoretically retire up to eight µops per cycle, so achieving only 0.485 IPC indicates that the core was mostly waiting rather than issuing useful work each cycle. This aligns with expectations for the dependent floating-point division chain, where every iteration must wait for the previous division to finish. The long divide latency prevents instruction-level parallelism, causing the pipeline to spend most of its time stalled in the backend.

Collect the Stage 1 top-down metrics using Arm's cycle accounting:

```console
taskset -c 1 topdown-tool -m Cycle_Accounting ./core-bound-div-chain 1000000000
```

The expected output is similar to:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── Cycle Accounting (Cycle_Accounting)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
            ┃ Metric                  ┃ Value ┃ Unit ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
            │ Backend Stalled Cycles  │ 89.22 │ %    │
            │ Frontend Stalled Cycles │ 0.02  │ %    │
            └─────────────────────────┴───────┴──────┘
```

The Cycle Accounting metrics show that during execution, 89.22% of all cycles were backend-stalled, while only 0.02% were frontend-stalled.

This means the Neoverse V2 core spent nearly all of its time waiting for backend execution resources rather than for instructions to be fetched or decoded. 

The result confirms that the workload is backend/core-bound by arithmetic execution latency. The frontend and memory subsystems remained fully capable of feeding the pipeline.

For operation mix:

```console
taskset -c 1 topdown-tool -m Operation_Mix ./core-bound-div-chain 1000000000
```

The expected output is similar to:

```output
Running 1000000000 dependent FP64 divisions...
Done. Final result: 0.000055492
CPU Neoverse V2 metrics
└── Stage 2 (uarch metrics)
    └── Speculative Operation Mix (Operation_Mix)
        ├── Follows
        │   ├── Backend Bound (backend_bound)
        │   └── Retiring (retiring)
        └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
            ┃ Metric                                           ┃ Value ┃ Unit ┃
            ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
            │ Barrier Operations Percentage                    │ 0.00  │ %    │
            │ Branch Operations Percentage                     │ 22.16 │ %    │
            │ Crypto Operations Percentage                     │ 0.00  │ %    │
            │ Integer Operations Percentage                    │ 33.52 │ %    │
            │ Load Operations Percentage                       │ 22.19 │ %    │
            │ Floating Point Operations Percentage             │ 11.03 │ %    │
            │ Advanced SIMD Operations Percentage              │ 0.00  │ %    │
            │ Store Operations Percentage                      │ 11.11 │ %    │
            │ SVE Operations (Load/Store Inclusive) Percentage │ 0.00  │ %    │
            └──────────────────────────────────────────────────┴───────┴──────┘
```


The Operation Mix report shows the relative share of different instruction types that executed on the Neoverse V2 core.
Even though this benchmark performs only a single arithmetic operation in the loop, the compiler and runtime add supporting instructions for loop control, memory access, and branching.

Key observations:

| Metric                                  | Interpretation                                                                                                                                                                                   |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Floating Point Operations is 11%      | These are the FP64 divide instructions that dominate runtime latency. Each divide is expensive (≈ 25–35 cycles) and fully serialized, explaining the high backend stall percentage seen earlier. |
| Integer Operations is 33%             | Loop-index increments, comparisons, and address arithmetic generated by the compiler. They retire quickly and contribute little to total time.                                                   |
| Load ≈ 22 % / Store is 11%            | Reading and writing the `result` variable in memory or registers each iteration. They show the loop’s basic data movement overhead.                                                              |
| Branch is 22%                         | The loop’s conditional branch that repeats until the iteration limit. Although frequent, branches are correctly predicted, so they don’t cause speculation stalls.                               |
| SIMD / SVE / Crypto / Barrier is 0%  | None of these specialized instruction classes are used, as expected for a scalar FP benchmark.                                                                                                   |

Overall, the mix confirms that this is a scalar floating-point workload with a high fraction of control and integer bookkeeping instructions.

The small proportion of FP operations but their long latency explains why the backend-bound stalls dominate performance: a few slow FP divides hold up many lightweight integer and branch instructions waiting behind them.

## Cross-architecture performance analysis summary

Both Arm Neoverse V2 and Intel x86 cores expose rich hardware Performance Monitoring Unit (PMU) events that enable Top-Down analysis. Although the counter names, formulas, and tools differ, both methodologies can identify pipeline efficiency and identify where bottlenecks occur. 

Intel x86 processors implement a multi-level hierarchical model known as the Top-Down Microarchitecture Analysis Methodology (TMAM). This approach uses slot-based pipeline accounting and PMU events such as UOPS_RETIRED.RETIRE_SLOTS, IDQ_UOPS_NOT_DELIVERED.CORE, and CPU_CLK_UNHALTED.THREAD to divide execution time into four categories: Retiring, Bad Speculation, Frontend Bound, and Backend Bound.

Linux Perf provides a standard interface for this analysis through commands like `perf stat --topdown` and metric groups such as `perf stat -M topdownl1`.

Arm Neoverse V2 offers a two-stage methodology implemented through the Arm Telemetry Solution and its `topdown-tool`.
Stage 1 measures the same four top-level categories using PMU events such as STALL_SLOT_BACKEND, STALL_SLOT_FRONTEND, OP_RETIRED, and OP_SPEC.

Stage 2 expands the analysis into resource-effectiveness groups including Cycle Accounting, Cache Effectiveness, Branch Effectiveness, and Operation Mix. This modular structure enables flexible exploration of specific pipeline subsystems without requiring a strict hierarchy.

When applied to the same floating-point division workload, both frameworks produced the same conclusion:
the program was Backend/Core-Bound, limited by execution-unit latency rather than instruction fetch, speculation, or memory access.

