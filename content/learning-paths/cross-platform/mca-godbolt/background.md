---
title: Background
weight: 2
### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Terminology

Before you get started, familiarize yourself with the terms below:

- **Instruction scheduling**: If two instructions appear in a sequence in a program, but are independent from each other, the compiler can swap them without affecting the program's behavior. The goal of instruction scheduling is to find a valid permutation of the program instructions that also optimizes the program's performance, by making use of processor resources.

- **Pipeline**: A pipeline is the mechanism used by the processor to execute instructions. Pipelining makes efficient use of processor resources by dividing instructions into stages that can overlap and be processed in parallel, reducing the time it takes for instructions to execute. Instructions can only be executed if the required data is available, otherwise this leads to a delay in execution called a pipeline stall.

- **Resource pressure**: Resources refer to the hardware units used to execute instructions. If instructions in a program all rely on the same resources, then it leads to pressure. Execution is slowed down as instructions must wait until the unit they need becomes available.

- **Data dependency**: Data dependency refers to the relationship between instructions. When an instruction requires data from a previous instruction this creates a data dependency.


### What is Machine Code Analyzer (MCA)?

Machine Code Analyzer (MCA) is a performance analysis tool that uses information available in [LLVM](https://github.com/llvm/llvm-project) to measure performance on a specific CPU.


### How can MCA be useful?

MCA takes as input a snippet of assembly code and then simulates the execution of that code in a loop of iterations, and the default is 100.

MCA then outputs a performance report, which contains information such as the latency and throughput of the assembly block and the resource usage for each instruction.

Using this information, you can identify bottlenecks in performance such as resource pressure and data dependencies. There are many options you can give MCA to get performance metrics. The options are explained in the [llvm-mca documentation](https://llvm.org/docs/CommandGuide/llvm-mca.html).

### How to acquire MCA

MCA is available as part of most Linux distributions, however the version tends to lag behind the current LLVM release. A recent version of MCA is also shipped as part of the Arm Toolchain for Linux (ATfL). You can find more information about ATfL and installation steps in the [ATfL user guide](https://developer.arm.com/documentation/110477/211/?lang=en). The set of cores available for performance estimation in MCA is determined by the LLVM version. You can check the version you are currently using by running `llvm-mca --version`. Using a recent version of LLVM is recommended in order to take advantage of improvements made to MCA. The most recent release can be obtained directly from LLVM, by downloading one of their [release packages](https://github.com/llvm/llvm-project/releases/). LLVM also makes nightly builds available to [download for Debian/Ubuntu](https://apt.llvm.org) based systems.
