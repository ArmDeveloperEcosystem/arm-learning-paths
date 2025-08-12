---
title: Use RenderDoc to debug and analyze workloads
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Debug and profile workloads with RenderDoc


Integrating machine learning into real-time rendering makes frame-level inspection and performance analysis critical. RenderDoc helps you visualize and debug the workloads by letting you step through frames, examine tensors, and inspect Vulkan API calls.

RenderDoc is a powerful GPU frame capture tool that lets you:

- Step through a frame’s rendering process
- Inspect Vulkan API calls
- View shader inputs and outputs
- Examine GPU resource states and memory usage

## When to use RenderDoc with the samples

RenderDoc can help in scenarios such as:

- Diagnosing unexpected visual output by stepping through draw calls
- Analyzing the order and behavior of Vulkan API calls
- Investigating memory consumption or GPU resource state
- Validating execution of data graph pipelines or identifying sync issues

## Installing Arm Performance Studio (includes RenderDoc)

To use RenderDoc with ML extensions, install the Arm-customized version via Performance Studio:

1. **Download Arm Performance Studio** from the [Arm Developer website](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads). The minimum version to use is `2025.4`
2. Run the installer:
   `Arm_Performance_Studio_<version>_windows_x86-64.exe`
3. Follow the installation instructions.

Once installed, launch RenderDoc for Arm GPUs via the Windows Start menu.

## Capture Vulkan frames with RenderDoc

You can capture and inspect Vulkan Samples that use ML extensions for Vulkan, including API calls such as `vkCreateTensorARM` and structures like `VK_STRUCTURE_TYPE_TENSOR_DESCRIPTION_ARM`.

RenderDoc is especially useful for visualizing tensor operations, inspecting resource bindings, and verifying correct data graph pipeline execution.

## Capture with RenderDoc

1. **Open RenderDoc**, and in the main window, go to the **Launch Application** section.
2. Configure the following fields:
   - **Executable Path**: Path to the built executable `vulkan_samples.exe`.
   - **Working Directory**: Path to the root of the Vulkan Samples project.
   - **Command-line Arguments**:
     ```
     sample simple_tensor_and_data_graph
     ```
     You can substitute `simple_tensor_and_data_graph` with any of the other sample names as needed.
3. Click **Launch**. The selected sample will start running.
4. Once the application window is active, press **F12** to capture a frame.
5. After the frame is captured, it will appear in RenderDoc’s capture list. Double-click it to explore the captured frame and inspect ML extensions for Vulkan calls in detail.

## Learn more

This workflow enables close inspection of how ML graphs are built and executed within Vulkan — an essential tool when optimizing pipelines or debugging integration issues. If you want to learn more about RenderDoc for Arm GPUs, you can check out the [Debug With RenderDoc User Guide](https://developer.arm.com/documentation/109669/latest).

Move on to the next section to review further resources on what is new, and what is coming.