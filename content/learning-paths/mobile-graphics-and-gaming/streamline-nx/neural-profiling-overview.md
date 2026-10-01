---
title: Understand NX, Streamline, and Project Moku
description: Understand the hardware and driver requirements for profiling an Android neural graphics workload with Streamline.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What NX adds to an Arm GPU

NX provides dedicated neural acceleration within supported Arm GPUs. An ML graph can contain work mapped to NX and work implemented as compute shaders on the GPU’s shader cores.

Arm ML Extensions for Vulkan, including `VK_ARM_tensors` and `VK_ARM_data_graph`, let applications describe tensor data and dispatch ML graphs through Vulkan. A graph dispatch can execute work on both NX and shader cores. The compiler maps graph operations to these execution engines according to the operations, tensor data types and shapes, and capabilities of the target GPU and driver

Neural graphics techniques use these capabilities within a rendering pipeline. Neural Super Sampling (NSS) reconstructs an image from a lower-resolution input. Neural Frame Rate Upscaling (NFRU) generates intermediate frames between rendered frames. For a broader set of potential use cases, see the [Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/).

## What Streamline shows you

Arm Streamline is a performance analyzer included in Arm Performance Studio. It brings CPU activity, GPU counters, and timeline events into a capture that you can inspect in its graphical interface.
For NX workloads, you'll use two complementary views:

| View | Question it helps you answer |
| --- | --- |
| Mali Timeline | When was a graph submitted and executed, and how did it overlap with other GPU work? |
| Dispatch Graph Workloads: Mali Timeline | Which graph operations took time, and which ran on NX or shader cores? |

Counters summarize activity over sampling intervals. Events describe work along a timeline. NX statistics add detail about neural execution. Reading these together helps you choose an operation to investigate without mistaking a busy interval for proof of a bottleneck.

## Example Workload: Project Moku

Project Moku is an Unreal Engine sample project developed by Arm that demonstrates neural rendering technologies for mobile platforms. It provides a controlled environment for testing Neural Frame Rate Upscaling (NFRU) and complementary neural rendering techniques, and is designed to exercise dedicated neural accelerators on GPUs with built-in neural processing support. For more context, see [the introduction to Project Moku](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/1-introduction_to_moku/).

This Learning Path uses Moku's NFRU configuration as a representative workload to collect a 30-second Streamline profile. **However, you will need to replace Moku with your own debuggable application that uses the ML extensions for Vulkan on supported hardware**. The [Arm ML SDK for Vulkan](https://github.com/arm/ai-ml-sdk-for-vulkan) provides tools and documentation for developing applications with these extensions.


For details about the sample and frame generation, see [Analyze Neural Frame Rate Upscaling using Project Moku](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/).

{{% notice Note %}}

Project Moku is running on a [Xiaomi 18 Fold](https://www.mi.com/global/discover/article?id=6357) with a [Mali G2-Ultra NX GPU](https://www.arm.com/products/silicon-ip-multimedia/gpu/mali-g2-ultra-nx). The device display is streamed to the local machine using [`scrcpy`](https://github.com/genymobile/scrcpy).

![Project Moku showing a robot in a red-lit science-fiction corridor in a scrcpy window, with the Content_SM5_NFRU device profile displayed in the debug overlay#center](./images/moku-screenshot.png "Project Moku's CorridorV2 scene running in Unreal Engine 5.6, with NFRU enabled in a debug build.")

{{% /notice %}}

## What you've learned and what's next

You now know how NX, shader execution, and Vulkan graph dispatches relate to the two Streamline views. You also know how the device hardware and supplied driver affect the available profiling features.

Next, [prepare the tools, device, and your workload](../prepare-tools-and-device/).
