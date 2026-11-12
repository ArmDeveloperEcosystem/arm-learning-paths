---
title: Compare a GEMM with gather loads
description: Step through a GEMM that loads matrix A with non-contiguous gather loads, and see why Streaming SVE mode needs FEAT_SME_FA64 to run them.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand gather loads

The previous General Matrix Multiplication (GEMM) began with an input matrix A that was already packed and transposed. It isn't always practical or desirable to transform the input data. The Scalable Vector Extension (SVE) supports Gather Load and Scatter Store. With these instructions, contiguous data in Z registers can be gathered from or scattered to non-contiguous addresses in memory. 

These instructions are available in Streaming SVE mode only if `FEAT_SME_FA64` is implemented and enabled. Scalable Matrix Extension (SME) functionality requires Streaming SVE mode to be enabled. If `FEAT_SME_FA64` isn't enabled, Gather Load and Scatter Store are illegal instructions while in Streaming SVE mode.

This visualization uses Gather Loads to access columns of matrix A data. The elements are separated by the length of a full row of matrix A.

{{% notice Note %}}
Gather Loads and Scatter Stores stress the memory system more than contiguous loads. They could potentially require multiple cache line loads before the operation can complete. Both these effects can impact performance.
{{% /notice %}}

## Compare the input path

If the embedded visualization doesn't load, [open the gather-load GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-2x2). Switch between the Learning Path and the visualization tab.

Focus on how Matrix A data is loaded into Z2 and Z3:

1. The first four steps read the first row of **B Input Data** into Z0 - Z1. They read the first column of **A Input Data** into Z2 - Z3. 
    
    Although the vector loads from **B Input Data** are from contiguous memory, the vector loads from **A Input Data** are not. The four 32-bit words loaded from **A Input Data** are from separate rows. Therefore, their addresses are 16 bytes apart.
2. The next four steps calculate the matrix outer products using the Z0 - Z3 data.
3. The next eight steps read the second row of B and the second column of A. They calculate the matrix outer products with accumulation of the result.
4. The next eight steps do the same for the third row of B and the third column of A.
5. The next eight steps do the same for the fourth row and column.
6. The next eight steps write ZA0 and ZA1 to **Output Matrix Data**.
7. The final eight steps write ZA2 and ZA3 to **Output Matrix Data**.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-2x2"
    title="Interactive GEMM with gather-load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## What you've learned and what's next

You've learned that input data can be loaded from different memory layouts. The output of the matrix operation is the same. However, the memory layout of the input data can have a performance impact.

Next, you'll view a visualization that rearranges matrix A in memory. The rearrangement means that data is loaded from contiguous addresses.
