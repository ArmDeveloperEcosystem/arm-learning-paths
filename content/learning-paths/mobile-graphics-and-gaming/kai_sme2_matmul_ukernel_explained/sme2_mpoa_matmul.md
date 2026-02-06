---
title: How are SME2 INT8 Outer Product Accumulate instructions used in a matrix multiplication?
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How are SME2 INT8 Outer Product Accumulate instructions used in a matrix multiplication?
The INT8 Outer Product Accumulate instructions calculate the sum of four INT8 outer products, widening results into INT32, then the result is destructively added to the destination tile.
![Figure showing SME2 INT8 MOPA instruction alt-text#center](images/sme2_mopa.jpg "SME2 INT8 MOPA instruction")

When SME2 SVL is 512-bit, each input register (Zn.B, Zm.B) is treated as a matrix of 16x4 INT8 elements, as if each block of four contiguous elements were transposed.
- The first source, Zn.B contains a 16x4 sub-matrix of 8-bit integer values.
- The second source, Zm.B, contains a 16 x4 sub-matrix of 8-bit integer values.
- The INT8 MOPA instruction calculates a 16x 16 widened 32-bit integer sum of outer products, which is then destructively added to the 32-bit integer destination tile, ZAda.

The video below shows how SME2 INT8 Outer Product Accumulate instructions are used for matrix multiplication.
![Figure showing Matrix Multiplication with 1VLx1VL SME2 MOPA alt-text#center](videos/matrix_mopa_sme2_1vl.gif "Matrix Multiplication with 1VLx1VL SME2 MOPA")
To calculate the result of a 16x16 sub-matrix in matrix C (element type: INT32):

First,
-	a 16x4 sub-matrix in matrix A (element type: INT8) is loaded to a SME2 Z register,
-	a 4x16 sub-matrix in matrix B (element type: INT8) is loaded to another SME2 Z register
-	a 16x16 sub-matrix in matrix C is stored in an SME2 ZA tile, which is initialized to zero only once 

Then, the SME2 INT8 MOPA instruction uses the data from these two Z registers to perform the outer product operation and accumulates the results into the ZA tile, which holds the 16x16 sub-matrix of matrix C, thus obtaining an intermediate result for this 16x16 sub-matrix.

Iterate over the K dimension, repeatedly loading 16x4 submatrices from matrix A and 4×16 submatrices from matrix B. For each step, use the SME2 INT8 MPOA instruction to compute outer products and accumulate the results into the same ZA tile. After completing the iteration over K, this ZA tile holds the final values for the corresponding 16×16 submatrix of matrix C. Finally, store the contents of the ZA tile back to memory.

Apply the same process to all 16x16 sub-matrices in matrix C to complete the entire matrix computation.

To improve performance, we can pipeline four MOPA instructions and fully utilize four ZA tiles in ZA storage, each MOPA instruction uses one ZA tile. 
The video below demonstrates how the four MOPA instructions are used to perfrom matrix multiplication of one 16x4 submatrix from matrix A and four 4x16 submatrices from matrix B in a single iteration. This approach can be referred to as 1VLx4VL, 

![Figure showing Matrix Multiplication with 1VLx4VL SME2 MOPA alt-text#center](videos/1vlx4vl_sme2_mopa.gif "Matrix Multiplication with 1VLx4VL SME2 MOPA")
The intermediate result of 4x16x16 output submatrix is held in four ZA.S tiles.

You can find more information about SME2 MOPA here,
-  [part 1 Arm Scalable Matrix Extension Introduction](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction)
- [part 2 Arm Scalable Matrix Extension Instructions](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2)
-  [part4 Arm SME2 Introduction](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction)
   