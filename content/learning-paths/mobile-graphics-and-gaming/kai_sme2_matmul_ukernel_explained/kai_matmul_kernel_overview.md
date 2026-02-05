---
title: How does a KleidiAI matmual microkernel perform matrix multiplication with quantized data?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How does a KleidiAI matmual microkernel perform matrix multiplication with quantized data? 
Essentially, a KleidiAI matmul microkernel uses tile-based matrix multiplication(matmul) where small submatrices of the output are computed one by one. 
- **mr**: number of rows of Matrix C (and Matrix A) computed at once
- **nr**: number of columns of Matrix C (and Matrix B) computed at once
- **bl**: number of elements from the K dimension processed per block at once
- **kr**: number of elements from the K dimension processed per inner step

The video below demonstrates how matrix multiplication is carried out using this method.
![Figure showing Tile-Based matrix multiplication with KleidiAI alt-text#center](videos/matrix_tile.gif "Tile-Based matrix multiplication with KleidiAI")

This process can be denoted with the following pseudocode,
```c
// RHS N LOOP
for(n_idx = 0; n_idx < n; n_idx+=nr){
    // LHS M LOOP
    for(m_idx = 0; m_idx < m; m_idx+=mr){
        // K LOOP, break K into blocks first
        blocks_in_K= K/bl;     // bl is the block length
        //Block Loop 
        for(bl_idx = 0; bl_idx< blocks_in_K; bl_idx += 1) {
              //Loop inside a block
              krs_in_block= bl/kr;  //kr is the number of elements in K dimension per inner loop
              for(k_idx = 0; k_idx < krs_in_block; k_idx +=1) {
               // Perform the matrix multiplication with source submatrices of size [mr, kr] and [kr, nr]
               // Accumulate the matrix multiplication result above into per block level result.
                 …
              }       
          // Accumulate per block level results along K dimension. When iteration on K dimension is completed,a submatrix of size [mr, nr] of the output matrix is ready        
        }
    //Continue computing a submatrix of size [mr, nr] of the output matrix along M dimension
   }
  //Continue computing a submatrix of size [mr, nr] of the output matrix along N dimension 
}
```
In general, KleidiAI matmul microkernels implement matrix mulitplication in a similar way as the pseudocode.

KleidiAI also provides corresponding packing microkernels for the matmul microkernels, in order to make efficient contiguous memory access to the input of the matrix multiplication, reducing cache misses.

KleidiAI supports quantized matrix multiplication to speed up AI inference on Arm CPUs. Instead of multiplying full precision (FP32) matrices A and B directly, it quantizes:
- The Left Hand Source (LHS , or Left Hand Martix/activation) matrix to 8-bit integers
- The Right Hand Source( RHS, or Left Hand Matrix/weights) matrix to 4-bit or 8-bit integers

then packs those quantized values into memory layouts suitable for the CPU vector instructions such as Dotprod, I8MM, SME2 instructions.
Runs a microkernel that efficiently computes on packed quantized data, then scales back to floating point.

This process can be illustrated in the following diagram,
![Figure showing quantized matrix multiplication with KleidiAI kernels alt-text#center](images/kai_matmul_kernel.jpg "Quantized matrix multiplication with KleidiAI kernel")

Please find more information in this learning path, [Accelerate Generative AI workloads using KleidiAI](https://learn.arm.com/learning-paths/cross-platform/kleidiai-explainer/).