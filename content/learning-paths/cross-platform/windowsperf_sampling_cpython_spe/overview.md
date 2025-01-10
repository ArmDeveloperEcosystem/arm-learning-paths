---
layout: learningpathall
title: Overview of Arm Statistical Profiling Extension 
weight: 2
---

## Arm Statistical Profiling Extension (SPE)

The Arm Statistical Profiling Extension (SPE) was introduced in the Armv8.2-A architecture, and is an optional feature from Armv8.1-A. 

SPE allows CPU instructions to be sampled and associated with the source code location where that instruction occurred.

 It provides non-invasive, hardware-based, statistical sampling for CPUs. Unlike the Performance Monitor Unit (PMU), SPE is a different module that integrates the sampling process into the instruction execution process within the pipelines of the CPU. 
 
 SPE provides a statistical view of the performance characteristics of executed instructions, which can be used by software writers to optimize their code for better performance.

SPE is particularly useful for performance analysis and optimization, as it provides detailed insights into the behavior of the CPU during execution. 

This can help identify performance bottlenecks and optimize software for better efficiency.

## Using SPE with WindowsPerf in this Learning Path

WindowsPerf includes `record` support for the Arm Statistical Profiling Extension (SPE). 

You will create a debug build of CPython from source and execute simple instructions in the Python interactive mode to obtain WindowsPerf sampling results from the CPython runtime image.

You will use the sampling to detect CPython program hot spots identified by the Arm Statistical Profiling Extension (SPE). 

{{% notice Note %}}
SPE is only available on Windows on Arm in Test Mode.
Windows Test Mode is a feature that allows you to install and test drivers that have not been digitally signed by Microsoft.
{{% /notice %}}
