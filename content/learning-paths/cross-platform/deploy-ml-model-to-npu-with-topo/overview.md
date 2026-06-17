---
title: Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration using Topo
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Get started

Before getting started, complete the Learning Path [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/) to learn how to install Topo, run host and target health checks, inspect a target, list compatible Templates, and deploy a containerized workload.

For more background on the underlying NPU example, read [Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration](/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/). You do not need to complete that Learning Path before using this one, but it helps explain the model, firmware, and [Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) execution flow.

## What is Topo?

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm used to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo can also build and deploy directly on the target.

## What you'll learn

In this Learning Path, you will deploy the [topo-imx93-npu-deployment](https://github.com/Arm-Examples/topo-imx93-npu-deployment) Topo Template to an NXP FRDM i.MX 93 board.

The Template builds and deploys a browser-based MobileNetV2 image classifier. The user interface runs on the Cortex-A Linux side of the SoC. The inference runner is packaged as Cortex-M33 firmware and is started by [remoteproc-runtime](https://github.com/arm/remoteproc-runtime). The model is exported to an [ExecuTorch](https://docs.pytorch.org/executorch/stable/index.html) `.pte` [file](https://docs.pytorch.org/executorch/stable/pte-file-format.html) for Ethos-U65 NPU acceleration.

### What does deploying the topo-imx93-npu-deployment Template do?

Deploying the Template starts two runtime services on the target:

- `webapp`: Web application running on the Cortex-A Linux host. It receives an image to run a classification on.
- `cm33-runner`: Cortex-M33 firmware, receives the image to classify from the web application and runs the classification Machine Learning model on it.

When you select an image in the browser and click **Classify**, the web application:

1. Resizes and normalizes the image to classify into an input tensor compatible with the [MobileNetV2](https://arxiv.org/abs/1801.04381) model.
2. Writes the ExecuTorch program and input tensor into reserved physical memory.
3. Sends a `RUN` command to the Cortex-M33 runner over `RPMsg`.
4. Waits for the Cortex-M33 firmware to run inference using Ethos-U65 acceleration.
5. Displays the top-1 and top-5 ImageNet classification results in the browser.

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
  | writes .pte and input tensor to reserved memory
  | sends RUN over RPMsg
  v
Cortex-M33 ExecuTorch runner firmware
  |
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

You now understand what the Topo Template deploys and how the Cortex-A, Cortex-M33, and Ethos-U65 parts work together. Next, you will prepare the i.MX 93 target and deploy the Template with Topo.
