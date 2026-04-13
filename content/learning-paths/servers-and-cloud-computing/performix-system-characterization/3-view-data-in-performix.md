---
title: View Benchmark results in Performix UI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## View the run results in the Performix GUI

Since the System Charcterization recipe uses the standalone Arm System Characterization Tool (ASCT), it creates an output directory of all ASCT's results and brings some of them into the GUI. At the time of writing, Performix presents the data in tabular form and links to the output directory for plots and raw data.

### Idle Latency

In Idle Latency, ASCT reports a list of memory latency seen in each non-uniform memory access (NUMA) node while idle. This could be used to detect performance bottlenecks caused by workload configuration and identify which nodes are closer to memory resources.
![Idle Latency#center](./idle-latency.webp "Idle Latency results")

### Peak bandwidth

Peak bandwidth shows the maximum measured memory bandwidth observed for different patterns of read-write behavior and how it compares to the expected theorical peak the system could achieve.
![Peak Bandwidth#center](./peak-bandwidth.webp)

### Cross-NUMA bandwidth

The cross-NUMA bandwidth results show the bandwidth achieved by memory requests crossing NUMA node boundaries.
![Cross NUMA bandwidth#center](./cross-numa-bandwidth.webp "Cross-NUMA bandwidth")

### Latency sweep

The latency sweep benchmarks measures latency by datasize to map cache hierarchy and find optimal datasize for other benchmarks.
It detects the performance characteristics of each level of the memory and cache hierarchy.
![Latency Sweep Table#center](./latency-sweep-table.webp "Latency Sweep Table")

### Bandwidth sweep

Sweep bandwidth by datasize to map cache hierarchy.
Similar to the latency sweep results, this benchmark varies the data size used to inject memory accesses and measures the bandwidth each level of the memory hierarchy.
![Bandwith Sweep Table#center](./bandwidth-sweep-table.webp "Bandwidth Sweep Table")

### Core-to-core latency

The core-to-core latency benchmark measures the latency of moving data from one core to another. Because of the combinatorial size of pairs of cores, this benchmark by default only runs on a small subset of the system cores by default.
![Core to Core Latency Table#center](./core-to-core-ui.webp "Core to Core Latency Table")

### System Information

This table shows the system information collected by ASCT, including CPU, memory, and storage details.
![System Information#center](./system-information.webp "System Information")


## Summary
In this section:
- You viewed the benchmark results from ASCT in the Performix run results view.

You're now ready to view plots from the ASCT results directory that can't yet be displayed natively in the Performix UI.