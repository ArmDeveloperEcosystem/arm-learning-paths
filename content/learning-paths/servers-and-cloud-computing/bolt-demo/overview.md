---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Tutorial Overview

This tutorial shows how to apply [BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) in different configurations.
It is based on a demo from the 2025 LLVM Developers Conference:  
[BOLT tutorial on AArch64 and how it competes or complements other PGOs](https://youtu.be/KdHtOMc5_c8?si=249wZTn_YcTFOjcJ&t=1452).


The input program is a pathological case based on [BubbleSort](../setup), a workload with poor spatial locality.
First, we check whether the input binary is a good candidate for code layout optimization.
If it is, we can capture a profile using one of several profiling methods:
-	**[BRBE](../brbe)**: Samples deep branch stacks with low profiling overheads.
-	**[Instrumentation](../instrumentation)**: Captures high-quality, complete profiles, but has high collection overhead.
-	**[SPE](../spe)**: Samples individual branches. Use it if BRBE is not available, as profile quality can be lower.
-	**[PMU](../pmu)**: Samples basic events such as instructions or cycles. This method provides the least profiling information.

<!-- TODO: Heatmap -->

ETM and ETE generate data that you can use with BOLT. This tutorial does not cover these tracing methods.

For each profiling method, we will perform the relevant BOLT optimization steps.  
Finally, we will use hardware metrics to confirm how effective the optimization was.
