---
layout: learningpathall
title: Summary
weight: 7
---
## Summary

WindowsPerf is a versatile performance analysis tool that offers two kinds of support:

* For software, it supports CPU PMU events.
* For hardware, it supports the SPE extension. 

The type of sampling it can perform depends on the availability of the Arm Statistical Profiling Extension (SPE) in the CPU. 

If the SPE extension is available, WindowsPerf can leverage hardware sampling to provide detailed performance insights. Otherwise, it relies on software sampling to gather performance data. 

This flexibility ensures that WindowsPerf can adapt to different hardware configurations and consistently deliver valuable performance metrics:

* You can use `wperf sample`, which is sampling mode, for determining the frequencies of event occurrences produced by program locations at the function, basic block, and instruction levels.

* You can use `wperf record`, which is the same as sample, but also automatically spawns the process and pins it to the core specified by `-c`. You can use `record` to pass verbatim arguments to the process.
