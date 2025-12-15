---
title: Explore LiteRT, XNNPACK, KleidiAI, and SME2
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inside the LiteRT software stack

LiteRT (Lite Runtime, formerly TensorFlow Lite) is a runtime for on-device AI. The default CPU acceleration library used by LiteRT is XNNPACK.

XNNPACK is an open-source library that provides highly optimized implementations of neural-network operators. It continuously integrates the KleidiAI library to use new CPU features such as Scalable Matrix Extension 2 (SME2).

KleidiAI is a library developed by Arm that offers performance-critical micro-kernels using Arm architecture features, such as SME2.

The software stack for LiteRT is shown below.

![Diagram showing the software stack for on-device AI on Arm platforms. The stack is organized in layers from top to bottom: LiteRT at the top, followed by XNNPACK, then KleidiAI, and SME2 at the bottom. Arrows indicate the flow of execution from LiteRT through XNNPACK to KleidiAI and SME2. The diagram includes the following text labels: LiteRT, XNNPACK, KleidiAI, SME2. The environment is technical and structured, emphasizing the integration of Arm-optimized libraries for efficient AI inference. alt-text#center](./litert-sw-stack.png "LiteRT, XNNPACK, KleidiAI, and SME2 software stack")

## How KleidiAI works in LiteRT

To understand how KleidiAI SME2 micro-kernels work in LiteRT, think about a LiteRT model with one fully connected operator using the FP32 data type. The following diagrams illustrate the execution workflow of XNNPACK's implementation compared with the workflow when KleidiAI SME2 is enabled in XNNPACK.

### LiteRT → XNNPACK workflow

![Diagram showing the workflow for a fully connected operator in LiteRT using XNNPACK. The diagram depicts the flow from LiteRT to XNNPACK, highlighting the use of NEON instructions for matrix multiplication and weight packing on Arm platforms. The technical environment emphasizes operator traversal, hardware detection, and parallel computation. alt-text #center](./litert-xnnpack-workflow.png "LiteRT, XNNPACK workflow")
For batch sizes greater than 1, a fully connected operator performs a matrix multiplication between the input activations (LHS) and the weights (RHS).

When LiteRT loads a model, it reads the operators and builds a computation graph. If you select the CPU as the accelerator, LiteRT uses XNNPACK by default.

XNNPACK scans the computation graph and looks for operators it can optimize. XNNPACK also checks the hardware compatibility and chooses the best available micro-kernel.Then, it packs the weight matrix to prepare for efficient computation. On Arm platforms, XNNPACK uses NEON instructions to speed up this packing.

During model inference, it splits the matrices into smaller tiles and runs the multiplications in parallel across multiple threads, using NEON instructions for faster processing.

### LiteRT → XNNPACK → KleidiAI workflow

![Diagram showing the workflow for a fully connected operator in LiteRT using XNNPACK and KleidiAI with SME2. The diagram illustrates the flow from LiteRT to XNNPACK, then to KleidiAI, highlighting SME2 micro-kernel integration for matrix multiplication and packing. The technical context emphasizes runtime hardware detection and optimized operator execution. alt-text #center](./litert-xnnpack-kleidiai-workflow.png "LiteRT, XNNPACK, KleidiAI workflow")

When KleidiAI and SME2 are enabled at build time, the KleidiAI SME2 micro-kernels are compiled into XNNPACK.

During the model loading stage, when XNNPACK optimizes the subgraph, it checks the operator’s data type to determine whether a KleidiAI implementation is available. If KleidiAI supports it, XNNPACK bypasses its own default implementation. As a result, RHS packing is performed using the KleidiAI SME packing micro-kernel. Because KleidiAI typically requires packing of the LHS, a flag is also set during this stage.

During model inference, the LHS packing micro-kernel is invoked. After the LHS is packed, XNNPACK performs the matrix multiplication. At this point, the KleidiAI SME micro-kernel is used to compute the matrix .

## What you've accomplished and what's next

In this section, you explored how LiteRT leverages XNNPACK and KleidiAI to accelerate fully connected operators on Arm platforms. You learned how XNNPACK uses NEON instructions for efficient matrix operations and how enabling KleidiAI with SME2 further optimizes performance by introducing specialized micro-kernels for packing and matrix multiplication.

You have completed the overview of LiteRT, XNNPACK, KleidiAI, and SME2 integration. Next, you’ll dive deeper into building and benchmarking models with these technologies.


