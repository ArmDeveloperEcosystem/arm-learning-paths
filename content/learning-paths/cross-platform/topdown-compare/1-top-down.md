---
title: "Analyze Intel x86 and Arm Neoverse top-down performance methodologies"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What are the differences between Arm and Intel x86 PMU counters?

This is a common question from both software developers and performance engineers working across architectures.

Both Intel x86 and Arm Neoverse CPUs provide sophisticated Performance Monitoring Units (PMUs) with hundreds of hardware counters. Instead of trying to list all available counters and compare microarchitecture, it makes more sense to focus on the performance methodologies they enable and the calculations used for performance metrics. 

While the specific counter names and formulas differ between architectures, both Intel x86 and Arm Neoverse have converged on top-down performance analysis methodologies that categorize performance bottlenecks into four key areas:

- Retiring
- Bad Speculation
- Frontend Bound
- Backend Bound

This Learning Path provides a comparison of how x86 processors implement multi-level hierarchical top-down analysis compared to Arm Neoverse's methodology, highlighting the similarities in approach while explaining the architectural differences in PMU counter events and formulas.

## Introduction to top-down performance analysis

The top-down methodology makes performance analysis easier by shifting focus from individual PMU counters to pipeline slot utilization. Instead of trying to interpret dozens of seemingly unrelated metrics, you can systematically identify bottlenecks by attributing each CPU pipeline slot to one of the four categories.

**Retiring** represents pipeline slots that successfully complete useful work, while **Bad Speculation** accounts for slots wasted on mispredicted branches and pipeline flushes. **Frontend Bound** identifies slots stalled due to instruction fetch and decode limitations, whereas **Backend Bound** covers slots stalled by execution resource constraints such as cache misses or arithmetic unit availability.

The methodology allows you to drill down only into the dominant bottleneck category, avoiding the complexity of analyzing all possible performance issues at the same time. 

The next sections compare the Intel x86 methodology with the Arm top-down methodology. 

{{% notice Note %}}
AMD also has an equivalent top-down methodology which is similar to Intel, but uses different counters and calculations. 
{{% /notice %}}
