---
# User change
title: Build Corstone-1000 software stack

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The Trusted Firmware software stack uses the [Yocto Project](https://www.yoctoproject.org/) to build a tiny Linux distribution suitable for the Corstone-1000 platform.

Use your Linux development machine to build the software and run on the Corstone-1000 FVP.

## Set up the build environment

Set up your build environment by installing the required software packages. 

```console
sudo apt-get install -y git curl wget build-essential libssl-dev python3 python3-pip cmake make
```
You can review the [Trusted Firmware Getting Started](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html) documentation for more information.

## Install the required software for the Corstone-1000 stack

As per the [User Guide](https://corstone1000.docs.arm.com/en/latest/user-guide.html), install these additional required software packages:

```console
sudo apt-get update
sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
 build-essential chrpath socat cpio python3 python3-pip python3-pexpect \
 xz-utils debianutils iputils-ping python3-git libegl1-mesa libsdl1.2-dev \
 xterm zstd liblz4-tool picocom
```
```console
sudo apt-get upgrade -y libstdc++6
```
The [kas](https://pypi.org/project/kas/) utility is used to build the supplied projects. Install with:

```console
sudo pip3 install kas
```

## Clone Yocto project

Clone the [Yocto repository](https://www.yoctoproject.org/software-overview/downloads/) to your build machine:

```console
git clone -b scarthgap git://git.yoctoproject.org/poky.git
```

## Clone Arm platform build recipes

Navigate into the project, and clone the `meta-arm` layer.

```console
cd poky
git clone https://git.yoctoproject.org/git/meta-arm
```

## Build the software 

You can build the software for FVP or MPS3

{{% notice Note%}}
Each build can take over one hour to complete!
{{% /notice %}}

### Build for Corstone-1000 FVP

Start the build:

```console
kas build meta-arm/kas/corstone1000-fvp.yml
```

### Build for MPS3 AN550

Start the build:

```console
kas build meta-arm/kas/corstone1000-mps3.yml
```
