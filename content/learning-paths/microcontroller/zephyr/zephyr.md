---
# User change
title: "Build and run Zephyr applications"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Zephyr](https://zephyrproject.org/) is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with security in mind.

The Zephyr RTOS is based on a small-footprint kernel designed for use on resource-constrained systems: from simple embedded environmental sensors and LED wearables to sophisticated smart watches and IoT wireless gateways.

We will get the Zephyr source, install the Zephyr SDK, build sample applications, and run them on the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

These instructions assume an Ubuntu Linux host machine, or use of [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware).

## Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page. For installation instructions see [this article](/install-tools/ecosystem_fvp/).

Alternatively, you can access the FVP with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware). For setup instructions see [here](/install-tools/avh#corstone).

## Install prerequisites for Zephyr build

Start by adding the extra repositories to your sources list. This is needed to install the Zephyr dependencies.
```console
wget https://apt.kitware.com/kitware-archive.sh
sudo bash kitware-archive.sh
```

Install prerequisites for Zephyr build as described in the documentation.

```console
sudo apt install --no-install-recommends -y git cmake ninja-build gperf ccache dfu-util device-tree-compiler wget python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
```
Next, install Python dependencies and activate a new virtual environment:

```console
sudo apt install -y python3-venv
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```
Get the Zephyr source code and install additional python dependencies declared in the source:

```console
west init ~/zephyrproject
cd ~/zephyrproject
west update
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```
## Install Zephyr SDK

To build Zephyr applications we need to install the Zephyr Software Development Kit (SDK). It contains the compiler, assembler, linker and other programs needed for building Zephyr applications. Zephyr SDK is supported on Arm-based hosts but in this case we install the x86_64 version of the SDK.

Download, verify, extract and setup the Zephyr SDK bundle. The below is for version `0.15.2`. You can check for the latest version [here](https://github.com/zephyrproject-rtos/sdk-ng/releases).

```console
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.2/zephyr-sdk-0.15.2_linux-x86_64.tar.gz
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.2/sha256.sum | shasum --check --ignore-missing
tar xvf zephyr-sdk-0.15.2_linux-x86_64.tar.gz
cd zephyr-sdk-0.15.2
./setup.sh
```

## Build the hello world sample application

There are sample applications included with Zephyr source repo. We will build the [hello world](https://docs.zephyrproject.org/latest/samples/hello_world/README.html) application for the Corstone-300.

```console
cd ~/zephyrproject/zephyr
west build -p auto -b mps3_an547 samples/hello_world
```
The application binaries are built in the `~/zephyrproject/zephyr/build/zephyr/` directory.

## Run Zephyr application on Corstone-300 FVP

To run the Zephyr application on the Corstone-300 FVP target, run the command below

### Standalone
```console
FVP_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf
```
### Within Arm Virtual Hardware
```console
VHT_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf
```
You will see telnet terminal windows pop up from the running simulation on the FVP with the output similar to:

```
*** Booting Zephyr OS build zephyr-v3.2.0-881-g35ec706d82a5  ***
Hello World! mps3_an547
```
## Congratulations

You have successfully built a Zephyr application and run it on the Corstone-300. You can now try some of the other sample applications included or build your own.

To build and run the [Dining Philosophers](https://docs.zephyrproject.org/latest/samples/philosophers/README.html) example, use:

```console
west build -p auto -b mps3_an547 samples/philosophers
VHT_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf
```
