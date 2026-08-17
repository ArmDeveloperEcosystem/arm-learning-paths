---
title: Examine the Instruction Mix

description: Use Arm Performix Instruction Mix to identify scalar and SIMD instruction patterns in a sample C++ application.

weight: 6

layout: learningpathall
---

## Run the Instruction Mix recipe

The Instruction Mix recipe in Arm Performix shows how your code uses different instruction types and Arm architectural features.

1. In Performix, select the **Instruction Mix** recipe.

1. Specify the path to your compiled binary and run it with the same parameters as before:

    ```bash
    performix-analysis/dot_scalar 16777216 2000
    ```

1. Leaving all other fields as defaults, select **Run Recipe** to start the analysis. Performix collects data and presents the results.

    ![Instruction Mix results showing the application is dominated by scalar operations with no SIMD usage#center](images/instruction_mix_scalar.png "Instruction Mix results for the scalar application")

## Interpret the results

The Instruction Mix analysis shows the distribution of instruction types used by your application. The results confirm that the code is dominated by scalar operations with no SIMD usage. Each loop iteration performs only a small amount of work but still consumes instruction bandwidth. This creates sustained pressure on the frontend because too many instructions are required per unit of useful computation.

The **Insights** panel identifies the root cause: the application is not using SIMD and is missing vectorization opportunities. Vectorization reduces the number of instructions required per element by performing multiple operations per instruction, directly relieving frontend pressure.

## What you've accomplished and what's next

The scalar application is frontend bound because it performs too many instructions per unit of useful work. Instruction Mix confirms that it misses SIMD opportunities, which the Neon optimization addresses next.
