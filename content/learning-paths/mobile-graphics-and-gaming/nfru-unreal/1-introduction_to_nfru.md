---
title: Understand neural graphics and Neural Framerate Upscaling (NFRU)
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What the Neural Graphics Development Kit is

The Neural Graphics Development Kit is a collection of tools and resources from Arm that helps you integrate AI-driven graphics techniques into mobile applications and games. The kit includes Unreal Engine plugins, Arm ML extensions for Vulkan, open neural network models, and development utilities to support neural rendering features such as Neural Super Sampling (NSS) and Neural Frame Rate Upscaling (NFRU).

By enabling neural network inference directly in the graphics pipeline, the kit lets you explore how AI can enhance image quality and performance.

## What Neural Frame Rate Upscaling is

Neural Frame Rate Upscaling (NFRU) is a deep learning–based technique that increases the perceived frame rate in real-time applications such as games. Instead of rendering every frame, NFRU uses a neural network to generate intermediate frames between rendered ones. The technique relies on motion information such as optical flow or motion vectors to predict pixel movement.

NFRU delivers smoother motion and higher frame rates — often doubling the display rate—without requiring the GPU to render additional full frames. As a result, you gain improved performance and efficiency on mobile devices, with predictable frame pacing due to a fixed additional frame of latency.

NFRU integrates with the Unreal Engine rendering pipeline, using motion vectors and previous frame data to synthesize extra frames. Through Arm ML extensions for Vulkan, neural network inference runs efficiently on neural-accelerated hardware, allowing you to render fewer frames while maintaining smooth motion and consistent pacing in real-time graphics workloads.

## What you've learned and what's next

You've learned what the Neural Graphics Development Kit and NFRU are.

Next, you'll set up the development environment to use NFRU with Unreal Engine. This includes installing dependencies, configuring your project, and enabling the NFRU plugin. After setup, you'll be ready to run and evaluate NFRU within the Unreal Engine rendering pipeline.
