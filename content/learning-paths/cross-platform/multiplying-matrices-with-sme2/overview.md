---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm's Scalable Matrix Extension Version 2 (SME2)

Arm’s Scalable Matrix Extension Version 2 (SME2) is a hardware feature designed to accelerate dense linear algebra operations, enabling high-throughput execution of matrix-based workloads. 

Whether you're building for AI inference, HPC, or scientific computing, SME2 provides fine-grained control and high-performance vector processing.


## Extending the SME architecture

SME is an extension to the Armv9-A architecture and is designed to accelerate matrix-heavy computations, such as outer products and matrix-matrix multiplications. 

SME2 builds on SME by accelerating vector operations to increase the number of applications that can benefit from the computational efficiency of SME, beyond its initial focus on outer products and matrix-matrix multiplication.

## Key architectural features of SME2

SME2 adds several capabilities to the original SME architecture:

* **Multi-vector multiply-accumulate instructions**, that use Z vectors as multiplier and multiplicand inputs, and accumulate results into ZA array vectors. This includes widening multiplies that write to more vectors than they read from.

* **Multi-vector load, store, move, permute, and convert instructions**, that use multiple SVE Z vectors as source and destination registers to efficiently pre-process inputs and post-process outputs of the ZA-targeting SME2 instructions.

* A **predicate-as-counter mechanism**, which is a new predication mechanism that is added alongside the original SVE approach to enable fine-grained control over operations across multiple vector registers.

* **Compressed neural network support**, using dedicated lookup table and outer product instructions that support binary neural network workloads.

* A **512-bit architectural register ZT0**, which is a dedicated register that enables fast, table-driven data transformations.

## Further information

This Learning Path does assume some basic understanding of SVE, SME, and matrix multiplication, however if you do want to refresh or grow your knowledge, these are some useful resources that you might find helpful: 

On matrix multiplication: 

- The [Wikipedia article](https://en.wikipedia.org/wiki/Matrix_multiplication)

On SVE and SME:

- [Introducing the Scalable Matrix Extension for the Armv9-A Architecture - Martin Weidmann, Arm](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture)
- [Arm Scalable Matrix Extension (SME) Introduction (Part 1) - Zenon Xiu](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction)
- [Arm Scalable Matrix Extension (SME) Introduction (Part 2) - Zenon Xiu](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2)
- [Matrix-matrix multiplication. Neon, SVE, and SME compared (Part 3)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/.matrix-matrix-multiplication-neon-sve-and-sme-compared)
- [Learn about function multiversioning - Alexandros Lamprineas, Arm](/learning-paths/cross-platform/function-multiversioning/)