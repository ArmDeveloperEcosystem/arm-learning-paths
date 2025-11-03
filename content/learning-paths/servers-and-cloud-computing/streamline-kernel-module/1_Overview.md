---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Linux kernel profiling with Arm Streamline

Performance tuning is not limited to user-space applications—kernel modules can also benefit from careful analysis. [Arm Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) is a powerful software profiling tool that helps developers understand performance bottlenecks, hotspots, and memory usage, even inside the Linux kernel. This learning path explains how to use Arm Streamline to profile a simple kernel module.

### Why profile a kernel module?

Kernel modules often operate in performance-critical paths, such as device drivers or networking subsystems. Even a small inefficiency in a module can affect the overall system performance. Profiling enables you to:

- Identify hotspots (functions consuming most CPU cycles)  
- Measure cache and memory behavior  
- Understand call stacks for debugging performance issues  
