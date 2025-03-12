---
title: What is Arm Accuracy Super Resolution?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

[Arm&reg; Accuracy Super Resolution™ (ASR)](https://www.arm.com/developer-hub/mobile-graphics-and-gaming/accuracy-super-resolution) is a mobile-optimized temporal upscaling technique derived from [AMD's Fidelity Super Resolution 2 v2.2.2](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK/blob/main/docs/techniques/super-resolution-temporal.md). Arm ASR extends this technology with multiple optimizations to make the technique suited for the more resource-constrained environment of mobile gaming.

With an Unreal Engine plug-in available now, open-source library code to integrate into your customized engines, and Unity and Godot plug-ins coming later in the year, you can easily improve frames per second, enhance visual quality, and prevent thermal throttling for smoother, longer gameplay.

## What is Super Resolution?

Super-resolution techniques render some frames at a lower resolution and use shader upscaling to reconstruct how the frames should look at native resolution. This offers significant performance and battery life improvements for mobile devices.

Arm ASR outperforms spatial upscalers when reconstructing fine details, such as:

- Thin features
- Grid-like structures
- Fast-moving objects

You can control a range of different settings for Arm ASR:

- The upscaling ratio. For example, a value of 50.0 will mean that the plugin upscales frames by a factor of 2.
- Use Arm ASR’s own auto-exposure or use the game engine’s auto-exposure value.
- Use a Robust Contrast Adaptive Sharpening (RCAS) filter to sharpen the output image.
- The shader quality preset: 1 - Quality, 2 - Balanced, 3 - Performance.

## Overview of Arm ASR

The [Arm ASR experience kit](https://github.com/arm/accuracy-super-resolution) is a combination of materials that provide access to the technology, to help you evaluate it and make the best use of it. It includes:

- The Arm ASR source code so developers can access it fully and even evolve the technology for their needs.
- Tutorials and sample materials to help developers with the integration of the technology and how to use it.
- Plugins for multiple game engines

Specific repositories for each game engine integration is also available. The following sections will cover those currently available.

## Unreal Engine Plugin

The Unreal Engine 5 plugin can be integrated into your project in a matter of minutes. Once installed, simply enable temporal upscaling on your project and the plugin will automatically handle the upscaling of all frames.

[Using Arm ASR in Unreal Engine](../03-ue)

## Custom engine usage

If you are using your own custom engine, you can still integrate Arm ASR using our open-source reference library.

[Using Arm ASR in a custom engine with the Universal SDK](../04-universal-sdk)
