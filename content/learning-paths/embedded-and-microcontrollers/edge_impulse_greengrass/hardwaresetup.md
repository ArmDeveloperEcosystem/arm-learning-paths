---
title: Select and set up your edge device
description: Choose an Arm edge platform and complete the hardware setup required for the Edge Impulse Greengrass workflow.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose your platform

Before you can install AWS IoT Greengrass and deploy an Edge Impulse model, you need a Linux-based Arm device to act as your edge device. You can use one of four platform options. Select the one that matches your available hardware and follow the setup instructions.

If you don't have any of the supported physical hardware boards, use the Amazon EC2 option. By following the Amazon EC2 instance setup instructions, you can create an Arm-based virtual machine in the cloud that behaves like a local edge device. With an EC2 instance, you can complete every step in the Learning Path without dedicated hardware.

When you set up your platform, you'll install the required dependencies such as build tools, Node.js, GStreamer, and Java. The instructions also include a device-specific JSON configuration that you'll use later when deploying the Greengrass component.

### Arm-based Amazon EC2 instance (no hardware required)

Use an Arm-based Amazon EC2 instance option if you don't have a physical edge device. Create an Ubuntu-based EC2 instance with an Arm processor (Graviton) that simulates a local edge device. Because there's no camera attached, you'll use a sample video file for inference input.

[Set up EC2 instance](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupec2/)

### Raspberry Pi 5 with Raspberry Pi OS

The Raspberry Pi 5 is a widely available, affordable Arm board with full Edge Impulse and Greengrass support. You can run inference with an attached USB camera or use a sample video file.

[Set up Raspberry Pi 5](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetuprpi5/)

### NVIDIA Jetson with JetPack 5.x or 6.0

If you have an NVIDIA Jetson board such as Nano, Xavier, or Orin, you can take advantage of GPU-accelerated inference. This option assumes JetPack is already flashed onto the device.

[Set up NVIDIA Jetson](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupnvidiajetson/)

### Qualcomm QC6490 with Ubuntu

For Qualcomm QC6490-based development boards running Ubuntu, you can use both the on-board Qualcomm camera and USB-attached cameras. You can also use file-based inference without a camera.

[Set up Qualcomm QC6490](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupqc6490ubuntu/)

## What you've accomplished and what's next

You've selected an Arm edge platform, completed its setup, and saved the device-specific component configuration.

Next, create your Edge Impulse project and build a model deployment.
