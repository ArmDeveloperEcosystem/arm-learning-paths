---
title: Introducing Scalable Matrix Extension (SME)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The [Scalable Matrix Extension](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture) (SME) is a system solution consisting of hardware components to efficiently process matrices.

SME introduces:
* A register array storage ("ZA") capable of holding two-dimensional matrix tiles.
* A Streaming SVE processing mode, which supports execution of SVE2 instructions with a vector length that matches the tile width.
* Instructions that accumulate the outer product of two vectors into a tile.
* Instructions that transfer a vector to or from a tile row or column.
* System registers and fields that identify the presence and capabilities of SME, and enable and control its behavior at each Exception level.

The ZA storage is a two-dimensional array of width SVL bits, and height equal to its width in bytes, in other words, (SVL / 8) rows. 
SVL (the Effective Streaming SVE Vector Length) can be configured in software, and is a power of two in the range 128 to 2048 bits inclusive.

The ZA storage is accessed as tiles. A ZA tile is a square, two-dimensional sub-array of elements within the ZA array, whose elements must all be the same width, which can be 8-bit, 16-bit, 32-bit, 64-bit, or 128-bit.

The tile width is the same as the ZA storage width, which is always SVL bits. If N = SVL/8 then the ZA storage would be N rows x N bytes in size. 
When accessing the tile as 16-bit halfwords, it would only be N/2 halfwords wide. Since tiles are square, it would also be N/2 rows high, and therefore there is space in the ZA storage for two such tiles.

Similarly, when accessing 32-bit elements, tiles would have height and width both equal to N/4, so there would be four such tiles in the ZA storage. This trend continues so that there would be 16 tiles of element width 128-bits.

You can read or write a ZA tile slice, which is a one-dimensional vector representing a complete row or column within a tile slice.

![example image alt-text#center](/learning-paths/cross-platform/sme/ZA.png "Figure 1. The ZA storage, accessed by 32-bit elements, shown for SVL = 256 bits, and showing the mapping to horizontal and vertical slices of the four ZA0-3 tiles.")

The Scalable Matrix Extension version 2 (SME2) extends the SME architecture to increase the number of applications that can benefit from the computational efficiency of SME, beyond its initial focus on outer products and matrix-matrix multiplication.  SME2 adds:
* Data processing instructions with multi-vector operands and a multi-vector predication mechanism.
* A Range Prefetch hint instruction.
* Compressed neural network capability using dedicated lookup table instructions and outer product instructions that support binary neural networks.
* A 512-bit architectural register, ZT0, to support the lookup table feature.

The new instructions enable SME2 to accelerate more workloads than the original SME, including GEMV, Non-Linear Solvers, Small and Sparse Matrices, and Feature Extraction or tracking.

SME is represented by the architectural feature FEAT_SME.  FEAT_SME is an optional extension from Armv9.2-A.
SME2 is represented by the architectural feature FEAT_SME2.  FEAT_SME2 is an optional extension from Armv9.2-A.  FEAT_SME2 requires FEAT_SME.
