---
title: Install Model Gym and Explore Neural Graphics Examples
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Neural Graphics?

Neural graphics is an intersection of graphics and machine learning. Rather than relying purely on traditional GPU pipelines, neural graphics integrates learned models directly into the rendering stack. The techniques are particularly powerful on mobile devices, where battery life and performance constraints limit traditional compute-heavy rendering approaches. The goal is to deliver high visual fidelity without increasing GPU cost. This is achieved by training and deploying compact neural networks optimized for the device's hardware.

## How does Arm support neural graphics?

Arm enables neural graphics through the [**Neural Graphics Development Kit**](https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics): a set of open-source tools that let developers train, evaluate, and deploy ML models for graphics workloads.

At its core are the ML Extensions for Vulkan, which bring native ML inference into the GPU pipeline using structured compute graphs. These extensions (`VK_ARM_tensors` and `VK_ARM_data_graph`) allow real-time upscaling and similar effects to run efficiently alongside rendering tasks.

The neural graphics models can be developed using well-known ML frameworks like PyTorch, and exported to deployment using Arm's hardware-aware pipeline. The workflow converts the model to `.vgf` via the TOSA intermediate representation, making it possible to do tailored model development for you game use-case. This Learning Path focuses on **Neural Super Sampling (NSS)** as the use case for training, evaluating, and deploying neural models using a toolkit called the [**Neural Graphics Model Gym**](https://github.com/arm/neural-graphics-model-gym). To learn more about NSS, you can check out the [resources on Hugging Face](https://huggingface.co/Arm/neural-super-sampling). Additonally, Arm has developed a set of Vulkan Samples to get started. Specifically, `.vgf` format is introduced in the `postprocessing_with_vgf` one. The Vulkan Samples and over-all developer resources for neural graphics is covered in the [introductory Learning Path](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample).

Starting in 2026, Arm GPUs will feature dedicated neural accelerators, optimized for low-latency inference in graphics workloads. To help developers get started early, Arm provides the ML Emulation Layers for Vulkan that simulate future hardware behavior, so you can build and test models now.

## What is the Neural Graphics Model Gym?

The Neural Graphics Model Gym is an open-source toolkit for fine-tuning and exporting neural graphics models. It is designed to streamline the entire model lifecycle for graphics-focused use cases, like NSS.

Model Gym gives you:

- A training and evaluation API built on PyTorch
- Model export to .vgf using ExecuTorch for real-time use in game development
- Support for quantization-aware training (QAT) and post-training quantization (PTQ) using ExecuTorch
- Optional Docker setup for reproducibility

The toolkit supports workflows via both Python notebooks (for rapid experimentation) and command-line interface. This Learning Path will walk you through the demonstrative notebooks, and prepare you to start using the CLI for your own model development.
