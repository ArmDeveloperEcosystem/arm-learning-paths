---
title: Transpose and packing
description: Visualize transpose and packing of matrix A using Arm SME.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare A for matrix multiplication

Packing changes the order of values in memory so that a matrix multiplication kernel can load those values more efficiently. This visualisation loads **Input Matrix A** values into rows of ZA, and writes columns of ZA into **Output Packed Data**. Packing changes the layout of data, but does not calculate the matrix product.

## Use the playback controls

Select the **rightmost double-arrow button (⏩)** to advance one step or the **leftmost double-arrow button (⏪)** to go back one step. The **middle Play/Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.

## Follow the transpose and pack algorithm

Press play or advance manually to follow the algorithm:

1. The first ten steps load rows from **Input Matrix A** into rows of ZA0 - ZA2. Note that because different implementations can have different Scalable Vector Length, predicates are used to determine which rows are active.
2. The next twelve steps write columns of ZA data into rows of **Output Packed Data**.
3. Notice that the last four steps write zero-padded values, because the rows of **Input Matrix A** are not an exact multiple of the ZA tile height. Predicates control which rows of ZA2 are active, and thus which elements of **Output Packed Data** are zero-padded.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pack32-a"
    title="Interactive packing of 32-bit matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the Pack A visualization in a full browser tab](/apps/sme-visualisations/#/sme/pack32-a) if the embedded view does not load.

## What you've accomplished

You have traced a change in matrix A's memory layout. The packed GEMM view later in this path begins with this kind of prepared A data. First, prepare its other operand, B.

The [preprocessing example in the SME2 matrix multiplication Learning Path](/learning-paths/cross-platform/multiplying-matrices-with-sme2/5-outer-product/#preprocessing-with-preprocess_l) shows how a C kernel prepares its left-hand matrix. Its precise layout belongs to that implementation.
