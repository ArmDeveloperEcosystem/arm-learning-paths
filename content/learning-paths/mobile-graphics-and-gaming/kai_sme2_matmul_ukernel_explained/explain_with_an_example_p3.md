---
title: Explain the SME2 matmul microkernel with an example- Part 3
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Explain the SME2 matmul microkernel with an example - Part 3
Once the required LHS and RHS are both ready, *kai_matmul_clamp_f32_qsi8d32p1vlx4_qsi4c32p4vlx4_1vlx4vl_sme2_mopa* microkernel can run now.

### Run the SME2 matmul microkernel
The operations performed to compute an 16x64 result submatrice (four 16x16 submatrices) (1VL x 4VL) are as follows:

- Iterate along blocks along K dimension
  - Iterate in a block with step of kr (kr=4) 
    - Load one SME2 SVL-length (512-bit) of data from the quantized and packed LHS (containing 64 INT8 values) into one SME2 Z register
    - Load two SME2 SVL-lengths of data from the packed RHS (containing 2 x64x2 INT4 values) into two SME2 Z registers, then use the SME2 LUTI4 lookup table instruction to convert these INT4 values into INT8 type, extending them to four SME2 Z registers (4VL).
    - Use the SME2 INT8 Outer Product Accumulate (MPOA) instruction to perform outer product operations with source from the Z register and each of the four Z registers, accumulates the results in four ZA tiles (which are initialized to zero). It produces intermediate results of four 16x16 output submatrices.
    The processes of the first itration can be illustrated in the diagram below:
![Figure showing the first itration of the inner loop alt-text#center](images/run_matmuLsme2_step1.jpg "The first itration of the inner loop")
    The diagram below illustrates the process of the second iteration along the K dimension,
![Figure showing the second itration of the inner loop alt-text#center](images/run_matmul_sme2_step2.jpg "The second itration of the inner loop")
  - After completing the iterations in the block, the intermediate INT32 results of four 16x16 output submatrices are dequantized with the per-block LHS and RHS scale to FP32 floats, using Floating-point Multiply (FMUL), Floating-point Multiply and Accumulate (FMLA) and Signed fixed-point Convert to Floating-point (SCVTF) vector instructions. It produces the intermediate FP32 results of four 16x16 output submatrices.
  - Accumulate the FP32 result above

After completing itration along the K dimension, the FP32 results of four 16x16 output submatrices is ready. Then, save the result into memory.

The code can be found [here](https://github.com/ARM-software/kleidiai/blob/main/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qai4c32p/kai_matmul_clamp_f32_qsi8d32p1vlx4_qai4c32p4vlx4_1vlx4vl_sme2_mopa_asm.S#L80) 
Some comments are added to the code to help understanding the code.
```asm
KAI_ASM_LABEL(label_3)              // K Loop
    KAI_ASM_INST(0xc00800ff)        // zero {za} ， zeros the four ZA tile (za0.s, za1.s, za2.s, za3.s)
    mov x11, x4                //Set block size
KAI_ASM_LABEL(label_4)              // Block Loop
    KAI_ASM_INST(0xa0404342)        //ld1w {z2.s - z3.s}, pn8/z, [x26]   // load two VLs packed RHS data (64x2x2 INT4 data)
    addvl x26, x26, #2    // increase RHS address by two VLs
    ld1h {z8.h}, p0/z, [x3]    //load one VL quantized and packed LHS data (64 INT8 data)
    addvl x3, x3, #1       // increase LHS address by one VLs
    KAI_ASM_INST(0xc08a4044)        // luti4 {z4.b - z5.b}, zt0, z2[0]  //use LUT4I instruction to convert INT4 to INT8, one source VL produces two VLs result 
    KAI_ASM_INST(0xc08a4066)        // luti4 {z6.b - z7.b}, zt0, z3[0]  //use LUT4I instruction to convert INT4 to INT8, one source VL produces two VLs result
    KAI_ASM_INST(0xa0840100)        // smopa za0.s, p0/m, p0/m, z8.b, z4.b   ]  //Outer Product Accumulate with the VL of LHS, the first VL of RHS and ZA0.S
    KAI_ASM_INST(0xa0850101)        // smopa za1.s, p0/m, p0/m, z8.b, z5.b   //Outer Product Accumulate with the VL of LHS, the second VL of RHS and ZA1.S
    KAI_ASM_INST(0xa0860102)        // smopa za2.s, p0/m, p0/m, z8.b, z6.b   //Outer Product Accumulate with the VL of LHS, the third VL of RHS and ZA2.S
    KAI_ASM_INST(0xa0870103)        // smopa za3.s, p0/m, p0/m, z8.b, z7.b  b   //Outer Product Accumulate with the VL of LHS, the forth VL of RHS and ZA3.S

    subs x11, x11, #4     //block_index - 4
    b.gt label_4       //end of block iteration?
    
   // the code below performs per block dequantization of the four tiles with LHS and RHS scales
    mov w12, #0
    mov x25, x24
    ld1b {z17.b}, p4/z, [x3]               // lhs sum
    ld1b {z16.b}, p4/z, [x3, #1, mul vl]   // lhs scale
    addvl x3, x3, #2
    KAI_ASM_INST(0xa040c354)        // ld1w { z20.s - z23.s }, pn8/z, [x26]            // rhs zp
    KAI_ASM_INST(0xa041c340)        // ld1w { z0.s - z3.s }, pn8/z, [x26, #4, mul vl ] // rhs scale
    addvl x26, x26, #8
    pfalse p3.b
KAI_ASM_LABEL(label_5)
    // omit some codes that perform the block quantization and save the result to memory 
    ……
    blt label_5
    subs x10, x10, x4     //decrease the K index
    b.gt label_3     //end of K loop?

```
In a single block loop, four pipelined SME2 INT8 MOPA instructions perform 4,096 MAC operations, calculating the intermediate results for the four 16x16 submatrices. It proves that SME2 MOPA can significantly improve matrix multiplication performance.

To help understand the whole process, we map the first itration of LHS and RHS quantization and packing steps, as well as SME2 outer product accumulate operation and dequantization, back to the original FP32 LHS and RHS operations. Essentially, they equally perform the operation as shown below (there might be some quantization loss),
![Figure showing the original matrix representing of the first itration alt-text#center](images/run_matmul_sme2_original_present_step1.jpg "the original matrix representing of the first itration")

The second iteration can be mapped back to the original FP32 LHS and RHS operations as below,
![Figure showing the original matrix representing of the second itration alt-text#center](images/run_matmul_sme2_original_present_step2.jpg "the original matrix representing of the second itration")

**Note**: In this diagram, the RHS is laid out in the dimension of [N, K], which is different from the [K, N] dimension layout of the RHS in the video demonstration of 1VLx4VL. If you interpret the RHS in the diagrams above using the [K, N] dimension, you can match the previous video demonstration with the diagrams above.

By repeating the submatrix computation across the M and N dimensions, the entire result matrix can be calculated. If a non-empty bias is passed to the SME2 matmul microkernel, it also adds the bias to the result matrix.