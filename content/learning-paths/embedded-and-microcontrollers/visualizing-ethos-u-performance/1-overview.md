---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Visualize ML on Embedded Devices

Choosing the right hardware for your machine learning (ML) model starts with having the right tools. In many cases, you need to test and iterate on software before the target hardware is even available,especially when working with cutting-edge accelerators like the Ethos-U NPU. 

Arm [Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) (FVPs) let you visualize and test model performance before any physical hardware is available.

## What is TinyML?

TinyML is machine learning optimized to run on low-power, resource-constrained devices such as Arm Cortex-M microcontrollers and NPUs like the Ethos-U. These models must fit within tight memory and compute budgets, making them ideal for embedded systems.

This Learning Path focuses on using TinyML models with virtualized Arm hardware to simulate real-world AI workloads on microcontrollers and NPUs.

If you're looking to build and train your own TinyML models, check out the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/).

## What is ExecuTorch?

ExecuTorch is a lightweight runtime for executing PyTorch models on embedded and edge devices. It supports efficient model inference on a range of Arm processors, ranging from Cortex-M CPUs to Ethos-U NPUs, with support for hybrid CPU+accelerator execution.

ExecuTorch provides:

- Ahead-of-time (AOT) compilation for faster inference
- Delegation of selected operators to accelerators like Ethos-U
- Tight integration with Arm compute libraries

## Why use virtual platforms?

Arm Fixed Virtual Platforms (FVPs) are virtual hardware models used to simulate Arm-based systems like the Corstone-320. They allow developers to validate and tune software before silicon is available, which is especially important when targeting newly-released accelerators like the [Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) NPU.

These virtual platforms also include a built-in graphical user interface (GUI) that helps you:

- Confirm your model is executing on the intended virtual hardware  
- Visualize instruction counts  
- Review total execution time  
- Capture clear outputs for demos and prototypes  
