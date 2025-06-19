---
title: Benchmark Types and Metrics
weight: 50

### FIXED, DO NOT MODIFY
layout: learningpathall
---

With setup complete, you can now run and analyze the benchmarks.  Before you do, it's good to understand all the different pieces in more detail.

## Choosing a Benchmark to Run

Whether running manually or automatically, the benchmarking process consists of two main steps:

1. **Running benchmarks with Sweet**: `sweet` executes the benchmarks on each VM, generating raw performance data

2. **Analyzing results with Benchstat**: `benchstat` compares the results from different VMs to identify performance differences.  Benchstat can output results in text format (default) or CSV format. The text format provides a human-readable tabular view, while CSV allows for further processing with other tools.

Sweet comes ready to run with the following benchmarks:  

| Benchmark       | Description                                                                                                                               | Command                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **biogo-igor**    | Processes pairwise alignment data using the biogo library, grouping repeat feature families and outputting results in JSON format.         | `sweet run -count 10 -run="biogo-igor" config.toml`           |
| **biogo-krishna** | Pure-Go implementation of the PALS algorithm for pairwise sequence alignment, measuring alignment runtime performance.                    | `sweet run -count 10 -run="biogo-krishna" config.toml`        |
| **bleve-index**   | Indexes a subset of Wikipedia articles into a Bleve full-text search index to assess indexing throughput and resource usage.            | `sweet run -count 10 -run="bleve-index" config.toml`          |
| **cockroachdb**   | Executes CockroachDB KV workloads with varying read percentages (0%, 50%, 95%) and node counts (1 & 3) to evaluate database performance. | `sweet run -count 10 -run="cockroachdb" config.toml`          |
| **esbuild**       | Bundles and minifies JavaScript/TypeScript code using esbuild on a representative codebase to measure build speed and efficiency.        | `sweet run -count 10 -run="esbuild" config.toml`              |
| **etcd**          | Uses the official etcd benchmarking tool to stress-test an etcd cluster, measuring request latency and throughput for key-value operations. | `sweet run -count 10 -run="etcd" config.toml`                 |
| **go-build**      | Compiles a representative Go module (or the Go toolchain) to measure compilation time and memory (RSS) usage on supported platforms.     | `sweet run -count 10 -run="go-build" config.toml`             |
| **gopher-lua**    | Executes Lua scripts using the GopherLua VM to benchmark the performance of a pure-Go Lua interpreter.                                   | `sweet run -count 10 -run="gopher-lua" config.toml`           |
| **markdown**      | Parses and renders Markdown documents to HTML using a Go-based markdown library to evaluate parsing and rendering throughput.            | `sweet run -count 10 -run="markdown" config.toml`             |
| **tile38**        | Stress-tests a Tile38 geospatial database with WITHIN, INTERSECTS, and NEARBY queries to measure spatial query performance.              | `sweet run -count 10 -run="tile38" config.toml`               |

## Metrics Summary

When running benchmarks, several key metrics are collected to evaluate performance.  The following summarizes the most common metrics and their significance:

### Seconds per Operation - Lower is better

This metric measures the time taken to complete a single operation, indicating the raw speed of execution. It directly reflects the performance efficiency of a system for a specific task, making it one of the most fundamental benchmarking metrics.

A system with lower seconds per operation completes tasks faster.
 This metric primarily reflects CPU performance but can also be influenced by memory access speeds and I/O operations. If seconds per operation is the only metric showing significant difference while memory metrics are similar, the performance difference is likely CPU-bound.

### Operations per Second - Higher is better
This metric provides a clear measure of system performance capacity, making it essential for understanding raw processing power and scalability potential. A system performing more operations per second has greater processing capacity.

This metric reflects overall system performance including CPU speed, memory access efficiency, and I/O capabilities.

If operations per second is substantially higher while memory usage remains proportional, the system likely has superior CPU performance. High operations per second with disproportionately high memory usage may indicate performance gains through memory-intensive optimizations. A system showing higher operations per second but also higher resource consumption may be trading efficiency for raw speed.

This metric is essentially the inverse of "seconds per operation" and provides a more intuitive way to understand throughput capacity.

### Average RSS Bytes - Lower is better

Resident Set Size (RSS) represents the portion of memory occupied by a process that is held in RAM (not swapped out). It shows the typical memory footprint during operation, indicating memory efficiency and potential for scalability.

Lower average RSS indicates more efficient memory usage. A system with lower average RSS can typically handle more concurrent processes before memory becomes a bottleneck.  This metric reflects both algorithm efficiency and memory management capabilities.

If one VM has significantly higher seconds per operation but lower RSS, it may be trading speed for memory efficiency. Systems with similar CPU performance but different RSS values indicate different memory optimization approaches; lower RSS with similar CPU performance suggests better memory management, which is a critical indicator of performance in memory-constrained environments.

### Peak RSS Bytes - Lower is better

Peak RSS bytes is the maximum Resident Set Size reached during execution, representing the worst-case memory usage scenario. The peak RSS metric helps to understand memory requirements and potential for memory-related bottlenecks during intensive operations.

Lower peak RSS indicates better handling of memory-intensive operations. High peak RSS values can indicate memory spikes that might cause performance degradation through swapping or out-of-memory conditions.

Large differences between average and peak RSS suggest memory usage volatility. A system with lower peak RSS but similar performance is better suited for memory-constrained environments.

### Peak VM Bytes - Lower is better

Peak VM Bytes is the maximum Virtual Memory size used, including both RAM and swap space allocated to the process. 

Lower peak VM indicates more efficient use of the total memory address space. High VM usage with low RSS suggests the system is effectively using virtual memory management. Extremely high VM with proportionally low RSS might indicate memory fragmentation issues.

If peak VM is much higher than peak RSS, the system is relying heavily on virtual memory management.  Systems with similar performance but different VM usage patterns may have different memory allocation strategies. High VM with performance degradation suggests potential memory-bound operations due to excessive paging.

## Summary of Efficiency Indicators

When comparing metrics across two systems, keep the following in mind:

### CPU-bound vs Memory-bound
A system is likely CPU-bound if seconds per operation differs significantly while memory metrics remain similar.

A system is likely memory-bound if performance degrades as memory metrics increase, especially when peak RSS approaches available physical memory.

### Efficiency Indicators
The ideal system shows lower values across all metrics - faster execution with smaller memory footprint. Systems with similar seconds per operation but significantly different memory metrics indicate different optimization priorities.

### Scalability Potential
Lower memory metrics (especially peak values) suggest better scalability for concurrent workloads. Systems with lower seconds per operation but higher memory usage may perform well for single tasks but scale poorly.

### Optimization Targets
Large gaps between average and peak memory usage suggest opportunities for memory optimization.  High seconds per operation with low memory usage suggests CPU optimization potential.

## Best Practices when benchmarking across different instance types

Here are some general tips to keep in mind as you explore benchmarking across different apps and instance types:

- Unlike Intel and AMD processors that use hyper-threading, Arm processors provide single-threaded cores without hyper-threading. A four-core Arm processor has four independent cores running four threads, while an four-core Intel processor provides eight logical cores through hyper-threading. This means each Arm vCPU represents a full physical core, while each Intel/AMD vCPU represents half a physical core. For fair comparison, this learning path uses a 4-vCPU Arm instance against an 8-vCPU Intel instance.  When scaling up instance sizes during benchmarking, make sure to keep a 2:1 Intel/AMD:Arm vCPU ratio if you wish to keep parity on CPU resources.

- It's suggested to run each benchmark at least 10 times (specified via the `count` parameter) to handle outlier/errant runs and ensure statistical significance.

- Results may be bound by CPU, memory, or I/O performance.  If you see significant differences in one metric but not others, it may indicate a bottleneck in that area; running the same benchmark with different configurations (e.g., more CPU cores, more memory) can help identify the bottleneck.



    



