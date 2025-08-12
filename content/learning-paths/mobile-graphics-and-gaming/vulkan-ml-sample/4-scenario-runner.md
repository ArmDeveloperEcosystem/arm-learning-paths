---
title: Running a test with the Scenario Runner
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you’ll explore how to run a complete inference test using the **Scenario Runner** from Arm’s ML SDK for Vulkan. You’ll also learn what’s provided on Arm’s Hugging Face page, including downloadable binaries and assets that demonstrate the ML extensions for Vulkan in action.

## About the ML SDK for Vulkan

The SDK provides a collection of tools and runtime components that help you integrate neural networks into Vulkan-based applications. While the ML extensions for Vulkan (`VK_ARM_data_graph` and `VK_ARM_tensors`) define the runtime interface, the SDK provides a practical workflow for converting, packaging, and deploying ML models in real-time applications such as games.

### SDK Component Summary

| Component        | Description                                                                                          | Usage Context                       | GitHub link
|------------------|------------------------------------------------------------------------------------------------------|-------------------------------------|--------------|
| **Model Converter** | Converts TOSA IR into SPIR-V graphs and packages them into `.vgf` files for runtime execution.      | Used in asset pipelines for model deployment | https://github.com/arm/ai-ml-sdk-model-converter |
| **VGF Library**      | Lightweight runtime decoder for `.vgf` files containing graphs, constants, and shaders.              | Integrate into game engine to load/use graphs | https://github.com/arm/ai-ml-sdk-vgf-library |
| **Scenario Runner** | Executes ML workloads declaratively using JSON-based scenario descriptions.                         | Ideal for rapid prototyping and validation | https://github.com/arm/ai-ml-sdk-scenario-runner |
| **Emulation Layer** | Vulkan layer that emulates data graph and tensor extensions using compute shaders.                      | For testing on devices without native ML extensions for Vulkan support | https://github.com/arm/ai-ml-emulation-layer-for-vulkan |


## About the Hugging Face release

Visit the [NSS model page on Hugging Face](https://huggingface.co/Arm/neural-super-sampling)

The landing page contains a minimal example - a _scenario_ - to run NSS with an actual frame. It contains a Windows-compatible Scenario Runner binary, the VGF model, and a single frame of input and expected output data. This allows you to run an end-to-end flow, and the landing page provides resources to explore the VGF model in more detail.

## Next steps

In the following section, you’ll explore how to debug and inspect the workloads in this Learning Path using RenderDoc.
