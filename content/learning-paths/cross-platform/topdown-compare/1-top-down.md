---
title: "Learn about Arm Neoverse and Intel x86 top-down performance analysis"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What are the differences between Arm and Intel x86 PMU counters?

This is a common question from both software developers and performance engineers working across architectures.

Both Intel x86 and Arm Neoverse CPUs provide sophisticated Performance Monitoring Units (PMUs) with hundreds of hardware counters. Instead of trying to list all available counters and compare microarchitecture, it makes more sense to focus on the performance methodologies they enable and the calculations used for performance metrics. 

While the specific counter names and formulas differ between architectures, both Intel x86 and Arm Neoverse have converged on top-down performance analysis methodologies that categorize performance bottlenecks into four buckets:

- Retiring
- Bad Speculation
- Frontend Bound
- Backend Bound

This Learning Path provides a comparison of how x86 processors implement four-level hierarchical top-down analysis compared to Arm Neoverse's two-stage methodology, highlighting the similarities in approach while explaining the architectural differences in PMU counter events and formulas.

## Introduction to top-down performance analysis

The top-down methodology makes performance analysis easier by shifting focus from individual PMU counters to pipeline slot utilization. Instead of trying to interpret dozens of seemingly unrelated metrics, you can systematically identify bottlenecks by attributing each CPU pipeline slot to one of four categories:

- Retiring: pipeline slots that successfully complete useful work
- Bad Speculation: slots wasted on mispredicted branches
- Frontend Bound: slots stalled due to instruction fetch/decode limitations
- Backend Bound: slots stalled due to execution resource constraints

The methodology uses a hierarchical approach that allows you to drill down only into the dominant bottleneck category, and avoid the complexity of analyzing all possible performance issues at the same time. 

The next sections compare the Intel x86 methodology with the Arm top-down methodology. 

{{% notice Note %}}
AMD also has an equivalent top-down methodology which is similar to Intel, but uses different counters and calculations. 
{{% /notice %}}
