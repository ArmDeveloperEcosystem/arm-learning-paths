---
title: Launching an Axion C4a Instance
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Go Benchmarking Learning Path Overview

Welcome to the **Go Benchmarking** learning path! In this module, you’ll learn how to measure, collect, and compare Go performance data using three key tools:

- **Golang Benchmark** (the core benchmark harness)  
- **Sweet** (a multi-node benchmark runner)  
- **Benchstat** (a statistical comparison tool)  

By the end of this path, you’ll be able to:

1. Install and configure all three tools  
2. Run benchmarks across one or more machines with Sweet  
3. Aggregate and compare benchmark outputs using Benchstat  

---

## 1. What Is Go Benchmark?

Go’s built-in benchmark support lives in the `testing` package (built into the standard library), but the **Golang Benchmark** suite in the `golang.org/x/benchmarks` repo provides additional harnesses and workloads for measuring more complex scenarios:

- **Repo:** [golang.org/x/benchmarks](https://pkg.go.dev/golang.org/x/benchmarks)  
- **Purpose:**  
  - Provide reproducible benchmark definitions  
  - Offer a consistent harness for CPU, memory, and I/O tests  
  - Include sample benchmarks covering common Go idioms  

You’ll use these harnesses as the basis for your own performance tests.

---

## 2. What Is Sweet?

**Sweet** is the command-line orchestrator for running Go benchmarks at scale:

- **Repo:** [golang.org/x/benchmarks/sweet](https://pkg.go.dev/golang.org/x/benchmarks/sweet)  
- **Purpose:**  
  - Automate running benchmarks on one or more remote hosts  
  - Collect and upload results in a structured JSON format  
  - Support tagging, profiling, and metadata annotations  

With Sweet, you can easily compare performance across different environments (e.g., Arm-based servers vs. x86 instances).

---

## 3. What Is Benchstat?

**Benchstat** is the statistical comparison tool for Go benchmark outputs:

- **Repo:** [golang.org/x/perf/cmd/benchstat](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat)  
- **Purpose:**  
  - Parse JSON or text benchmark results  
  - Compute statistical metrics (mean, median, % change)  
  - Highlight significant regressions or improvements  

Benchstat helps you make data-driven decisions by surfacing real performance deltas.

---

## 4. Learning Path Workflow

### Step 1: Installation

1. Ensure you have Go 1.20+ installed.  
2. Install the benchmarks harness and tools:
   ```bash
   go install golang.org/x/benchmarks/cmd/benchcmp@latest
   go install golang.org/x/benchmarks/sweet@latest
   go install golang.org/x/perf/cmd/benchstat@latest