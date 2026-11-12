---
title: Transpose a matrix with an incomplete edge
description: Trace a 32-bit transpose with a two-element edge to see how a partial block moves through ZA into output memory.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Handle real-world matrix sizes

Real matrices don't always divide evenly into vector-sized blocks. This visualization adds a two-element edge beyond the complete 32-bit blocks. It separates **Input Matrix Data** from **Output Matrix Data**. That way, you can follow the remaining values without losing sight of the original input.

If the embedded visualization doesn't work, [open the incomplete-edge transpose visualization in a full browser tab](/apps/sme-visualisations/#/sme/transpose32-overflow2).

## Follow the edge values

Press the play button or advance manually to follow the algorithm. Focus on how the last two columns of **Input Matrix Data** are loaded into ZA0 - ZA2 as partial rows in step 5:

1. The first 10 steps load rows from the first four columns of the input matrix into rows of ZA0-ZA2.
2. The next 12 steps store data sequentially into the output matrix from columns of ZA0-ZA2.
3. The next 10 steps load rows from the next four columns of the input matrix into rows of ZA0-ZA2.
4. The next 12 steps store data sequentially into the output matrix from columns of ZA0-ZA2.
5. The next 10 steps load rows from the last two columns of the input matrix into rows of ZA0-ZA2. Note that only two data values per row are loaded into ZA tiles. This is achieved by using a predicate mask that marks only two columns as active.
6. The last six steps store data sequentially into the output matrix from columns of ZA0-ZA2. Only two columns are active, which is why only six steps are needed instead of 12.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/transpose32-overflow2"
    title="Interactive 32-bit transpose with a two-element edge"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}


## What you've learned and what's next

You've learned that the final block can contain fewer valid elements than a full tile. Predicate masks constrain which rows or columns the Scalable Matrix Extension (SME) operations act on. This means you don't need any special handling of the final loop.

Next, you'll learn how to vectorize matrix multiplication.
