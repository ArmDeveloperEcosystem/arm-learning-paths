---
title: Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path uses Arm Performix CPU Mircoarchitecture and Instruction Mix recipes to analyze performance in a sample application.

## Before you begin

Use the Arm Performix [installation guide](/install-guides/atp/) to install the tool if this is your first run. From the host machine, open the **Targets** tab, set up an SSH connection to the target that runs the workload, and test the connection. In this Learning Path's examples, I'll connect to an Arm Neoverse V1 workstation.

Install required OS packages on the target. For Debian-based distributions, run:
```bash
sudo apt-get install python3 python3-venv binutils
```

## Build sample application on remote server

Connect to your target machine and download the sample application for this Learning Path, a Mandelbrot set generator.
The code is available under the [Arm Education License](https://github.com/arm-university/Mandelbrot-Example?tab=License-1-ov-file). Create a directory where you want to store and build the example, then run:

```bash
git clone https://github.com/arm-university/Mandelbrot-Example.git
cd Mandelbrot-Example && mkdir images builds
```

Install a C++ compiler by using your operating system's package manager.

```bash
sudo apt install build-essential
```

Build the application:

```bash
./build.sh
```

The binary in the `./builds/` directory generates an image similar to the fractal below.

![Green-Parallel-512.bmp](./Green-Parallel-512.bmp)