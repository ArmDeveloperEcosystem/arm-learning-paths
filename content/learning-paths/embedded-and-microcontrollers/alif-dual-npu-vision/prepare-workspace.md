---
title: Prepare the board and workspace
description: Connect the E8 hardware and create a west workspace with the validated dual-NPU dependencies.
weight: 3
layout: "learningpathall"
---

## Connect the hardware

Power off the E8 DevKit before changing camera or display connections.

1. Connect the MT9M114 camera module to the bottom-side J16 connector.
2. Connect the MW405 display to the display connector.
3. Connect the board's USB ports for power, SE UART, and U4 UART.
4. Confirm that the board runs SEROM 1.105.65 and SERAM 1.110.0.
5. Move the boot switch to the SE position before flashing.

{{% notice Note %}}
The supplied overlay targets the J16 selfie-camera connection. J22 uses a different I2C address and device-tree route.
{{% /notice %}}

## Install the host tools

Confirm that the Xcode Command Line Tools are installed:

```bash
xcode-select -p
```

If the command reports that the tools are missing, install them before you continue:

```bash
xcode-select --install
```

Install Git, CMake, and Python 3.12 with Homebrew. Then create the west Python environment:

```bash
brew install git cmake python@3.12
mkdir -p $HOME/alif-dual-npu
cd $HOME/alif-dual-npu
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install west pyelftools fdt ninja
```

Confirm that west and Ninja are available:

```bash
west --version
ninja --version
```

Both commands print a version number.

## Create the west workspace

Clone the SDK fork that contains the dual-NPU sample at the validated revision,
then initialize a local west workspace from that checkout.
The fork's ``main`` branch stays synchronized with the Alif SDK ``main``
branch. The dual-NPU application is maintained separately on the
``dual-npu-main-integration`` branch, which also includes the merged MT9M114,
ISP, and MW405 changes from pull request 879:

```bash
cd $HOME/alif-dual-npu
source .venv/bin/activate
git clone --branch dual-npu-main-integration --single-branch \
  https://github.com/varunchariArm/sdk-alif.git sdk-alif
git -C sdk-alif checkout fb6d0e61ebcad3098dc6298bc40386cacc4ad38a
west init -l sdk-alif
west config manifest.project-filter +executorch
west update
python -m pip install -r zephyr/scripts/requirements.txt
west sdk install
```

The manifest project appears at `sdk-alif`, and the remaining projects appear under `modules`, `bootloader`, `tools`, and `zephyr`.

{{% notice Note %}}
Commit ``fb6d0e61ebcad3098dc6298bc40386cacc4ad38a`` on the
``dual-npu-main-integration`` branch contains everything required for this
Learning Path: the camera and display support from the upstream Alif SDK
``main`` branch, plus the ``dual_npu_vision`` application. Use the fork and
revision shown in the command. Do not initialize from
``alifsemi/sdk-alif`` directly because the dual-NPU application has not yet
been merged there. The fork's ``main`` branch remains synchronized with the
upstream Alif SDK and does not contain the application.
{{% /notice %}}

Initialize the ExecuTorch submodules:

```bash
git -C modules/lib/executorch submodule update --init --recursive
```

## Add the multi-variant dependencies

The demo uses the multi-variant support merged into the Ethos-U core driver
``main`` branch. This support allows one Cortex-M55 to manage the U55 and U85
through one driver registry, avoiding the system power overhead of assigning
each NPU to a separate MCU. Clone the current ``main`` branch:

```bash
git clone --branch main \
  https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver.git \
  modules/ethos-u-core-driver-src
git -C modules/ethos-u-core-driver-src merge-base --is-ancestor \
  b7cd193afde80afe8bbae9a26d2ca6586554f054 HEAD
```

The Alif west manifest also downloads Zephyr's `hal_ethos_u` module. That
module is a separately maintained snapshot and its manifest revision does not
yet contain the merged multi-variant implementation. The explicit clone above
therefore remains necessary. The ancestor test is a guard rather than a pin:
it permits newer `main` revisions while rejecting an old or stale checkout
that cannot run U55 and U85 through the same driver registry.

Clone and pin CMSIS-NN:

```bash
git clone https://github.com/ARM-software/CMSIS-NN.git \
  modules/cmsis-nn-src
git -C modules/cmsis-nn-src checkout \
  d933672e7ca97eec70ef43230baee7b20c2a28ae
```

Create the Python environment used by the ExecuTorch CMake integration:

```bash
python3.12 -m venv .venv-executorch
cd modules/lib/executorch
../../../.venv-executorch/bin/python -m pip install \
  -r requirements-examples.txt
env -u DEBUG ./install_executorch.sh
cd ../../..
```

Python 3.12 is used for compatibility with the pinned ExecuTorch revision.
Removing a host `DEBUG` variable prevents ExecuTorch from interpreting a
non-numeric shell value as its numeric build option. You do not need the
optional `ethos_u` Python dependency group for the firmware build.

Apply the sample's ExecuTorch integration patch and check the dependencies:

```bash
./sdk-alif/samples/modules/executorch/dual_npu_vision/setup_workspace.sh
```

You see output similar to:

```output
Applied ExecuTorch dual-NPU patch.
Ethos-U core driver main: ...
Workspace dependencies are ready.
```

If you run the script again, it reports that the patch is already applied. You
now have the sources and dependencies required for the build.
