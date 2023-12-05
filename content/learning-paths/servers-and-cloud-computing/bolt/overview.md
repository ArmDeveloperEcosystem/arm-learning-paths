---
title: Overview of the BOLT optimization process
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) is an optimization tool that uses Linux Perf data to re-order the executable code layout to reduce memory overhead and improve performance.

The BOLT optimization process is performed in three steps:
1. Collect performance data by running the executable on an Arm Linux target system
2. Convert the performance profile data into a new format used by BOLT
3. Run BOLT using the converted performance profile data to optimize the target executable and save a new, optimized executable

After these steps are run, the optimized executable should have improved performance compared to the original executable. 

There are different ways to collect performance profiles and different ways to convert the data for BOLT. 

You can run everything on a single Linux computer, or you can use two Linux computers and separate the software build and running BOLT from the collection of the performance data. 

The different ways of using BOLT are described in more detail in this Learning Path.
