---
title: Package and flash the application
description: Use Alif SEToolkit to package the Zephyr image and model payload and write them to MRAM.
weight: 5
layout: "learningpathall"
---

The Alif boot flow uses a table of contents to load and start each processor image. The sample provides a SEToolkit JSON file that assigns the application and model payload to their validated MRAM addresses.

## Stage the images

Set `ALIF_SE_TOOLS_DIR` to your SEToolkit 1.10 application directory. This example uses the macOS package name:

```bash
cd $HOME/alif-dual-npu
export ALIF_SE_TOOLS_DIR=$HOME/Alif/alif_se_toolkit_110/app-release-exec-macos
APP=$PWD/sdk-alif/samples/modules/executorch/dual_npu_vision
```

Confirm that SEToolkit and the support objects referenced by the sample's package configuration are present:

```bash
test -x "$ALIF_SE_TOOLS_DIR/app-gen-toc"
test -x "$ALIF_SE_TOOLS_DIR/app-write-mram"
test -f "$ALIF_SE_TOOLS_DIR/build/config/app-device-config.json"
test -f "$ALIF_SE_TOOLS_DIR/build/images/a32_stub_0.bin"
test -f "$ALIF_SE_TOOLS_DIR/build/images/m55_stub_he.bin"
```

Each command completes without output when the file is present. Obtain the validated SEToolkit and firmware updates through the [Alif E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/) if any check fails.

Copy the images and package configuration into SEToolkit:

```bash
cp build-dual-npu-vision/zephyr/zephyr.bin \
  build-dual-npu-vision/model_assets.bin \
  "$ALIF_SE_TOOLS_DIR/build/images/"
cp "$APP/flash/dual-npu-vision.json" \
  "$ALIF_SE_TOOLS_DIR/build/config/"
```

## Generate and write the package

Close serial terminals connected to the board. Confirm that the boot switch is in the SE position, then run:

```bash
cd "$ALIF_SE_TOOLS_DIR"
./app-gen-toc -f build/config/dual-npu-vision.json
./app-write-mram -p
```

Wait until `app-write-mram` reports that the write completed. Do not reset or disconnect the board during this operation.

## Boot the application

Move the switch from SE to U4. Open the U4 serial port at 115200 baud, 8 data bits, no parity, and 1 stop bit. Reset the board.

The secure-enclave log shows entries for `HP_APP` and `U85MOD`. The U4 log starts with the Zephyr boot banner and the application name:

```output
*** dual ExecuTorch parallel SSD(U55) + MobileNetV2(U85) ***
```

The application is now ready to run the startup test and live camera pipeline.
