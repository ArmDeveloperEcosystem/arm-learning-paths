---
title: Set up the development environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
The rise of Large Language Models (LLMs) reshapes the landscape of what is possible. *Transformer networks* are known for their ability to generate coherent responses to complex strings of text. A known collection of LLMs is [Llama](https://llama.meta.com/). It successfully generates text so contextually-accurate that it can, at times, be indistinguishable from a real human.

In this Learning Path, you will prepare an LLM for edge deployment on the Raspberry Pi 5. A Docker container with Raspberry Pi OS is used to build the binaries needed to deploy the model on the actual device.

## Arm Linux development machine requirements

You can run the steps in this Learning Path on any Arm-based Linux computer; either a physical machine, or a cloud instance. Because of the size of the model, you need one with a generous amount of memory (RAM), which is needed to compile the transformer model. These instructions were tested on an AWS instance of type `m7gd.4xlarge` and `c7g.8xlarge`, with 64 GB of memory (RAM) and a disk volume of 100 GB. If necessary, you can use 32 GB RAM and 16 GB of swap space, but build time is slower. 

Information on launching an AWS instance is available in [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/).

Verify the architecture of your machine:
```bash
uname -m
```
and confirm the output is:
```console
aarch64
```

## Run Raspberry Pi OS in a Docker container

Developing large, complex AI applications for running on edge hardware like the Raspberry Pi 5 is often difficult. The complexity comes from resource intensive C++ compilation, large files, and many dependencies. 

This example uses Docker to run Raspberry Pi OS in a container, providing the same operating system on the development machine and the edge device. A container is also useful to try out workflows without hardware access. 

Make sure Docker is installed on your Arm Linux development machine. Refer to the [Docker install guide](/install-guides/docker/docker-engine) for instructions.

Raspberry Pi has Docker images available for download, but for this example, a [GitHub repository](https://github.com/jasonrandrews/rpi-os-docker-image) is provided with everything you need to get started. It uses an image of Raspberry Pi OS, which also comes with a number of useful tools such as Git, Python, and the Arm toolchain. 

On your Arm Linux development machine, clone the example repository:

```bash
git clone https://github.com/jasonrandrews/rpi-os-docker-image
cd rpi-os-docker-image
```

Take a look at the `Dockerfile` and scripts to see how the process of creating the Docker image works.

The scripts download Raspberry Pi OS and build a container image using the Dockerfile. 

Download the Raspberry Pi OS image:

```bash
./get-pi-sw.sh
```

In addition to downloading Raspberry Pi OS, the `get-pi-sw.sh` script extracts the root file system so it can be used in the container. 

Build the Docker image:

```bash
./build.sh
```

The `run.sh` script starts the container with an interactive terminal session:

```bash
./run.sh
```

You are now at a shell prompt named `pi@rpi` and you are running Raspberry Pi OS in a container.

{{% notice Note %}}
For the next steps, continue working at the Docker container shell prompt.
{{% /notice %}}