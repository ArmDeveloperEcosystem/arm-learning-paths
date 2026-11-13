---
title: Explore the ZA tile layout
description: Select data types and streaming vector lengths in an interactive view to see how Arm SME maps ZA storage to logical tiles.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## See ZA as an array of tiles

Arm Scalable Matrix Extension (SME) builds on the Scalable Vector Extension (SVE) by adding the following features: 

- ZA storage, a two-dimensional square register array
- Outer product instructions
- Instructions that can move a vector to or from a tile row or column

The ZA storage width and height each equal the Streaming Vector Length (SVL) in bytes. A matrix operation can keep partial results in ZA. Subsequent vector operations accumulate their results into ZA by addition or subtraction. The ZA storage maps to one or more logical tiles, where the number of logical tiles depends on the data element size.

SME masks data when dealing with matrices that aren't an exact multiple of the ZA storage dimensions. To do so, SME uses the SVE predicate mechanism. This avoids the need to handle data masking in software.

SME2 builds on this programming model with the following additional features:

- Multi-vector operations
- A new predicate-as-counter mechanism
- A range prefetch hint
- Compressed neural network support using lookup table instructions

You'll view a set of interactive ZA visualizations in this Learning Path, starting with the ZA Tile Layout view. All visualizations run in your browser, so you don't need an SME2 device. The browser isn't running SME2 instructions.

{{% notice Note %}}
Use the following controls to explore the visualizations:

- If you need more space to view any of the visualizations in the Learning Path, use the **Full screen** button.
- If a visualization includes playback, select the rightmost **double-arrow (⏩)** button to advance one step at a time. The leftmost **double-arrow (⏪)** button goes back one step. The middle button runs or pauses the remaining sequence. Reload the page to return to the initial state.
{{% /notice %}}

The ZA Tile Layout interactive view shows the same ZA storage as a full array and as logical tiles. The values and colors illustrate register layout. 

## Explore ZA storage and logical tiles

If the embedded visualization doesn't load, [open the ZA layout visualization in a separate browser tab](/apps/sme-visualisations/#/sme/layout). Switch between the Learning Path and the visualization tab.

Use the visualization to explore how the data type and scalable vector length affect the organization of ZA storage.

1. For **Data Type**, select **int8**.

2. For **Scalable Vector Length**, select **128-bit**.

   The visualization shows one logical tile, ZA0, which is the same size as ZA.

3. For **Data Type**, select **int16**.

   The visualization now shows two logical tiles, ZA0 and ZA1. Their rows are interleaved in ZA storage.

4. Explore the mapping between ZA storage and the logical tiles:

   1. Hover over a row in ZA storage to highlight the corresponding row in a logical tile.
   2. Hover over a row in a logical tile to highlight the corresponding row in ZA storage.

5. Select or tap a logical tile or ZA storage to switch from row highlighting to column highlighting.

6. Hover over a column in ZA0 to highlight the corresponding cells in alternate rows of ZA storage.

7. For **Data Type**, select **int32**.

   The visualization now shows four logical tiles, ZA0 to ZA3.

8. Hover over the logical tiles or ZA storage to explore the mapping of rows and columns.

9. For **Scalable Vector Length**, select **256-bit**.

   The visualization still shows four logical tiles, but each tile now contains more elements.


{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/layout"
    title="Interactive ZA tile layout visualization"
    height="760px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

### Compare ZA storage configurations

The following table summarizes how the data type and scalable vector length affect ZA storage and logical tiles.

| Data type | Vector length | Elements per row | ZA storage rows | Logical tiles | Logical tile dimensions |
|---|---|---|---|---|---|
| `int8` | 128 bits | 16 | 16 | 1 (ZA0) | 16 × 16 |
| `int16` | 128 bits | 8 | 16 | 2 (ZA0–ZA1) | 8 × 8 |
| `int32` | 128 bits | 4 | 16 | 4 (ZA0–ZA3) | 4 × 4 |
| `int32` | 256 bits | 8 | 32 | 4 (ZA0–ZA3) | 8 × 8 |

Increasing the element size reduces the number of elements per row and increases the number of logical tiles.

Increasing the scalable vector length from 128 bits to 256 bits for `int32` increases the number of elements in each logical tile. However, there's no change in the number of logical tiles.

### Read ZA tile addresses

When you hover over a cell, the addressing of its row or column is shown under the **ZA Tile Layout** title. For example, with `int16` data type, the first row of the ZA storage is addressed as ZA0H.H[0]. 

ZA0H.H[0] can be decoded as follows:

- ZA0 represents the logical tile.
- H represents horizontal tile slice access.
- .H represents half-word (16-bit).
- [0] represents the first row. 

Similarly, the third column of ZA1 from the right is addressed as ZA1V.H[2].

ZA1V.H[2] can be decoded as follows:
- ZA1 represents the logical tile. 
- V represents vertical tile slice access.
- .H represents half-word (16-bit). 
- [2] represents the third column.


Continue exploring other data types such as **float64** and **float128**, and other **Scalable Vector Length** values.


## What you've learned and what's next

You've learned that ZA storage is one scalable array with one or more logical tile views. Changing the scalable vector length alters its dimensions. Changing element size alters how many elements fit in each row, and how many logical tiles the ZA storage maps to.

Next, you'll view a visualization that applies this to transposing a matrix.
