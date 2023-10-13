---
title: "Introduction to performance analysis"
weight: 2
layout: "learningpathall"
---

This Learning Path provides instructions to use the Arm Telemetry solution and Linux Perf for performance analysis on an example application presented in the [Arm Neoverse N1 Core: Performance Analysis Methodology](https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/neoverse-n1-core-performance-v2.pdf) white paper (referred to as "white paper" for the remainder of the Learning Path).

## Before you begin

Follow the [Telemetry Solution install guide](/install-guides/topdown-tool/) to install the required tools on an Arm Neoverse server. The Telemetry Solution install guide includes instructions to install Python and Linux Perf.

You will also need the GNU C++ compiler, `g++`. Refer to the [GNU Compiler install guide](/install-guides/gcc/native/) to install it. 


## Introduction to performance analysis

Application performance analysis involves measuring hardware and software events, understanding their meaning, and making software changes to improve performance. Performance analysis is a challenging task that may or may not yield meaningful results, but learning how to measure software performance and knowing how to identify performance issues is an important skill. 

The Linux Perf event system provides a way to collect events for performance analysis. The most common way to collect performance information is Linux Perf, but there are others. 

There are two types of events, software events and hardware events. Examples of software events are context switches and page faults. Examples of hardware events are instructions executed and cache accesses.

In addition to the two types of events, there are two ways to collect the events, counting and sampling.

**Counting** collects the number of times an event occurs over a period of time, such as an entire program or a section of a program. Counting indicates how many times the event occurred, but does not help identify which instructions in an application are causing the events. Counting is a useful first step to characterize application performance.

**Sampling** is used to find places for performance improvement in code. It identifies which sections of code are executing most frequently. This information is gathered by taking a "sample" and recording where the program is executing (program counter). The samples can be collected based on time passing (such as every 10 milliseconds) or triggered by hardware events occurring. By sampling the software execution it is possible to locate the areas in the code that are running most often and connect the code to the hardware events. 

## Hardware events

Performance analysis requires an understanding of the hardware events, and how to connect them to causes of suboptimal performance. 

Arm Neoverse processors include more than 100 hardware counters, but not all are important to get started with performance analysis. 

Some important event categories are:
- Cycle and instruction counting 
- Branch prediction effectiveness
- Translation Lookaside Buffer (TLB) effectiveness
- Cache effectiveness
- Memory traffic
- Instruction mix

The white paper covers these events in more detail. Each Neoverse CPU also has a complete PMU guide documenting all events. 

## Performance metrics

To make performance analysis easier, combinations of events are used to compute frequently used metrics. For example, the L1 instruction cache miss rate is computed by dividing the L1 instruction cache refill count by the number of L1 instruction cache accesses. 

The important performance metrics for the Neoverse N1 are outlined in the white paper and the calculations are provided. The metrics are built into the Telemetry Solution so you don't need to make the calculation or write scripts to compute the metrics. 

If the events and metrics are not familiar to you, you may want to learn more about common CPU architecture features so you are better able to connect software execution to hardware events. Additional resources are provided in the Next Steps section of this Learning Path.

## Performance analysis methodology 

The white paper uses the hardware events and performance metrics to build a methodology you can follow to improve application performance. 

The first step is to collect instructions per clock cycle (IPC), front end stall rate, and back end stall rate. The results will determine where to go next. 

A high front end stall rate indicates cycles are being wasted due to pipeline stalls in the instruction fetch, L1 instruction cache, L1 instruction TLB, and the branch predictor. Such an application is characterized as front end bound.

A high back end stall rate indicates cycles are wasted due to pipeline stalls. Such an application is characterized as back end bound.

For front end bound applications look at the following metrics:

* Instruction TLB metrics
* L1 Instruction cache metrics as well as L2 cache and last level cache metrics
* Branch predictor metrics

For back end bound applications look at the following metrics:

* Data TLB metrics
* Memory System related metrics
* Data cache metrics as well as L2 cache and last level cache metrics 
* Instruction mix

The following sections demonstrate the performance analysis methodology on an example application. 