---
title: Transpose with incomplete edge
description: Trace a 32-bit transpose with a two-element edge to see how a partial block moves through ZA into output memory.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Handling real world data

Real matrices do not always divide evenly into vector-sized blocks. This example adds a two-element edge beyond the complete 32-bit blocks. It separates **Input Matrix Data** from **Output Matrix Data** so you can follow the remaining values without losing sight of the original input.

## Use the playback controls

Select the **rightmost double-arrow button (⏩)** to advance one step or the **leftmost double-arrow button (⏪)** to go back one step. The **middle Play/Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.

## Follow the edge values

See how the last two columns of **Input Matrix Data** are loaded into ZA0 - ZA2 as partial rows (step 5 below):

1. The first ten steps load rows from the first four columns of the input matrix, into rows of ZA0-ZA2.
2. The next twelve steps store data sequentially into the output matrix, from columns of ZA0-ZA2.
3. The next ten steps load rows from the next four columns of the input matrix, into rows of ZA0-ZA2.
4. The next twelve steps store data sequentially into the output matrix, from columns of ZA0-ZA2.
5. The next ten steps load rows from the last two columns of the input matrix, into rows of ZA0-ZA2. Note that only two data values per row are loaded into ZA tiles. This is achieved using a predicate mask that marks only two columns as active.
6. The last six steps store data sequentially into the output matrix, from columns of ZA0-ZA2. Only two columns are active, which is why we only need six steps instead of twelve.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/transpose32-overflow2"
    title="Interactive 32-bit transpose with a two-element edge"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the incomplete-edge transpose visualization in a full browser tab](/apps/sme-visualisations/#/sme/transpose32-overflow2) if the embedded view does not load.

## What you've learned

The final block can contain fewer valid elements than a full tile. Predicate masks constrain which rows or columns the SME operations act on, which means we do not need any special handling of the final loop.

Next, learn how to vectorize matrix multiplication.
