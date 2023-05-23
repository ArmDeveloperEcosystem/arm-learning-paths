---
# User change
title: "Build and run Zephyr applications"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Zephyr](https://zephyrproject.org/) is a scalable real-time operating system (RTOS) supporting multiple hardware architectures, optimized for resource constrained devices, and built with security in mind.

The Zephyr RTOS is based on a small-footprint kernel designed for use on resource-constrained systems: from simple embedded environmental sensors and LED wearables to sophisticated smart watches and IoT wireless gateways.

You can get the Zephyr source, install the Zephyr SDK, build sample applications, and run them on the [Corstone-300](https://developer.arm.com/Processors/Corstone-300) Fixed Virtual Platform (FVP).

## Before you begin 

The instructions assume an Ubuntu Linux host machine or use of Arm Virtual Hardware (AVH).

The Ubuntu version can be 20.04 or 22.04. The `x86_64` architecture must be used because the Corstone-300 FVP is not currently available for the Arm architecture. You will need a Linux desktop to run the FVP because it opens `xterm` windows to print output from the software applications. 

## Corstone-300 FVP {#fvp}

The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page. Setup instructions are given in the [install guide](/install-guides/fm_fvp).

Alternatively, you can access the FVP with [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware). Setup instructions are given in the [Arm Virtual Hardware install guide](/install-guides/avh#corstone).

## Install the required software to build Zephyr

1. Add the Kitware repository to your sources list

The repository is needed to install the Zephyr dependencies.

```bash { env="DEBIAN_FRONTEND=noninteractive" }
wget https://apt.kitware.com/kitware-archive.sh
sudo bash kitware-archive.sh
```

2. Install the Zephyr prerequisites

Use the `apt` command to install the required software:

```bash { env="DEBIAN_FRONTEND=noninteractive" }
sudo -E apt install --no-install-recommends -y git cmake ninja-build gperf ccache dfu-util device-tree-compiler wget python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1 xterm
```

3. Install the Python dependencies 

Install Python dependencies and activate a new virtual environment:

```bash { cwd="/shared" }
sudo apt install -y python3-venv
ls -al
mkdir zephyrproject
python3 -m venv zephyrproject/.venv
source zephyrproject/.venv/bin/activate
pip install west
```

4. Download the Zephyr source code and install additional python dependencies declared in the source:

```bash { env_source="/shared/zephyrproject/.venv/bin/activate"; cwd="/shared" }
west init zephyrproject
cd zephyrproject
west update
west zephyr-export
pip install -r zephyr/scripts/requirements.txt
```

## Install Zephyr SDK

You need the Zephyr Software Development Kit (SDK) to build Zephyr applications.

It contains the compiler, assembler, linker and other programs needed for building Zephyr applications. 

{{% notice Note %}}
The Zephyr SDK is supported on Arm-based hosts, but you must use the `x86_64` version to run applications on the FVP. 
{{% /notice %}}

Download, verify, extract and setup the Zephyr SDK bundle. The current latest version is `0.15.2`. You can check for newer versions in the [Zephyr project on GitHub](https://github.com/zephyrproject-rtos/sdk-ng/releases).

```bash { env_source="/shared/zephyrproject/.venv/bin/activate" }
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.2/zephyr-sdk-0.15.2_linux-x86_64.tar.gz
wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.15.2/sha256.sum | shasum --check --ignore-missing
tar xf zephyr-sdk-0.15.2_linux-x86_64.tar.gz
cd zephyr-sdk-0.15.2
./setup.sh -t all
cd ~
```

## Build the hello world sample application

There are sample applications included in the Zephyr source code repository. 

You can build the [hello world](https://docs.zephyrproject.org/latest/samples/hello_world/README.html) application for the Corstone-300 using `west`: 

```bash { env_source="/shared/zephyrproject/.venv/bin/activate"; cwd="/shared" }
cd zephyrproject/zephyr
west build -p auto -b mps3_an547 samples/hello_world
```

The application binaries are placed in the `~/zephyrproject/zephyr/build/zephyr/` directory.

## Run Zephyr application on Corstone-300 FVP

Two options are provided to run the Zephyr application on the Corstone-300 FVP, your own Linux machine or Arm Virtual Hardware. 

Select either option. 

### Using your computer with the FVP installed 

To run on your computer: 

```fvp { fvp_name="FVP_Corstone_SSE-300_Ethos-U55"; cwd="/shared/zephyrproject/zephyr" }
FVP_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf --simlimit 24
```

### Using Arm Virtual Hardware

To run on AVH:

```console
VHT_Corstone_SSE-300_Ethos-U55 -a build/zephyr/zephyr.elf --simlimit 24
```

You will see telnet terminal windows pop up from the running simulation on the FVP with the output similar to:

```output
*** Booting Zephyr OS build zephyr-v3.2.0-881-g35ec706d82a5  ***
Hello World! mps3_an547
```

You have successfully built a Zephyr application and run it on the Corstone-300. 

## Additional applications

You can try some of the other sample applications included or build your own.

To build the [Dining Philosophers](https://docs.zephyrproject.org/latest/samples/philosophers/README.html) example, use:

```console
west build -p auto -b mps3_an547 samples/philosophers
```

Run the new executable at `build/zephyr/zephyr.elf` on the FVP. 

