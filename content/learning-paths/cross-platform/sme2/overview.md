---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Overview of Arm's Scalable Matrix Extension Version 2 

### What is SME2?

The Scalable Matrix Extension Version 2 (SME2) extends the SME architecture by accelerating vector operations to increase the number of applications that can benefit from the computational efficiency of SME, beyond its initial focus on outer products and matrix-matrix multiplication.

SME2 extends SME by introducing multi-vector data-processing instructions, load to and store from multi-vectors, and a multi-vector predication mechanism.

Additional architectural features of SME2 include:

Multi-vector multiply-accumulate instructions, with Z vectors as multiplier and multiplicand inputs and accumulating results into ZA array vectors, including widening multiplies that accumulate into more vectors than they read.

Multi-vector load, store, move, permute, and convert instructions, that use multiple SVE Z vectors as source and destination registers to pre-process inputs and post-process outputs of the ZA-targeting SME2 instructions

“Predicate-as-counter”, an alternative predication mechanism is added to the original SVE predication mechanism, to control operations performed on multiple vector registers

Compressed neural network capability using dedicated lookup table instructions and outer product instructions that support binary neural networks

SME2 adds a 512-bit architectural register ZT0, that supports the lookup table feature.

### Suggested reading

If you are not familiar with matrix multiplication, or need a refresh, this [wikipedia article on Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) is a good
start.

If you are not familiar with SVE and / or SME, it is strongly suggested that you
first read some material as this learning path assumes some basic understanding
of those technologies:

 - [Introducing the Scalable Matrix Extension for the Armv9-A
   Architecture](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture).
 - [Arm Scalable Matrix Extension (SME) Introduction (Part
   1)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction).
 - [Arm Scalable Matrix Extension (SME) Introduction (Part
   2)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2).