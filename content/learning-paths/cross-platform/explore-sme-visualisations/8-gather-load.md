---
title: Compare a GEMM with gather loads
description: Step through a GEMM that loads matrix A with non-contiguous gather loads, and see why Streaming SVE mode needs FEAT_SME_FA64 to run them.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand gather loads

The previous General Matrix Multiplication (GEMM) began with an input matrix A that was already packed and transposed. It isn't always practical or desirable to transform the input data. The Scalable Vector Extension (SVE) supports Gather Load and Scatter Store. With these instructions, contiguous data in Z registers can be gathered from or scattered to non-contiguous addresses in memory. 

These instructions are available in Streaming SVE mode only if `FEAT_SME_FA64` is implemented and enabled. Scalable Matrix Extension (SME) functionality requires Streaming SVE mode to be enabled. If `FEAT_SME_FA64` isn't enabled, Gather Load and Scatter Store are illegal instructions while in Streaming SVE mode.

This visualization uses Gather Loads to access columns of matrix A data. The elements are separated by the length of a full row of matrix A.

{{% notice Note %}}
Gather Loads and Scatter Stores stress the memory system more than contiguous loads. They could potentially require multiple cache line loads before the operation can complete. Both these effects can impact performance.
{{% /notice %}}

## Compare the input path

If the embedded visualization doesn't load, [open the gather-load GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-2x2). Switch between the Learning Path and the visualization tab.

Focus on how matrix A data is loaded into Z2 and Z3:

| Stage | Visualization steps | Operation |
|---|---|---|
| Load the first inputs | 1–4 | Read the first row of **B Input Data** into Z0–Z1 and the first column of **A Input Data** into Z2–Z3. |
| Calculate the first outer products | 5–8 | Use Z0–Z3 to calculate the first matrix outer products. |
| Process the second inputs | 9–16 | Read the second row of B and second column of A. Calculate the matrix outer products with accumulation of the result. |
| Process the third inputs | 17–24 | Repeat for the third row of B and third column of A. |
| Process the fourth inputs | 25–32 | Repeat for the fourth row of B and fourth column of A. |
| Store the first results | 33–40 | Write ZA0 and ZA1 to **Output Matrix Data**. |
| Store the remaining results | 41–48 | Write ZA2 and ZA3 to **Output Matrix Data**. |

The **B Input Data** loads use contiguous addresses. The four 32-bit words loaded from **A Input Data** come from separate rows, so their addresses are 16 bytes apart.
{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-2x2"
    title="Interactive GEMM with gather-load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

## What you've learned and what's next

You've learned that input data can be loaded from different memory layouts. The output of the matrix operation is the same. However, the memory layout of the input data can have a performance impact.

Next, you'll view a visualization that rearranges matrix A in memory. The rearrangement means that data is loaded from contiguous addresses.
