---
title: Trace GEMM with interleaved A
description: Step through a 2 x 2 tile GEMM that loads interleaved matrix A from contiguous addresses, and compare its output with the gather-load version.
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare input layouts in GEMM

This final General Matrix Multiplication (GEMM) visualization begins with matrix A in transposed-and-interleaved layout. It loads input values into Z registers, accumulates outer products in ZA, and writes the output matrix. Compared to the gather-load version, all loads from **A Input Data** are from contiguous addresses.

## Trace the interleaved loads

If the embedded visualization doesn't load, [open the interleaved GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-2x2-interleave). Switch between the Learning Path and the visualization tab.

Follow the same stages as the gather-load GEMM and compare how matrix A reaches Z2 and Z3:

| Stage | Visualization steps | Operation |
|---|---|---|
| Load the first inputs | 1–4 | Load the first row of **B Input Data** into Z0–Z1 and the first two rows of **A Input Data** into Z2–Z3. The A loads use contiguous addresses. |
| Calculate the first outer products | 5–8 | Accumulate the first partial results in ZA0–ZA3. |
| Process the second inputs | 9–16 | Load the second row of B and the third and fourth rows of A, then accumulate outer products. |
| Process the third inputs | 17–24 | Repeat for the third row of B and the fifth and sixth rows of A. |
| Process the fourth inputs | 25–32 | Repeat for the fourth row of B and the last two rows of A. |
| Store the first results | 33–40 | Write ZA0 and ZA1 to **Output Matrix Data**. |
| Store the remaining results | 41–48 | Write ZA2 and ZA3 to **Output Matrix Data**. |

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-2x2-interleave"
    title="Interactive GEMM with interleaved load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

You can compare the **Output Matrix Data** with the final output matrix from the [Gather Load version](/learning-paths/cross-platform/explore-sme-visualisations/8-gather-load/) to confirm that they're identical.

## What you've learned

You've followed ZA layout, transposition, operand preparation, and three GEMM input strategies. These visualizations illustrate data movement. The visualizations don't benchmark the strategies or verify executable Scalable Matrix Extension 2 (SME2) instructions. 

To write and validate a kernel, continue with [Accelerate matrix multiplication performance with SME2](/learning-paths/cross-platform/multiplying-matrices-with-sme2/).
