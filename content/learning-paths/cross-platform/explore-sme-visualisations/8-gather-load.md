---
title: Compare a GEMM with gather loads
description: Step through a GEMM that loads matrix A with non-contiguous gather loads, and see why Streaming SVE mode needs FEAT_SME_FA64 to run them.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand gather loads

The previous GEMM began with an input matrix A that was already packed and transposed. It isn't always practical or desirable to transform the input data. The Scalable Vector Extension (SVE) supports Gather Load and Scatter Store, where contiguous data in Z registers can be gathered from or scattered to non-contiguous addresses in memory. These instructions are available in Streaming SVE mode only if `FEAT_SME_FA64` is implemented and enabled. SME functionality requires Streaming SVE mode to be enabled. If `FEAT_SME_FA64` isn't enabled, Gather Load and Scatter Store are illegal instructions while in Streaming SVE mode.

This visualization uses Gather Loads to access columns of Matrix A data, whose elements are separated by the length of a full row of Matrix A.

Gather Loads and Scatter Stores stress the memory system more than contiguous loads, and could potentially require multiple cache line loads before the operation can complete. Both these effects can impact performance.

## Use the playback controls

Select the **rightmost double-arrow button (⏩)** to advance one step and read the current-step description. The **leftmost double-arrow button (⏪)** goes back one step. The **middle Play/Pause button** runs or pauses the remaining sequence. Reload the page to return to the initial state.

## Compare the input path

Focus on how Matrix A data is loaded into Z2 and Z3:

1. The first four steps read the first row of **B Input Data** into Z0 - Z1, and the first column of **A Input Data** into Z2 - Z3. Notice that although the vector loads from **B Input Data** are from contiguous memory, the vector loads from **A Input Data** are not. The four 32-bit words loaded from **A Input Data** are from separate rows, and thus their addresses are 16 bytes apart.
2. The next four steps calculate the matrix outer products using the Z0 - Z3 data.
3. The next 8 steps read the second row of B and the second column of A, and calculate the matrix outer products with accumulation of the result.
4. The next 8 steps do the same for the third row of B and the third column of A.
5. The next 8 steps do the same for the fourth row and column.
6. The next 8 steps write ZA0 and ZA1 to **Output Matrix Data**.
7. The final 8 steps write ZA2 and ZA3 to **Output Matrix Data**.

{{< fullscreen-iframe
    src="/apps/sme-visualisations/#/sme/gemm32-2x2"
    title="Interactive GEMM with gather-load"
    height="940px"
    width="100%"
    border="1px solid #999"
    loading="lazy"
>}}

If you need more space then use the "Full screen" button at the top-right, or [open the gather-load GEMM visualization in a full browser tab](/apps/sme-visualisations/#/sme/gemm32-2x2) if the embedded view does not load.

## What you've accomplished

The input data can be loaded from different memory layouts. The output of the matrix operation is the same, but the memory layout of the input data can have a performance impact.

Next, rearrange A in memory so that data is loaded from contiguous addresses.
