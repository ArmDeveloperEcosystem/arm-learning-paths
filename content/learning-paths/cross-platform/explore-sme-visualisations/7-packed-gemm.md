---
title: Trace packed GEMM through ZA
description: Step through packed 32-bit GEMM to follow prepared operands through Z registers, ZA accumulation, and output memory.
weight: 8
aliases:
    - /learning-paths/cross-platform/explore-sme-visualisations/2-matrix-multiplication/

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Follow a GEMM with packed and padded inputs

This General Matrix Multiplication (GEMM) visualization multiplies matrix A (10 x 4) and matrix B (4 x 10), storing the resulting 10 x 10 matrix in **Output Matrix Data**.

You've seen in the previous visualizations how matrix A is transposed and packed, and how matrix B is padded. This packed 32-bit GEMM visualization starts with transposed and packed matrix A data and padded matrix B data already in memory.

The visualization processes horizontal blocks of three ZA tiles at a time, accumulating four partial results for each tile. Next, it writes the four rows of completed results to **Output Matrix Data**. It then resets the ZA tiles to zero before calculating three tiles for the next four rows. 

The visualization stores the results and resets the tiles again to calculate the last three tiles, which cover the final two rows. In total, it processes nine tiles of matrix data.

![GEMM using packed transposed matrix A and padded matrix B#center](images/gemm_packed.png "GEMM using packed transposed matrix A and padded matrix B")

## Why use a linear arrangement of three tiles

For large matrices, the most efficient arrangement is to process four tiles at a time, arranged in a 2 x 2 block. This requires four vector loads per four tiles of partial results.

This visualization processes three tiles at a time arranged in a 1 x 3 horizontal block. This arrangement requires four vector loads per three tiles of partial results. For a large matrix, it would be slightly less efficient than 2 x 2. However, this visualization uses a small matrix of size 10 x 10.

Consider scalable vector length equal to 128 bits and 32-bit data elements. Using a 2 x 2 tile arrangement for a 10 x 10 matrix would require four passes. Using a 1 x 3 tile arrangement requires only three passes. For small matrices whose dimensions are known at compile time, the 2 x 2 configuration is sometimes outperformed by other tiling arrangements.

Note that for larger scalable vector lengths, the calculus can change. For scalable vector length equal to 256 bits, the 2 x 2 configuration would require only one pass. Alternatively, the 1 x 3 configuration would require two passes. 

In this visualization, the code is functionally correct on all devices regardless of scalable vector length. However, it's optimized for devices with scalable vector length equal to 128 bits.

## Step through the example visualization

If the embedded view doesn't load, [open the GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-packed). Switch between the Learning Path and the visualization tab.

Follow the data from input through accumulation and storage:

1. The first four steps load the first row of **A Packed Data** into Z0. They load the first row of **B Padded Data** into Z1 - Z3.
2. The next three steps calculate the Matrix Outer Product in ZA0 - ZA2.
3. The next seven steps load the second row of **A Packed Data** into Z0 and the second row of **B Padded Data** into Z1 - Z3. They accumulate their Matrix Outer Products into ZA0-ZA2.
4. The next seven steps do the same for row three, and the following seven steps do the same for row four.
5. The next 12 steps store rows of ZA0 - ZA2 into rows of **Output Matrix Data**.
6. The following three steps zero the ZA0 - ZA2 tiles, so that the next block of four rows can be processed.
7. Next, all of the previous steps repeat, using the next four rows of **A Packed Data** and going back to the beginning of **B Padded Data**. The algorithm has moved down by a tile-sized block and starts again at the leftmost column of the matrix. 

    Processing the new row of tile-sized blocks involves another 43 steps:
    - Four rows x seven steps to load data for each row and calculate the output product
    - 12 steps to write the result to **Output Matrix Data**
    - Three steps to zero the ZA tiles
8. The next 34 steps deal with the final block of three tiles, as follows:
    - Four rows x seven steps to load data for each row and calculate the output product
    - Six steps to write the result to **Output Matrix Data**, because there are only two rows

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-packed"
    title="Interactive GEMM with packed interleaved load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## Why this is better than scalar processing

The visualization calculates 100 elements of the output matrix with only 120 instructions, excluding loop control instructions. This is an efficiency of 0.83 output elements per instruction.

With scalar processing, excluding loop control instructions, each output element would require the following instructions:

- Eight load instructions
- Four multiply-accumulate instructions
- One store instruction

This is 13 instructions, which is an efficiency of 0.08 output elements per instruction.

Consider a larger matrix of 12 x 12. The Scalable Matrix Extension (SME) implementation would take the same 120 cycles to process 144 output elements. This is 1.44 output elements per instruction. The scalar implementation would produce the same 0.08 output elements per instruction.

For larger scalable vector lengths, the efficiency is much higher. Every time the scalable vector length doubles, the efficiency quadruples for large matrices. For small matrices, edge effects can limit these gains. For example, for scalable vector length  equal to 512 bits, each ZA tile is 16 x 16 elements of 32-bit data. This is 256 elements in total. The 10 x 10 matrix is only 100 elements, and therefore uses just under 40% of the available throughput of one tile.

## What you've learned and what's next

You've traced loads, outer product accumulations, and stores in a GEMM that uses prepared operands. The visualization models data movement. It doesn't measure performance or prove which instructions a processor executes.

For executable code built around the same outer-product idea, see [matrix multiplication using SME2 intrinsics in C](/learning-paths/cross-platform/multiplying-matrices-with-sme2/7-sme2-matmul-intr/). The code uses its own FP32 data layout and instruction sequence.

Next, you'll compare a version that loads matrix A in a different layout.
