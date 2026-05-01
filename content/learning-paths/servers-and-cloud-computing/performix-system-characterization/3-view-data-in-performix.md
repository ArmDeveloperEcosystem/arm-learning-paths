---
title: View benchmark results in the Performix UI
weight: 4

layout: learningpathall
---

Because the System Characterization recipe uses the standalone Arm System Characterization Tool (ASCT), it creates an output directory for all ASCT results and imports a subset of those results into the GUI. Performix presents the data in tabular form and links to the output directory for plots and raw data.

### Idle latency

In **Idle latency**, ASCT reports memory latency for each non-uniform memory access (NUMA) node while the system is idle. You can use this view to spot bottlenecks caused by workload placement, and to identify which nodes are closest to memory resources.

![Arm Performix Idle latency table showing NUMA-node memory latency#center](./idle-latency.webp "Idle latency per NUMA node while the system is idle")

### Peak bandwidth

**Peak bandwidth** shows the maximum measured memory bandwidth for different read and write patterns. It compares those results with the theoretical peak bandwidth of the system.

![Arm Performix Peak bandwidth table comparing measured and theoretical bandwidth#center](./peak-bandwidth.webp "Measured vs theoretical peak memory bandwidth")

### Cross-NUMA bandwidth

**Cross-NUMA bandwidth** shows the bandwidth achieved when memory requests cross NUMA node boundaries.

![Arm Performix Cross-NUMA bandwidth table showing inter-node bandwidth#center](./cross-numa-bandwidth.webp "Bandwidth across NUMA node boundaries")

### Latency sweep

The **Latency sweep** benchmark measures latency by data size to map the cache hierarchy and identify appropriate data sizes for other benchmarks. It highlights the performance characteristics of each level of the cache and memory hierarchy.

![Arm Performix Latency sweep table mapping latency across data sizes#center](./latency-sweep-table.webp "Latency by data size mapping the cache hierarchy")

### Bandwidth sweep

The **Bandwidth sweep** benchmark varies the data size used to generate memory accesses. It measures the bandwidth delivered by each level of the memory hierarchy.

![Arm Performix Bandwidth Sweep table mapping bandwidth across data sizes#center](./bandwidth-sweep-table.webp "Bandwidth by data size across the memory hierarchy")

### Core-to-core latency

The **Core-to-core latency** benchmark measures the latency of moving data from one core to another. Because the number of core pairs grows quickly, this benchmark runs on only a subset of system cores by default.

![Arm Performix Core-to-core latency table showing latency between selected cores#center](./core-to-core-ui.webp "Core-to-core latency for a subset of system cores")

### System Information

The **System Information** table shows the information collected by ASCT, including CPU, memory, and storage details. Use this view to cross-reference benchmark results with the hardware configuration of the target machine.

![Arm Performix System Information table with CPU, memory, and storage details#center](./system-information.webp "System Information")

## What you've learned and what's next

You've viewed the tabular benchmark results from ASCT in the Arm Performix UI.

Next, you'll inspect plots from the ASCT output directory that are not yet displayed directly in Performix.
