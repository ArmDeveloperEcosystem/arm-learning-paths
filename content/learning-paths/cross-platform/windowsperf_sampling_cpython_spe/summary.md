---
layout: learningpathall
title: Summary
weight: 7
---
## Summary

WindowsPerf is a versatile performance analysis tool supporting both software (with CPU PMU events) and hardware sampling (with the SPE extension). 

The type of sampling it can perform depends on the availability of the Arm Statistical Profiling Extension (SPE) in the CPU. If the Arm SPE extension is present, WindowsPerf can leverage hardware sampling to provide detailed performance insights. Otherwise, it will rely on software sampling to gather performance data. This flexibility ensures that WindowsPerf can adapt to different hardware configurations and still deliver valuable performance metrics.

Use `wperf sample`, sampling mode, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and/or instruction levels.

Use `wperf record`, is the same as sample, but also automatically spawns the process and pins it to the core specified by `-c`. You can use `record` to pass verbatim arguments to the process.
