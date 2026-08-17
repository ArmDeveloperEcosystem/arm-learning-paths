---
title: Validate the optimized dot-product application

description: Compare scalar and Neon runs in Arm Performix to validate changes in runtime, instruction mix, and CPU bottlenecks.

weight: 8

layout: learningpathall
---

## Run the recipes on the optimized binary

You can now compare the scalar and Neon-optimized versions using Arm Performix to validate changes in runtime, instruction mix, and bottleneck behavior.

Run each recipe one at a time by specifying the path to the optimized binary `performix-analysis/dot_neon 16777216 2000` and the same parameters as before. 

## Compare Code Hotspots results

The exact results depend on your hardware, but the most visible improvement is wall-clock time and total cycle count. Processing four elements per loop iteration using SIMD reduces the total number of instructions executed. The flame graph shows the same dominant function (`dot_neon`), but the sample count is significantly lower.

![Arm Performix Code Hotspots Flame Graph view for dot_neon showing the function rows and an Insights panel reporting 99.98% of samples for dot_neon, confirming it is the dominant function in the optimized run#center](images/neon_cpu_hotspots_flame_graph.png "Code Hotspots flame graph for the Neon-optimized binary")

## Compare Instruction Mix results

Select the previous scalar Instruction Mix run to compare it with the optimized version side by side:

![Arm Performix Instruction Mix comparison with the scalar instruction_mix_scalar run selected in the Compare with control, preparing a side-by-side comparison with the optimized run#center](images/comparison.png "Selecting the scalar Instruction Mix run from the Compare with control")

The exact results depend on your hardware, but the overlay shows Advanced SIMD instructions appearing in the optimized version while scalar operations decrease. This confirms more work is done per instruction.

![Arm Performix Instruction Mix breakdown for the NEON-optimized binary showing Advanced SIMD instructions, which confirms that vector operations are executing#center](images/neon_instruction_mix.png "Instruction Mix for the Neon-optimized binary")

The scalar version is dominated by floating-point and load operations. The Neon version introduces Advanced SIMD, reducing the number of instructions required per element and directly relieving frontend pressure.

## Compare CPU Microarchitecture results

The CPU Microarchitecture recipe confirms the bottleneck has shifted. After vectorization, frontend stalled cycles drop and backend effects become dominant. 

The exact results depend on your hardware. In this case, frontend stalls drop to zero, while backend stalls increase to ~47%. 

![Arm Performix CPU Microarchitecture Cycle Accounting comparison showing Frontend Stalled Cycles at 0% versus a 0.34% baseline and Backend Stalled Cycles at 46.76% versus a 0.042% baseline after Neon optimization#center](images/neon_cpu_ma_summary.png "CPU Microarchitecture results for the Neon-optimized binary")

The exact results depend on your hardware, but this demonstrates a common pattern in performance optimization: improving one part of the pipeline shifts pressure elsewhere. With the bottleneck moved from the frontend to the backend, the CPU executes more efficiently. Demand shifts to execution units and memory. This iterative cycle of measure, change, and validate is what Performix is designed to support.

## What you've accomplished

You've compared performance between scalar and Neon-optimized versions of a C++ application using Arm Performix.

Now that you've completed a full optimization cycle, you can explore how to integrate Performix into broader development workflows and use these profiling steps for your own applications.
