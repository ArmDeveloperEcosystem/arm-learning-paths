---
title: Simple Tensor and Data Graph
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand how the Simple Tensor and Data Graph sample works

The **Simple Tensor and Data Graph** sample is your starting point for working with the ML extensions for Vulkan. It demonstrates how to execute a simple neural network using a data graph pipeline — specifically, a 2D average pooling operation.

## Clone the Vulkan Samples

With the environment set up, you can now grab the sample code. These examples are maintained in a fork of the Khronos Group's repository.

```bash
git clone --recurse-submodules https://github.com/ARM-software/Vulkan-Samples --branch tensor_and_data_graph
cd Vulkan-Samples
```

This repository includes the framework and samples showcasing the ML extensions for Vulkan.

## Build the Vulkan Samples

You're now ready to compile the project. From the root of the repository:

{{% notice Note %}}
Be sure to run the commands in [Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode) to avoid permission issues.
{{% /notice %}}

Generate Visual Studio project files using CMake:
```bash
cmake -G "Visual Studio 17 2022" -A x64 -S . -Bbuild/windows
```
Finally, compile the `vulkan_samples` target in Release mode:

```bash
cmake --build build/windows --config Release --target vulkan_samples
```
## Run the Simple Tensor and Data Graph sample

Run the built executable using the following command:

```bash
build\windows\app\bin\Release\AMD64\vulkan_samples.exe sample simple_tensor_and_data_graph
```

This should open a new window visualizing the operation. In this sample, a minimal Vulkan application sets up a data graph pipeline configured to process a small neural network.

The sample creates input and output tensors, binds them using descriptor sets and pipeline layouts, and supplies a SPIR-V module that defines the network operation. Finally, it records and dispatches commands to execute the pipeline — and visualizes the results in real time. More details about what's going on under the hood can be found in the [documentation](https://arm-software.github.io/Vulkan-Samples/samples/extensions/tensor_and_data_graph/simple_tensor_and_data_graph/README.html).

## Summary and next steps

By running this sample, you’ve stepped through a complete Vulkan data graph pipeline powered by the ML extensions for Vulkan. You’ve created tensors, set up descriptors, built a SPIR-V-encoded ML graph, and dispatched inference — all without needing custom shaders. This sets the foundation for neural graphics. As you explore the remaining samples, you’ll see how this core pattern extends into real-world graphics scenarios.

As a next step, you can explore the remaining samples for the data graph pipeline. The documentation sits in each sample's directory, available under `samples/extensions/tensor_and_data_graph/` in the repository.

## Overview of Additional Samples

| Sample Name                      | Description                                                                                  | Focus Area                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------|
| **Graph Constants**              | Shows how to include constants like weights and biases into the data graph pipeline using tensors| Constant tensor injection           |
| **Compute Shaders with Tensors** | Demonstrates how to feed tensor data into or out of data graph pipelines using compute shaders   | Shader interoperability      |
| **Tensor Image Aliasing**      | Demonstrates tensor aliasing with Vulkan images to enable zero-copy workflows                  | Memory-efficient data sharing |
| **Postprocessing with VGF**      | Explores using VGF format, which contains SPIR-V, input, output and constant data used to run a data graph pipeline.   | Neural network model     |

Next, you'll review additional tools to help you work with ML extensions for Vulkan in your own development environment.