---
title: Transpose and pack matrix A
description: Step through an interactive view that loads matrix A into ZA rows and writes ZA columns to a packed, zero padded output buffer.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare matrix A for multiplication

Packing changes the order of values in memory so that a matrix multiplication kernel can load those values more efficiently. The following visualization loads **Input Matrix A** values into rows of ZA, and writes columns of ZA into **Output Packed Data**. Packing changes the layout of data, but it doesn't calculate the matrix product.

To keep this Learning Path open while exploring, <a href="/apps/sme-visualisations/#/sme/pack32-a" target="_blank" rel="noopener">open the Pack A visualization in a separate browser tab</a>. Move the tab to a separate window to view the visualization and Learning Path side by side.

## Follow the transpose and pack algorithm

Select the play button or advance manually to follow the algorithm:

| Stage | Visualization steps | Operation |
| --- | --- | --- |
| Load matrix A | 1–10 | Load **Input Matrix A** into rows of ZA0–ZA2. |
| Store packed data | 11–22 | Write columns of ZA data into rows of **Output Packed Data**. |
| Pad the final rows | 23–26 | Write zero-padded values because the rows of **Input Matrix A** aren't an exact multiple of the ZA tile height. |

During matrix A load, predicates determine which rows are active because different implementations can have different scalable vector lengths. Predicates also control which elements of **Output Packed Data** are zero-padded.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pack32-a"
    title="Interactive packing of 32-bit matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## What you've learned and what's next

You've traced a change in the memory layout of matrix A. The packed General Matrix Multiplication (GEMM) visualization begins with this kind of prepared A data. 

The [preprocessing example in the SME2 matrix multiplication Learning Path](/learning-paths/cross-platform/multiplying-matrices-with-sme2/5-outer-product/#preprocessing-with-preprocess_l) shows how a C kernel prepares its left-hand matrix. Its precise layout belongs to that implementation.

Next, you'll view a visualization that prepares the other operand for the GEMM visualization, matrix B.
