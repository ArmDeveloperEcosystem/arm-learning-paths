---
title: Profile Linux kernel modules with Arm Streamline
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
Performance tuning is just as important for kernel modules as it is for user-space applications. Arm Streamline is a powerful profiling tool that helps you find performance bottlenecks, hotspots, and memory issues - even inside the Linux kernel. In this Learning Path, you'll learn how to use Arm Streamline to profile a simple kernel module on Arm-based systems. You'll see how profiling can reveal optimization opportunities and help you improve your module's efficiency.
## Benefits of profiling Linux kernel modules with Arm Streamline

Kernel modules often operate in performance-critical paths, such as device drivers or networking subsystems. Even a small inefficiency in a module can affect the overall system performance.

Profiling enables you to do the following:

- Identify hotspots (functions consuming most CPU cycles)
- Measure cache and memory behavior
- Understand call stacks for debugging performance issues
- Detect synchronization bottlenecks and race conditions
- Quantify the impact of code changes on system latency and throughput
- Validate that optimizations improve performance on Arm-based systems

By using Arm Streamline, you gain visibility into how your kernel module interacts with the rest of the system. This insight helps you make data-driven decisions to optimize code paths, reduce resource contention, and ensure your module performs efficiently on Arm platforms. Profiling is especially valuable when porting modules from x86 to Arm, as architectural differences can reveal new optimization opportunities or highlight previously hidden issues.
