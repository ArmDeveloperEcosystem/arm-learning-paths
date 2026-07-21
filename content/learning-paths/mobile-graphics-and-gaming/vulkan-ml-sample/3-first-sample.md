---
title: Simple Tensor and Data Graph
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand how the Simple Tensor and Data Graph sample works

The **Simple Tensor and Data Graph** sample is a starting point for working with ML Extensions for Vulkan. It demonstrates how to execute a simple neural network with a data graph pipeline, specifically a 2D average pooling operation.

## Clone the Vulkan Samples

With the environment set up, clone the sample code from the Khronos Group repository:

```bash
git clone --recurse-submodules https://github.com/KhronosGroup/Vulkan-Samples.git
cd Vulkan-Samples
```

The repository includes the framework and samples that demonstrate ML Extensions for Vulkan.

## Build the Vulkan Samples

You're now ready to compile the project.

{{% notice Note %}}
Enable [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode) before running the commands to avoid permission issues.
{{% /notice %}}

Generate Visual Studio project files using CMake:

```bash
cmake -G "Visual Studio 17 2022" -A x64 -S . -Bbuild/windows
```

Compile the `vulkan_samples` target in Release mode:

```bash
cmake --build build/windows --config Release --target vulkan_samples
```

## Run the Simple Tensor and Data Graph sample

Run the built executable using the following command:

```bash
build\windows\app\bin\Release\AMD64\vulkan_samples.exe sample simple_tensor_and_data_graph
```

A new window opens and visualizes the operation. The sample uses a minimal Vulkan application to create a data graph pipeline that processes a small neural network.

The sample creates input and output tensors, binds them with descriptor sets and pipeline layouts, and supplies a SPIR-V module that defines the network operation. It then records and dispatches commands to execute the pipeline and visualize the results in real time. For implementation details, see the [Simple Tensor and Data Graph documentation](https://arm-software.github.io/Vulkan-Samples/samples/extensions/tensor_and_data_graph/simple_tensor_and_data_graph/README.html).

## Summary and next steps

By running this sample, you've stepped through a complete Vulkan data graph pipeline powered by ML Extensions for Vulkan. You've created tensors, set up descriptors, built a SPIR-V-encoded ML graph, and dispatched inference without custom shaders. This workflow provides a foundation for neural graphics and extends to more complex graphics scenarios.

You can also explore the remaining data graph pipeline samples. Each sample's documentation is in its directory under `samples/extensions/tensor_and_data_graph/`.

## Overview of additional samples

| Sample name                      | Description                                                                                  | Focus area                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------|
| **Graph Constants**              | Shows how to add constants, such as weights and biases, to the data graph pipeline using tensors | Constant tensor injection           |
| **Compute Shaders with Tensors** | Demonstrates how to feed tensor data into or out of data graph pipelines using compute shaders   | Shader interoperability      |
| **Tensor Image Aliasing**      | Demonstrates tensor aliasing with Vulkan images to enable zero-copy workflows                  | Memory-efficient data sharing |
| **Postprocessing with VGF**      | Explores how a VGF file packages SPIR-V with input, output, and constant data for a data graph pipeline | Neural network model     |

Next, you'll review additional tools for working with ML Extensions for Vulkan in your development environment.
