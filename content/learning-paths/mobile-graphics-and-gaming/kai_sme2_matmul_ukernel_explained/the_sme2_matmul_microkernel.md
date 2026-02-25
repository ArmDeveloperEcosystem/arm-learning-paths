---
title: What is the sme2 lvlx4vl microkernel?
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the sme2 lvlx4vl microkernel?
We use a KleidiAI microkernel, *kai_matmul_clamp_f32_qsi8d32p1vlx4_qsi4c32p4vlx4_1vlx4vl_sme2_mopa*, to explain KleidiAI SME2 microkernels in detail. It is referred as ‘the SME2 matmul microkernel’ in this learning path onwards, unless otherwise noted.

“_1vlx4vl” in the name indicates that, in a single inner loop iteration, it computes an intermediate result for a 1VL x 4VL submatrix (one SME2 Streaming Vector Length x four SME2 Streaming Vector Length) of the ouput matrix. Assuming the SME2 SVL is 512 bits, it is a 16 x 64 (512/sizeof(FP32)) x (4 x 512/sizeof(FP32)) submatrix. 

To improve performance, we can pipeline four MOPA instructions and fully utilize four ZA tiles in ZA storage, each MOPA instruction uses one ZA tile. 
The video below demonstrates how the four MOPA instructions are used to perfrom matrix multiplication of one 16x4 submatrix (1VL) from matrix A and four 4x16 submatrices from matrix B (4VL) in a single iteration.
![Figure showing Matrix Multiplication with 1VLx4VL SME2 MOPA alt-text#center](videos/1vlx4vl_sme2_mopa.gif "Matrix Multiplication with 1VLx4VL SME2 MOPA")
The intermediate result of 4x16x16 output submatrix is held in four ZA.S tiles.

“qsi8d32p1vlx4” in the name indicates that it expects the LHS with a layout of [M, K] to be symmetrically quantized into signed INT8 type within blocks of 32 elements. 
The entire quantized LHS is then divided into submatrices of size 1VL × 4 (since the SME2 SVL is set as 512 bits, it is 16 × 4). Then, each submatrix is packed row-wise into a contiguous memory layout, all the submatrices are packed in this way one after another. So that when using the packed LHS in the SME2 matmul microkernel, memory accesses are to contiguous addresses, improving cache locality.

“qsi4c32p4vlx4” in its name indicates that the SME2 matmul microkernel expects the RHS with a layout of [N, K] to be symmetrically quantized into signed INT4 type within blocks of 32 elements.
The entire quantized RHS is then divided into submatrices of size 4VL × 4 (since the SME2 SVL is set as 512 bits, it is 4x16× 4). Each submatrix is packed row-wise into a contiguous memory layout. Since the quantization type is INT4, each byte contains two INT4 elements. In the SME2 matmul microkernel, the SME2 LUTI instructions efficiently dequantize INT4 elements into INT8 type, thereby enabling fast matrix multiplication with SME2 INT8 MOPA instructions.

“_f32_” in its name indicates that the SME2 matmul microkernel outputs FP32 result matrix. The INT32 result produced by SME2 INT8 MOPA instructions has to be dequantized back to FP32 type.

Sometimes, the original LHS or RHS may not conform to the quantization and packing format requirement of the SME2 matmul microkernel. The software needs to quantize and pack the LHS and RHS appropriately first.

Next, we will take llama.cpp and the Llama-3.2-3B-Q4_0.gguf model for example to demonstrate,
- how to quantize and pack the LHS and RHS 
- perform matrix multiplication using the SME2 matmul microkernel