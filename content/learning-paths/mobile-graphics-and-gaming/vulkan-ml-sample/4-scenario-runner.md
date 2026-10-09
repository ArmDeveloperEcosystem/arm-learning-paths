---
title: Running a test with the Scenario Runner
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

You'll learn how to run a complete inference test with the **Scenario Runner** from Arm's ML SDK for Vulkan. You'll also explore the downloadable binaries and assets on Arm's Hugging Face page that demonstrate ML Extensions for Vulkan.

## About the ML SDK for Vulkan

The SDK provides tools and runtime components that help you integrate neural networks into Vulkan-based applications. ML Extensions for Vulkan (`VK_ARM_data_graph` and `VK_ARM_tensors`) define the runtime interface. The SDK provides a workflow for converting, packaging, and deploying ML models in real-time applications such as games.

### SDK component summary

| Component        | Description                                                                                          | Usage context                       | GitHub link |
|------------------|------------------------------------------------------------------------------------------------------|-------------------------------------|--------------|
| **Model Converter** | Converts TOSA IR into SPIR-V graphs and packages them into `.vgf` files for runtime execution.      | Deploy models through asset pipelines | https://github.com/arm/ai-ml-sdk-model-converter |
| **VGF Library**      | Lightweight runtime decoder for `.vgf` files containing graphs, constants, and shaders.              | Load and use graphs in a game engine | https://github.com/arm/ai-ml-sdk-vgf-library |
| **Scenario Runner** | Executes ML workloads declaratively using JSON-based scenario descriptions.                         | Prototype and validate workloads | https://github.com/arm/ai-ml-sdk-scenario-runner |
| **Emulation Layer** | Vulkan layer that emulates data graph and tensor extensions using compute shaders.                      | Test on devices without native support for ML Extensions for Vulkan | https://github.com/arm/ai-ml-emulation-layer-for-vulkan |


## About the Hugging Face release

The [NSS model page on Hugging Face](https://huggingface.co/Arm/neural-super-sampling) provides a minimal example, called a *scenario*, for running NSS on a sample frame. It includes a Windows-compatible Scenario Runner binary, the VGF model, and one frame of input and expected output data. You can use these assets to run an end-to-end workflow and explore the VGF model in more detail.

## Next steps

Next, you'll use RenderDoc to debug and inspect the workloads in this Learning Path.
