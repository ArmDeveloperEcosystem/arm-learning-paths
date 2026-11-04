---
title: Explore the ZA tile layout
description: Explore ZA tile views in the Arm SME visualization to see how element size and streaming vector length shape the array.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## See ZA as an array of tiles

Arm Scalable Matrix Extension (SME) builds on the Scalable Vector extension (SVE) by adding **ZA** storage (a two-dimensional square register array), outer product instructions, and instructions that can move a vector to or from a tile row or column.

The ZA storage width and height each equal the streaming vector length (SVL) in bytes. A matrix operation can keep partial results in ZA, with subsequent vector operations accumulating their results into ZA by addition or subtraction. The ZA storage maps to one or more logical tiles, where the number of logical tiles depends on the data element size.

SME uses the SVE predicate mechanism to enable masking of data when dealing with matrices that are not an exact multiple of the ZA storage dimensions, avoiding the need. This avoids the need to handle this in software.

SME2 builds on this programming model with additional multi-vector operations, a new predicate-as-counter mechanism, a range prefetch hint, and compressed neural network support using lookup table instructions.

The interactive view shows the same ZA storage as a full array and as logical tiles. It runs in your browser, so you do not need an SME2 device for this exercise. The values and colors illustrate register layout; the browser is not executing SME2 instructions.

## Explore the ZA views

Use the selectors and grid to explore the ZA storage and ZA tile views:

1. In **Data Type**, select `int8`. In **Scalable Vector Length**, select `128-bit`. Notice there is only one logical tile, ZA0, which is the same size as ZA. With SVL=128 bits, there are 16 byte-sized elements in each row, and 16 rows in each tile.
2. Select `int16` data type. Notice there are now two tiles, ZA0 and ZA1. The ZA storage is still 128 bits wide, which maps to 8 16-bit elements in each row. There are still 16 rows in the ZA storage, while only 8 rows are needed for a square tile, so the ZA storage now maps to two logical tiles.
3. Notice that the rows of the logical tiles are interleaved in the ZA storage. Hovering over the ZA storage will highlight the corresponding row in a logical tile, and hovering over a logical tile highlights the corresponding row in the ZA storage.
4. Click or tap on a logical tile or the ZA storage to toggle highlighting of columns instead of rows. Hover over a column in the ZA0 tile and note that it maps to the same cell in alternate rows of the ZA storage.
5. Note that when you hover over a cell, the addressing of its row or column is shown immediately under the "ZA Tile Layout" title. For example, with `int16` data type, the first row of the ZA storage is addressed as ZA0H.H[0]. This decodes as:<br>
{{< indent >}}<span style="color: red;">**ZA0**</span> logical tile<br>
{{< indent >}}<span style="color: red;">**H**</span>orizontal tile slice access<br>
{{< indent >}}<span style="color: red;">**H**</span>alf-word (16-bit)<br>
{{< indent >}}<span style="color: red;">**[0]**</span> = first row<br>
The third column of ZA1 (from the right) is addressed as ZA1V.H[2], which decodes as:<br>
{{< indent >}}<span style="color: red;">**ZA1**</span> logical tile<br>
{{< indent >}}<span style="color: red;">**V**</span>ertical tile slice access<br>
{{< indent >}}<span style="color: red;">**H**</span>alf-word (16-bit)<br>
{{< indent >}}<span style="color: red;">**[2]**</span> = third column

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/layout"
    title="Interactive ZA tile layout visualization"
    height="760px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the ZA layout visualization in a full browser tab](/apps/sme-visualisations/#/sme/layout) if the embedded view does not load.

6. Click `int32` data type. For SVL=128 bits there are 4 32-bit elements in each row, and 4 rows in each logical tile. The ZA storage is still 16 rows high, so there are now four logical tiles, ZA0-ZA3. Hover over the logical tiles or the ZA storage and note the mapping of rows and columns.
7. Select 256-bit Scalable Vector Length. Now each row of the ZA storage and the logical tiles is 256 bits which is 32 bytes or eight 32-bit elements. The ZA storage is now 32 rows high, so there are still four logical tiles, each of 8 x 8 elements.
8. Hover over the ZA storage and the logical tiles to inspect the mapping of rows and columns.
9. Explore other data types such as float64 and float128, and other Scalable Vector Lengths.

## What you've learned

ZA storage is one scalable array with one or more logical tile views. Changing SVL alters its dimensions, and changing element size alters how many elements fit in each row, and how many logical tiles the ZA storage maps to.

Next, we look at how we can apply this when transposing a matrix.
