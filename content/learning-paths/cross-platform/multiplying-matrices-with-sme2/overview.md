---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm's Scalable Matrix Extension Version 2 (SME2)

## What is SME2?

The Scalable Matrix Extension (SME) is an extension to the Armv9-A architecture designed to accelerate matrix-heavy computations, such as outer products and matrix-matrix multiplications. SME Version 2 (SME2) extends the SME architecture by accelerating vector operations to increase the number of applications that can benefit from the computational efficiency of SME, beyond its initial focus on outer products and matrix-matrix multiplication.

SME2 extends SME by introducing multi-vector data-processing instructions, load to and store from multi-vectors, and a multi-vector predication mechanism.

## Key architectural features of SME2

The key architectural features of SME2 include:

* Multi-vector multiply-accumulate instructions, with Z vectors as multiplier and multiplicand inputs and accumulating results into ZA array vectors, including widening multiplies that accumulate into more vectors than they read.

* Multi-vector load, store, move, permute, and convert instructions, that use multiple SVE Z vectors as source and destination registers to pre-process inputs and post-process outputs of the ZA-targeting SME2 instructions.

* *Predicate-as-counter*, which is an alternative predication mechanism that is added to the original SVE predication mechanism, to control operations performed on multiple vector registers.

* Compressed neural network capability using dedicated lookup table instructions and outer product instructions that support binary neural networks.

* A 512-bit architectural register ZT0, that supports the lookup table feature.

### Suggested reading

If you are not familiar with matrix multiplication, or would benefit from refreshing your knowledge, this [Wikipedia article on Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) is a good start.

This Learning Path assumes some basic understanding of SVE and SME. If you are not familiar with SVE or SME, these are some useful resources that you can read first:
- [Introducing the Scalable Matrix Extension for the Armv9-A Architecture](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture).
- [Arm Scalable Matrix Extension (SME) Introduction (Part 1)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction).
- [Arm Scalable Matrix Extension (SME) Introduction (Part 2)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2).
- [Part 3: Matrix-matrix multiplication. Neon, SVE, and SME compared](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared).
- [Build adaptive libraries with multiversioning](https://learn.arm.com/learning-paths/cross-platform/function-multiversioning/)