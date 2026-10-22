---
title: Prepare the Android workload
description: Prepare Scenario Runner and generate a scenario from the VGF model you will profile on NX hardware.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the host tools and device

Continue in the Bash terminal from the previous page.

This example uses Scenario Runner to execute `workload/model.vgf` with `workload/scenario.json` on your NX device. The Neural Statistics layer records the execution for MLIA to analyze.

**Using an existing application:** Scenario Runner is optional. You can instead capture a debuggable Android application that executes your model through the Vulkan data-graph APIs, including an application with its own VGF runtime. The same Neural Statistics layer captures its dispatches without a Scenario Runner scenario file. Follow the [existing-application capture instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#capture-an-existing-vulkan-data-graph-application), adapting the package name, paths, and launch steps. This Learning Path's commands and capture helper use Scenario Runner; after collecting your application's capture, continue with [Analyze measured performance in VS Code](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/4-analyze-in-vscode/) using the capture and its matching VGF.

For the Scenario Runner example below, prepare these host tools:

| Tool | Version or requirement |
| --- | --- |
| Python | Python 3.12 with virtual environment support |
| Device connection | Android Debug Bridge (ADB) |
| Download and extraction | `curl` and `tar` |

If you choose Scenario Runner, you'll also need a debuggable Android Arm64 Scenario Runner v0.11.0 APK. If you need to build it, follow the [Scenario Runner setup and build guide](https://github.com/arm/ai-ml-sdk-scenario-runner/blob/v0.11.0/README.md#cloning-the-repository), then return here. Select SDK manifest `v2026.09.0` by adding `-b v2026.09.0` to `repo init`. Use the guide's Android APK build command with `--package-version 0.11.0`. Keep its SDK build environment separate from your model-export environment.

If you build the APK, use JDK 17, Gradle 8.4, Android SDK 34 with build-tools 34.0.0, and NDK r28c (`28.2.13676358`). Use `-j 4` on a four-vCPU host, or fewer jobs if memory is limited. Android cross-compilation is experimental.

The manifest selects Scenario Runner and VGF Library v0.11.0, which support the VGF 0.4.3 model exported on the previous page. Download Neural Statistics layer v1.0.0 separately in the final step. The extension's [capture guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md) describes the capture procedure.

Enable **Developer options > USB debugging** on your NX device, connect it, and check ADB:

```bash
adb devices -l
```

The device must appear with status `device`. Unlock it and accept the authorization prompt if it shows `unauthorized`. If several devices are connected, select one for every command in this terminal:

```bash
export ANDROID_SERIAL="<your-device-serial>"
```

Replace the placeholder with the serial shown by ADB. Save the device's Vulkan information:

```bash
adb shell cmd gpu vkjson > "$NX_WORKSPACE/device-vulkan.json"
```

Open `device-vulkan.json` in VS Code and find the Arm GPU's `driverInfo`. Check for the documented r56p0 revision, such as a value beginning `v1.r56p0-`. Check that the same device lists `VK_ARM_data_graph` and `VK_ARM_data_graph_neural_accelerator_statistics` among its extensions.

If the command is unavailable, the driver differs from r56p0, or either extension is missing, confirm support with your device provider before continuing. These checks establish advertised capabilities; executing the scenario and collecting statistics will verify this workload on the device.

## Select the Scenario Runner APK

Set the path to your debug APK. Replace the example path with the file's absolute location on your host:

```bash
export APK="/path/to/ai-ml-sdk-scenario-runner-0.11.0-debug.apk"
test -s "$APK"
```

Continue only if the file exists and contains data. The debug build permits the `run-as` commands used for capture.

## Generate a scenario for your model

Download the prebuilt Linux x86-64 tools from the [VGF Library v0.11.0 release](https://github.com/arm/ai-ml-sdk-vgf-library/releases/tag/release/v0.11.0) for your Ubuntu host:

```bash
cd "$NX_WORKSPACE"
mkdir -p tools/vgf-lib-0.11.0
curl -fL https://github.com/arm/ai-ml-sdk-vgf-library/releases/download/release/v0.11.0/ai_ml_sdk_vgf_library-0.11.0-Linux_x86_64.tar.gz \
    -o vgf-library-0.11.0-linux-x86_64.tar.gz
tar -xzf vgf-library-0.11.0-linux-x86_64.tar.gz -C tools/vgf-lib-0.11.0
export VGF_DUMP="$NX_WORKSPACE/tools/vgf-lib-0.11.0/bin/vgf_dump"
"$VGF_DUMP" --help
```

The help output should list `--input`, `--output`, and `--scenario-template`. Generate a scenario from the exact model copied on the previous page:

```bash
"$VGF_DUMP" \
    --input workload/model.vgf \
    --output workload/scenario.json \
    --scenario-template
```

Remove the generated tensor-file placeholders with this script. It changes only tensor `src` and `dst` properties beginning `TEMPLATE_PATH_TENSOR_` and preserves the graph's `src: "model.vgf"`:

```bash
python - <<'PY'
import json
from pathlib import Path

path = Path("workload/scenario.json")
scenario = json.loads(path.read_text())
for resource in scenario["resources"]:
    tensor = resource.get("tensor", {})
    for key in ("src", "dst"):
        if tensor.get(key, "").startswith("TEMPLATE_PATH_TENSOR_"):
            del tensor[key]
path.write_text(json.dumps(scenario, indent=4) + "\n")
PY
```

All generated dimensions, formats, identifiers, bindings, and commands remain in place.

An input tensor without `src` is initialized to zero by Scenario Runner. An output without `dst` isn't written to a file. These settings are sufficient to exercise the graph and capture statistics. To measure representative inference later, supply matching input tensors instead of zeros.

Check that the edited file is valid JSON and inspect the resources and dispatch command:

```bash
python -m json.tool workload/scenario.json
```

Confirm that no `TEMPLATE_PATH` values remain and that every referenced resource file is in `workload/`. JSON parsing checks syntax; successful execution on the device will check the workload itself.

## Install the debug APK and capture layer

Install Scenario Runner and verify that `run-as` can access the debuggable app:

```bash
export PACKAGE=com.arm.ai_ml_sdk_scenario_runner
adb install -r "$APK"
adb shell run-as "$PACKAGE" id
```

Installation should report `Success`; `run-as` should print the application's UID. If it reports `package not debuggable`, install a debug APK. Unlock the device and approve any install-over-USB prompt.

Download and extract the Android Arm64 capture layer:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
    -o "$NX_WORKSPACE/neural-statistics-layer.tar.gz"
tar -xzf "$NX_WORKSPACE/neural-statistics-layer.tar.gz" -C "$NX_WORKSPACE"
export LAYER_LIB="$NX_WORKSPACE/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so"
test -s "$LAYER_LIB"
```

The next page copies this library into the application's private storage.

## What you've accomplished and what's next

You've installed a debug runner, generated a scenario from your model, verified `run-as` access, and downloaded the capture layer. Next, you'll execute the workload with the layer enabled and retrieve a complete capture.
