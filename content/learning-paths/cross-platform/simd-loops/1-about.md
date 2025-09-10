---
title: About single instruction, multiple data (SIMD) loops
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Writing high-performance software for Arm processors often involves delving into
SIMD technologies. For many developers, that journey started with NEON, a
familiar, fixed-width vector extension that has been around for many years. But as
Arm architectures continue to evolve, so do their SIMD technologies.

Enter the world of Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME): two powerful, scalable vector extensions designed for modern
workloads. Unlike NEON, they are not just wider; they are fundamentally different. These
extensions introduce new instructions, more flexible programming models, and
support for concepts like predication, scalable vectors, and streaming modes.
However, they also come with a learning curve.

That is where [SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) becomes a valuable resource, enabling you to quickly and effectively learn how to write high-performance SIMD code.

SIMD Loops is designed to help
you learn how to write SVE and SME code. It is a collection
of self-contained, real-world loop kernels written in a mix of C, Arm C Language Extensions (ACLE)
intrinsics, and inline assembly. These kernels target tasks ranging from simple arithmetic
to matrix multiplication, sorting, and string processing. You can compile them,
run them, step through them, and use them as a foundation for your own SIMD
work.

If you are familiar with NEON intrinsics, you can use SIMD Loops to learn and explore SVE and SME.

## What is SIMD Loops?

SIMD Loops is an open-source
project, licensed under BSD 3-Clause, built to help you learn how to write SIMD code for modern Arm
architectures, specifically using SVE and SME.
It is designed for programmers who already know
their way around NEON intrinsics but are now facing the more powerful and
complex world of SVE and SME.

The goal of SIMD Loops is to provide working, readable examples that demonstrate
how to use the full range of features available in SVE, SVE2, and SME2. Each
example is a self-contained loop kernel, a small piece of code that performs
a specific task like matrix multiplication, vector reduction, histogram, or
memory copy. These examples show how that task can be implemented across different
vector instruction sets.

Unlike a cookbook that tries to provide a recipe for every problem, SIMD Loops
takes the opposite approach. It aims to showcase the architecture rather than
the problem. The loop kernels are chosen to be realistic and meaningful, but the
main goal is to demonstrate how specific features and instructions work in
practice. If you are trying to understand scalability, predication,
gather/scatter, streaming mode, ZA storage, compact instructions, or the
mechanics of matrix tiles, this is where you will see them in action.

The project includes:
- Dozens of numbered loop kernels, each focused on a specific feature or pattern
- Reference C implementations to establish expected behavior
- Inline assembly and/or intrinsics for scalar, NEON, SVE, SVE2, SVE2.1, SME2, and SME2.1
- Build support for different instruction sets, with runtime validation
- A simple command-line runner to execute any loop interactively
- Optional standalone binaries for bare-metal and simulator use

You do not need to worry about auto-vectorization, compiler flags, or tooling
quirks. Each loop is hand-written and annotated to make the use of SIMD features
clear. The intent is that you can study, modify, and run each loop as a learning
exercise, and use the project as a foundation for your own exploration of
Arm’s vector extensions.


