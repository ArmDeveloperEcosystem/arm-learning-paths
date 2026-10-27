---
title: Prepare the Android workload
description: Prepare Scenario Runner, an Android device, and the supplied scenario file to capture an NX profile of the sample VGF model.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare Scenario Runner and connect the device

Continue in the Bash terminal from earlier.

You'll use Scenario Runner to run `workload/model.vgf` on your neural accelerator (NX) device. The Neural Statistics layer records the run for Arm ML Inference Advisor (MLIA) to analyze.

For the Scenario Runner example, prepare a debuggable Android Arm64 Scenario Runner v0.11.0 APK. To build it, follow the [MLIA Scenario Runner build instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#download-and-build-scenario-runner) in a separate terminal and virtual environment. Add `-b v2026.09.0` to `repo init`, use NDK r28c (`28.2.13676358`), and add `--package-version 0.11.0` to the APK build command. This SDK manifest selects the runner and VGF Library versions compatible with the exported VGF 0.4.3 model.

Enable **Developer options > USB debugging** on your NX device using the [Android developer options and USB debugging instructions](https://developer.android.com/studio/debug/dev-options). 

Connect only this device and check `adb`:

```bash
adb devices -l
```

The device appears with status `device` after you accept its USB-debugging authorization prompt. For information about driver compatibility, see the [MLIA device requirements](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md#requirements).

## Add the scenario file

Save the supplied [scenario file](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/files/scenario.json) as `scenario.json` in `$NX_WORKSPACE/workload`, alongside `model.vgf`.

This scenario runs the `SmallUpscalerModel` that you exported earlier with zero-filled inputs. It doesn't write output tensors.

To create a scenario for another model, see the [VGF Dump Tool documentation](https://arm.github.io/ai-ml-sdk-for-vulkan/vgf-lib/docs/in/vgf_dump.html#scenario-template) and the [Scenario Runner JSON specification](https://arm.github.io/ai-ml-sdk-for-vulkan/scenario-runner/docs/in/json.html).

## Install the debug APK and capture layer

Set `APK` to the absolute path of your debug APK and install it:

```bash
export APK="/path/to/ai-ml-sdk-scenario-runner-0.11.0-debug.apk"
adb install -r "$APK"
```

For installation problems, see the [MLIA capture troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting).

Download and extract the Android Arm64 capture layer:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
    -o "$NX_WORKSPACE/neural-statistics-layer.tar.gz"
tar -xzf "$NX_WORKSPACE/neural-statistics-layer.tar.gz" -C "$NX_WORKSPACE"
export LAYER_LIB="$NX_WORKSPACE/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so"
```

## What you've accomplished and what's next

You've prepared the scenario file, installed Scenario Runner, and downloaded the capture layer. 

Next, you'll capture one run on the device.
