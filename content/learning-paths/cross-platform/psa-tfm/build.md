---
# User change
title: Setup build and run on FVP

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The software stack uses the [Yocto Project](https://www.yoctoproject.org/) to build a tiny Linux distribution suitable for the Corstone-1000 platform.

Full instructions are given in the [User Guide](https://tf-m-user-guide.trustedfirmware.org/platform/arm/corstone1000/readme.html).

## Set up build environment

Set up your build environment as per the [Trusted Firmware Getting Started](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html) documentation.
```console
sudo apt-get install -y git curl wget build-essential libssl-dev python3 \
python3-pip cmake make
```
Alternatively launch Arm Virtual Hardware instance as per [these instructions](/install-guides/avh/) which has these preconfigured.

## Resolve build dependencies

Resolve build dependencies with:
```console
sudo apt-get update
sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
 build-essential chrpath socat cpio python3 python3-pip python3-pexpect \
 xz-utils debianutils iputils-ping python3-git libegl1-mesa libsdl1.2-dev \
 xterm zstd liblz4-tool picocom
sudo apt-get upgrade -y libstdc++6
pip3 install kas
```
## Clone Yocto project

Clone the latest Yocto [repository](https://www.yoctoproject.org/software-overview/downloads/) to your build machine.
```console
git clone -b langdale git://git.yoctoproject.org/poky.git
```
## Clone Arm platform build recipes

Navigate into the above project, and clone the `meta-arm` layer.
```console
cd poky
git clone https://git.yoctoproject.org/git/meta-arm
```
## Build software stack

It is recommended to first build for the FVP. If you wish to use the MPS3 only, proceed to the next section now.

{{% notice Note%}}
The build step can take over one hour to complete!
{{% /notice %}}

### Build for FVP
```console
kas build meta-arm/kas/corstone1000-fvp.yml
```
## Run stack on FVP
When the build is complete, run the image on the FVP.
```console
meta-arm/scripts/runfvp --terminals=xterm build/tmp/deploy/images/corstone1000-fvp/corstone1000-image-corstone1000-fvp.fvpconf
```
When the boot sequence is complete, you will be presented with a login prompt.
```output
corstone1000-fvp login:
```
Use `root` as your username to proceed.
