---
title: Trace GEMM with interleaved A
description: Step through a 2 x 2 tile GEMM that loads interleaved matrix A from contiguous addresses, and compare its output with the gather-load version.
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare input layouts in GEMM

This final General Matrix Multiplication (GEMM) visualization begins with matrix A in transposed-and-interleaved layout. It loads input values into Z registers, accumulates outer products in ZA, and writes the output matrix. Compared to the gather-load version, all loads from **A Input Data** are from contiguous addresses.

## Trace the interleaved loads

If the embedded visualization doesn't load, [open the interleaved GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-2x2-interleave). Switch between the Learning Path and the visualization tab.

Follow the algorithm as contiguous data is loaded from the input matrices:

1. The first four steps load a row of **B Input Data** into Z0 and Z1, and two rows of **A Input Data** into Z2 and Z3. The **A Input Data** is loaded from contiguous memory addresses.
2. The next four steps perform matrix outer product calculations to store the first partial results into the ZA0 - ZA3 tiles.
3. The next eight steps load the second row of **B Input Data** and the third and fourth rows of **A Input Data**. They accumulate outer product results into the ZA0 - ZA3 tiles.
4. The next eight steps do the same for the third row of **B Input Data** and the fifth and sixth rows of **A Input Data**.
5. The next eight steps address the last row of **B Input Data** and the last two rows of **A Input Data**.
6. After the results are fully calculated, the next eight steps store ZA0 and ZA1 in **Output Matrix Data**. 
7. A further eight steps store ZA2 and ZA3.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-2x2-interleave"
    title="Interactive GEMM with interleaved load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

You can compare the **Output Matrix Data** with the final output matrix from the [Gather Load version](/learning-paths/cross-platform/explore-sme-visualisations/8-gather-load/) to confirm that they're identical.

## What you've learned

You've followed ZA layout, transposition, operand preparation, and three GEMM input strategies. These visualizations illustrate data movement. The visualizations don't benchmark the strategies or verify executable Scalable Matrix Extension 2 (SME2) instructions. 

To write and validate a kernel, continue with [Accelerate matrix multiplication performance with SME2](/learning-paths/cross-platform/multiplying-matrices-with-sme2/).
