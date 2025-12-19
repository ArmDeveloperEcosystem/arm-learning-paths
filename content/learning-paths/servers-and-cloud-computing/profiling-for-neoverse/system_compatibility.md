---
title: System compatibility check
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## System compatibility check

Before you begin, you can use the Arm Sysreport utility to determine whether your system configuration supports hardware-assisted profiling. Follow the instructions in [Get ready for performance analysis with Sysreport][1] to discover how to download and run this utility.

[1]: /learning-paths/servers-and-cloud-computing/sysreport/

The `perf counters` entry in the generated report indicates how many CPU counters are available. The `perf sampling` entry indicates if SPE is available. You can achieve the best profiles in systems with at least 6 available CPU counters and SPE.

You can use the Streamline CLI tools in systems without any CPU counters, but can only return a basic hot-spot profile based on time-based sampling.
No top-down methodology metrics are available.

The Streamline CLI tools can generate top-down metrics in systems with as few as three available CPU counters. The effective sample rate for each metric is lower, because the counters need to be time-sliced to capture all of the requested metrics. You will need to run your application for longer to return the same number of samples for each metric. Metrics that require more input counters than are available cannot be captured.

The Streamline CLI tools can be used without SPE. Load operation data source metrics will not be available, and branch mispredict metrics may be less accurate.

{{% notice Note%}}The Streamline CLI tools are native command-line tools that are designed to run directly on an Arm server running Linux. The tools provide a software profiling methodology that gives you clear and actionable performance data. You can use this data to guide the optimization of the heavily used functions in your software.{{% /notice %}}