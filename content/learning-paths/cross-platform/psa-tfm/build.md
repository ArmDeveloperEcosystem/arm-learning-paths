---
# User change
title: Build and run Trusted Firmware on the FVP

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

If you want to use Arm Virtual Hardware as a development machine, set it up now using the [install guide](/install-guides/avh/). All required software is pre-installed in the virtual machine so there is nothing to install. 

You can review the [Trusted Firmware Getting Started](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html) documentation for more information.

## Install additional software

Install additional required software packages:

```console
sudo apt-get update
sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
 build-essential chrpath socat cpio python3 python3-pip python3-pexpect \
 xz-utils debianutils iputils-ping python3-git libegl1-mesa libsdl1.2-dev \
 xterm zstd liblz4-tool picocom
sudo apt-get upgrade -y libstdc++6
sudo pip3 install kas
```

## Clone Yocto project

Clone the [Yocto repository](https://www.yoctoproject.org/software-overview/downloads/) to your build machine:

```console
git clone -b langdale git://git.yoctoproject.org/poky.git
```

## Clone Arm platform build recipes

Navigate into the project, and clone the `meta-arm` layer.

```console
cd poky
git clone https://git.yoctoproject.org/git/meta-arm
```

## Build the software 

You should build for the FVP first. 

If you want to skip the FVP and move to the MPS3 board, proceed to the next section.

{{% notice Note%}}
The build can take over one hour to complete!
{{% /notice %}}

### Build for the FVP

Start the build:

```console
kas build meta-arm/kas/corstone1000-fvp.yml
```
## Run the software on the FVP

When the build is complete, run the image on the FVP:

```console
meta-arm/scripts/runfvp --terminals=xterm build/tmp/deploy/images/corstone1000-fvp/corstone1000-image-corstone1000-fvp.fvpconf
```

When the boot sequence is complete, you will be presented with a login prompt.

```output
corstone1000-fvp login:
```

Use `root` as your username to proceed.

You have run Trusted Firmware on the Corstone-1000 FVP. 

Refer to the [User Guide](https://tf-m-user-guide.trustedfirmware.org/platform/arm/corstone1000/readme.html) for complete documentation.

