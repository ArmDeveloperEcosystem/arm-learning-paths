---
title: Set up the development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
The rise of Large Language Models (LLM) re-shapes the landscape of what is possible. The *transformer networks* are known for their ability to generate coherent responses to complex strings of text. A known collection of LLMs is [Llama](https://llama.meta.com/). It successfully generates text so contextually accurate that it can be indistinguishable from a real human.

In this learning path, you will prepare an LLM for edge deployment on the Raspberry Pi 5. A Docker container emulates the edge device, which is used to build the binaries needed to deploy the model on the actual device.

## Arm machine memory requirements

You can run the steps in this learning path on any Arm-based Linux, either a physical machine or instance in the cloud (later on referred to as _host_). Because of the size of the model, you need one with a generous amount of memory (RAM), which is needed to compile the transformer model. These instructions were tested on an AWS instance of type `m7gd.4xlarge` and `c7g.8xlarge`, with 64 GB of memory (RAM) and a disk volume of 100 GB .

Information on launching an AWS instance is available in the [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/) install guide.

Verify the architecture of your machine:
```bash
uname -m
```
and observe the output
```console
aarch64
```

## Run Raspberry Pi OS in a Docker container

This example uses Docker to run an Raspberry Pi OS container in the cloud. You can go through the [Docker](/install-guides/docker/docker-engine) install guide for installation instructions.

A Docker container is useful to try out embedded workflows without hardware access. Raspberry Pi has Docker images available for download. For this example, a [GitHub repository](https://github.com/jasonrandrews/rpi-os-docker-image) is set up with everything you need to get started. It uses an image of the Raspberry Pi OS, which also comes with a number of useful tools such as Git, Python and the Arm toolchain. In the host machine, clone the example repository:

```bash
git clone https://github.com/jasonrandrews/rpi-os-docker-image
cd rpi-os-docker-image
```

Run the scripts to set up the container.

```bash
./get-pi-sw.sh
./build.sh
./run.sh
```

These scripts will download the Raspberry Pi OS image and build it using the Dockerfile. Finally, it will run the container as an interactive terminal session.

You should now be in a shell named `pi@rpi`. With this, you now know how to run the Raspberry Pi OS in a cloud container.

{{% notice Note %}}
The rest of this learning path will be run in this running Docker container shell.
{{% /notice %}}