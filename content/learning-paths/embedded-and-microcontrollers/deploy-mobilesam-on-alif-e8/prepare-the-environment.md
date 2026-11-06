---
title: Prepare ExecuTorch, Zephyr, and the Alif E8
description: Install the matching MobileSAM sample source, pin the Alif SDKs, and configure the E8 programming tools.
weight: 3
layout: learningpathall
---

## Check the host and dependency requirements

Use an Apple silicon Mac. The pinned Arm setup and Python installer do not support Intel macOS for this workflow.

{{% notice Important %}}
The supplied sample patch uses released PyTorch and TorchAO packages by default. Install the exporter from this source checkout so it matches the ExecuTorch runtime used to build the firmware.
{{% /notice %}}

## Set up the MobileSAM sample source

The live-camera application uses an ExecuTorch sample revision with int8 I/O, independent prompts, camera capture, and display support. Download the [sample patch](../mobilesam-alif-e8.patch), then apply it to the matching public upstream base.

Choose a new workspace and the installed Zephyr SDK path:

```bash
export ALIF_WORK="$HOME/mobilesam-alif-e8"
export EXECUTORCH_ROOT="$ALIF_WORK/executorch"
export ZEPHYR_BASE="$ALIF_WORK/zephyr_alif"
export SDK_ALIF="$ALIF_WORK/sdk-alif"
export ZEPHYR_SDK_INSTALL_DIR=/absolute/path/to/zephyr-sdk-0.17.0
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
export MOBILE_SAM_OUTPUT="$ALIF_WORK/model-and-builds"
export MOBILE_SAM_SOURCE="$MOBILE_SAM_OUTPUT/mobile-sam/source"

mkdir -p "$ALIF_WORK" "$MOBILE_SAM_OUTPUT"
```

Save the downloaded patch as `$ALIF_WORK/mobilesam-alif-e8.patch`. Check its SHA256 with `shasum -a 256`; the expected value is:

```output
579839a6f27318833ba061b5633346303f9b11139182b417c039829445f62f03
```

Clone ExecuTorch and apply the patch to the pinned base:

```bash
git clone https://github.com/pytorch/executorch.git "$EXECUTORCH_ROOT"
cd "$EXECUTORCH_ROOT"
git checkout --detach baafd7e8eaa4ed7f7e1cacaa42db6ae16f247b2d
git apply --check "$ALIF_WORK/mobilesam-alif-e8.patch"
git apply "$ALIF_WORK/mobilesam-alif-e8.patch"
git submodule update --init --recursive
```

The patch includes the live-camera sample from revision `488e4fe96d97af1189d66916477fb017b52a2245` and updates its installer to use released CPU dependencies by default. Applying it leaves local modifications on the pinned upstream base. Installation and the four-prompt export were checked in a fresh Python 3.12 environment using the original deployment calibration image. A firmware build and hardware run with these released dependencies remain to be validated.

## Pin the vendor repositories

Clone the vendor repositories into the new workspace and select the tested revisions:

```bash
git clone https://github.com/alifsemi/zephyr_alif.git "$ZEPHYR_BASE"
git -C "$ZEPHYR_BASE" checkout --detach \
  f002a4d8499c35fc70ec4d5324faa7b01c152c72

git clone https://github.com/alifsemi/sdk-alif.git "$SDK_ALIF"
git -C "$SDK_ALIF" checkout --detach \
  1db82c9d0cc594e2b548a13699e8a4157e6dcd4c
```

The original validated build used Zephyr 4.1.0, Zephyr SDK 0.17.0, Python 3.12.13, west 1.5.0, and J-Link Commander 9.66. Install the SDK and vendor tools for your host before continuing. Use macOS on Apple silicon, matching the validated host.

## Establish the Python and Arm tools

Create a Python 3.12 environment and install the matching ExecuTorch source and Arm tools:

```bash
python3.12 -m venv "$ALIF_WORK/.venv"
source "$ALIF_WORK/.venv/bin/activate"
cd "$EXECUTORCH_ROOT"
CMAKE_GENERATOR=Ninja ./install_executorch.sh --minimal --optional-dependency ethos_u
python -m pip install torchvision==0.28.0 timm==1.0.7 west==1.5.0 fdt
./examples/arm/setup.sh --i-agree-to-the-contained-eula \
  --disable-ethos-u-deps --enable-vela
source examples/arm/arm-scratch/setup_path.sh
```

The patched installer selects released `torch==2.13.0` and `torchao==0.18.0` packages. The Ethos-U tools use Vela 5.1.0. `--minimal` skips unrelated example dependencies; the explicit package command supplies this workflow’s image and Zephyr tools. The installer still builds the ExecuTorch host components, and the Zephyr firmware is built separately in a later lesson. Keep this Python environment active for export and firmware metadata generation.

The setup flags disable FVP and GNU bare-metal toolchain installation, then enable Vela. Keep this flag order: `--disable-ethos-u-deps` also disables Vela, so `--enable-vela` must follow it. TOSA tooling still installs, and the separately configured Zephyr SDK supplies the firmware toolchain.

## Initialize the west workspace once

Use the same active Python environment for export and CMake metadata generation:

```bash
cd "$ALIF_WORK"
west init -l "$ZEPHYR_BASE"
west update
west manifest --freeze > "$MOBILE_SAM_OUTPUT/west-manifest.yml"
python -m pip install -r "$ZEPHYR_BASE/scripts/requirements.txt"
west zephyr-export
python -m pip freeze > "$MOBILE_SAM_OUTPUT/python-requirements.txt"
cd "$EXECUTORCH_ROOT"
```

Run `west init` only for a new workspace. If resuming an existing workspace, verify its manifest and revisions instead of initializing again. The vendor manifest includes moving references, including LVGL's `generic-arm-cortex-m-flagging` branch and imported debug metadata on `main`. Pinning `zephyr_alif` alone therefore does not freeze every west dependency. The original build has no retained frozen west manifest. Preserve the manifest generated above and your resolved Python dependencies with your validation results.

## Prepare board programming and debug access

Connect a data-capable USB cable to the E8's **PRG USB** port, retain the vendor's default jumper configuration, and leave **SW4 on SEUART**. A power LED alone does not establish USB data connectivity. Check that the host can discover both the serial device used by SETOOLS and the J-Link probe.

For first-time provisioning, follow the Security Toolkit and debug-probe portions of the [Arm E8 board setup guide](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/). That guide's later CMSIS image-classification application is a separate project; this tutorial uses Zephyr. Close any terminal holding SEUART before programming.

Set the paths to your installed tools:

```bash
export ALIF_SE_TOOLS_DIR=/absolute/path/to/alif-security-toolkit
export JLINK_COMMANDER=/absolute/path/to/JLinkExe
export ALIF_DEVICE=AE822FA0E5597LS0_M55_HP
command -v west
command -v expect
test -x "$JLINK_COMMANDER"
```

The validated board was revision A0. Match SETOOLS to your actual silicon revision; an A0/A1 mismatch prevents correct programming. The full device name above selects the HP core used by this sample.

Before proceeding, confirm that your source includes `zephyr/samples/mobilesam-ethosu`, your SDK contains the MT9M114 selfie overlay, and your programming tools can discover the E8.

## What you've accomplished

You have selected the matching sample source and vendor SDKs, initialized the Zephyr workspace, and configured the programming tools for E8 HP. Next, export the four-prompt model and inspect its quantization and delegation artifacts.
