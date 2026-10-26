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
- Investigating memory consumption or GPU resource states
- Validating data graph pipeline execution or identifying synchronization issues

## Install Arm Performance Studio

To use RenderDoc with ML Extensions for Vulkan, install the Arm-customized version included with Arm Performance Studio:

1. **Download Arm Performance Studio** from the [Arm Developer website](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads). Use version 2025.4 or later.
2. Run the installer:
   `Arm_Performance_Studio_<version>_windows_x86-64.exe`
3. Follow the installation instructions.

After installation, launch RenderDoc for Arm GPUs from the Windows Start menu.

## Capture Vulkan frames with RenderDoc

You can capture and inspect Vulkan Samples that use ML Extensions for Vulkan, including API calls such as `vkCreateTensorARM` and structures such as `VK_STRUCTURE_TYPE_TENSOR_DESCRIPTION_ARM`.

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
3. Select **Launch**. The selected sample starts running.
4. When the application window is active, press **F12** to capture a frame.
5. The captured frame appears in RenderDoc's capture list. Double-click it to explore the frame and inspect ML Extensions for Vulkan calls in detail.

## Learn more

This workflow gives you a detailed view of how Vulkan builds and executes ML graphs when you optimize pipelines or debug integration issues. To learn more, see the [Debug with RenderDoc User Guide](https://developer.arm.com/documentation/109669/latest).

Continue to the final section to review what you've learned and explore additional resources.
