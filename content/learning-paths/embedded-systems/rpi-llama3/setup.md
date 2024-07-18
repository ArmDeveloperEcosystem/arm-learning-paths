---
title: Set up the development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
The rise of Large Language Models (LLM) re-shapes the landscape of what is possible. The *transformer networks* are known for their ability to generate coherent responses to complex strings of text. A known collection of LLMs is [Llama](https://llama.meta.com/). It successfully generates text so contextually accurate that it can be indistinguishable from a real human.

In this learning path, you will prepare an LLM for edge deployment on the Raspberry Pi 5. A Docker container in the cloud emulates the edge device, which means you can complete the guide without needing access to the actual board. 

## Setting up an AWS instance

The first step is to set up an AWS instance in the cloud. Because of the size of the model you will run, you need a powerful machine to compile the necessary components. These instructions were tested on a `m7gd.4xlarge` instance with 64 GB of memory (RAM) and a 100 GB disk volume. Any Arm-based Linux machine with sufficient memory will work for these instructions.

Information about launching an AWS instance is available in the [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/) install guide.

As the cloud instance runs on Arm, no cross-compilation is needed. Verify the architecture of your machine:
```bash
uname -m
```
and observe the output
```console
aarch64
```

## Run Raspberry Pi OS in a Docker container

This example uses Docker to run an Raspberry Pi OS container in the cloud. Refer to the [Docker](/install-guides/docker/) install guide for installation instructions.

Using a Docker container is an easy way to try out embedded workflows without hardware access. Raspberry Pi has Docker images available for download. For this example, a [GitHub repository](https://github.com/jasonrandrews/rpi-os-docker-image) is set up with everything you need to get started. It uses an image of the Raspberry Pi OS, which also comes with a number of useful tools such as Git, Python and the Arm toolchain. In the AWS instance, clone the example repository:

```bash
git clone https://github.com/jasonrandrews/rpi-os-docker-image
cd rpi-os-docker-image
```

Run the scripts to set up the container:
```bash
# Download the Raspberry Pi OS image
./get-pi-sw.sh
```
```bash
# Build the image using the Dockerfile
./build.sh
```
```bash
# Run the container as an interactive terminal session
./run.sh
```

You should now be in a shell named `pi@rpi`. With this, you now know how to run the Raspberry Pi OS in a cloud container.

{{% notice Note %}}
The rest of this learning path will be run in this container shell. 
{{% /notice %}}

## (optional) Set up your Raspberry Pi 5

If you want to see how the LLM behaves in an embedded environment, you need a Raspberry Pi 5 running Raspberry Pi OS. Install Raspberry Pi OS on your Raspberry Pi 5 using the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html). There are numerous ways to prepare an SD card, but Raspberry Pi recommends [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on a Windows, Linux, or macOS computer with an SD card slot or SD card adapter.

Make sure to install the 64-bit version of Raspberry Pi OS. 

The 8GB RAM Raspberry Pi 5 model is preferred for exploring an LLM.