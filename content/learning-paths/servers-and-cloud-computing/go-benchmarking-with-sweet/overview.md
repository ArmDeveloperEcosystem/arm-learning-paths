---
title: Overview
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Go Benchmarking Overview

In this section, you will learn how to measure, collect, and compare Go performance data across different CPU architectures. This knowledge is essential for developers and system architects who need to make informed decisions about infrastructure choices for their Go applications.

You'll gain hands-on experience with:

- **Go Benchmarks**, a collection of pre-written benchmark definitions that standardizes performance tests for popular Go applications, leveraging Go's built-in benchmark support.

- **Sweet**, a benchmark runner that automates running Go benchmarks across multiple environments, collecting and formatting results for comparison.

- **Benchstat**, a statistical comparison tool that analyzes benchmark results to identify meaningful performance differences between systems.

Benchmarking is critical for modern software development because it allows you to:
- Quantify the performance impact of code changes
- Compare different hardware platforms objectively
- Make data-driven decisions about infrastructure investments
- Identify optimization opportunities in your applications

You'll use Intel c4-standard-8 and Arm-based c4a-standard-4 (both four-core) instances running on GCP to run and compare benchmarks using these tools.

{{% notice Note %}}
Arm-based c4a-standard-4 instances and Intel-based c4-standard-8 instances both utilize four cores. Both instances are categorized by GCP as members of the **consistently high performing** series; the main difference between the two is that the c4a has 16 GB of RAM, while the c4 has 30 GB of RAM. We've chosen to keep CPU cores equivalent across the two instances of the same series to keep the comparison as close as possible.
{{% /notice %}}   



