---
title: Select and set up your edge device
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose your platform

Before you can install AWS IoT Greengrass and deploy an Edge Impulse model, you need a Linux-based Arm device to act as your edge device. This Learning Path supports four platform options. Select the one that matches your available hardware and follow the setup instructions.

If you don't have any of the physical hardware boards listed below, use the AWS EC2 option. It creates an Arm-based virtual machine in the cloud that behaves like a local edge device, so you can complete every step in this Learning Path without dedicated hardware.

Each setup guide installs the required dependencies (build tools, Node.js, GStreamer, Java) and provides a device-specific JSON configuration that you'll use later when deploying the Greengrass component. After completing your chosen setup, return to this page and continue to the next section.

### Option 1: AWS EC2 Arm instance (no hardware required)

Use this option if you don't have a physical edge device. You create an Ubuntu-based EC2 instance with an Arm processor (Graviton) that simulates a local edge device. Because there is no camera attached, this option uses a sample video file for inference input.

[Set up EC2 instance](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupec2/)

### Option 2: Raspberry Pi 5 with Raspberry Pi OS

The Raspberry Pi 5 is a widely available, affordable Arm board with full Edge Impulse and Greengrass support. You can run inference with an attached USB camera or use a sample video file.

[Set up Raspberry Pi 5](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetuprpi5/)

### Option 3: Nvidia Jetson with Jetpack 5.x or 6.0

If you have an Nvidia Jetson board (Nano, Xavier, Orin), you can take advantage of GPU-accelerated inference. This option assumes Jetpack is already flashed onto the device.

[Set up Nvidia Jetson](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupnvidiajetson/)

### Option 4: Qualcomm QC6490 with Ubuntu

For Qualcomm QC6490-based development boards running Ubuntu, this option supports both the on-board Qualcomm camera and USB-attached cameras, as well as file-based inference without a camera.

[Set up Qualcomm QC6490](/learning-paths/embedded-and-microcontrollers/edge_impulse_greengrass/hardwaresetupqc6490ubuntu/)

## After setup

Once you finish the setup for your chosen platform, continue to the next page to create your Edge Impulse project and build a model deployment.