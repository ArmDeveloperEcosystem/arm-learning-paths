---
title: Explore LiteRT, XNNPACK, KleidiAI, and SME2
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT, XNNPACK, KleidiAI, and SME2

LiteRT (Lightweight Runtime, formerly TensorFlow Lite) is a runtime for on-device AI on Arm platforms. The default CPU acceleration library used by LiteRT is XNNPACK (an open-source library providing highly optimized neural-network operators).

XNNPACK is an open-source library that provides highly optimized implementations of neural-network operators. It continuously integrates the KleidiAI library to use new CPU features such as Scalable Matrix Extension version 2 (SME2).

KleidiAI is a library developed by Arm that offers performance-critical micro-kernels using Arm architecture features, such as SME2.

The software stack for LiteRT is shown below.

![Diagram showing the software stack for on-device AI on Arm platforms. The stack is organized in layers from top to bottom: LiteRT at the top, followed by XNNPACK, then KleidiAI, and SME2 at the bottom. Arrows indicate the flow of execution from LiteRT through XNNPACK to KleidiAI and SME2. The diagram includes the following text labels: LiteRT, XNNPACK, KleidiAI, SME2. The environment is technical and structured, emphasizing the integration of Arm-optimized libraries for efficient AI inference. #center](./litert-sw-stack.png "LiteRT, XNNPACK, KleidiAI and SME2")

## How KleidiAI works in LiteRT

To understand how KleidiAI SME2 micro-kernels work in LiteRT, consider a LiteRT model with one Fully Connected operator using the FP32 data type.

The following diagrams illustrate the execution workflow of XNNPACK’s implementation compared with the workflow when KleidiAI SME2 is enabled in XNNPACK.

### LiteRT → XNNPACK workflow

![Diagram showing the workflow for a Fully Connected operator in LiteRT using XNNPACK. The diagram depicts the flow from LiteRT to XNNPACK, highlighting the use of NEON instructions for matrix multiplication and weight packing on Arm platforms. The technical environment emphasizes operator traversal, hardware detection, and parallel computation. #center](./litert-xnnpack-workflow.png "LiteRT, XNNPACK workflow")

A Fully Connected operator is essentially implemented as a matrix multiplication.

When LiteRT loads a model, it parses the operators and creates a computation graph. If the CPU is selected as the accelerator, LiteRT uses XNNPACK by default.

XNNPACK traverses the operators in the graph and tries to replace them with its own implementations. During this stage, XNNPACK packs the weight matrix, using NEON instructions for Arm platforms to speed up the process. XNNPACK provides different implementations for different hardware platforms. At runtime, it detects hardware capabilities and selects the appropriate micro-kernel.

During model inference, XNNPACK performs matrix multiplication on the activation matrix (left-hand side, LHS) and the repacked weight matrix (right-hand side, RHS). XNNPACK applies tiling strategies to the matrices and performs parallel multiplication across the resulting tiles using multiple threads. To accelerate computation, XNNPACK uses NEON instructions.

### LiteRT → XNNPACK → KleidiAI workflow

![Diagram showing the workflow for a Fully Connected operator in LiteRT using XNNPACK and KleidiAI with SME2. The diagram illustrates the flow from LiteRT to XNNPACK, then to KleidiAI, highlighting SME2 micro-kernel integration for matrix multiplication and packing. The technical context emphasizes runtime hardware detection and optimized operator execution. alt-text #center](./litert-xnnpack-kleidiai-workflow.png "LiteRT, XNNPACK, KleidiAI workflow")

When KleidiAI and SME2 are enabled at build time, the KleidiAI SME2 micro-kernels are compiled into XNNPACK.

During the model loading stage, when XNNPACK optimizes the subgraph, it checks the operator’s data type to determine whether a KleidiAI implementation is available. If KleidiAI supports it, XNNPACK bypasses its own default implementation. As a result, RHS packing is performed using the KleidiAI SME packing micro-kernel. Because KleidiAI typically requires packing of the LHS, a flag is also set during this stage.

During model inference, the LHS packing micro-kernel is invoked. After the LHS is packed, XNNPACK performs the matrix multiplication. At this point, the KleidiAI SME micro-kernel is used to compute the matrix product.
