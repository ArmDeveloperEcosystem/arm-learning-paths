---
title: Identify CPU pipeline bottlenecks

weight: 5

layout: learningpathall
---

The CPU Microarchitecture recipe in Arm Performix provides a [Topdown analysis](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology) breakdown of how CPU execution capacity is used. This helps you identify where performance is lost due to stalls or inefficiencies, and whether your application is limited by frontend, backend, memory, or other CPU pipeline effects.

## Run the CPU Microarchitecture recipe

1. In Performix, select the **CPU Microarchitecture** recipe.

1. Specify the path to your compiled binary and run it with the same parameters as before:

    ```bash
    performix-analysis/dot_scalar 16777216 2000
    ```

1. Select **Run Recipe** to start the analysis. Performix collects data and presents the results using Topdown analysis.

    ![Topdown summary showing over 60% frontend bound classification for the dot_scalar function#center](images/cpu_ma_summary.png "CPU Microarchitecture Topdown summary")

## Interpret the results

The analysis shows that the application is over 60% frontend bound. This means the CPU frequently stalls while fetching or decoding instructions, even though backend resources are available. The CPU isn't compute-bound; it's waiting for instructions.

Performix provides guidance in the Insights panel to help you understand these results.

![Insights panel recommending investigation of instruction fetch and decode bottlenecks#center](images/cpu_ma_insights.png "CPU Microarchitecture insights")

## What you've accomplished

You now know the application is frontend bound, but this is a tight loop with predictable control flow. Frontend stalls in this context often indicate that the CPU is processing too many instructions per unit of work. The Instruction Mix recipe helps you confirm this by showing exactly what types of instructions the CPU executes.
