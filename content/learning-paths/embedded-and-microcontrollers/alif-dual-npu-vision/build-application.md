---
title: Build the dual-NPU application
description: Configure the Zephyr overlays and build the firmware and model payload for the E8 high-performance core.
weight: 4
layout: "learningpathall"
---

The sample includes compiled PTE models for Ethos-U55 and Ethos-U85. It also includes a startup image that verifies both inference pipelines before the application starts the live camera.

## Define the build inputs

From the west workspace root, activate the Python environment and define the sample paths:

```bash
cd $HOME/alif-dual-npu
source .venv/bin/activate
APP=$PWD/sdk-alif/samples/modules/executorch/dual_npu_vision
OD=$PWD/sdk-alif/samples/modules/tflite-micro/alif_object_detection
MODULES=$(west list -f '{abspath}' | grep -v '/modules/lib/executorch$' | paste -sd';' -)
MODULES="$MODULES;$PWD/modules/lib/executorch;$PWD/modules/ethos-u-core-driver-src"
```

The overlay order matters. The final `isp_route.overlay` file disables the CPI memory endpoint and routes camera frames exclusively through the ISP.

## Build the firmware

Run the complete build command:

```bash
west build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  -d build-dual-npu-vision \
  "$APP" --pristine -- \
  -DZEPHYR_MODULES="$MODULES" \
  -DPYTHON_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DPython3_EXECUTABLE="$PWD/.venv-executorch/bin/python" \
  -DCMSIS_NN_LOCAL_PATH="$PWD/modules/cmsis-nn-src" \
  -DDTC_OVERLAY_FILE="$APP/boards/dual_npu_e8.overlay;$OD/boards/alif_e8_dk_ae822fa0e5597xx0_rtss_hp.overlay;$OD/serial_camera.overlay;$OD/serial_camera_mt9m114.overlay;$OD/serial_camera_isp.overlay;$OD/serial_camera_mt9m114_isp.overlay;$APP/isp_route.overlay" \
  -DOVERLAY_CONFIG="$APP/vision.conf"
```

A successful build ends with messages showing that Zephyr linked the ELF file and generated the binary.

Confirm that the three expected outputs exist:

```bash
ls -lh build-dual-npu-vision/zephyr/zephyr.bin \
  build-dual-npu-vision/zephyr/zephyr.elf \
  build-dual-npu-vision/u85_model.bin
```

The files have these roles:

| File | Purpose |
| --- | --- |
| `zephyr.bin` | Cortex-M55 Zephyr application |
| `zephyr.elf` | Symbols and debug information |
| `u85_model.bin` | U55 PTE, U85 PTE, and startup image payload |

You can regenerate the two PTE files with the scripts in the sample's `tools` directory. The checked-in files let you build and run this Learning Path without retraining or recompiling the models.
