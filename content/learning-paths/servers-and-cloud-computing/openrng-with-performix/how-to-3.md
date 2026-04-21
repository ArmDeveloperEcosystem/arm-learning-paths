---
title: Identify code hotspots with Arm Performix
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profile the baseline with Code Hotspots

Arm Performix includes a Code Hotspots recipe that shows which functions consume the most CPU time. This helps you prioritize optimization work based on evidence instead of guesswork. If you aren't familiar with flame graphs or sample-based profiling, see the [Find code hotspots with Arm Performix](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/) Learning Path.

From your local machine, open the Arm Performix GUI and run the Code Hotspots recipe on the baseline executable at `/home/ec2-user/Data-Processing-Example/build/src/main`.

![Arm Performix GUI showing where to create a new Code Hotspots analysis run for the baseline executable#center](./run-code-hotspot.jpg)

Configure the recipe with the path to the baseline executable, set the profiling duration to **No time limit** so the capture runs for the full workload, and set the sample rate to **High** for better resolution. Select **Run Recipe** to begin profiling.

When the run completes, Performix displays the flame graph:

![Arm Performix GUI showing flame graph#center](./flame-graph.jpg)

The flame graph shows CPU time distribution across the call stack, where wider blocks indicate higher cumulative execution time. The dominant feature is the wide base associated with `generateDistribution(...)`, indicating it is the primary hotspot and consumes the largest share of execution time.

Drilling into that region, most of the work comes from standard library random generation routines, particularly paths involving `std::normal_distribution<float>`. Those stacks are visibly wider than those involving `std::uniform_real_distribution<float>`, indicating that Gaussian (normal) sampling is significantly more expensive in terms of CPU cycles than uniform sampling. The imbalance wouldn't have been obvious from higher-level instrumentation, because both operations conceptually generate random numbers, but their computational cost differs.

In contrast, functions related to computing properties such as counting points within a rectangle or identifying a minimum point (for example, `min_length`-type operations) occupy relatively narrow regions of the graph, contributing only a small fraction of total runtime and representing no meaningful bottleneck.

## What you've learned and what's next

You used profiling data to highlight which function to optimize. Next, you accelerate random generation by enabling OpenRNG through Arm Performance Libraries.
