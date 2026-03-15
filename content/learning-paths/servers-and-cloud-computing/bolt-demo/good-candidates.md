---
title: Identify programs for BOLT optimization
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What makes a program a good BOLT candidate?
Hardware performance metrics can help determine whether a program is a good candidate for code layout optimization with BOLT. Developers often analyze these metrics using methodologies such as the [Arm TopDown methodology](https://developer.arm.com/documentation/109542/02/Arm-Topdown-methodology).

In this tutorial, you will focus on a small set of TopDown indicators related to instruction delivery and code locality. These indicators describe how efficiently the processor fetches instructions and keeps the execution pipeline busy.

When instruction delivery is inefficient, the workload is referred to as **front-end bound**, meaning the CPU often waits for instructions instead of executing them.
This usually points to instruction fetch or code layout issues, where improving code layout can help.

The L1 instruction cache (L1 I-cache) is the first and fastest cache used to store instructions close to the CPU.
When instructions are not found there, the CPU must fetch them from slower memory, which can stall execution.
MPKI, short for misses per kilo instructions, measures how often an event misses per 1,000 executed instructions, which makes it easier to compare across programs and workloads.
A high L1 I-cache MPKI usually indicates poor instruction locality in the binary.

Based on these observations, the BOLT community typically considers a program a good candidate for layout optimization when:
- The workload is more than 10% front-end bound
- The L1I cache misses per kilo instructions (MPKI) exceeds 30

Higher branch mispredictions or I-TLB misses can also indicate that code layout optimization may improve performance.

## Collecting the metrics

You can collect these metrics using the Topdown Methodology (see [installation guide](/install-guides/topdown-tool)) which builds on the Linux [perf](/install-guides/perf/) profiling tool.

Alternatively, you can compute only the L1 I-cache MPKI metric manually using a basic Linux `perf stat` command.

{{< tabpane code=true >}}
  {{< tab header="topdown-tool" language="bash" output_lines="2-21">}}
    topdown-tool ./out/bsort
      CPU Neoverse V1 metrics
      ├── Stage 1 (Topdown metrics)
      │   └── Topdown Level 1 (Topdown_L1)
      │       └── ┏━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
      │           ┃ Metric          ┃ Value ┃ Unit ┃
      │           ┡━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
      │           │ Backend Bound   │ 11.77 │ %    │
      │           │ Bad Speculation │ 17.92 │ %    │
      │         » │ Frontend Bound  │ 55.73 │ %    │ «
      │           │ Retiring        │ 14.88 │ %    │
      │           └─────────────────┴───────┴──────┘
      └── Stage 2 (uarch metrics)
          ├── Misses Per Kilo Instructions (MPKI)
          │   └── ┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
          │       ┃ Metric                  ┃ Value  ┃ Unit                          ┃
          │       ┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
          │       │ Branch MPKI             │ 16.583 │ misses per 1,000 instructions │
          │     » │ L1I Cache MPKI          │ 60.408 │ misses per 1,000 instructions │ «
          │       └─────────────────────────┴────────┴───────────────────────────────┘
          ...
  {{< /tab >}}
  {{< tab header="perf stat" language="bash" output_lines="2-10">}}
    perf stat -e instructions,L1-icache-misses:u ./out/bsort
      Performance counter stats for './out/bsort':

          957828603 instructions
           58003648 L1-icache-misses

        0.282472631 seconds time elapsed

        0.282541000 seconds user
        0.000000000 seconds sys
  {{< /tab >}}
{{< /tabpane >}}

## Interpreting the results

In this example, the program is **55% front-end bound**, which indicates that the processor frequently stalls while waiting for instructions.
At Stage 2, the microarchitectural metrics report an **L1I cache MPKI of about 60**, which strongly suggests poor instruction locality. This value exceeds the typical threshold of 30 MPKI for good BOLT candidates.

The **branch MPKI of 16** also indicates frequent branch mispredictions, which code layout optimization may improve.

## Computing MPKI manually

The `topdown-tool` collects performance counters using `perf` and applies formulas to derive higher-level metrics.

To compute the **L1I cache MPKI** manually from the `perf stat` output, apply the following formula:

$$\frac{(\text{L1-icache-misses} \times 1000)}{\text{instructions}}$$

## What you've learned and what's next

You've learned how to evaluate whether a program is a good candidate for BOLT optimization by analyzing frontend stalls and L1I cache MPKI. The example program shows clear signs of poor instruction locality with 55% frontend bound and an L1I MPKI of 60.

In the following sections, you'll explore different profiling methods to collect the data BOLT needs for optimization, starting with BRBE profiling.
