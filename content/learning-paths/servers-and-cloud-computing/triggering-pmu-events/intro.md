---
title: Introduction to the PMU
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Neoverse Core PMU
The Neoverse core PMU measures hardware events that occur during software execution. 

PMU events:

* Measure performance.
* Monitor workload efficiency.
* Track resource utilization and requirements. 

The [Arm Neoverse N2 PMU guide](https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en) describes the architecture and PMU event definitions. You can find other Neoverse core PMU guides on https://developer.arm.com/. 

This Learning Path explains how to trigger common PMU events in specific metric groups and explains why certain events are triggered. 

You can review example code fragments and see the resultant triggered PMU events.

## PMU Events 

This Learning Path uses the Neoverse N2 core to count PMU events, however the code and analysis of events can also be applied to other Neoverse cores. Check your Neoverse core's Technical Reference Manual to ensure compatibility. 

The Neoverse N2 has six counters that can be programmed to count any PMU event supported by the CPU. Some common microarchitectural events that might be tracked are cache or TLB accesses, and executed instructions.

This Learning Path covers cache events, specifically:

* Level 1 Data Cache Events.
* Level 1 Instruction Cache Events.
* Level 2 Unified Cache Events.
* Last Level Cache Events.