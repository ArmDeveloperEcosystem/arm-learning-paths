---
# User change
title: Build Corstone-1000 software stack

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The Trusted Firmware software stack uses the [Yocto Project](https://www.yoctoproject.org/) to build a tiny Linux distribution suitable for the Corstone-1000 platform.

Use your Linux development machine to build the software and run on the Corstone-1000 FVP. The instructions have been tested with an Ubuntu 22.04 host.

## Set up the build environment

Set up your build environment by installing the required software packages. 

```console
sudo apt-get update
sudo apt-get install -y git curl wget build-essential libssl-dev python3 python3-pip cmake make
```
You can review the [Trusted Firmware Getting Started](https://tf-m-user-guide.trustedfirmware.org/getting_started/index.html) documentation for more information.

## Install the required software for the Corstone-1000 stack

As per the [User Guide](https://corstone1000.docs.arm.com/en/latest/user-guide.html), install these additional required software packages:

```console
sudo apt-get update
sudo apt install -y gawk wget git diffstat unzip texinfo gcc build-essential chrpath \
socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping \
python3-git python3-jinja2 python3-subunit zstd liblz4-tool file locales libacl1

```
```console
sudo apt-get upgrade -y libstdc++6
```
The [kas](https://pypi.org/project/kas/) utility is used to build the supplied projects. Install with:

```console
sudo pip3 install kas
```

## Clone Arm platform build recipes

Create a build directory, and clone the repository:

```console
mkdir corstone1000
cd corstone1000
git clone https://git.yoctoproject.org/git/meta-arm -b CORSTONE1000-2024.06
```

## Build the software 

You can build the software for [FVP](#fvp) or [MPS3](#mps3)

{{% notice Note%}}
The build can take over one hour to complete!
{{% /notice %}}

### Build for Corstone-1000 FVP {#fvp}

Start the build, accepting the EULA to install the FVP.

```console
export ARM_FVP_EULA_ACCEPT="True"
kas build meta-arm/kas/corstone1000-fvp.yml:meta-arm/ci/debug.yml
```

### Build for MPS3 AN550 {#mps3}

Start the build:

```console
kas build meta-arm/kas/corstone1000-mps3.yml:meta-arm/ci/debug.yml
```
