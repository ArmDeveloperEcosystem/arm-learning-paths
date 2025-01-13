---
title: Basics of Compilers 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to C++ and Compilers

The C++ language gives the programmer the freedom to be expressive in the way they write code - allowing low-level manipulation of memory and data structures. Compared to managed languages, such as Java, C++ source code is generally less portable, requiring recompilation to the target Arm architecture. In the context of performance optimisation of C++ workloads on Arm, the biggest wins will come from how you effectively use the compiler and potentially adjusting source code. 

Writing performant C++ code is a topic in itself and out of scope for this learning path. Instead we will focus on how to effectively use the compiler to target Arm on a cloud instance. 

### Compiler Versions

The two main compiler options for compiling C++ source code are the GNU Compiler Collection (GCC) or LLVM - both of which are open-source compilers and have contributions from Arm engineers to support the latest architectures. Proprietary or vendor specific compilers, such as `nvcc` for compiling for NVIDIA GPUs, are often based on these open-source compilers. Alternative proprietory compilers are often for specific use cases, for example safety critical applications may need to comply with various ISO standards, which also include the compiler. The [Arm Compiler for Embedded FuSa](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded%20FuSa) is such an example of a C/C++ compiler. 

Most application developers are not in this safety qualification domain so we will be using the open-source GCC/G++ compiler for this learning path. 

There are multiple Linux distribtions available to choose from. Each Linux distribution and operating system is bundled with an included compiler. For example, for on a AWS Graviton instance running Ubuntu 22.04 LTS the C++ compiler bundled is below. 

``` output
g++ --version
g++ (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```

The table below shows the default (*) and available compilers for a variety of linux distributions. This is taken from the [AWS-graviton performance runbook](https://github.com/aws/aws-graviton-getting-started/blob/main/c-c%2B%2B.md).

Distribution    | GCC                  | Clang/LLVM
----------------|----------------------|-------------
Amazon Linux 2023  | 11*               | 15*
Amazon Linux 2  | 7*, 10               | 7, 11*
Ubuntu 24.04    | 9, 10, 11, 12, 13*, 14 | 14, 15, 16, 17, 18*
Ubuntu 22.04    | 9, 10, 11*, 12       | 11, 12, 13, 14*
Ubuntu 20.04    | 7, 8, 9*, 10         | 6, 7, 8, 9, 10, 11, 12
Ubuntu 18.04    | 4.8, 5, 6, 7*, 8     | 3.9, 4, 5, 6, 7, 8, 9, 10
Debian10        | 7, 8*                | 6, 7, 8
Red Hat EL8     | 8*, 9, 10            | 10
SUSE Linux ES15 | 7*, 9, 10            | 7


The biggest and most simple performance gain can be achieved by using the most recent compiler available. The most recent optimisations and support will be available through the latest compiler. Recompilation using a newer compiler may lead to optimisations without having to develop your source code. As an example, the most recent version of GCC available at the time of writing, version 14.2, has the following support and optimisations listed on their website [changes page](https://gcc.gnu.org/gcc-14/changes.html). 

```output
A number of new CPUs are supported through the -mcpu and -mtune options (GCC identifiers in parentheses).
    - Ampere-1B (ampere1b).
    - Arm Cortex-A520 (cortex-a520).
    - Arm Cortex-A720 (cortex-a720).
    - Arm Cortex-X4 (cortex-x4).
    - Microsoft Cobalt-100 (cobalt-100).
...
```