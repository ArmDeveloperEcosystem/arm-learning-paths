---
title: Troubleshoot the demo
description: Diagnose common workspace, camera, display, packaging, and inference failures.
weight: 7
layout: "learningpathall"
---

## Ninja is not available

If CMake reports that it cannot find Ninja, install it in the active virtual environment:

```bash
source $HOME/alif-dual-npu/.venv/bin/activate
python -m pip install ninja
```

Run the build again with `--pristine`.

## The Alif flash runner cannot import fdt

Install the Python `fdt` module in the environment that runs west:

```bash
source $HOME/alif-dual-npu/.venv/bin/activate
python -m pip install fdt
```

## The camera reports chip ID 0000 or I2C error -5

Power off the board and check the camera connection. The supplied overlay expects the MT9M114 on J16 at the selfie-camera I2C address. Reseat the flex cable and confirm that its contacts face the correct direction.

Do not combine a J16 overlay with a camera connected to J22. J22 uses the standard camera address and route.

## The display D-PHY does not lock

Confirm that the board runs SERAM 1.110.0 and that SEToolkit 1.10 generated the package. Rebuild with the full overlay list from the build section. A missing board overlay can prevent the display power and clock configuration from being applied before the Zephyr display driver starts.

## The ISP reports no empty video buffer

Confirm that `isp_route.overlay` is the final device-tree overlay in the build command. The application circulates five buffers and must return each processed buffer to the ISP queue. Do not remove the ISP configuration fragments from `vision.conf`.

## The live preview is grainy or monochrome

This symptom usually means the application is displaying packed sensor data as RGB565. Confirm that the build includes both ISP overlays and that the selected video endpoint is `isp@49046000`. The native pipeline requests planar RGB888 output from the ISP before it creates the display preview and model inputs.

## The startup test works but the live result does not change

Look for this message:

```output
dual-et: live dual-NPU pipeline started
```

Then confirm that live-frame messages and NPU interrupt counters continue to increase. If capture errors repeat, power-cycle the board, flash the package again, and recheck the camera connector and overlay order.

These checks cover the failures most likely to affect this exact hardware and software configuration.
