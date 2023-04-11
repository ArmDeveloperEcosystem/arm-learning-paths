---
# User change
title: "Application porting" 

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application porting

## Access aarch64 system

### AVA

[AVA system](https://www.adlinktech.com/Products/Computer_on_Modules/COM-HPC-Server-Carrier-and-Starter-Kit/AVA_Developer_Platform) running [SOAFEE](https://www.soafee.io/) reference implementation: Yocto-based Linux [EWAOL](https://gitlab.com/soafee/ewaol/meta-ewaol).

EWAOL comes with Docker installed.

### Qemu 

On a x86_64 machine with Docker installed, we can use [buildx](/learning-paths/cross-platform/docker/buildx) to run multi-architecture containers.

### AWS Graviton

Launch an aarch64 Graviton instance using [AWS EC2](https://aws.amazon.com/ec2/) and install [Docker](/install-guides/docker/docker-engine).

## Docker software development image

### Dockerfile

Create a Dockerfile with the content below to set up the necessary development tools:

```
FROM ubuntu:22.04
 
RUN if ! [ "$(arch)" = "aarch64" ] ; then exit 1; fi
 
ENV DEBIAN_FRONTEND=noninteractive
 
RUN apt-get -y update
RUN apt-get -y install vim wget sudo git make cmake tar
RUN apt-get -y install environment-modules python3 libc6-dev
RUN apt-get clean
 
ENV USER=ubuntu
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
 
ENV ACFL_MAJ_VER=23
ENV ACFL_MIN_VER=04
 
RUN wget https://developer.arm.com/-/media/Files/downloads/hpc/arm-compiler-for-linux/${ACFL_MAJ_VER}-${ACFL_MIN_VER}/arm-compiler-for-linux_${ACFL_MAJ_VER}.${ACFL_MIN_VER}_Ubuntu-22.04_aarch64.tar
RUN tar xf arm-compiler-for-linux_${ACFL_MAJ_VER}.${ACFL_MIN_VER}_Ubuntu-22.04_aarch64.tar
RUN cd arm-compiler-for-linux_${ACFL_MAJ_VER}.${ACFL_MIN_VER}_Ubuntu-22.04 && ./arm-compiler-for-linux_${ACFL_MAJ_VER}.${ACFL_MIN_VER}_Ubuntu-22.04.sh -a
RUN rm -rf arm-compiler-for-linux_${ACFL_MAJ_VER}.${ACFL_MIN_VER}_Ubuntu-20.04*
 
RUN echo "source /usr/share/modules/init/bash" >> /home/ubuntu/.bashrc
RUN echo "module use /opt/arm/modulefiles" >> /home/ubuntu/.bashrc
RUN echo "module load binutils acfl gnu" >> /home/ubuntu/.bashrc
RUN echo "echo Arm Compiler for Linux environment loaded." >> /home/ubuntu/.bashrc
 
WORKDIR /home/ubuntu
USER ubuntu
```

### Build image

On AVA or AWS Graviton:

```bash
docker build -t arm-compiler-for-linux .
```

On x86_64:

```bash
docker buildx build --platform linux/amd64 -t arm-compiler-for-linux .
```

### Pull image

As an alternative, you can also pull the image from Docker Hub:

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux arm-compiler-for-linux
```
