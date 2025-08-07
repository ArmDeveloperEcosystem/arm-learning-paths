---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Simulate and evaluate TinyML performance on Arm virtual hardware

In this section, you’ll learn how TinyML, ExecuTorch, and Arm Fixed Virtual Platforms work together to simulate embedded AI workloads before hardware is available.

Choosing the right hardware for your machine learning (ML) model starts with having the right tools. In many cases, you need to test and iterate before your target hardware is even available, especially when working with cutting-edge accelerators like the Ethos-U NPU.

Arm [Fixed Virtual Platforms](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) (FVPs) let you visualize and test model performance before any physical hardware is available.

 By simulating hardware behavior at the system level, FVPs allow you to:

- Benchmark inference speed and measure operator-level performance
- Identify which operations are delegated to the NPU and which execute on the CPU
- Validate end-to-end integration between components like ExecuTorch and Arm NN
- Iterate faster by debugging and optimizing your workload without relying on hardware

This makes FVPs a crucial tool for embedded ML workflows where precision, portability, and early validation matter.

## What is TinyML?

TinyML is machine learning optimized to run on low-power, resource-constrained devices such as Arm Cortex-M microcontrollers and NPUs like the Ethos-U. These models must fit within tight memory and compute budgets, making them ideal for embedded systems.

This Learning Path focuses on using TinyML models with virtualized Arm hardware to simulate real-world AI workloads on microcontrollers and NPUs.

If you're looking to build and train your own TinyML models, follow the [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/).

## What is ExecuTorch?

ExecuTorch is a lightweight runtime for running PyTorch models on embedded and edge devices. It supports efficient model inference on a range of Arm processors, ranging from Cortex-M CPUs to Ethos-U NPUs, with support for hybrid CPU+accelerator execution.

ExecuTorch provides:

- Ahead-of-time (AOT) compilation for faster inference
- Delegation of selected operators to accelerators like Ethos-U
- Tight integration with Arm compute libraries

## Why use Arm Fixed Virtual Platforms?

Arm Fixed Virtual Platforms (FVPs) are virtual hardware models used to simulate Arm-based systems like the Corstone-320. They allow developers to validate and tune software before silicon is available, which is especially important when targeting newly-released accelerators like the [Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) NPU.

These virtual platforms also include a built-in graphical user interface (GUI) that helps you:

- Confirm your model is running on the intended virtual hardware  
- Visualize instruction counts  
- Review total execution time  
- Capture clear outputs for demos and prototypes  

## What is Corstone-320?

The Corstone-320 FVP is a virtual model of an Arm-based microcontroller system optimized for AI and TinyML workloads. It supports Cortex-M CPUs and the Ethos-U NPU, making it ideal for early testing, performance tuning, and validation of embedded AI applications, all before physical hardware is available.

The Corstone-320 reference system is free to use, but you'll need to accept the license agreement during installation. For more information, see the [Corstone-320 documentation](https://developer.arm.com/documentation/109761/0000?lang=en).

## What's next?
In the next section, you'll explore how ExecuTorch compiles and deploys models to run efficiently on simulated hardware.
