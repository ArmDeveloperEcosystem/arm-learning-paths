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

You can build the example natively on aarch64 using [AWS EC2 Graviton instances](https://aws.amazon.com/ec2/) or a Raspberry Pi 4 and install [Docker](/install-guides/docker/docker-engine).

You can even build the example for aarch64 on a x86_64 machine with Docker. [Buildx](/learning-paths/cross-platform/docker/buildx) can be used to run multi-architecture containers.

## Docker software development image

### Dockerfile

Create a Dockerfile with the content below to set up the necessary development tools and replicate the configuration shown in the previous section:

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

On a aarch64 system:

```bash
docker build -t sobel_example .
```

On x86_64:

```bash
docker buildx build --platform linux/amd64 -t sobel_example .
```
### Run container and check the environment

Run an interactive session with a container instance:
```bash
docker run --rm -ti sobel_example
```

When launched, you can check the environment configuration with a few commands:
```bash
cat /etc/issue
gcc --version
cmake --version
cat /usr/lib/aarch64-linux-gnu/pkgconfig/opencv4.pc | grep Version
```

### [Alternative] Pull ACfL development image

As an alternative, instead of building a Docker image from scratch, you can also pull this image from Docker Hub:
```bash
docker pull armswdev/arm-compiler-for-linux
```

This image is based on Ubuntu 22.04 and provides the latest version of the [Arm Compiler for Linux](/install-guides/acfl/), but also GCC and cmake. 

For the rest of the Learning Path, you can tag the image `sobel_example`:

```bash
docker tag armswdev/arm-compiler-for-linux sobel_example
```

And launch an interactive session with the same command than above:
```bash
docker run --rm -ti sobel_example
```


#### Install dependencies

This image doesn't have the OpenCV libraries installed. So, when the container is launched, use the following command to install them:

```bash
sudo apt install -y libopencv-dev
```