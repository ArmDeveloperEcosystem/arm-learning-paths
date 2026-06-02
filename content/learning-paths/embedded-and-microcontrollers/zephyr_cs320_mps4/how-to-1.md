---
title: Set up the Zephyr build environment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the development environment

Before you build Zephyr for the Arm Corstone-320 MPS4 platform, you need to install the required host packages, initialize a Zephyr workspace, and install the Arm GNU Toolchain.

## Install host dependencies

Update your package list and install the packages that Zephyr requires. Select the tab for your host architecture:

{{< tabpane-normal >}}
  {{< tab header="aarch64" >}}
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y --no-install-recommends git cmake ninja-build gperf \
  ccache dfu-util device-tree-compiler wget python3-dev python3-venv python3-tk \
  xz-utils file make gcc libsdl2-dev libmagic1
```
  {{< /tab >}}
  {{< tab header="x86_64" >}}

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y --no-install-recommends git cmake ninja-build gperf \
  ccache dfu-util device-tree-compiler wget python3-dev python3-venv python3-tk \
  xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Verify that the installed versions meet Zephyr's minimum requirements (CMake 3.20.5, Python 3.12, dtc 1.4.6):

```bash
cmake --version
python3 --version
dtc --version
```

## Set up the Zephyr workspace

Create a Python virtual environment and use `west` to initialize the Zephyr workspace. The following commands place the workspace in `~/zephyrproject`, but you can choose a different location.

Create and activate the virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
```

After activation, your shell prompt is prefixed with `(.venv)`. Run `source ~/zephyrproject/.venv/bin/activate` each time you open a new terminal before working with Zephyr.

Install `west` and download the Zephyr source code:

```bash
pip install west
west init ~/zephyrproject
cd ~/zephyrproject
west update
```

Export the Zephyr CMake package so that CMake can automatically load the boilerplate required for Zephyr builds:

```bash
west zephyr-export
```

Install the Python packages that Zephyr requires:

```bash
west packages pip --install
```

## Install the Arm GNU Toolchain

The Corstone-320 target uses the Cortex-M85 processor, so you need the `arm-none-eabi` bare-metal toolchain from the Arm GNU Toolchain. For a detailed installation guide covering all platforms, see the [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/) install guide.

{{% notice Note %}}
The following commands use Arm GNU Toolchain version 15.2.Rel1. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Arm GNU Toolchain downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).
{{% /notice %}}

Download, unpack, and add the Arm GNU Toolchain to your `PATH` for your host architecture:

{{< tabpane-normal >}}
  {{< tab header="aarch64" >}}

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
```
  {{< /tab >}}
  {{< tab header="x86_64" >}}

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Verify the installation:

```bash
arm-none-eabi-gcc --version
```

The output is similar to:

```output
arm-none-eabi-gcc (Arm GNU Toolchain 15.2.Rel1 (Build arm-15.86)) 15.2.1 20251203
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Configure the toolchain for Zephyr

Zephyr uses two environment variables to locate the Arm GNU Toolchain. Set these each time you open a new terminal, or add them to your shell configuration file:

{{< tabpane-normal >}}
  {{< tab header="aarch64" >}}

```bash
export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
export GNUARMEMB_TOOLCHAIN_PATH=$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi
```
  {{< /tab >}}
  {{< tab header="x86_64" >}}

```bash
export ZEPHYR_TOOLCHAIN_VARIANT=gnuarmemb
export GNUARMEMB_TOOLCHAIN_PATH=$HOME/arm-gnu-toolchain-15.2.rel1-x86_64-arm-none-eabi
```
  {{< /tab >}}
{{< /tabpane-normal >}}

## What you've accomplished and what's next

You've now set up a build environment to build Zephyr. 

Next, you'll add Zephyr board support files for the Corstone-320 MPS4 platform.
