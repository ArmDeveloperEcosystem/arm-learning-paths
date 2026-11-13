---
title: Pad matrix B to the ZA tile width
description: Step through an interactive view that zero-pads matrix B with predicated loads so every row matches the device's ZA tile width.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why pad matrix B

Although unaligned vector loads from memory are supported, they have drawbacks. Vectors can straddle cache lines. Loop code is complicated by the need to adjust the pointer register at the end of every row. 

Consider a matrix with a column count that isn't an exact multiple of the ZA tile column count for a given data element size. For such a matrix, padding the data might be a better solution. Padding results in cleaner loop code and fully sequential memory access.

The same code running on different devices can produce different output data structures, and that isn't a problem. Each device generates a data structure for its own ZA tile width. Each device later uses that data structure with its ZA tiles to compose input vectors for the Outer Product operation. Although the data structure can vary between devices, the Outer Product results are the same across all devices.

## Inspect the padded result

The following visualization depicts the padded matrix B. If the embedded visualization doesn't load, [open the Pad B visualization in a separate browser tab](/apps/sme-visualisations/#/sme/pad32-b). Switch between the Learning Path and the visualization tab.

Compare a complete group with one at the edge:

1. The first three steps load the first row of **Input Matrix B** into rows of ZA0. The third step loads only the last two columns of the matrix, and leaves the other columns zero-padded. This is achieved by using a predicate register to control which columns are active.
2. The next three steps load the second row of **Input Matrix B** into rows of ZA0 - ZA1. The final load is zero-padded.
3. The following six steps finish loading the third and fourth rows into ZA1 - ZA2.
4. The next 12 steps write the rows of ZA0 to ZA2 into rows of **Output Padded Data**. The rows are written with all columns active, so the zero padding is copied verbatim to the output buffer.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/pad32-b"
    title="Interactive padding of 32-bit matrix"
    height="650px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

{{% notice Important %}}
Scalable vector length can vary between devices. This visualization zero-pads the data for the tile size of the device. Running the same code on a different device with a different scalable vector length can result in a different output data structure. Specifically, for larger scalable vector lengths, there's likely to be more padding. However, it depends on the number of columns.
{{% /notice %}}

## What you've learned and what's next

You've seen how the visualization pads an input matrix with zeros so that it aligns with the tile width of the device. You've learned that this padded structure can vary on devices with a different scalable vector length. However, the final matrix multiplication result is identical on all devices.

Next, you'll view a visualization that starts with packed A and padded B, then multiplies them into an output matrix.
