---
title: Introduction to the PMU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Neoverse Core PMU

The Neoverse Core PMU measures hardware events that occur during software execution. You can use PMU events to measure performance, monitor workload efficiency, and track resource utilization and requirements. 

The [Arm Neoverse N2 PMU guide](https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en)  describes the behavior of the different Performance Monitor Unit (PMU) events 
implemented in the Neoverse N2. You can find other Neoverse core PMU guides at https://developer.arm.com/. 

This Learning Path explains how you can trigger common PMU events in specific metric groups. 

You can find further introductory information on Arm CPU architecture and Arm assembly language by visiting the resources at [Learn the Architecture - A-profile – Arm®](https://www.arm.com/architecture/learn-the-architecture/a-profile). 

On that website, the following guides are helpful:

 - AArch64 Instruction Set Architecture (ISA).
 - AArch64 Memory Management.
 - AArch64 Memory Attributes and Properties.
 - Memory Systems, Ordering, and Barriers.

## PMU Events 

This Learning Path focuses on the Neoverse N2 core counting PMU events, however you can apply the code and analysis of events to other Neoverse cores. Check your Neoverse core's Technical Reference Manual to ensure compatibility. 

The Neoverse N2 has six counters that can be programmed to count any PMU event supported by the CPU. Some common microarchitectural events that can be tracked are cache or TLB accesses, and executed instructions.

This Learning Path covers these event groups:

- Topdown L1 Events.

- TLB Events:
   - Instruction TLB.
   - Data TLB.

 - Operation Events:
    - SIMD.
    - Scalar Floating-Point.
    - Integer and Branch.



