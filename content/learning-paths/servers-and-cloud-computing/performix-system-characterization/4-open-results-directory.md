---
title: View raw benchmark results and generated plots
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## View the System Characterization tool results directly

The previous section showed you how to view and understand the tabular benchmark results in Arm Performix. Performix also gives a link to the underlying run directory for Arm System Characterization Tool in case you want to access the plots which aren't yet available in the Performix GUI or the underlying .json data files for integrating with other tools.

Click the "Open Run Directory" button on the "Summary" page of your run.

![Open Run Directory#center](./report-generated "Open Run Directory")

This will open a file browser full of `.png` and `.json` files for various benchmarks.

![Run Directory#center](./run-directory.webp "Run Directory")

## Some example plots

### Latency sweep
The latency sweep plot shows how the size of a memory access pattern affects memory latency. Red bars indicate points at which the different levels of cache get involved.
![Latency Sweep#center](./latency-sweep-plot.webp "Latency Sweep")

### Bandwidth

The `bandwidth.png` file shows the results of the bandwidth sweep recipe.
![Bandwidth Sweep#center](./bandwidth-sweep-plot.webp "Bandwidth Sweep")
The plot shows how certain memory access sizes dramatically impact the system memory bandwidth.


### Core to core latency
The `core_latency_heatmap_local.png` plot shows a color-coded heatmap of which combinations of cores incur higher latencies.
![Core to core latency#center](./core-to-core-latency-plot.webp "Core to core latency")


In this section:
- You viewed some of the plots that ASCT generates

You're now ready to analyze and optimize your own platform with Arm Performix and the Arm System Characterization Tool recipe.