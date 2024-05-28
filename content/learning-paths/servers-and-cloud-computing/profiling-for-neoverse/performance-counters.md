---
title: Performance counters
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance counters

Arm CPUs include a Performance Monitoring Unit (PMU) that measures instances of low-level execution events occurring in the hardware. These measurements have several uses:

* Counting instructions or cycles is useful for sizing a workload.
* Counting SIMD vector instructions is useful for identifying whether a
  workload is taking advantage of the available hardware acceleration.
* Counting branch mispredictions or cache misses is useful for identifying
  whether a workload is triggering specific performance pathologies.

To make performance analysis easier, Arm has defined a standardized performance
analysis methodology for the Neoverse CPUs. This methodology defines a common
set of hardware performance counters, and how to use them to derive the
higher-level metrics that enable you to optimize your applications.

### The top-down methodology

The top-down methodology provides a systematic way to use performance counter data to identify performance problems in an application.

The methodology describes performance using a simple hierarchical tree of performance metrics. The basic metrics described for the abstract model provide the root nodes of the tree. Additional levels of hierarchy below each node provide a more detailed breakdown for causal analysis.

![The major top-down metrics](images/topdown-tree.svg)

This hierarchical approach, with clear causal metrics, provides an intuitive way to find and understand the microarchitecture-sensitive performance issues that your software is triggering. Using this information, you can target the problem with specific corrective actions to improve performance.

One of the major usability benefits of the top-down methodology for software developers is that the first few levels of the top-down tree do not require any knowledge of the specific CPU you are running on. You can profile on any of the Neoverse CPUs and get the same metrics, despite differences in the underlying hardware design. This lets you focus on your software and improving performance, instead of worrying about which event to capture on a specific
CPU.

The deeper levels of the tree become increasingly hardware specific, which is useful for developers who want to optimize very deeply for a specific microarchitecture. For most common software optimizations these levels are not necessary.

### Stall metrics

The most common causes of stalls are cache misses and branch mispredictions. To make it easier to understand the impact of stalls, two forms of miss metrics are given:

* _Miss rate_ metrics tell you the percentage of misses for that specific operation type. These metrics tell you how effectively a particular cache or prediction unit is performing.
* _Misses per thousand instruction_ (MPKI) metrics tell you how many misses of that type occurred, on average, when running 1000 instructions of any type. These metrics tell you how significant the impact of a particular type of miss is, given the instruction makeup of the program.

For example, you measure a _Branch mispredict rate_ of 45% when profiling, which tells you that 45% of branches are mispredicted. This is a clear sign that the branch predictor is struggling, so improving branches can be an optimization candidate. However, when you check the _Branch MPKI_ metric you see that you only have 0.8 mispredictions for every 1000 instructions in the sample. Even though branches are not predicting well, optimizing will not bring
significant improvements because branches are only a small proportion of the instruction mix.

### Function attribution

The top-down metrics provide a systematic approach to identifying performance problems in your software, but this is only actionable feedback if the metrics are associated with a specific location in the running program.

The Streamline CLI Tools implement function-attributed metrics by measuring the performance counters over a small sample window of just a few hundred cycles. This allows the tool to see the useful function-frequency signals in the performance counter data that are lost with traditional 1ms periodic sampling.

To reduce the volume of data produced, our approach uses a strobing sampling pattern with an uneven mark-space ratio. For example, we capture data for a 200 cycle window, but only do so once every 2 million cycles. This approach gives us the high frequency data visibility that we need for function-attribution,
while keeping a low probe-effect on the running application and a manageable profile data size.

**Note:** Support for strobing counter sample windows is a new capability for the Linux Perf kernel driver, which is not yet available upstream. A kernel patch is provided to implement this functionality.

## Arm Statistical Profiling Extension

Arm CPUs can support the Statistical Profiling Extension (SPE), which adds support for hardware-based instruction sampling.

When using SPE, the hardware triggers a sample after a configurable number of micro-ops. It writes the sample data directly into a memory buffer without any software involvement. This sampling is not invasive to the running program, until software is needed to process a full memory buffer.

Each sample contains the program counter (PC) of the sampled operation, and additional operation-specific event data. This event data provides additional feedback about the execution of that operation. For example:

* For branch samples, the event data indicates if the branch was mispredicted.
* For load samples, the event data indicates which cache returned the data.

SPE provides a complementary technology to the traditional performance counters, and the best results can be achieved by using both together.
