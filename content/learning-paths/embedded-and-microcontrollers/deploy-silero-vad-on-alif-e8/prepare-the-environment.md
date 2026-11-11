---
title: Prepare ExecuTorch and the E8 tools
description: Pin the source and vendor SDKs, install released export dependencies, and prepare the board connection.
weight: 3
layout: learningpathall
---

## Select the host and workspace

Use an Apple silicon Mac with Python 3.12, CMake, Ninja, Git, and ripgrep installed. Install [Zephyr SDK 0.17.0](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.17.0) for macOS on Arm, including the Arm toolchain. Set its location below.

The upstream Silero example supplies the exporter and audio helpers. The downloadable application adds the E8 Zephyr target. It is a local port, so use the exact source and vendor revisions in this lesson when reproducing it.

Choose a new workspace and define the paths used throughout this Learning Path:

```bash
export ALIF_WORK="$HOME/silero-alif-e8"
export EXECUTORCH_ROOT="$ALIF_WORK/executorch"
export ZEPHYR_BASE="$ALIF_WORK/zephyr_alif"
export SDK_ALIF="$ALIF_WORK/sdk-alif"
export SILERO_OUTPUT="$ALIF_WORK/model-and-builds"
export SILERO_BUILD="$SILERO_OUTPUT/build-alif"
export ZEPHYR_SDK_INSTALL_DIR=/absolute/path/to/zephyr-sdk-0.17.0
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
mkdir -p "$ALIF_WORK" "$SILERO_OUTPUT"
```

## Get the model source and E8 application

Clone the pinned ExecuTorch source, including its build dependencies:

```bash
git clone https://github.com/pytorch/executorch.git "$EXECUTORCH_ROOT"
git -C "$EXECUTORCH_ROOT" checkout --detach \
  12dac4aa042b66a7229e8d7d3af2bdde8c9f262f
git -C "$EXECUTORCH_ROOT" submodule update --init --recursive
```

Download the [E8 Silero application](../silero-alif-e8.zip) and save it as `$ALIF_WORK/silero-alif-e8.zip`. The archive contains source code for `zephyr/samples/silero-vad-ethosu`, its license notices, and a README. It contains no model weights or audio.

Check the archive hash, then extract it into the new checkout:

```bash
shasum -a 256 "$ALIF_WORK/silero-alif-e8.zip"
unzip "$ALIF_WORK/silero-alif-e8.zip" -d "$EXECUTORCH_ROOT"
test -f "$EXECUTORCH_ROOT/zephyr/samples/silero-vad-ethosu/src/main.cpp"
```

The expected SHA256 is `7c671b6665bdf11d087cc4574fd8def27a75b2c5f8ec3b3db0a7ef83eac32f78`.

## Pin the vendor board support

This application uses Alif's Zephyr fork and SDK. The board name and NPU configuration below belong to these revisions:

```bash
git clone https://github.com/alifsemi/zephyr_alif.git "$ZEPHYR_BASE"
git -C "$ZEPHYR_BASE" checkout --detach \
  f002a4d8499c35fc70ec4d5324faa7b01c152c72
git clone https://github.com/alifsemi/sdk-alif.git "$SDK_ALIF"
git -C "$SDK_ALIF" checkout --detach \
  1db82c9d0cc594e2b548a13699e8a4157e6dcd4c
```

The selected target is `alif_e8_dk/ae822fa0e5597xx0/rtss_hp`: the Cortex-M55 HP core with an Ethos-U85-256. Do not substitute the HE target or an older sample's U55 configuration.

## Install released Python dependencies

Create an isolated environment for export and firmware code generation:

```bash
python3.12 -m venv "$ALIF_WORK/.venv"
source "$ALIF_WORK/.venv/bin/activate"
python -m pip install "torch==2.14.0" \
  --index-url https://download.pytorch.org/whl/cpu
python -m pip install "executorch[ethos_u]==1.5.1" \
  "torchao==0.18.0" "cmake<4" "west==1.5.0" fdt pytest
python -m pip install -r "$ZEPHYR_BASE/scripts/requirements.txt"
```

These are released packages. The wheel supplies host export and code-generation components; the pinned source supplies the example scripts and the C++ runtime built for Zephyr. Keep this environment active for both operations. The source revision and wheel version are separate pins, so retain the model/firmware validation results for this combination.

The `ethos_u` extra installs Vela and TOSA tooling. This board workflow uses the Zephyr SDK compiler and does not require an FVP installation. Do not run the source tree's general nightly dependency installer over this environment.

## Initialize the vendor west workspace

Initialize west once in the new workspace, resolve the vendor modules, and save the resolved versions:

```bash
cd "$ALIF_WORK"
west init -l "$ZEPHYR_BASE"
west update
west zephyr-export
west manifest --freeze > "$SILERO_OUTPUT/west-manifest.yml"
python -m pip freeze > "$SILERO_OUTPUT/python-requirements.txt"
cd "$EXECUTORCH_ROOT"
```

If resuming an existing workspace, verify its manifest instead of initializing it again. The pinned vendor manifest includes moving module references. Save the frozen manifest above with each build; the Zephyr and SDK commit pins alone do not lock every west project.

## Prepare the board tools

Install Alif Security Toolkit for your E8 silicon revision and SEGGER J-Link. Follow the Security Toolkit and debug-probe portions of the [E8 board setup guide](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/). Its CMSIS application build is a separate example.

Connect the board's **PRG USB** port with a data-capable cable, retain the vendor jumper settings, and leave **SW4 on SEUART** for programming. Confirm that the host discovers the serial port and J-Link probe. Close applications holding the programming serial port.

The E8 DevKit has an onboard USB-to-UART bridge. SW4 routes it to SEUART for programming or UART4 for the HP application console at 115200 baud, 8N1. No separate adapter is required. The programming lesson shows the single switch change to UART4 after flashing and the return to SEUART before any later programming.

Set the installed tool locations and HP device:

```bash
export ALIF_SE_TOOLS_DIR=/absolute/path/to/alif-security-toolkit
export JLINK_COMMANDER=/absolute/path/to/JLinkExe
export ALIF_DEVICE=AE822FA0E5597LS0_M55_HP
test -d "$ALIF_SE_TOOLS_DIR/build/config"
test -x "$JLINK_COMMANDER"
command -v west
```

Match the toolkit's A0/A1 configuration to your actual board. The device above selects the HP core; it does not detect the silicon revision for you.

## What you've accomplished

You have selected the source, E8 vendor revisions, released Python packages, and board tools. Next, generate the quantized streaming model and its matching probability reference.
