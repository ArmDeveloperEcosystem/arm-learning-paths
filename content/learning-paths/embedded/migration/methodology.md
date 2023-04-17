---
# User change
title: "Porting methodology" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Methodology

## List application requirements and configuration

Before migrating to Arm, it is important to understand the original platform environment to build, run and develop the application.

- What is the original platform architecture (e.g. x86_64)?
- Does the application benefit from hardware acceleration (e.g. Nvidia GPU)?
- What OS does the application run on?
- Does the application run in a virtual machine or a software container?
- What is the application's source langage?
- Is the application built natively or cross-compiled?
- What are the application's system dependencies? Does the application use external libraries?
- How is the application built (e.g. configuration) and which tools are used (e.g. compilers)?

These questions help draw a picture of the migration process to identify:

- the target platform configuration (e.g. hardware acceleration, OS, system dependencies),
- development tools (e.g. compilers),
- application requirements and configuration (e.g. compiler flags, third-party libraries that may need porting as well).

## Replicate setup

To minimize compatibility issues between software versions and facilitate the migration, it is important to replicate the same setup as much as possible.

To illustrate this, we have summarized our example's original configuration in the table below:

| Source code | Build type | OS | Compiler | Build tools | External libraries |
| ----------- | ---------- | -- | -------- | ----------- | ------------------ |
| C++ | Native build | Ubuntu 20.04.5 | GCC 9.4.0 | Cmake 3.25.3 | OpenCV 4.2.0 |

This configuration can easily be reproduced on aarch64 by installing Ubuntu 20.04.05 and installing the system's packages. We can already foresee that building the pure C and the OpenCV version of the Sobel filter on aarch64 won't be an issue.

## Identify non-portable settings

Running the application on the original architecture and inspecting the source code can provide useful information. With this, we suspect that most of the porting work on our example will be spent on the SIMD version of the Sobel filter because it uses architecture-specific intrinsics. The header file `x86intrin.h` will likely be problematic when building natively on aarch64.

In addition, inspecting the compilers options when building indicates that an architecture-specific flag `-mavx` is used with GCC. Again, this might also be an issue and might prevent building the application completely.

