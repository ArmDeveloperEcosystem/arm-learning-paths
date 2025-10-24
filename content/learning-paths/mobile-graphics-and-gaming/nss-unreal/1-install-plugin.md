---
title: Introduction to neural graphics and Neural Super Sampling (NSS)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is the Neural Graphics Development Kit?

The Neural Graphics Development Kit empowers game developers to build immersive mobile gaming experiences using a neural accelerator for post-processing effects like upscaling. By combining Unreal Engine and the ML extensions for Vulkan, these tools allow you to integrate and evaluate AI-based upscaling technologies like Neural Super Sampling (NSS). This Learning Path walks you through the setup and execution of NSS for Unreal Engine.

## What is Neural Super Sampling?

NSS is an upscaling technology from Arm, purpose-built for real-time performance and power efficiency on mobile and embedded platforms.

It uses a compact neural network to:
- Upscale low-resolution frames into high-resolution visuals
- Incorporate temporal data such as motion vectors, depth, and feedback
- Reduce bandwidth usage and GPU load

Powered by the ML extensions for Vulkan, this new technology delivers smooth, crisp image quality, optimized for **mobile-class hardware** with a **Neural Accelerator** (NX). You’ll be able to render frames at a lower resolution and then upscale them using the technology, which helps you achieve higher frame rates without compromising the visual experience. This is especially useful on mobile, handheld, or thermally limited platforms, where battery life and thermal headroom are critical. It can also deliver improved image quality compared to other upsampling techniques, like spatio-temporal implementations.

Under the hood, Neural Super Sampling for Unreal Engine (NSS for UE) runs its neural inference through Vulkan using **ML extensions for Vulkan**, which bring machine learning workloads into the graphics pipeline. The Development Kit includes **emulation layers** that simulate the behavior of the extensions on Vulkan compute capable GPUs. These layers allow you to test and iterate without requiring access to NX hardware.

## Neural Upscaling in Unreal Engine

With these resources, you can seamlessly integrate NSS into any Unreal Engine project. The setup is designed to work with Vulkan as your rendering backend, and you don’t need to overhaul your workflow - just plug it in and start leveraging ML-powered upscaling right away. The technology is available as a source-code implementation that you will build with Visual Studio.

## Download required artifacts

Before you begin, download the required plugins and dependencies. These two repositories contain everything you need to set up NSS for Unreal Engine, including the VGF model file, and the ML Emulations Layers for Vulkan.

### 1. Download the NSS plugin

[**Neural Super Sampling Unreal Engine Plugin** → GitHub Repository](https://github.com/arm/neural-graphics-for-unreal)

Download the latest release package and extract it on your Windows machine. Use the folder corresponding to your Unreal version.


### 2. Download the runtime for ML Extensions for Vulkan
[**Unreal NNE Runtime RDG for ML Extensions for Vulkan** → GitHub Repository](https://github.com/arm/ml-extensions-for-vulkan-unreal-plugin).

Download and extract the release package on your Windows machine.

Once you’ve extracted both repositories, proceed to the next section to set up your development environment and enable the NSS plugin.