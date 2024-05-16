---
title: Introduction to the PMU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The Neoverse core PMU measures hardware events that occur during software execution. PMU events are used to measure performance, monitor workload efficiency, and track resource utilization and requirements. The [Arm Neoverse N2 PMU guide](https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en) describes the architectural background and PMU event definitions. You can find other Neoverse core PMU guides on https://developer.arm.com/. 

This Learning Path explains how to trigger common PMU events in specific metric groups and why certain events are triggered. 

You may want to review CPU architecture and Arm assembly language. More detail on [Learn the Architecture - A-profile – Arm®](https://www.arm.com/architecture/learn-the-architecture/a-profile). 

The following sections may be helpful:
 - AArch64 Instruction Set Architecture (ISA)
 - AArch64 Memory Management
 - AArch64 Memory Attributes and Properties
 - Memory Systems, Ordering, and Barriers

## PMU Events 

This Learning Path uses the Neoverse N2 core to count PMU events. The following code and analysis of events can be applied to other Neoverse cores. However, check your Neoverse core's Technical Reference Manual to ensure your core supports the event. 

The Neoverse N2 has six counters that can be programmed to count any PMU event supported by the CPU. This Learning Path describes common microarchitectural events, some of which may be cache or TLB accesses and executed instructions.

The event groups covered in this learning path are:
- Topdown L1 Events
- TLB Events
    - Instruction TLB
    - Data TLB
- Branch Events
- Operation Events
    - SIMD
    - Scalar Floating-Point
    - Integer & Branch



