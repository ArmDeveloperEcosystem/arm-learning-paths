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

The live-camera application uses int8 I/O, independent prompts, camera capture, and UART reporting. The display is disabled by default; a separate configuration enables an experimental dashboard. Download the [sample patch](../mobilesam-alif-e8.patch), then apply it to the matching public upstream base.

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
e49e11ce7becf49d4b58f3618f97f38e8bdbc8e31dd43f441fbde75e84a794ec
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

The patch starts from the live-camera sample at revision `488e4fe96d97af1189d66916477fb017b52a2245`, uses released CPU dependencies, and stages the Ethos-U headers from the pinned Zephyr driver's own module. Its default `CONFIG_MOBILESAM_DISPLAY=n` excludes display initialization and keeps the MIPI route on the camera. It removes a misleading checksum log; the writer's CRC and flash readback provide the model-integrity checks. Applying the patch leaves local modifications on the pinned upstream base. Installation and the public-image export passed with the released dependencies. The validation lesson records the exact firmware tested, integer-reference agreement, and the failed original strict PT2E comparison.

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

The application also requires the [camera and display driver patch](../alif-e8-camera-display.patch) for this exact vendor revision. Save it as `$ALIF_WORK/alif-e8-camera-display.patch`. Its SHA256 is:

```output
8bf1b9a9a6bcd4bafe854ead8645eb1f6370d67b56b6aa2bdd5395e0d8ee3961
```

Apply it before building:

```bash
git -C "$ZEPHYR_BASE" apply --check "$ALIF_WORK/alif-e8-camera-display.patch"
git -C "$ZEPHYR_BASE" apply "$ALIF_WORK/alif-e8-camera-display.patch"
```

The camera changes arm the receiver before starting the upstream sensor, publish completed frames only after the pipeline stops, and reset the idle CSI IPI at stream start. The patch also supplies frame-boundary display suspension for the optional dashboard. The default build does not enable that display path. Dashboard runs retained DSI error reports despite visibly advancing frames; enabling the extension requires accepting and investigating that known limitation. Peripheral error reporting remains enabled.

The original validated build used Zephyr 4.1.0, Zephyr SDK 0.17.0, Python 3.12.13, west 1.5.0, and J-Link Commander 9.66. Install the SDK and vendor tools for your host before continuing. Use macOS on Apple silicon, matching the validated host.

## Establish the Python and Arm tools

Create a Python 3.12 environment and install the matching ExecuTorch source and Arm tools:

```bash
python3.12 -m venv "$ALIF_WORK/.venv"
source "$ALIF_WORK/.venv/bin/activate"
cd "$EXECUTORCH_ROOT"
CMAKE_GENERATOR=Ninja ./install_executorch.sh --minimal --optional-dependency ethos_u
python -m pip install torchvision==0.28.0 timm==1.0.7 west==1.5.0 fdt
```

The patched installer selects released `torch==2.13.0` and `torchao==0.18.0` packages. Its `ethos_u` extra supplies Vela 5.1.0 and TOSA tools 2026.5.0. `--minimal` skips unrelated example dependencies; the explicit package command supplies this workflow’s image and Zephyr tools. The installer still builds the ExecuTorch host components, and the Zephyr firmware is built separately in a later lesson. Keep this Python environment active for export and firmware metadata generation.

The separately configured Zephyr SDK supplies the firmware toolchain.

## Initialize the west workspace once

Use the same active Python environment for export and CMake metadata generation:

```bash
cd "$ALIF_WORK"
west init -l "$ZEPHYR_BASE"
west update
west manifest --freeze --active-only > "$MOBILE_SAM_OUTPUT/west-manifest.yml"
python -m pip install -r "$ZEPHYR_BASE/scripts/requirements-base.txt"
python -m pip check
west zephyr-export
python -m pip freeze > "$MOBILE_SAM_OUTPUT/python-requirements.txt"
cd "$EXECUTORCH_ROOT"
```

`--active-only` freezes the active projects selected by this manifest; unused optional projects do not need to be cloned. Run `west init` only for a new workspace. If resuming an existing workspace, verify its manifest and revisions instead of initializing again. The vendor manifest includes moving references, including LVGL's `generic-arm-cortex-m-flagging` branch and imported debug metadata on `main`. Pinning `zephyr_alif` alone therefore does not freeze every west dependency. The clean vendor bootstrap completed all 58 active projects, and its frozen manifest was used for an independent firmware build with the public calibration model. Preserve the manifest generated above and your resolved Python dependencies with your validation results.

## Prepare board programming and debug access

With board power disconnected, retain the vendor's default jumper configuration and verify that **SW3 (JLOB) is set to EN**, as shown in Figure 1 of the [official Alif DK-E8 User Guide (AUGD0023)](https://alifsemi.com/download/AUGD0023).

Use the separate **SW4 UART selector on SEUART** for SETOOLS ISP programming. SW3 enables the on-board J-Link block; SW4 selects which UART reaches the USB-to-UART bridge. The programming lesson uses J-Link SWD for application MRAM, which does not depend on SW4's UART selection.

Connect a data-capable USB cable to the E8's **PRG USB** port. A power LED alone does not establish USB data connectivity. Check that the host can discover both the serial device used by SETOOLS and the J-Link probe.

For first-time provisioning, follow the Security Toolkit and debug-probe portions of the [Arm E8 board setup guide](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/). That guide's later CMSIS image-classification application is a separate project; this tutorial uses Zephyr. Close any terminal holding SEUART before programming.

Set the paths to your installed tools:

```bash
export ALIF_SE_TOOLS_DIR=/absolute/path/to/alif-security-toolkit
export JLINK_COMMANDER=/absolute/path/to/JLinkExe
export ALIF_DEVICE=AE822FA0E5597LS0_M55_HP
export ALIF_APP_CONFIG="$ALIF_SE_TOOLS_DIR/build/config/app-cpu-stubs.json"
command -v west
command -v expect
test -x "$JLINK_COMMANDER"
test -s "$ALIF_APP_CONFIG"
```

This workflow targets the tested E8 revision A0 device, `AE822FA0E5597LS0`. Use the Security Toolkit configuration for that silicon revision; an A0/A1 mismatch prevents correct programming. The full device name above selects its HP core. Other silicon revisions require separately validated board and tool configurations.

Use `ALIF_APP_CONFIG` only after confirming it contains the device configuration and companion images for your working E8 setup. If that setup uses a different application JSON, set the variable to that file instead. The programming lesson creates separate writer and live-application configurations from this template and preserves its other boot entries.

The onboard USB-to-UART bridge uses SW4 to select SEUART for SETOOLS ISP or UART4 for the HP application console. To capture application logs, disconnect board power, select UART4, and reconnect PRG USB. The application console runs at 115200 baud, 8N1. Return SW4 to SEUART before using SETOOLS ISP again; J-Link SWD uses the separate debug connection.

Before proceeding, confirm that your source includes `zephyr/samples/mobilesam-ethosu`, your SDK contains the MT9M114 selfie overlay, and your programming tools can discover the E8.

## What you've accomplished

You have selected the matching sample source and vendor SDKs, initialized the Zephyr workspace, and configured the programming tools for E8 HP. Next, export the four-prompt model and inspect its quantization and delegation artifacts.
