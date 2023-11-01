---
title: Introducing Scalable Matrix Extension (SME)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The [Scalable Matrix Extension](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture) (`SME`) is a system solution consisting of hardware and software components to optimize the processing of matrices.

SME introduces:
* A register array storage ("ZA") capable of holding two-dimensional matrix tiles.
* A Streaming SVE processing mode, which supports execution of SVE2 instructions with a vector length that matches the tile width.
* Instructions that accumulate the outer product of two vectors into a tile.
* Instructions that transfer a vector to or from a tile row or column.
* System registers and fields that identify the presence and capabilities of SME, and enable and control its behavior at each Exception level.

The Scalable Matrix Extension version 2 (SME2) extends the SME architecture to increase the number of applications that can benefit from the computational efficiency of SME, beyond its initial focus on outer products and matrix-matrix multiplication, by adding data processing instructions with multi-vector operands and a multi-vector predication mechanism.

SME is represented by the architectural feature FEAT_SME.  FEAT_SME is an optional extension from Armv9.2-A.
SME2 is represented by the architectural feature FEAT_SME2.  FEAT_SME2 is an optional extension from Armv9.2-A.  FEAT_SME2 requires FEAT_SME.

