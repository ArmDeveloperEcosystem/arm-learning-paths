---
title: Run neural graphics workloads with ML Extensions for Vulkan
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is neural graphics, and why does it matter for real-time rendering?

Neural graphics combines real-time rendering with the power of machine learning to enhance visual quality and performance. By integrating ML techniques like neural upscaling directly into the GPU pipeline, developers can achieve next-gen fidelity and efficiency. This is especially valuable on mobile and embedded devices, where power efficiency is critical.

## How do ML Extensions for Vulkan support neural graphics workloads?

Vulkan's data graph pipelines, introduced through the `VK_ARM_data_graph` and `VK_ARM_tensors` extensions, bring structured compute graph execution to the Vulkan API by introducing support for processing tensors. These pipelines are designed to execute ML inference workloads efficiently using SPIR-V-defined graphs.

To help developers adopt these features, the Tensor and Data Graph Vulkan Samples offer hands-on demonstrations.

These samples address key challenges in ML integration, such as:

- **Understanding graph-based compute with Vulkan**: See how compute workloads can be structured using explicit graph topologies.
- **Demystifying ML inference in real-time rendering**: Learn how ML fits into the graphics pipeline.

Samples range from basic setups to more advanced features like tensor aliasing and compute shader integration.

This Learning Path walks you through setting up and running the first sample, `simple_tensor_and_data_graph`.


### Why use ML Extensions for Vulkan for game and graphics development?

As a game developer, you've probably noticed the rising demand for smarter, more immersive graphics — but also the increasing strain on GPU resources, especially on mobile. Vulkan's traditional pipelines give you fine-grained control, but finding the right tooling to integrate machine learning has been a challenge. That’s where the new ML extensions for Vulkan come in.

Arm’s `VK_ARM_tensors` and `VK_ARM_data_graph` extensions give you native Vulkan support for executing neural networks on the GPU — using structured tensors and data graph pipelines. Instead of chaining compute shaders to simulate ML models, you can now express them as dataflow graphs in SPIR-V and run them more efficiently. This opens the door to using AI techniques right alongside the graphics pipeline.

And while ML has found success in image classification and LLMs, these extensions are designed from the ground up for gaming and graphics workloads — prioritizing predictable execution, GPU compatibility, and memory efficiency. With built-in support for tensor formats and pipeline sessions, the extensions are optimized for developers looking to blend traditional rendering with machine learning on Vulkan.

Arm provides emulation layers for development on any modern Vulkan-capable hardware, and PyTorch support is available for model conversion workflows.

For an example of real-time upscaling, see the Learning Path [**Neural Super Sampling with Unreal Engine**](/learning-paths/mobile-graphics-and-gaming/nss-unreal/).

With the Vulkan Samples, you can experiment directly with these ideas. Move on to the next section to set up your machine for running the samples.
