---
title: Prepare the Android workload
description: Prepare Scenario Runner and generate a scenario from the VGF model you will profile on NX hardware.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare Scenario Runner and connect the device

Continue in the Bash terminal from the previous page.

This example uses Scenario Runner to execute `workload/model.vgf` with `workload/scenario.json` on your NX device. The Neural Statistics layer records the execution for MLIA to analyze.

**Using an existing application:** You can also capture a debuggable Android application that runs your model through Vulkan data-graph APIs, including its own VGF runtime. Follow the MLIA docs for [capturing an existing application](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#capture-an-existing-vulkan-data-graph-application), then continue with [Analyze measured performance in VS Code](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/4-analyze-in-vscode/) using your capture and matching VGF. The commands and helper here use Scenario Runner.

For the Scenario Runner example below, prepare a debuggable Android Arm64 Scenario Runner v0.11.0 APK. To build it, follow the [MLIA Scenario Runner build instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#download-and-build-scenario-runner) in a separate terminal and virtual environment. Add `-b v2026.09.0` to `repo init`, use NDK r28c (`28.2.13676358`), and add `--package-version 0.11.0` to the APK build command. This SDK manifest selects the runner and VGF Library versions compatible with the exported VGF 0.4.3 model.

Enable **Developer options > USB debugging** on your NX device. Connect only this device and check ADB:

```bash
adb devices -l
```

The device appears with status `device` after you accept its USB-debugging authorization prompt. See the [MLIA device requirements](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md#requirements) for driver compatibility.

## Generate a scenario for your model

Download the prebuilt Linux x86-64 tools from the [VGF Library v0.11.0 release](https://github.com/arm/ai-ml-sdk-vgf-library/releases/tag/release/v0.11.0) for your Ubuntu host:

```bash
cd "$NX_WORKSPACE"
mkdir -p tools/vgf-lib-0.11.0
curl -fL https://github.com/arm/ai-ml-sdk-vgf-library/releases/download/release/v0.11.0/ai_ml_sdk_vgf_library-0.11.0-Linux_x86_64.tar.gz \
    -o vgf-library-0.11.0-linux-x86_64.tar.gz
tar -xzf vgf-library-0.11.0-linux-x86_64.tar.gz -C tools/vgf-lib-0.11.0
export VGF_DUMP="$NX_WORKSPACE/tools/vgf-lib-0.11.0/bin/vgf_dump"
```

Generate a scenario from the exported model:

```bash
"$VGF_DUMP" \
    --input workload/model.vgf \
    --output workload/scenario.json \
    --scenario-template
```

Remove the tensor-file placeholders so Scenario Runner uses zero-filled inputs and doesn't write output tensors:

```bash
python3.12 - <<'PY'
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

The script preserves the graph's `src: "model.vgf"` and its generated bindings and commands.

## Install the debug APK and capture layer

Set `APK` to the absolute path of your debug APK and install it:

```bash
export APK="/path/to/ai-ml-sdk-scenario-runner-0.11.0-debug.apk"
adb install -r "$APK"
```

Installation reports `Success`. The debug build permits the helper's `run-as` commands. For installation problems, see the [MLIA capture troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting).

Download and extract the Android Arm64 capture layer:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
    -o "$NX_WORKSPACE/neural-statistics-layer.tar.gz"
tar -xzf "$NX_WORKSPACE/neural-statistics-layer.tar.gz" -C "$NX_WORKSPACE"
export LAYER_LIB="$NX_WORKSPACE/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so"
```

## What you've accomplished and what's next

You've generated the scenario, installed Scenario Runner, and downloaded the capture layer. Next, capture one execution on the device.
