---
title: Transpose a 32-bit matrix in place with ZA
description: Step through an interactive 32-bit transpose to see how Arm SME loads rows into ZA tiles and stores columns back to memory.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## See how ZA transposes values

A transpose exchanges rows and columns. ZA tiles make this easy because you can move vectors of values into rows, and extract those values back as columns or vice versa. This visualization shows a transpose in-place, where no external memory is used and the transposed result overwrites the original data.

## Use the playback controls

Select the **rightmost double-arrow button (⏩)** to advance one step at a time. The **leftmost double-arrow button (⏪)** goes back one step. The **middle Play/Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.

The description of each step appears immediately under the "32-bit Transpose" title, and includes the tile addressing; the highlights show the memory and ZA locations involved.

## Trace the algorithm

With SVL=256 bits and accessing 32-bit data elements, there are four logical ZA tiles available. The algorithm uses all of them to maximize memory efficiency.

Press play or advance manually to follow the algorithm:

1. The first 16 steps load data sequentially from memory into rows of the ZA0 and ZA1 tiles.
2. The next 16 steps load data sequentially from memory into rows of the ZA2 and ZA3 tiles.
3. The next 16 steps store data sequentially into memory from columns of the ZA0 and ZA2 tiles.
4. The final 16 steps store data sequentially into memory from columns of the ZA1 and ZA3 tiles.
5. The transpose is achieved by loading data into rows and storing it back from columns.
6. Satisfy yourself that the original matrix had data increasing sequentially along each row, whereas the resulting transposed matrix instead has data increasing sequentially down each column. To quickly see the original data, use browser reload to reset the visualization.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/transpose32"
    title="Interactive 32-bit matrix transpose"
    height="800px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the 32-bit transpose visualization in a full browser tab](/apps/sme-visualisations/#/sme/transpose32) if the embedded view does not load.

## Why is the data mirrored left-to-right?

Reload the page to reset the visualization, and advance one step. The first 8 values of **Matrix Data** read 0, 1, 2, 3, 4, 5, 6, 7. The values loaded into ZA0 read 7, 6, 5, 4, 3, 2, 1, 0.

There is no mirroring. Memory isn't addressed as a two dimensional grid. Memory is addressed as one-dimensional storage from low to high addresses, like floors of a skyscraper. The visualization arranges **Matrix Data** as a grid so that you can see clearly how the data values relate to the matrix. By convention, humans draw matrices with the lowest indexed value at the top left. Here, the top-left element of the grid would have the lowest memory address, and elements to the right would have increasing memory addresses. Moving down from the end of one row to the beginning of the next, also increases memory address. Thus, in that first data read, the 0 is at the lowest address and the 7 is at the highest address.

By convention, ZA tiles are drawn with column 0 on the right side and row 0 at the top. This is purely a convention. The ZA storage is a register file, and there is no left, right, up or down in register files. Because of this convention, in that first data read the zero is stored in the top-right element of ZA0 and the 7 is stored in the top-left.

## What you've accomplished

The ZA tiles provide row and column access to stored values, which can be used to transpose data in memory.

For a related C example, see [Optimize memory layout with transposition](/learning-paths/cross-platform/multiplying-matrices-with-sme2/5-outer-product/#optimize-memory-layout-with-transposition). That kernel prepares a matrix operand for multiplication; it doesn't reproduce this animation step for step.

Next, see what changes when the matrix size isn't an exact multiple of the ZA tile size.
