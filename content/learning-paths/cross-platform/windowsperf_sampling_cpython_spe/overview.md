---
layout: learningpathall
title: Overview
weight: 2
---

## Introduction to the Arm Statistical Profiling Extension (SPE)

The Arm Statistical Profiling Extension (SPE) is an optional feature in Armv8.2 hardware that allows CPU instructions to be sampled and associated with the source code location where that instruction occured.

 It provides non-invasive, hardware-based statistical sampling for CPUs. Unlike the Performance Monitor Unit (PMU), SPE is a different module that integrates the sampling process into the instruction execution process within the CPU's pipelines.

SPE is particularly useful for performance analysis and optimization, as it provides detailed insights into the behavior of the CPU during execution. This can help identify performance bottlenecks and optimize software for better efficiency.

## Overview

You will use sampling to determine the CPython program "hot" locations as provided by the Arm Statistical Profiling Extension (SPE).

WindowsPerf includes `record` support for the Arm Statistical Profiling Extension (SPE). 

{{% notice Note %}}
SPE is only available on Windows on Arm in Test Mode.
Windows Test Mode is a feature that allows you to install and test drivers that have not been digitally signed by Microsoft.
{{% /notice %}}
