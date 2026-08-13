---
title: Analyze the optimized code

weight: 8

layout: learningpathall
---
In this section, you'll compare the performance of the scalar and NEON-optimized versions of your workload using Arm Performix. This comparison will help you validate changes in runtime, instruction mix, and bottleneck behavior.

## Running the Optimized Workload

1. In Arm Performix, select the Code Hotspots, CPU Microarchitecture, and Instruction Mix recipes.

2. Specify the path to your optimized workload and run it with the same parameters as before:

    ```bash
    ./dot_neon 16777216 2000
    ```

3. Start the analysis for each recipe.

## Comparing Results
When we run the same recipes with the optimized version, the most obvious improvement is wall-clock time and total cycle count. This comes from processing four elements per loop iteration using SIMD. The flame graph shows the same dominant function, but the sample count has reduced significantly.

![Viewing the flame graph for the NEON-optimized code #center](images/neon_cpu_hotspots_flame_graph.png "Viewing the flame graph for the NEON-optimized code")

Re-running the Instruction Mix recipe, we should see:

- Increased percentage of Advanced SIMD instructions
- Reduced proportion of scalar floating-point operations
- Fewer loop-control instructions relative to work done

We can compare the new Instruction Mix data with the scalar version, by selecting the previous Instruction Mix run:

![Comparing Instruction Mix results with the previous run #center](images/comparison.png "Comparing Instruction Mix results with the previous run")

Being able to overlay runs directly makes it easy to see how instruction usage changes after optimization. Here, it shows SIMD instructions in the optimized version, while scalar operations decrease, indicating more work done per instruction.

![Viewing Instruction Mix for the NEON-optimized code #center](images/neon_instruction_mix.png "Viewing Instruction Mix for the NEON-optimized code")

While the scalar version is dominated by integer, FP and load operations, the NEON version introduces vectorization with Advanced SIMD, reducing the number of instructions required per element and directly relieving frontend pressure.

### Validating Improvements

Re-running the CPU microarchitecture recipe shows that after vectorization, frontend stalls drop significantly, and backend effects become dominant. The change is dramatic:

- **Frontend Bound**: Drops from ~60% to ~11%.
- **Backend Bound**: Increases to ~63%.

![Viewing CPU microarchitecture results for the NEON-optimized code #center](images/neon_cpu_ma_summary.png "Viewing CPU microarchitecture results for the NEON-optimized code")

This example demonstrates a common pattern in modern performance optimization: Improving one part of the pipeline increases pressure elsewhere. With the bottleneck shifted from the frontend to the backend, the CPU executes more efficiently, and demand shifts to execution units and memory. This iterative investigation (measure, change, validate) is exactly what Arm Performix is designed to support.
