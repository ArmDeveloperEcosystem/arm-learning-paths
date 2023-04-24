---
# User change
title: "Target system setup" 

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Target system setup

Embedded systems are increasingly using container engines such as Docker to deploy and isolate applications. In our example, we are going to show how to build or pull a container image to perform our porting and build natively on aarch64.

## Access aarch64 system

You can build the example natively using [AWS EC2 Graviton instances](https://aws.amazon.com/ec2/) or a Raspberry Pi 4 and install [Docker](/install-guides/docker/docker-engine).

You can even build the example for `aarch64` on a `x86_64` machine with Docker. [Buildx](/learning-paths/cross-platform/docker/buildx) can be used to run multi-architecture containers.

## Docker software development image

### Dockerfile

Create a Dockerfile with the content below to set up the necessary development tools:

```
FROM ubuntu:22.04

RUN if ! [ "$(arch)" = "aarch64" ] ; then exit 1; fi

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update
RUN apt-get -y install vim wget sudo git tar build-essential libopencv-dev cmake
RUN apt-get clean

ENV USER=ubuntu
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/ubuntu
USER ubuntu
```

### Build image

On AVA or AWS Graviton:

```bash
docker build -t sobel_example .
```

On x86_64:

```bash
docker buildx build --platform linux/amd64 -t sobel_example .
```

You can check the environment with a few commands:

```bash
cat /etc/issue
gcc --version
cmake --version
cat /usr/lib/aarch64-linux-gnu/pkgconfig/opencv4.pc | grep Version
```

### [Alternative] Pull ACfL development image

As an alternative, you can also pull this image from Docker Hub:

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_example
```

This image is based on Ubuntu 22.04 and provides the latest version of the Arm Compiler for Linux and GCC.

#### Install dependencies

The image has generic software development tools but still miss the OpenCV libraries our application requires. When the container is running (see next page for how to launch it), use the following command to install them:

```bash
sudo apt install -y libopencv-dev
```