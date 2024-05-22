---
title: Introduction to the PMU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Neoverse Core PMU

The Neoverse core PMU measures hardware events that occur during software execution. PMU events are used to measure performance, monitor workload efficiency, and track resource utilization and requirements. 

The [Arm Neoverse N2 PMU guide](https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en) describes the architectural background and PMU event definitions. You can find other Neoverse core PMU guides on https://developer.arm.com/. 

This Learning Path explains how to trigger common PMU events in specific metric groups and explains why certain events are triggered. 

You can learn more about the Arm CPU architecture and Arm assembly language, by reading [Learn the Architecture - A-profile – Arm®](https://www.arm.com/architecture/learn-the-architecture/a-profile). 

The following sections are particularly helpful:

 - AArch64 Instruction Set Architecture (ISA).
 - AArch64 Memory Management.
 - AArch64 Memory Attributes and Properties.
 - Memory Systems, Ordering, and Barriers.

## PMU Events 

This Learning Path uses the Neoverse N2 core to count PMU events, however the code and analysis of events can be applied to other Neoverse cores. Check your Neoverse core's Technical Reference Manual to ensure compatibility. 

The Neoverse N2 has six counters that can be programmed to count any PMU event supported by the CPU. Some common microarchitectural events that might be tracked are cache or TLB accesses, and executed instructions.

This Learning Path covers these event groups:

- Topdown L1 Events.

- TLB Events:
   - Instruction TLB.
   - Data TLB.

- Branch Events.

- Operation Events:
    - SIMD.
    - Scalar Floating-Point.
    - Integer and Branch.



