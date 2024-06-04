---
title: System compatibility check
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The Streamline CLI tools are native command-line tools that are designed to run directly on an Arm server running Linux. The tools provide a software profiling methodology that gives you clear and actionable performance data. You can use this data to guide the optimization of the heavily used functions in your software.

## System compatibility check

Before you begin, you can use the the Arm Sysreport utility to determine whether your system configuration supports hardware-assisted profiling. Follow the instructions in this [Learning Path tutorial][1] to discover how to download and run this utility.

[1]: https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/

The `perf counters` entry in the generated report will indicate how many CPU counters are available. The `perf sampling` entry will indicate if SPE is available. You will achieve the best profiles in systems with at least 6 available CPU counters and SPE.

The Streamline CLI tools can be used in systems with no CPU counters, but can only return a basic hot-spot profile based on time-based sampling.
No top-down methodology metrics will be available.

The Streamline CLI tools can give top-down metrics in systems with as few as 3 available CPU counters. The effective sample rate for each metrics will be lower, because we will need to time-slice the counters to capture all of the requested metrics, so you will need to run your application for longer to get the same number of samples for each metric. Metrics that require more input counters than are available cannot be captured.

The Streamline CLI tools can be used without SPE. Load operation data source metrics will not be available, and branch mispredict metrics may be less
accurate.
