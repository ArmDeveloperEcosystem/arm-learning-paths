---
title: Overview
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview of Go benchmarking tools

This section shows you how to measure, collect, and compare Go performance data across different CPU architectures. These techniques help developers and system architects make informed infrastructure decisions for their Go applications.

You'll gain hands-on experience with:

- **Go Benchmarks**, standardized definitions for popular Go applications, using Go’s built-in testing framework.

- **Sweet**, a benchmark runner that automates execution and formats results for comparison across multiple environments.

- **Benchstat**, a statistical comparison tool that analyzes benchmark results to identify meaningful performance differences between systems.

Benchmarking is critical for modern software development because it allows you to:
- Quantify the impact of code changes
- Compare performance across hardware platforms 
- Make data-driven decisions about infrastructure
- Identify optimization opportunities in your application code

In this learning path, you'll compare performance using two four-core GCP instance types: the Intel-based c4-standard-8 and the Arm-based c4a-standard-4.

{{% notice Note %}}
Arm-based c4a-standard-4 instances and Intel-based c4-standard-8 instances both utilize four cores. Both instances are categorized by GCP as members of the **consistently high-performing** series; the main difference between the two is that c4a has 16 GB of RAM, while c4 has 30 GB of RAM. This Learning Path uses equivalent core counts to ensure a fair performance comparison.
{{% /notice %}}   



