---
title: "Analyze Intel x86 and Arm Neoverse top-down performance methodologies"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What are the differences between Arm Neoverse and Intel x86 PMU counters?

This is a common question from both software developers and performance engineers working with multiple architectures.

Both Intel x86 and Arm Neoverse CPUs provide sophisticated Performance Monitoring Units (PMUs) with hundreds of hardware counters. Instead of trying to list all available counters and compare microarchitectures, it makes more sense to focus on the performance methodologies they enable and the calculations used for performance metrics. 

Although counter names and formulas differ, both Intel x86 and Arm Neoverse classify performance bottlenecks into the same four top-level categories:

- Retiring
- Bad Speculation
- Frontend Bound
- Backend Bound

The first step is to focus on the dominant top-level bucket. Then, on Intel x86 you descend through the formal sub-levels. On Arm, you derive similar insights using architecture-specific event groups and formulas that approximate those sub-divisions.

This Learning Path compares Intel x86 Top-down Microarchitecture Analysis (a formal multi-level hierarchy) with Arm Neoverse top-down guidance (the same four level-1 buckets, but fewer standardized sub-levels). You will learn how the approaches align conceptually while noting differences in PMU event semantics and machine width.

## Introduction to top-down performance analysis

The top-down methodology makes performance analysis easier by shifting focus from individual PMU counters to pipeline utilization. Instead of trying to interpret dozens of metrics, you can systematically identify bottlenecks by attributing CPU pipeline activity to one of the four categories.

A slot represents one potential opportunity for a processor core to issue and execute a micro-operation (µop) during a single clock cycle. 
The total slots = (machine width × cycles), where each slot can be used productively or wasted through speculation or stalls.

**Retiring** represents slots that retire useful instructions (µops).

**Bad Speculation** accounts for slots consumed by mispredicted branches, pipeline flushes, or other speculative work that does not retire.
On Intel x86, this includes machine clears and on Arm Neoverse it is modeled through misprediction and refill events.

**Frontend Bound** identifies slots lost because the core cannot supply enough decoded micro-ops. On Intel this subdivides into frontend latency (instruction cache, ITLB, branch predictor) versus frontend bandwidth (µop supply limits). On Arm Neoverse you approximate similar causes with instruction fetch, branch, and L1 I-cache events.

**Backend Bound** covers slots where issued micro-ops wait on data or execution resources. Intel x86 subdivides this into memory bound (cache / memory hierarchy latency or bandwidth) versus core bound (execution port pressure, scheduler or reorder buffer limits). Arm Neoverse guidance uses memory versus core style breakdown with different PMU event groupings and separates long-latency data access from execution resource contention.

The methodology allows you to focus on the dominant bottleneck category, avoiding the complexity of analyzing all possible performance issues at the same time. 

The next sections compare the Intel x86 methodology with the Arm top-down methodology. 

{{% notice Notes %}}
This Learning Path uses the Arm Neoverse V2 when specific details are required, and some things will be different from other Neoverse N and Neoverse V processors. 

AMD also has an equivalent top-down methodology which is similar to Intel, but uses different counters and calculations. 
{{% /notice %}}

