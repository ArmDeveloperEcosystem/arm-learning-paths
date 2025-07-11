---
title: About SIMD Loops
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Writing high-performance software for Arm processors often involves delving into
its SIMD technologies. For many developers, that journey started with Neon --- a
familiar, fixed-width vector extension that has been around for years. But as
Arm architectures continue to evolve, so do their SIMD technologies.

Enter the world of SVE and SME: two powerful, scalable vector extensions designed for modern
workloads. Unlike Neon, they aren’t just wider --- they’re different. These
extensions introduce new instructions, more flexible programming models, and
support for concepts like predication, scalable vectors, and streaming modes.
However, they also come with a learning curve.

That’s where [SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) comes
in.

[SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) is designed to help
you in the process of learning how to write SVE and SME code. It is a collection
of self-contained, real-world loop kernels --- written in a mix of C, ACLE
intrinsics, and inline assembly --- that target everything from simple arithmetic
to matrix multiplication, sorting, and string processing. You can compile them,
run them, step through them, and use them as a foundation for your own SIMD
work.

If you’re familiar with Neon intrinsics and would like to explore what SVE and
SME have to offer, the [SIMD
Loops](https://gitlab.arm.com/architecture/simd-loops) project is for you !

## What is SIMD Loops ?

[SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) is an open-source
project built to help you learn how to write SIMD code for modern Arm
architectures --- specifically using SVE (Scalable Vector Extension) and SME
(Scalable Matrix Extension). It is designed for programmers who already know
their way around Neon intrinsics but are now facing the more powerful --- and
more complex --- world of SVE and SME.

The goal of SIMD Loops is to provide working, readable examples that demonstrate
how to use the full range of features available in SVE, SVE2, and SME2. Each
example is a self-contained loop kernel --- a small piece of code that performs
a specific task like matrix multiplication, vector reduction, histogram or
memory copy --- and shows how that task can be implemented across different
vector instruction sets.

Unlike a cookbook that tries to provide a recipe for every problem, SIMD Loops
takes the opposite approach: it aims to showcase the architecture, not the
problem. The loop kernels are chosen to be realistic and meaningful, but the
main goal is to demonstrate how specific features and instructions work in
practice. If you’re trying to understand scalability, predication,
gather/scatter, streaming mode, ZA storage, compact instructions, or the
mechanics of matrix tiles --- this is where you’ll see them in action.

The project includes:
- Dozens of numbered loop kernels, each focused on a specific feature or pattern
- Reference C implementations to establish expected behavior
- Inline assembly and/or intrinsics for scalar, Neon, SVE, SVE2, and SME2
- Build support for different instruction sets, with runtime validation
- A simple command-line runner to execute any loop interactively
- Optional standalone binaries for bare-metal and simulator use

You don’t need to worry about auto-vectorization, compiler flags, or tooling
quirks. Each loop is hand-written and annotated to make the use of SIMD features
clear. The intent is that you can study, modify, and run each loop as a learning
exercise --- and use the project as a foundation for your own exploration of
Arm’s vector extensions.

## Where to get it?

[SIMD Loops](https://gitlab.arm.com/architecture/simd-loops) is available as an
open-source code licensed under BSD 3-Clause. You can access the source code
from the following GitLab project:
https://gitlab.arm.com/architecture/simd-loops

