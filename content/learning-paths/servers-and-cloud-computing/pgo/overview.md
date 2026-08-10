---
title: Understand PGO and LTO for AArch64 code
description: Compare LLVM LTO and sample-based, frontend, IR-level, and context-sensitive PGO workflows for optimizing AArch64 code with Clang.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Combine LTO and PGO

You'll use LLVM Link-Time Optimization (LTO) and Profile-Guided Optimization (PGO) together on AArch64 Linux.

LTO gives the compiler visibility across source-file boundaries during the link stage. Without LTO, LLVM optimizes each translation unit separately before linking it into the application. PGO adds information about runtime behavior. LLVM can use function frequencies and branch counts to guide inlining, code layout, and other optimization decisions.

LTO and PGO are complementary. LTO enables whole-program optimizations, while PGO provides runtime profile data that guides optimization decisions.

The example that you'll use is a deliberately small C++ application. The application demonstrates the LLVM workflow and compiler options, but its single source file doesn't show the cross-module optimization opportunities that LTO provides in a larger application.

For useful PGO results, train the instrumented or sampled binary with inputs that represent your production workload. LLVM can optimize code that the profile identifies as hot and reduce optimization of unexecuted code. An unrepresentative profile can therefore reduce performance for important use cases.

The following sections cover LLVM LTO and several LLVM PGO workflows, each with different trade-offs:

- [LLVM Link-Time Optimization (LTO)](/learning-paths/servers-and-cloud-computing/pgo/lto/) gives the compiler visibility across source file boundaries at link time. This provides the baseline for the later profile-guided workflows.

- [LLVM sample-based Profile-Guided Optimization (S-PGO)](/learning-paths/servers-and-cloud-computing/pgo/s-pgo/) uses sampled execution data collected with `perf` instead of compiler-inserted instrumentation. S-PGO has lower profiling overhead, but the Branch Record Buffer Extension (BRBE) workflow requires supported Arm hardware and Linux kernel 6.17 or later.

- [LLVM frontend Profile-Guided Optimization (FE-PGO)](/learning-paths/servers-and-cloud-computing/pgo/fe-pgo/) instruments the program in the Clang frontend to record execution counts. FE-PGO can be useful when profile data needs to map closely to the source code, but IR-PGO is usually the better starting point for optimization.

- [LLVM Intermediate Representation-level Profile-Guided Optimization (IR-PGO)](/learning-paths/servers-and-cloud-computing/pgo/ir-pgo/) instruments the program at the LLVM IR level to record execution counts. IR-PGO is the default instrumentation-based workflow in this Learning Path and is typically the preferred option for performance optimization with Clang.

- [LLVM context-sensitive Intermediate Representation-level Profile-Guided Optimization (CSIR-PGO)](/learning-paths/servers-and-cloud-computing/pgo/csir-pgo/) adds a second, context-sensitive profiling pass after an initial IR-PGO build. CSIR-PGO can give LLVM more precise profile data, but it requires an extra build and profiling run.

## What you've learned and what's next

You now understand how LTO expands the scope of LLVM optimization and how the available PGO workflows collect runtime behavior.

Next, you'll prepare the test directory and verify the LLVM tools.
