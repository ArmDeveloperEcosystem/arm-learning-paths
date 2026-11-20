---
title: Understand ML Drift
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Explore GPU compute with ML Drift

ML Drift is Google's open-source GPU compute engine for on-device AI and ML inference. It powers GPU acceleration in LiteRT and is available as a standalone library for custom graphics and inference runtimes. Its unified shaders separate computation from how data is stored and accessed through currently supported GPU APIs: OpenCL, Metal, WebGPU, and OpenGL ES 3.1 or later. ML Drift generates GPU-specific shader code at runtime, when preparing a workload for execution. This helps you share shader logic across supported platforms while retaining hardware-specific performance optimizations.

Application developers can use ML Drift through LiteRT's GPU accelerator without writing shaders. For custom graphics and inference runtimes, you can use ML Drift's standalone C++ APIs to assemble and run GPU workloads. When you need custom computations, you can write portable shaders in ML Drift's Unified Compute Language (UCL). This Learning Path uses the OpenCL backend to run an existing workload on an Android device with an Arm Mali GPU.

One example is the [Mali-specific tuning within ML Drift's general convolution implementation](https://github.com/google-ai-edge/ml-drift/blob/main/ml_drift/common/kernels/conv_generic.cc#L3007). Convolution applies filters to input data, a common operation in image-processing models. ML Drift adjusts how this work is divided across the GPU according to the GPU generation and workload. When you use this built-in operation, ML Drift applies these settings internally; you don't need to select them or write separate shaders for each GPU.

You'll build the standalone Stable Diffusion command-line example, inspect one of its unified shaders, and profile execution on an Arm Mali GPU. You won't need a LiteRT application or changes to the ML Drift source.

You now know where standalone ML Drift fits. Next, prepare your host tools and device connection.
