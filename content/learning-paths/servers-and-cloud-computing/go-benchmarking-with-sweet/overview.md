---
title: Overview
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Go Benchmarking Learning Path Overview

In this module, you’ll learn how to measure, collect, and compare Go performance data using:

- **Go Benchmarks**, a collection of pre-written benchmark definitions, standardizes performance tests for popular Go applications, leveraging Go's built-in benchmark support.

- **Sweet**, a benchmark runner, automates running Go benchmarks across multiple environments, collecting and formatting results for comparison.

- **Benchstat**, a statistical comparison tool, analyzes benchmark results to identify meaningful performance differences between systems.

You'll use Intel c4-standard-8 and Arm-based c4a-standard-4 instances on running on GCP to run and compare our benchmarks using the above tools.

{{% notice Note %}}
Arm-based c4a-standard-4 instances, and Intel-based c4-standard-8 instances both utilize four cores.  Both instances are  categorized by GCP as members of the **consistently high performing** series;  the main difference between these the two is that the c4a has 16 GB of RAM, while the c4 has 30 GB of RAM.  We've chosen to keep CPU cores equivalent across the two instances of the same series to keep the comparison as close as possible.
{{% /notice %}}

When you are finished running through this learning path, you'll have:

1. Brought up Arm and x86 instances of GCP-based VMs
2. Installed Go, benchmarks, benchstat, and sweet on the two VMs
3. Used sweet and benchstat to compare performance of Go applications on the two VMs
4. Extrapolated the knowledge to create Go Benchmarks for your own workloads and systems
