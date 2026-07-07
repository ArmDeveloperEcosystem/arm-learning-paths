---
title: Install Model Gym and explore NFRU examples
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What neural graphics is

Neural graphics is an intersection of graphics and machine learning. Rather than relying purely on traditional GPU pipelines, neural graphics integrates learned models directly into the rendering stack. 

These techniques are particularly powerful on mobile devices, where battery life and performance constraints limit traditional compute-heavy rendering approaches. When developing for mobile devices, your goal is to deliver high visual fidelity without increasing GPU cost. You achieve this by training and deploying compact neural networks optimized for your device's hardware.

## How Arm supports neural graphics

Arm enables neural graphics through the [Neural Graphics Development Kit](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics): a set of open-source tools that you can use to train, evaluate, and deploy ML models for graphics workloads.

At its core are the ML Extensions for Vulkan, which bring native ML inference into the GPU pipeline using structured compute graphs. These extensions (`VK_ARM_tensors` and `VK_ARM_data_graph`) allow real-time upscaling and similar effects to run efficiently alongside rendering tasks.

You can develop neural graphics models using well-known ML frameworks such as PyTorch, then export them for deployment with Arm's hardware-aware pipeline. The workflow converts your model to `.vgf` using the TOSA intermediate representation, making it possible to tailor model development for your game use case. 

In the following sections, you'll focus on Neural Frame Rate Upscaling (NFRU) as the primary example for training, evaluating, and deploying neural models using the [Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym). Arm has also developed a set of Vulkan Samples to help you get started. The `postprocessing_with_vgf` sample introduces the `.vgf` format. 

For a broader overview of neural graphics developer resources, including the Vulkan Samples, see the introductory Learning Path [Get started with neural graphics using ML Extensions for Vulkan](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/).

Arm GPUs are adding dedicated neural accelerators, optimized for low-latency inference in graphics workloads. To help you get started early, Arm provides the ML Emulation Layers for Vulkan that simulate neural accelerator behavior, so you can build and test models now.

## What the Neural Graphics Model Gym is

The Neural Graphics Model Gym is an open-source toolkit for fine-tuning and exporting neural graphics models. It's designed to streamline the entire model lifecycle for graphics-focused use cases such as NFRU.

With Model Gym, you can:

- Train and evaluate models using a PyTorch-based API
- Export models to `.vgf` using ExecuTorch for real-time use in game development
- Take advantage of quantization-aware training (QAT) and post-training quantization (PTQ) with ExecuTorch
- Use an optional Docker setup for reproducibility

You can choose to work with Python notebooks for rapid experimentation or use the command-line interface for automation. You'll run demonstrative notebooks and prepare to start using the CLI for your own model development.

## What you've learned and what's next

You've now learned about neural graphics and Arm's tools such as the Neural Graphics Model Gym that support neural graphics. 

Next, you'll set up your environment and start working with neural graphics models. 
