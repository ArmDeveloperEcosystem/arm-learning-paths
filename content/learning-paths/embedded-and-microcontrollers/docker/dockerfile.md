---
# User change
title: "Create Dockerfile and build docker image"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can prepare a Docker image containing [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) and a library of [Fixed Virtual Platforms (FVPs)](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms), for use as a basic build and run environment.

The operating system of the docker image is `Ubuntu`, though the host machine could be Windows or a different flavor of Linux.

Linux users may need to precede the `docker` commands below with `sudo`, as the docker daemon always runs as the root user.

## Before you begin

Download and [install](/install-guides/docker/) the appropriate version of Docker for your host platform.

## Prepare files to copy into image

Download the installation packages for Arm Compiler for Embedded and the FVP library from the [Product Download Hub](https://developer.arm.com/downloads).

Create a (temporary) directory, and copy the compiler and FVP library installers here. 

Note that the exact file names are dependent on the versions used - you may need to update the below `Dockerfile` as necessary.

## Create Dockerfile

A [Dockerfile](https://docs.docker.com/engine/reference/builder/) is a text file containing all the instructions to build your docker image.

In the same directory, create a text file named exactly `Dockerfile` containing the [below](#dockerfile).

### Notes regarding Dockerfile

This file copies the installers to the Docker image. The exact filename(s) will depend on the versions used.

Edit the Dockerfile as necessary (`ACfE` and `FVP` arguments), else edit on the build command line (see later).

While installing the [compiler](/install-guides/armclang/) and [FVP library](/install-guides/fm_fvp/fvp/), the EULA(s) are silently accepted. Be sure that this is satisfactory for you.

You will need to edit the licensing portion of the file to match your internal license setup. See [Arm User-Based Licenses](/install-guides/license/) for more information.

## Dockerfile {#dockerfile}
```Dockerfile
FROM ubuntu:20.04 as base

# Install packages: update filenames if necessary
ARG ACfE=ARMCompiler6.21_standalone_linux-x86_64.tar.gz
ARG FVP=FVP_ARM_Std_Library_11.24_11_Linux64.tgz
ARG ARCH=x86_64

ENV USER=ubuntu

# Update docker image OS
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y upgrade

# Install necessary dependencies
RUN apt-get install -y nano sudo ca-certificates git make cmake lsb-core libx11-dev libxext6 libsm6 libxcursor1 libxft2 libxrandr2 libxt6 libxinerama1 libz-dev lsb xterm telnet dos2unix

# Setup default user
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:$USER" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/$USER
USER ubuntu

# Install Arm Compiler for Embedded
COPY $ACfE /home/$USER
RUN mkdir /home/$USER/tmp
RUN tar xvfz $ACfE  -C /home/$USER/tmp
RUN /home/$USER/tmp/install_$ARCH.sh --i-agree-to-the-contained-eula --no-interactive -q -f -d /home/$USER/ACfE
RUN rm -rf /home/$USER/tmp
RUN rm $ACfE
ENV PATH "/home/$USER/ACfE/bin:$PATH"

# Install FVP Library
COPY $FVP /home/$USER
RUN mkdir /home/$USER/tmp
RUN tar xvfz $FVP  -C /home/$USER/tmp
RUN /home/$USER/tmp/FVP_ARM_Std_Library.sh --i-agree-to-the-contained-eula --no-interactive -q -f -d /home/$USER/FVP
RUN rm -rf /home/$USER/tmp
RUN rm $FVP
ENV PATH "/home/$USER/FVP/bin:/home/$USER/FVP/FVP_Base:/home/$USER/FVP/FVP_MPS2:/home/$USER/FVP/FVP_VE:/home/$USER/FVP/FVP_BaseR:$PATH"

# License configuration
# Uncomment and modify below as appropriate
#
# ENV ARMLM_ONDEMAND_ACTIVATION=product_code@https://internal.ubl.server
#   or
# RUN armlm activate --code <activation-code>
#   or
# ENV ARMLMD_LICENSE_FILE=port@server
```
## Build docker image
Use the command:
```console
docker build -t arm-environment .
```
to build a docker image named `arm-environment`. This name is arbitrary, and can be changed if you wish.

To change `Dockerfile` arguments from the command line, use the `--build-arg` option. For example to build an Arm-hosted docker image:
```console
docker build --build-arg ARCH=aarch64 --build-arg ACfE=ARMCompiler6.21_standalone_linux-aarch64.tar.gz --build-arg FVP=FVP_ARM_Std_Library_11.24_11_Linux64_armv8l.tgz -t arm-environment:aarch64 .
```
After a few minutes the docker image will be built and be ready for use. You can see all available images with the command:
```console
docker images
```
## Access the docker image
To interact with your docker image, enter the command:
```console
docker run -i -t arm-environment /bin/bash
```
and you will enter the terminal of the docker image. Verify everything is working correctly with, for example:
```console
armclang --version
```
You have created a docker environment containing Arm Compiler for Embedded and the FVP library, which you can share and replicate as needed.
