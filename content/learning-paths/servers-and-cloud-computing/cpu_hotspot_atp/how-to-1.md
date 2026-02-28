---
title: Background Information
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

A flame graph is a visualization built from many sampled call stacks that shows where a program spends CPU time. In a performance investigation it is often the first thing to generate when it is not yet clear which parts of the codebase are affecting execution time. Instead of guessing where the bottleneck is, you take a quick sample of real execution and use the resulting graph to identify the hottest code paths that deserve deeper analysis.

## Example Flame Graph

Take a look at the example flame graph below. 

![example](./flame-graph-example.jpg)

The x axis represents the relative number of samples attributed to code paths ordered alphabetically, **not** a timeline. A wider block means that function appeared in more samples and therefore consumed more of the measured resource, typically CPU time. The y axis represents call stack depth. Frames at the bottom are closer to the root of execution such as a thread entry point, and frames above them are functions called by the frames below. A common workflow is to start with the widest blocks, then move upward through the stack to understand which callees dominate that hot path. Each sample captures a snapshot of the current call stack. Many samples are then aggregated by grouping identical stacks and summing their counts. This merging step is what makes flame graphs compact and readable. Reliable stack walking matters, and frame pointers are a common mechanism used to reconstruct the function call hierarchy consistently. When frame pointers are present, it is easier to unwind through nested calls and produce accurate stacks that merge cleanly into stable blocks.

This learning path is not meant as a detailed explanation of flame graphs, if you would like to learn more please read [this blog](https://www.brendangregg.com/flamegraphs.html) by the original creator, Brendan Gregg. 

## Tooling options

On Linux, flame graphs are commonly generated from samples collected with `perf`. perf periodically interrupts the running program and records a stack trace, then the collected stacks are converted into a folded format and rendered as the graph. Sampling frequency is important. If the frequency is too low you may miss short lived hotspots, and if it is too high you may introduce overhead or skew the results. To make the output informative, compile with debug symbols and preserve frame pointers so stacks resolve to meaningful function names and unwind reliably. A typical build uses `-g` and `-fno-omit-frame-pointer`.

Arm has also developed a tool that simplifies this workflow through the CPU Cycle hotspot recipe in Arm Total Performance, making it easier to configure collection, run captures, and explore the resulting call hierarchies without manually stitching together the individual steps. This is the tooling solution we will use in this learning path.