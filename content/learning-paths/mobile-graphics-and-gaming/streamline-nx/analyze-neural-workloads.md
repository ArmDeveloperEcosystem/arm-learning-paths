---
title: Analysis of data
description: Inspect neural accelerator utilization, memory traffic, frame scheduling, and graph-operation costs on Mali G2-Ultra with Streamline.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

We will not cover all the information from a capture but focus on neural-related Timeline rows. Mali Timeline and Dispatch Graph Workloads connect these patterns to frames and operation costs. Performance engineers should also examine CPU scheduling, shader-core workloads and their opportunities for parallel execution, and traffic involving other GPU units.

Available rows depend on the counters collected and the chart template selected. See the [Mali G2 neural accelerator counter reference](https://arm-software.github.io/libGPUCounters/mali_g2_counter_reference.html#neural-accelerator) for metric definitions and the [Streamline ML for Vulkan analysis guide](https://support.arm.com/documentation/101816/9-9/Analyze-your-capture/Analyze-ML-for-Vulkan-workloads?lang=en) for workload analysis.

Select the **gear icon** beside a Timeline row to open its chart configuration. Each series has a **Description** field explaining what the counter measures. See the [Streamline 9.9 User Guide](https://developer.arm.com/documentation/101816/9-9) for more about chart configuration.

## Mali Neural Accelerator Overview

Expand **Mali Neural Accelerator Overview** to see overall activity and processing utilization. Compare **Neural Accelerator Usage** with **Neural Accelerator Utilization** to investigate gaps between queued work and computation. The example shows 89.7% data processing utilization during accelerator-active cycles, rather than across the entire frame.

![Streamline Mali Neural Accelerator Overview showing activity cycles and 89.7% data processing utilization during accelerator-active cycles#center](./images/nx_overview.png "Compare accelerator activity with processing utilization to select intervals for investigation.")

## Mali Neural Accelerator Details

Expand **Mali Neural Accelerator Details** to compare individual hardware-unit utilization over time. The example shows 80.6% convolution utilization, alongside lower reader and vector utilization. This highlights the convolution unit as a starting point for investigating operation costs. The **Clock Ratio** row estimates the neural accelerator clock relative to the top-level GPU clock.

![Streamline Mali Neural Accelerator Details showing clock ratio and hardware-unit utilization, with convolution utilization at 80.6% above reader and vector utilization#center](./images/nx_details.png "Compare hardware-unit utilization over time to identify the busiest parts of the accelerator.")

## Mali memory system

Expand **Mali Memory System** to compare **Neural Accelerator L2 Reads** with **Neural Accelerator L2 Writes**. These rows separate input and weight reads from output writes through the L2 memory system. The example shows more input-read traffic than weight reads or output writes, helping you identify traffic-heavy intervals. The values measure transferred bytes over the selected interval; they are not bandwidth rates.

![Streamline neural accelerator L2 read and write rows showing larger input-read traffic than weight reads or output writes over the selected interval#center](./images/nx_read_write.png "Compare input reads, weight reads, and output writes to investigate memory traffic over the same interval.")

Avoid interpreting these charts in isolation. Compare the same interval across utilization, memory traffic, and GPU activity rows to investigate possible bottlenecks.

## Mali Timeline

Mali Timeline helps you connect slow frames with GPU scheduling and neural accelerator activity. You can inspect individual frames, queue submissions, and workloads. Follow the **Neural stream (NX)** to identify idle gaps and see how neural work is scheduled relative to rendering. Selecting a workload reveals its Mali NX statistics, which you can compare with the neural accelerator utilization charts.

![Streamline Mali Timeline showing individual frames, GPU submissions, and Neural stream (NX) workloads alongside neural accelerator utilization charts#center](./images/mali-nx-timeline.png "You can inspect specific frames and see neural accelerator utilization alongside their GPU workloads.")

{{% notice Note %}}
In Streamline 9.9, [optical-flow pipelines using `VK_ARM_data_graph_optical_flow` do not provide Mali NX statistics](https://support.arm.com/documentation/101816/9-9/Getting-started-with-Streamline/Limitations-of-ML-for-Vulkan-workload-profiling). Pipeline events and summary information can still appear, as shown below, but detailed hardware-unit statistics are unavailable.

![Streamline Mali Timeline showing an optical-flow pipeline event with instance and duration information but no detailed Mali NX hardware-unit statistics#center](./images/optical_flow_limitation.png "Optical-flow pipeline information appears without detailed Mali NX hardware statistics.")
{{% /notice %}}

## Dispatch Graph Workloads

Dispatch Graph Workloads lets you compare the execution cost of neural workloads at different levels of detail. You can inspect TOSA operations and fused operation chains, comparing their durations and instance counts. Hardware-unit statistics show how operations use the input and weight readers, convolution unit, and vector unit, helping you investigate potential bottlenecks. You can also locate the corresponding workload in Mali Timeline to relate operation costs to frame scheduling.

![Streamline Dispatch Graph Workloads showing TOSA operation durations, instance counts, and hardware-unit utilization, including high convolution-unit utilization#center](./images/dispatch_graph_workloads.png "You can see execution times for specific operations in the Duration column. The convolution unit is well utilized in the operation shown.")

Each aggregation groups execution statistics differently. These breakdowns help you move from overall graph costs to individual operations and dispatches.

| Breakdown | Useful when |
|---|---|
| TOSA Operators | Finding operations that repeatedly consume the most time across dispatches |
| Graph | Comparing the total execution cost of different models in one capture |
| Session | Comparing graph sessions and their accumulated execution statistics |
| Instance | Finding individual dispatches that run longer than other instances |
| Command | Checking hardware or shader execution and mapping commands back to operations |

## Summary

You can compare utilization, hardware-unit activity, and memory traffic to identify intervals worth investigating. Mali Timeline connects those intervals to specific frames and GPU scheduling. Dispatch Graph Workloads helps you examine expensive operations and their hardware-unit utilization. Together, these views help you decide whether to investigate scheduling, computation, or data movement.
