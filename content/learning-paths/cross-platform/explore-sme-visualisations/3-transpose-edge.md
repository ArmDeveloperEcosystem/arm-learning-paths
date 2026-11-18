---
title: Transpose a matrix with an incomplete edge
description: Trace a 32-bit transpose with a two-element edge to see how a partial block moves through ZA into output memory.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Handle real-world matrix sizes

Real matrices don't always divide evenly into vector-sized blocks. The following visualization adds a two-element edge beyond the complete 32-bit blocks. It separates **Input Matrix Data** from **Output Matrix Data**. That way, you can follow the remaining values without losing sight of the original input.

To keep this Learning Path open while exploring, <a href="/apps/sme-visualisations/#/sme/transpose32-overflow2" target="_blank" rel="noopener">open the incomplete-edge transpose visualization in a separate browser tab</a>. Move the tab to a separate window to view them side by side.

## Follow the edge values

Select the play button or advance manually to follow the algorithm. The table shows how each group of **Input Matrix Data** columns moves through ZA0–ZA2:

| Stage | Visualization steps | Operation |
| --- | --- | --- |
| Load the first block | 1–10 | Load rows from the first four columns of **Input Matrix Data** into rows of ZA0–ZA2. |
| Store the first block | 11–22 | Store data sequentially in **Output Matrix Data** from columns of ZA0–ZA2. |
| Load the second block | 23–32 | Load rows from the next four columns of **Input Matrix Data** into rows of ZA0–ZA2. |
| Store the second block | 33–44 | Store data sequentially in **Output Matrix Data** from columns of ZA0–ZA2. |
| Load the edge block | 45–54 | Load partial rows from the last two columns of **Input Matrix Data** into rows of ZA0–ZA2. Only two data values per row are loaded into ZA tiles. This is achieved by using a predicate mask that marks only two columns as active. |
| Store the edge block | 55–60 | Store data sequentially in **Output Matrix Data** from columns of ZA0–ZA2. Only two columns are active during the final store, so it takes six steps instead of 12. |

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/transpose32-overflow2"
    title="Interactive 32-bit transpose with a two-element edge"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}


## What you've learned and what's next

You've learned that the final block can contain fewer valid elements than a full tile. Predicate masks constrain which rows or columns the Scalable Matrix Extension (SME) operations act on. You therefore don't need any special handling of the final loop.

Next, you'll learn how to vectorize matrix multiplication.
