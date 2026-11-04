---
title: Padding matrix data
description: Visualize padding of data using Arm SME.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Padding matrix B

Unaligned vector loads from memory, whilst supported, have drawbacks. Vectors may straddle cache lines, and loop code is complicated by the need to adjust the pointer register at the end of every row. If a matrix has a column count that is not an exact multiple of the number of ZA tile columns for a given data element size, then padding the data may be a better solution. This results in cleaner loop code and fully sequential memory access.

**Important:** Scalable Vector Length (SVL) can vary between devices. This example zero-pads the data for the native tile size. Running the code on a different device with a different SVL may result in a different output data structure. Specifically, for larger SVL there is likely to be more padding, though it depends on the number of columns.

The fact that the same code running on different devices can produce different output data structures, is not a problem. Each device generates a data structure for its own native tile width. Each device later uses that data structure with its native tiles, to compose input vectors for the Outer Product operation. Whilst the data structure may vary between devices, the Outer Product results will be the same across all devices.

## Use the playback controls

Select the **rightmost double-arrow button (⏩)** to advance one step or the **leftmost double-arrow button (⏪)** to go back one step. The **middle Play/Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.

## Inspect the padded result

Compare a complete group with one at the edge:

1. The first three steps load the first row of **Input Matrix B** into rows of ZA0. Notice that the third step loads only the last two columns of the matrix, and leave the other columns zero-padded. This is achieved using a predicate register to control which columns are active.
2. The next three steps load the second row of **Input Matrix B** into rows of ZA0 - ZA1. Notice again that the final load is zero-padded.
3. The following six steps finish loading the third and fourth rows into ZA1 - ZA2.
4. The next twelve steps write the rows of ZA0 - ZA2, into rows of **Output Padded Data**. Notice that the rows are written with all columns active, so the zero padding is copied verbatim to the output buffer.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pad32-b"
    title="Interactive padding of 32-bit matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the Pad B visualization in a full browser tab](/apps/sme-visualisations/#/sme/pad32-b) if the embedded view does not load.

## What you've accomplished

You have seen how the example pads an input matrix with zeros so that it aligns with the native tile width. You have learned that this padded structure may vary on devices with a different Scalable Vector Length, but that the final matrix multiplication result will be identical on all devices.

The next view starts with packed A and padded B, then multiplies them into an output matrix.
