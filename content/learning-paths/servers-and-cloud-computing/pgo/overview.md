---
title: Understand PGO and LTO
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This Learning Path demonstrates how to use LLVM Link-Time Optimization (LTO) and Profile-Guided Optimization (PGO) together on AArch64 Linux.

LTO gives the compiler visibility of the entire program during the link stage. Instead of optimizing each source file independently, LLVM performs additional whole-program optimizations across source file boundaries. PGO uses runtime behavior to guide compiler decisions. When the compiler knows which functions and branches are frequently executed, it can make better decisions about function inlining, branch prediction, code layout, and other optimizations.

LTO and PGO are complementary. LTO enables whole-program optimizations, while PGO provides runtime profile data that guides optimization decisions.

This guide focuses on using LLVM LTO and PGO.
The example application and build configuration are intentionally simple to demonstrate the LLVM workflows and compiler options. Real-world applications are typically more complex and might require different build configurations and optimization strategies.

The following sections cover LLVM LTO and several LLVM PGO workflows, each with different trade-offs:

- [LLVM LTO](/learning-paths/servers-and-cloud-computing/pgo/lto/) gives the compiler visibility across source file boundaries at link time. This provides the baseline for the later profile-guided workflows.

- [LLVM S-PGO](/learning-paths/servers-and-cloud-computing/pgo/s-pgo/) uses sampled execution data, usually collected with `perf`, instead of compiler-inserted instrumentation. It has much lower profiling overhead than instrumentation, but it requires hardware and operating system support.

- [LLVM FE-PGO](/learning-paths/servers-and-cloud-computing/pgo/fe-pgo/) instruments the program in the Clang frontend to record execution counts. It can be useful when profile data needs to map closely to the source code, but IR-PGO is usually the better starting point for optimization.

- [LLVM IR-PGO](/learning-paths/servers-and-cloud-computing/pgo/ir-pgo/) instruments the program at the LLVM IR level to record execution counts. This is the default instrumentation-based workflow in this guide and is typically the preferred option for performance optimization with Clang.

- [LLVM CSIR-PGO](/learning-paths/servers-and-cloud-computing/pgo/csir-pgo/) adds a second, context-sensitive profiling pass after an initial IR-PGO build. This can give LLVM more precise profile data, but it requires an extra build and profiling run.

## What you've learned and what's next

You’ve now seen an overview of LLVM LTO, PGO, and the optimization workflows covered in this guide.

In the next section, you'll prepare the test directory and verify the LLVM tools.
