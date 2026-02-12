---
title: What is Arm Accuracy Super Resolution?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

[Arm&reg; Accuracy Super Resolution™ (Arm ASR)](https://www.arm.com/developer-hub/mobile-graphics-and-gaming/arm-accuracy-super-resolution) is a mobile-optimized temporal upscaling technique derived from [AMD's Fidelity Super Resolution 2 v2.2.2](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK/blob/main/docs/samples/super-resolution.md). 

Arm ASR extends this technology with optimizations suited to the resource-constrained environment of mobile gaming.

Arm ASR is currently available as an easy-to-integrate plug-in for Unreal Engine versions 5.3, 5.4, and 5.5, with a Unity plugin coming soon. It is also available as a generic library that you can integrate into other engines.

Using ASR, you can improve frames per second (FPS), enhance visual quality, and prevent thermal throttling for smoother and longer gameplay.

## What is Super Resolution?

Super Resolution techniques render frames at a lower resolution and apply shader-based upscaling to reconstruct how the frames should look at native resolution. This approach significantly improves performance and extends battery life on mobile devices.

Arm ASR outperforms spatial upscalers when reconstructing fine details, such as:

- Thin features.
- Grid-like structures.
- Fast-moving objects.

You have control over a range of different settings, including:

- **The upscaling ratio**. For example, a value of 50.0 indicates that the plugin upscales frames by a factor of 2.
- **Auto-exposure**. Use Arm ASR's own auto-exposure or use your game engine's auto-exposure value.
- **Sharpening**. Apply Robust Contrast Adaptive Sharpening (RCAS) filters to enhance output image clarity.
- **Shader quality presets**. Select from: 1 - Quality, 2 - Balanced, or 3 - Performance presets.

## Overview of Arm ASR

The [Arm ASR Experience Kit](https://github.com/arm/accuracy-super-resolution) provides resources to help you evaluate and effectively utilize this technology.

It includes:

- Arm ASR source code, which provides developers with the full access and the flexibility to evolve the technology for their needs.
- Tutorials and sample materials to simplify integration and usage.
- Plugin support for Unreal Engine.

## Unreal Engine Plugin

The Arm ASR plugin for Unreal Engine 5 integrates into your project within minutes. Once installed, simply enable temporal upscaling, and the plugin automatically handles frame upscaling.

The plugin for Unreal Engine is available in the [Fab store](https://www.fab.com/listings/9a75a41d-6fad-44c3-995f-646f62cd2512).

To set it up from source, proceed to [Using Arm ASR in Unreal Engine](../02-ue).

## Custom Engine Usage

If you are using your own custom engine, integrate Arm ASR using our generic library.

See [Using Arm ASR in a custom engine](../04-generic_library).
