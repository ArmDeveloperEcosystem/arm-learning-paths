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

You'll view a set of interactive ZA visualizations in this Learning Path, starting with the ZA Tile Layout view. All visualizations runs in your browser, so you don't need an SME2 device. The browser isn't running SME2 instructions.

{{% notice Note %}}
- If you need more space to view any of the visualizations in the Learning Path, use the **Full screen** button.
- If a visualization includes playback, select the rightmost **double-arrow button (⏩)** to advance one step at a time. The leftmost **double-arrow button (⏪)** goes back one step. The middle **Play or Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.
{{% /notice %}}

The ZA Tile Layout interactive view shows the same ZA storage as a full array and as logical tiles. The values and colors illustrate register layout. 

## Explore the ZA views

If the embedded visualization doesn't load, [open the ZA layout visualization in a full browser tab](/apps/sme-visualisations/#/sme/layout). Switch between the Learning Path and the visualization tab.

Use the selectors and grid to explore the ZA storage and ZA tile views:

1. For **Data Type**, select **int8**.
2. For **Scalable Vector Length**, select `128-bit`. 

    Notice that there's only one logical tile, ZA0, which is the same size as ZA. With the **Scalable Vector Length** equal to 128 bits, there are 16 byte-sized elements in each row. There are 16 rows in each tile.
3. Update **Data Type** to **int16**. 

    Notice that there are now two tiles, ZA0 and ZA1. The ZA storage is still 128 bits wide, which maps to eight 16-bit elements in each row. There are still 16 rows in the ZA storage, while only eight rows are needed for a square tile. The ZA storage now maps to two logical tiles.

    Also notice that the rows of the logical tiles are interleaved in the ZA storage. Hovering over the ZA storage highlights the corresponding row in a logical tile. Hovering over a logical tile highlights the corresponding row in the ZA storage.
4. Select or tap a logical tile or the ZA storage to toggle highlighting of columns instead of rows. Hovering over a column in the ZA0 tile maps to the same cell in alternate rows of the ZA storage.
6. Update **Data Type** to **int32**. 
    
    When **Scalable Vector Length** equals 128 bits, there are four 32-bit elements in each row. There are four rows in each logical tile. The ZA storage is still 16 rows high, so there are now four logical tiles, ZA0 to ZA3. Hovering over the logical tiles or the ZA storage highlights the mapping of rows and columns.

7. Update **Scalable Vector Length** to **256-bit**. 

    Now, each row of the ZA storage and the logical tiles is 256 bits. This is 32 bytes or 8 elements of 32 bits. The ZA storage is now 32 rows high. There are still four logical tiles, each of 8 x 8 elements. 


{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/layout"
    title="Interactive ZA tile layout visualization"
    height="760px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

{{% notice Note %}}
When you hover over a cell, the addressing of its row or column is shown under the **ZA Tile Layout** title. For example, with `int16` data type, the first row of the ZA storage is addressed as ZA0H.H[0]. 

ZA0H.H[0] can be decoded as follows:

- ZA0 represents the logical tile.
- H represents horizontal tile slice access.
- H[0] represents half-word (16-bit) and the first row. 

Similarly, the third column of ZA1 from the right is addressed as ZA1V.H[2].

ZA1V.H[2] can be decoded as follows:
- ZA1 represents the logical tile. 
- V represents vertical tile slice access.
- H[2] represents half-word (16-bit) and the third column.

{{% /notice %}}


Continue exploring other data types such as **float64** and **float128**, and other **Scalable Vector Length** values.


## What you've learned and what's next

You've learned that ZA storage is one scalable array with one or more logical tile views. Changing the scalable vector length alters its dimensions. Changing element size alters how many elements fit in each row, and how many logical tiles the ZA storage maps to.

Next, you'll view a visualization that applies this to transposing a matrix.
