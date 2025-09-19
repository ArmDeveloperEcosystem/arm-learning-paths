---
title: About Single Instruction, Multiple Data loops
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to SIMD on Arm and why it matters for performance on Arm CPUs

Writing high-performance software on Arm often means using single-instruction, multiple-data (SIMD) technologies. Many developers start with NEON, a familiar fixed-width vector extension. As Arm architectures evolve, so do the SIMD capabilities available to you.

This Learning Path uses the Scalable Vector Extension (SVE) and the Scalable Matrix Extension (SME) to demonstrate modern SIMD patterns. They are two powerful, scalable vector extensions designed for modern workloads. Unlike NEON, these architecture extensions are not just wider; they are fundamentally different. They introduce predication, vector-length-agnostic (VLA) programming, gather/scatter, streaming modes, and tile-based compute with ZA state. The result is more power and flexibility, but there can be a learning curve to match.

## What is the SIMD Loops project?

The SIMD Loops project offers a hands-on way to climb the learning curve. It is a public codebase of self-contained, real loop kernels written in C, Arm C Language Extensions (ACLE) intrinsics, and selected inline assembly. Kernels span tasks such as matrix multiply, sorting, and string processing. You can build them, run them, step through them, and adapt them for your own SIMD workloads.

Visit the [SIMD Loops Repo](https://gitlab.arm.com/architecture/simd-loops).

This open-source project (BSD-3-Clause) teaches SIMD development on modern Arm CPUs with SVE, SVE2, SME, and SME2. It’s aimed at developers who know NEON intrinsics and want to explore newer extensions. The goal of SIMD Loops is to provide working, readable examples that demonstrate how to use the full range of features available in SVE, SVE2, and SME2. Each example is a self-contained loop kernel - a small piece of code that performs a specific task like matrix multiplication, vector reduction, histogram, or memory copy. These examples show how that task can be implemented across different vector instruction sets.

Unlike a cookbook that attempts to provide a recipe for every problem, SIMD Loops takes the opposite approach. It aims to showcase the architecture rather than the problem itself. The loop kernels are chosen to be realistic and meaningful, but the main goal is to demonstrate how specific features and instructions work in practice. If you are trying to understand scalability, predication, gather/scatter, streaming mode, ZA storage, compact instructions, or the mechanics of matrix tiles, this is where you can see them in action.

The project includes:
- Many numbered loop kernels, each focused on a specific feature or pattern
- Reference C implementations to establish expected behavior
- Inline assembly and/or intrinsics for scalar, NEON, SVE, SVE2, SVE2.1, SME2, and SME2.1
- Build support for different instruction sets, with runtime validation
- A simple command-line runner to execute any loop interactively
- Optional standalone binaries for bare-metal and simulator use

You do not need to rely on auto-vectorization or guess at compiler flags. Each loop is handwritten and annotated to make the intended use of SIMD features clear. Study a kernel, modify it, rebuild, and observe the effect - this is the core learning loop.


