---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Visualize ML on Embedded Devices

Choosing the right hardware for your machine learning (ML) model starts with the right tools. 

Arm [Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) (FVPs) let you visualize and test model performance early—before any physical hardware is available.

## What is TinyML?

TinyML is machine learning optimized to run on low-power, resource-constrained devices. These models must fit within tight memory and compute budgets, making them ideal for embedded systems.

This Learning Path focuses on using TinyML models with virtualized Arm hardware to simulate real-world AI workloads on microcontrollers and NPUs.

If you're looking to build and train your own TinyML models, check out the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/).

## What is ExecuTorch?

ExecuTorch is a lightweight runtime designed for efficient execution of PyTorch models on resource-constrained devices. It enables machine learning inference on embedded and edge platforms, making it well-suited for Arm-based hardware. Since Arm processors are widely used in mobile, IoT, and embedded applications, ExecuTorch leverages Arm's efficient CPU architectures to deliver optimized performance while maintaining low power consumption. By integrating with Arm's compute libraries, it ensures smooth execution of AI workloads on Arm-powered devices, from Cortex-M microcontrollers to Cortex-A application processors.

ExecuTorch provides:

- Ahead-of-time (AOT) compilation for faster inference

- Delegation of selected operators to accelerators like Ethos-U

- Tight integration with Arm compute libraries

## Why use virtual platforms?

New Arm hardware, such as the [Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) NPU, becomes available on FVPs before physical devices ship. These virtual platforms also include a built-in graphical user interface (GUI) that helps you:

- Confirm your model is executing on the intended virtual hardware  
- Visualize instruction counts  
- Review total execution time  
- Capture clear outputs for demos and prototypes  
