---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup

This learning path uses a worked example to make flame graphs and sampling based profiling practical. We will generate a fractal bitmap image by computing the Mandelbrot set and mapping its iteration counts to pixel values. The program is written in C++11, and you will have access to the full source code so you can rebuild it, profile it, and relate what you see in the flame graph back to specific functions and loops.

A fractal is a pattern with detail at many scales, often showing self similar structure. Fractals are typically produced by repeatedly applying a mathematical rule. In the Mandelbrot case, each pixel represents a complex number and is iterated through a simple recurrence. How quickly the value escapes, or whether it stays bounded, determines the coloring and creates the distinctive image. Please refer to the [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set) page for more information.

## Connect to APT Target

Please refer to the [installation guide](https://learn.arm.com/install-guides/atp) if it is your first time setting up Arm Total Performance. In this learning path, I will be connection to an AWS Graviton3 metal instance with 64 Neoverse V1 cores. From the host machine, test the connection to the remote server by navigating to `'Targets`->`Test Connection`. You should see the successul connection below. 

![successful-connection](./successful-connection.jpg).

## Build Application on Remote Server

Next, connect to the remote server, for example using SSH or VisualStudio Code, and clone the Mandelbrot repository 

```bash
cd ~
git clone git@github.com:arm-university/Mandelbrot-Example.git # TODO - UPDATE WITH PUBLIC HTTPS
cd Mandelbrot-Example
git checkout single-thread
```

Install a C++ compiler using your operating system's package manager.

```
sudo dnf install g++ gcc
```

Build the application. 

```bash
./build.sh
```