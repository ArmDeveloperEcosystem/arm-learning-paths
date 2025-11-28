---
title: Profile Linux kernel modules with Arm Streamline
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Performance tuning is not limited to user-space applications as kernel modules can also benefit from careful analysis. [Arm Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) is a powerful software profiling tool that helps developers understand performance bottlenecks, hotspots, and memory usage, even inside the Linux kernel. This Learning Path explains how to use Arm Streamline to profile a simple kernel module.
## Benefits of profiling Linux kernel modules with Arm Streamline

Kernel modules often operate in performance-critical paths, such as device drivers or networking subsystems. Even a small inefficiency in a module can affect the overall system performance.

Profiling enables you to:

- Identify hotspots (functions consuming most CPU cycles)
- Measure cache and memory behavior
- Understand call stacks for debugging performance issues
- Detect synchronization bottlenecks and race conditions
- Quantify the impact of code changes on system latency and throughput
- Validate that optimizations improve performance on Arm-based systems

By using Arm Streamline, you gain visibility into how your kernel module interacts with the rest of the system. This insight helps you make data-driven decisions to optimize code paths, reduce resource contention, and ensure your module performs efficiently on Arm platforms. Profiling is especially valuable when porting modules from x86 to Arm, as architectural differences can reveal new optimization opportunities or highlight previously hidden issues.
