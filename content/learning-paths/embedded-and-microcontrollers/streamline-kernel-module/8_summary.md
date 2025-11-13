---
title: Summary
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Summary

In this learning path, you learned how to build and profile Linux kernel modules step by step. You started with an out-of-tree character driver that had a cache performance issue and then used Arm Streamline to spot where the problem was. Later, you tried the same idea with an in-tree driver and saw how profiling works with the full kernel. Although the example problem was simple, the same methods apply to complex, real-world drivers and scenarios.

The key takeaway is that profiling isn’t just about making code faster—it’s about understanding how your code talks to the hardware. Streamline gives us a clear picture of what’s happening inside the CPU so you can write better, more efficient drivers. By learning to identify bottlenecks, you will be more confident in fixing them and avoiding common mistakes in kernel programming.
