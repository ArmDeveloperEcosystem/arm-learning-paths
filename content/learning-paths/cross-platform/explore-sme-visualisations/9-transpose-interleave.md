---
title: Interleave matrix A
description: Step through an interactive view that transposes and interleaves matrix A through ZA so a 2 x 2 tile GEMM can load it from contiguous addresses.
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arrange input matrix A for adjacent loads

To eliminate the need for Gather Loads, transform the **Input Matrix**. Process four ZA tiles at a time, arranged in a 2 x 2 grid. The top ZA tiles need four rows of the first column (shown in dark red). The bottom ZA tiles need the next four rows of the first column (shown in dark orange). These rows need to be adjacent in the output memory buffer. Continue for the subsequent columns, until all have been arranged contiguously in memory. Do the same for the next set of rows, shown in green and blue.

![Transposing and interleaving the input matrix#center](images/transpose_interleave.png "Transposing and interleaving the input matrix")

The visualization shows the output **Interleaved Matrix** as a 16 x 16 matrix. If you represent the output memory buffer as a 16 x 16 matrix, it looks similar to:

![Transposed interleaved output buffer shown as 16-column array#center](images/transpose_interleave_wide.png "Transposed interleaved output buffer shown as 16-column array")

## Follow the transpose and interleave

If the embedded visualzation doesn't load, [open the A interleave visualization in a full browser tab](/apps/sme-visualisations/#/sme/pack32-2x2-a). Switch between the Learning Path and the visualization tab.

Follow the algorithm that transposes and interleaves the **Input Matrix** data:

1. The first eight steps load partial rows of **Input Matrix** data into rows of the ZA0 and ZA1 tiles.
2. The next eight steps load partial rows of **Input Matrix** data into rows of the ZA2 and ZA3 tiles.
3. The next eight steps store columns of ZA0 and ZA2 into rows of the **Interleaved Matrix** output buffer.
4. The next eight steps store columns of ZA1 and ZA3 into the next two rows of the **Interleaved Matrix** output buffer.
5. The next 32 steps repeat this procedure for the remainder of the horizontal strip of **Input Matrix** that's being processed. The matrix has exactly 16 columns and 16 rows. As a result, the remainder of the horizontal strip happens to be the top-right quadrant.
6. After the first two-tile-deep horizontal strip is complete, the algorithm moves to the next one. The next 32 steps process the bottom-left quadrant of **Input Matrix** into four rows of the **Interleaved Matrix** output buffer.
7. The final 32 steps process the remainder of this horizontal strip into the last four rows of the **Interleaved Matrix** output buffer. This happens to be the bottom-right quadrant.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pack32-2x2-a"
    title="Interactive transpose and interleave of matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## What you've learned and what's next

You've followed the transpose and interleave of **Input Matrix** data. The visualization arranges it so that a General Matrix Multiplication (GEMM) can load the data it needs contiguously from memory.

Next, you'll explore a GEMM that uses this data layout for efficient matrix multiplication.
