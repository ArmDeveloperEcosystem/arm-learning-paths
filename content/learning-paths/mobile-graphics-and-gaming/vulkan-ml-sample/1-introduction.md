---
title: Run neural graphics workloads with ML Extensions for Vulkan
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is neural graphics, and why does it matter for real-time rendering?

Neural graphics combines real-time rendering with machine learning to improve visual quality and performance. Integrating ML techniques, such as neural upscaling, directly into the GPU pipeline can improve visual fidelity and efficiency. This approach is especially valuable on mobile and embedded devices, where power efficiency is critical.

## How do ML Extensions for Vulkan support neural graphics workloads?

The `VK_ARM_data_graph` and `VK_ARM_tensors` extensions bring structured compute graph execution and tensor processing to the Vulkan API. Their data graph pipelines use SPIR-V-defined graphs to execute ML inference workloads efficiently.

To help developers adopt these features, the Tensor and Data Graph Vulkan Samples offer hands-on demonstrations.

These samples address key challenges in ML integration, such as:

- **Understanding graph-based compute with Vulkan**: See how compute workloads can be structured using explicit graph topologies.
- **Demystifying ML inference in real-time rendering**: Learn how ML fits into the graphics pipeline.

The samples range from basic configurations to more advanced features, such as tensor aliasing and compute shader integration.

This Learning Path walks you through setting up and running the first sample, `simple_tensor_and_data_graph`.

### Why use ML Extensions for Vulkan in game and graphics development?

As a game developer, you've probably noticed the rising demand for smarter, more immersive graphics — but also the increasing strain on GPU resources, especially on mobile. Vulkan's traditional pipelines give you fine-grained control, but finding the right tooling to integrate machine learning has been a challenge. That’s where the new ML extensions for Vulkan come in.

Arm’s `VK_ARM_tensors` and `VK_ARM_data_graph` extensions give you native Vulkan support for executing neural networks on the GPU — using structured tensors and data graph pipelines. Instead of chaining compute shaders to simulate ML models, you can now express them as dataflow graphs in SPIR-V and run them more efficiently. This opens the door to using AI techniques right alongside the graphics pipeline.


Although ML is widely used for image classification and large language models (LLMs), these extensions target game and graphics workloads. They prioritize predictable execution, GPU compatibility, and memory efficiency. Built-in support for tensor formats and pipeline sessions helps you combine traditional Vulkan rendering with machine learning.

Arm provides emulation layers for development on any modern Vulkan-capable hardware, and PyTorch support is available for model conversion workflows.

For an example of real-time upscaling, see the Learning Path [**Neural Super Sampling with Unreal Engine**](/learning-paths/mobile-graphics-and-gaming/nss-unreal/).

With the Vulkan Samples, you can experiment directly with these ideas. Move on to the next section to set up your machine for running the samples.
