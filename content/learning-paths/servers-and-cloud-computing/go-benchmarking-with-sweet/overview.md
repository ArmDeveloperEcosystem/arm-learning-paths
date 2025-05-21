---
title: Overview
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Go Benchmarking Learning Path Overview

Welcome to the **Go Benchmarking** learning path! In this module, you’ll learn how to measure, collect, and compare Go performance data using three key codebases:

- **Go Benchmarks** (a collection of pre-written benchmark definitions)
- **Sweet** (a benchmark runner)  
- **Benchstat** (a statistical comparison tool)

### What's are Go Benchmarks?

Go has built-in benchmark support built into the standard library, allowing you to create custom benchmarks for your own workloads.  The **Golang Benchmark** suite available at `https://github.com/golang/benchmarks` repo provides pre-written benchmarks for popular Go-based applications, making it easy to run standardized benchmarks across different systems with very little effort.

You will have the benchmarks pre-written for you from the github repo, but you will need to install and configure the **Sweet** tool to run them.

### What Is Sweet?

The **Sweet** tool is a command-line orchestrator for running Go benchmarks at scale.  It is designed to automate the process of running benchmarks on one or more remote hosts, collecting results, and writing them in a structured JSON format.

With Sweet, you can easily compare performance across different environments (e.g., Arm-based servers vs. x86 instances).

Once you've run the benchmarks, you can use the **Benchstat** tool to analyze the results and identify performance regressions or improvements.

### What Is Benchstat?

**Benchstat** is the statistical comparison tool for Go benchmark outputs.  It parses JSON or text benchmark results, and compares them using statistical methods to identify performance changes.  Benchstat helps you make data-driven decisions by surfacing real performance deltas.

When you are finished running through this learning path, you'll have:

1. Brought up Arm and x86 instances of GCP-based VMs
2. Installed Go, benchmarks, benchstat, and sweet on the two VMs
3. Used sweet and benchstat to compare performance of Go applications on the two VMs
4. Extrapolate the knowledge to create Go Benchmarks for your own workloads and systems
