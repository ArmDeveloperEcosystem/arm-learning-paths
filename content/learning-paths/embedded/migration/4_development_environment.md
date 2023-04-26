---
# User change
title: "Development environment" 

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Development environment

Two different development environments will be setup; one with GNU Compiler Collection ([GCC](https://gcc.gnu.org/)) and the other with Arm Compiler for Linux ([ACfL](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)). For convenience, containers will be used to set up the development environments allowing us to compile and run the example application.

See [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) for instructions how to install Docker in your Linux environment.

Note: GCC compiler options are compatible with ACfL compiler options, i.e., the same `CMakeLists.txt` file is used for both compilers in this guide.

## GCC

Create a file named `Dockerfile` with the following content:
```docker
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install vim wget sudo git tar build-essential libopencv-dev cmake
RUN apt-get clean

ENV USER=ubuntu
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/ubuntu
USER ubuntu
```

This is our GCC development environment. The `Dockerfile` stays the same for cross-platform and native build of the Docker image, however the build command is slightly different.

### Cross-platform

The cross-platform build using `buildx` enables us to build an `aarch64` container on an `x86_64` machine. Once built, the cross-platform built container can be run on that same `x86_64` machine using QEMU, quite convenient!

To build the container, run the following command:
```bash
docker buildx build --platform linux/aarch64 -t sobel_gcc_example .
```

### Native

On the Graviton instances and Raspberry Pi 4, the container will be built natively.
```bash
docker build -t sobel_gcc_example .
```

## ACfL

The ACfL container won't be built as the base container already exists. This container will be used in Graviton instances and on the Raspberry Pi 4.


The base container image already exists, only OpenCV needs to be installed inside.

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_acfl_example
```

Now that we have our development environments defined we can compile and run the Sobel filter application.