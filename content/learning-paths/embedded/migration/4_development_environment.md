---
# User change
title: "Development environment" 

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Development environment

The original application uses GNU Compiler Collection ([GCC](https://gcc.gnu.org/)) so we want to create a development environment with this compiler and with the same version (when possible). For convenience and to be able to run on `x86_64`, we'll use a container for our development environments. This will allow us to compile and run the ported application using a `aarch64` container on our `x86_64` machine.

See [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) for instructions how to install Docker in your Linux environment.

## GCC container

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

This defines our GCC development environment.

## Cross-platform build

The cross-platform build using `buildx` enables us to build an `aarch64` container on an `x86_64` machine. Once built, the cross-platform built container can be run on that same `x86_64` machine using QEMU behind the scenes, quite convenient!

To build the container, run the following command:
```bash
docker buildx build --platform linux/aarch64 -t sobel_gcc_example .
```

## Run the container

Finally, we want to run the cross-platform built container on our `x86_64` machine. Do so by running the command below.
```bash
xhost +local:*
docker run -it --rm --platform linux/aarch64 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_gcc_example /bin/bash
```

Now that we have our development environment running, we can port the Sobel filter application.