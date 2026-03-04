---
title: Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path demonstrates Arm Performix's Top-Down and Instruction Mix recipes for performance analysis on an example application.

## Before you begin

The Performix [installation guide](https://learn.arm.com/install-guides/atp) will walk you through installing the tool for the first time. In this learning path, I will be connecting to an Arm Neoverse V1 workstation. From the host machine, establish an ssh connection to the target running the workload from the 'Targets' tab and test the connection.

There are some OS packages that need to be set up on the target. For Debian distributions, this command should handle the prerequisites:
```bash
sudo apt-get install python3 python3-venv objdump
```

## Build Sample Application on Remote Server

Next, connect to your target machine and download our sample application for this learning path: a Mandelbrot set generator.
This code is available under [Arm Education License](https://github.com/arm-university/Mandelbrot-Example?tab=License-1-ov-file) for teaching and learning. Create a new directory where you will store and build this example. Next, run the commands below.

```bash
git clone https://github.com/arm-university/Mandelbrot-Example.git
cd Mandelbrot-Example && mkdir images builds
```

Install a C++ compiler, for example using your operating system's package manager.

```bash
sudo dnf update && sudo dnf install g++ gcc
```

Build the application. 

```bash
./build.sh
```

The binary in the ./builds/ directory should output an image like the fractal below

[Green-Parallel-512.bmp](./Green-Parallel-512.bmp)