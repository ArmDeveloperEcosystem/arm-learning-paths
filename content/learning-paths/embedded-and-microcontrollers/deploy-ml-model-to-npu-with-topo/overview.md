---
title: Understand the architecture of the machine learning application 
description: Review how the Topo Project deploys a Cortex-A web application, Cortex-M33 firmware, and Ethos-U65 NPU acceleration for image classification on NXP FRDM i.MX 93.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll deploy

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm that you can use to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo Projects are the standardized format for deploying projects with Topo.

In this Learning Path, you'll deploy the [topo-imx93-npu-deployment](https://github.com/Arm-Examples/topo-imx93-npu-deployment) Topo Project to an NXP FRDM i.MX 93 board, and understand how this Topo Project was created.

The Topo Project builds and deploys a browser-based MobileNetV2 image classifier. The user interface runs on the Cortex-A (Linux) side of the SoC. The inference runner is packaged as Cortex-M33 firmware and is started by [remoteproc-runtime](https://github.com/arm/remoteproc-runtime). The model is exported to an [ExecuTorch](https://docs.pytorch.org/executorch/stable/index.html) `.pte` [file](https://docs.pytorch.org/executorch/stable/pte-file-format.html) for Ethos-U65 NPU acceleration.

## Prerequisites

Before getting started, ensure that your i.MX 93 board is set up with Linux and accessible over SSH. Use the Learning Path [Use Linux on the NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) as a guide.

Complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) to learn how to install Topo, run host and target health checks, inspect a target, list compatible Topo Projects, and deploy a containerized workload.

## (Optional) Background reading

To learn more about Topo Projects, and how to create a basic Topo Project for a web application, complete the introductory [Create and deploy a custom Topo Project](https://learn.arm.com/learning-paths/cross-platform/create-your-own-topo-project/) Learning Path. 

To learn more about the model, firmware, and [Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) execution flow behind this NPU example, see the [Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/) Learning Path. 

## What the project does

Deploying the Topo Project starts two runtime services on the target:

- `webapp`: Web application running on the Cortex-A Linux host. It receives an image input from the user and outputs the results of the ML image classification.
- `cm33-runner`: Cortex-M33 firmware that receives the image tensor from the web application, runs the compiled MobileNetV2 ExecuTorch `.pte` program, delegates supported operators to the Ethos-U65 NPU, and runs non-delegated operators on the Cortex-M33 CPU.

## System architecture

The deployed application spans three processing domains on the i.MX 93:

- Cortex-A Linux host: runs Docker, Topo-deployed containers, the Flask web app, and the Linux `remoteproc` and `RPMsg` interfaces.
- Cortex-M33 firmware domain: runs the ExecuTorch runner firmware loaded by `remoteproc-runtime`.
- Ethos-U65 NPU: accelerates delegated neural network operators from the ExecuTorch MobileNetV2 program.

The high-level data flow is:

```output
Browser
  |
  v
Flask web application on Cortex-A Linux
  |
  | writes .pte file and input tensor to reserved memory
  | sends RUN over RPMsg
  v
Cortex-M33 ExecuTorch runner firmware
  |
  | loads the .pte program from reserved memory
  | delegates supported operators
  v
Ethos-U65 NPU
  |
  v
Cortex-M33 returns classification results over RPMsg
  |
  v
Browser displays ImageNet top-1 and top-5 results
```

## What you've learned and what's next

You now understand that the Topo Project deploys a Cortex-A web application, a Cortex-M33 ExecuTorch runner, and Ethos-U65 NPU acceleration as one heterogeneous application. You've also seen how inference uses reserved memory for the `.pte` program and input tensor, with `RPMsg` carrying commands and results between Cortex-A and Cortex-M33.

Next, you'll review the toolchains and runtime interfaces used by the Topo Project.
