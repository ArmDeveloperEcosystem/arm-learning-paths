---
title: Transpose and pack matrix A
description: Step through an interactive view that loads matrix A into ZA rows and writes ZA columns to a packed, zero padded output buffer.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare matrix A for multiplication

Packing changes the order of values in memory so that a matrix multiplication kernel can load those values more efficiently. This visualization loads **Input Matrix A** values into rows of ZA, and writes columns of ZA into **Output Packed Data**. Packing changes the layout of data, but doesn't calculate the matrix product.

If the embedded visualization doesn't load, [open the Pack A visualization in a full browser tab](/apps/sme-visualisations/#/sme/pack32-a). Switch between the Learning Path and the visualization tab.

## Follow the transpose and pack algorithm

Press play or advance manually to follow the algorithm:

1. The first 10 steps load rows from **Input Matrix A** into rows of ZA0 - ZA2. Predicates are used to determine which rows are active because different implementations can have different scalable vector lengths.
2. The next 12 steps write columns of ZA data into rows of **Output Packed Data**.
3. The last four steps write zero-padded values. This is because the rows of **Input Matrix A** aren't an exact multiple of the ZA tile height. Predicates control which rows of ZA2 are active. As a result, they control which elements of **Output Packed Data** are zero-padded.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pack32-a"
    title="Interactive packing of 32-bit matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## What you've learned and what's next

You've traced a change in the memory layout of matrix A. The packed GEMM (General Matrix Multiplication) visualization begins with this kind of prepared A data. 

The [preprocessing example in the SME2 matrix multiplication Learning Path](/learning-paths/cross-platform/multiplying-matrices-with-sme2/5-outer-product/#preprocessing-with-preprocess_l) shows how a C kernel prepares its left-hand matrix. Its precise layout belongs to that implementation.

Next, you'll view a visualization that prepares the other operand for the GEMM visualization, matrix B.