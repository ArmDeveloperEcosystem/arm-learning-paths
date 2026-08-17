---
title: Identify CPU pipeline bottlenecks in the scalar dot-product application

description: Use Arm Performix CPU Microarchitecture analysis to identify frontend and backend pipeline bottlenecks in a sample C++ application.

weight: 5

layout: learningpathall
---

## Run the CPU Microarchitecture recipe

The CPU Microarchitecture recipe in Arm Performix provides a [Topdown analysis](https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology) breakdown of how CPU execution capacity is used. You can use this analysis to identify where performance is lost due to stalls or inefficiencies. It also shows whether your application is limited by frontend, backend, memory, or other CPU pipeline effects.

To run the recipe:

1. In Performix, select the **CPU Microarchitecture** recipe.

1. Specify the path to your compiled binary and run it with the same parameters as before:

    ```bash
    performix-analysis/dot_scalar 16777216 2000
    ```

1. Leaving all other values as defaults, select **Run Recipe** to start the analysis. Performix collects data and presents the results using Topdown analysis.

## Interpret the results

The analysis shows that the application is 0.34% frontend stalled compared to 0.042% backend stalled. The exact values depend on your hardware.

This difference between frontend and backend stalls means the CPU stalls while fetching or decoding instructions, even though backend resources are available. The CPU isn't compute-bound. Instead, it's waiting for instructions.

![Arm Performix CPU Microarchitecture summary for dot_scalar showing Cycle Accounting with Frontend Stalled Cycles at 0.34% and Backend Stalled Cycles at 0.042%, followed by cache and branch efficiency metrics#center](images/cpu_ma_summary.png "CPU Microarchitecture Topdown summary")

Performix provides guidance in the **Insights** panel to help you understand these results.

![Arm Performix Insights panel recommending investigation of instruction fetch and decode bottlenecks, which explains the frontend-bound result#center](images/cpu_ma_insights.png "CPU Microarchitecture insights")

## What you've accomplished and what's next

You now know the application is frontend bound, but this is a tight loop with predictable control flow. Frontend stalls in this context often indicate that the CPU is processing too many instructions per unit of work.

Next, you'll run the Instruction Mix recipe to confirm this by seeing what types of instructions the CPU executes.
