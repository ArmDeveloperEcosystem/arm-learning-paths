---
title: Analyze Instruction Mix

weight: 6

layout: learningpathall
---
The Instruction Mix recipe in Arm Performix helps you understand how your code uses different instruction types and Arm architectural features.

### Running the Instruction Mix Recipe

1. In Arm Performix, select the Instruction Mix recipe.

2. Specify the path to your compiled workload and run it with the same parameters as before:

```bash
./dot_scalar 16777216 2000
```

3. Start the analysis. Arm Performix will collect data and present the results.

    ![Viewing Instruction Mix results in Arm Performix #center](images/instruction_mix_scalar.png "Viewing Instruction Mix results in Arm Performix")

### Interpreting the Results

The Instruction Mix analysis shows the distribution of different instruction types used by your workload. In this example, the analysis shows that the workload is dominated by scalar operations, with no SIMD usage. The frontend is overloaded not because the code is complex, but because it takes too many instructions to do too little work. This suggests that there are opportunities to optimize the code by introducing data-level parallelism using Advanced SIMD instructions.

Each iteration does only a small amount of work but still consumes instruction bandwidth. This creates sustained pressure on the frontend, not because instruction fetch is slow, but because too many instructions are required.
The insights panel lists the possible causes. It correctly identifies that we are not making use of SIMD and are missing vectorization opportunities. Vectorization would reduce the number of instructions required per element by performing multiple operations per instruction, directly relieving frontend pressure.

Let's optimize the scalar dot-product loop using Arm NEON intrinsics to improve instruction efficiency.
