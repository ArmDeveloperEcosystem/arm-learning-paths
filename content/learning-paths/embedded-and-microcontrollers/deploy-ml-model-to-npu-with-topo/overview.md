---
title: Overview - deploying an image classification app on i.MX 93 with Topo
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll learn

In this Learning Path, you will deploy the [topo-imx93-npu-deployment](https://github.com/Arm-Examples/topo-imx93-npu-deployment) Topo Template to an NXP FRDM i.MX 93 board, and understand how this Topo Template was created.

To refresh, [Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm used to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo Templates are the standardized format by which projects are deployed with Topo.

The Topo Template builds and deploys a browser-based MobileNetV2 image classifier. The user interface runs on the Cortex-A (Linux) side of the SoC. The inference runner is packaged as Cortex-M33 firmware and is started by [remoteproc-runtime](https://github.com/arm/remoteproc-runtime). The model is exported to an [ExecuTorch](https://docs.pytorch.org/executorch/stable/index.html) `.pte` [file](https://docs.pytorch.org/executorch/stable/pte-file-format.html) for Ethos-U65 NPU acceleration.

## Prerequisites

Before getting started, ensure that your i.MX 93 board is set up with Linux and accessible over SSH. You can use this Learning Path as a guide: [Use Linux on the NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/).

You should also be familiar with Topo and have it installed on your host development machine. You can complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) to learn how to install Topo, run host and target health checks, inspect a target, list compatible Templates, and deploy a containerized workload.

## (Optional) Background reading

To understand more about Topo Templates, and how to create a basic Topo Template for a web application, you can complete the introductory [Create and deploy a custom Topo Template](https://learn.arm.com/learning-paths/cross-platform/create-your-own-topo-templates/) Learning Path. However, this is not required for this guide.

For more background on the underlying NPU example, use the [Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/) Learning Path. This can help explain the model, firmware, and [Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) execution flow.

## What does the Template do?

Deploying the Template starts two runtime services on the target:

- `webapp`: Web application running on the Cortex-A Linux host. It receives an image input from the user and outputs the results of the ML image classification.
- `cm33-runner`: Cortex-M33 firmware that receives the image tensor from the web application, runs the compiled MobileNetV2 ExecuTorch `.pte` program, delegates supported operators to the Ethos-U65 NPU, and runs non-delegated operators on the Cortex-M33 CPU.

## System Architecture

The deployed application spans three processing domains on the i.MX 93:

- **Cortex-A Linux host**: runs Docker, Topo-deployed containers, the Flask web app, and the Linux `remoteproc` and `RPMsg` interfaces.
- **Cortex-M33 firmware domain**: runs the ExecuTorch runner firmware loaded by `remoteproc-runtime`.
- **Ethos-U65 NPU**: accelerates delegated neural network operators from the ExecuTorch MobileNetV2 program.

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

## What you've accomplished and what's next

You now understand that the Topo Template deploys a Cortex-A web application, a Cortex-M33 ExecuTorch runner, and Ethos-U65 NPU acceleration as one heterogeneous application. You have also seen how inference uses reserved memory for the `.pte` program and input tensor, with `RPMsg` carrying commands and results between Cortex-A and Cortex-M33.

Next, you will review the toolchains and runtime interfaces used by the Template.
