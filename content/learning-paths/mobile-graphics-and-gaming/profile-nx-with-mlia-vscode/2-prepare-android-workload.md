---
title: Prepare the Android workload
description: Build a debuggable Scenario Runner APK and generate a scenario from the VGF model you will profile on NX hardware.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the host tools and device

Continue in the Bash terminal from the previous page. Use the Linux host for the SDK builds, ADB connection, and MLIA extension.

Prepare these tools before building:

| Tool | Version or requirement |
| --- | --- |
| Python | Python 3.12 with virtual environment support |
| Host compiler | C++17-capable GCC or Clang |
| Build tools | CMake 3.25 or later and Ninja 1.10 or later |
| Android SDK | `platforms;android-34` and `build-tools;34.0.0` |
| Android NDK | r28c (`28.2.13676358`) |
| Java and Gradle | JDK 17 and Gradle 8.4 on `PATH` |
| Other tools | Git, the Android `repo` tool, ADB, and `curl` |

Use the [Android SDK command-line tools](https://developer.android.com/tools), [NDK installation guide](https://developer.android.com/studio/projects/install-ndk), [Repo installation instructions](https://source.android.com/docs/setup/download), and [Gradle installation guide](https://docs.gradle.org/8.4/userguide/installation.html) where needed. Builds require network access for Python packages, Gradle dependencies, and downloaded source dependencies.

The commands below use SDK manifest `v2026.09.0`, which selects Scenario Runner and VGF Library `v0.11.0`, and Neural Statistics layer `v1.0.0`. The extension's [capture guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md) describes the underlying procedure. Keep these versions together while validating this example.

Enable **Developer options > USB debugging** on your NX device, connect it, and check ADB:

```bash
adb devices -l
```

The device must appear with status `device`. Unlock it and accept the authorization prompt if it shows `unauthorized`. If several devices are connected, select one for every command in this terminal:

```bash
export ANDROID_SERIAL="<your-device-serial>"
```

Replace the placeholder with the serial shown by ADB. The device must support the model's Vulkan data-graph workload and `VK_ARM_data_graph_neural_accelerator_statistics`. A working ADB connection alone doesn't establish those capabilities. The extension documents support for Arm Mali GPU Driver r56p0.

## Build Scenario Runner

Download the SDK projects needed by Scenario Runner into the profiling workspace:

```bash
cd "$NX_WORKSPACE"
mkdir ml-sdk
cd ml-sdk
repo init -u https://github.com/arm/ai-ml-sdk-manifest -b v2026.09.0 -g scenario-runner
repo sync --no-clone-bundle
export SDK_PATH="$PWD"
repo manifest -r > "$NX_WORKSPACE/sdk-manifest.xml"
```

The resolved manifest records the source revisions used for the build. Create a separate SDK build environment and install its requirements:

```bash
python3.12 -m venv "$SDK_PATH/.venv"
source "$SDK_PATH/.venv/bin/activate"
python -m pip install -r "$SDK_PATH/sw/scenario-runner/tooling-requirements.txt"
```

Set the Android tool locations. Replace the SDK and JDK paths with your installed locations:

```bash
export ANDROID_HOME="$HOME/Android/Sdk"
export ANDROID_SDK_ROOT="$ANDROID_HOME"
export ANDROID_NDK_HOME="$ANDROID_HOME/ndk/28.2.13676358"
export JAVA_HOME=/path/to/jdk-17
export PATH="$JAVA_HOME/bin:$PATH"
java -version
gradle --version
test -f "$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake"
```

Confirm Java 17, Gradle 8.4, and an existing NDK toolchain file. Then build the debuggable Arm64 APK. The subshell matters: the build creates `apk_package` relative to its working directory.

```bash
(
cd "$SDK_PATH/sw/scenario-runner"
python scripts/build.py \
    -j 8 \
    --target-platform android \
    --cmake-toolchain-for-android "$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake" \
    --flatbuffers-path "$SDK_PATH/dependencies/flatbuffers" \
    --argparse-path "$SDK_PATH/dependencies/argparse" \
    --json-path "$SDK_PATH/dependencies/json" \
    --vulkan-headers-path "$SDK_PATH/dependencies/Vulkan-Headers" \
    --glslang-path "$SDK_PATH/dependencies/glslang" \
    --dxc-path "$SDK_PATH/dependencies/DirectXShaderCompiler" \
    --spirv-headers-path "$SDK_PATH/dependencies/SPIRV-Headers" \
    --spirv-tools-path "$SDK_PATH/dependencies/SPIRV-Tools" \
    --vgf-lib-path "$SDK_PATH/sw/vgf-lib" \
    --package-type apk \
    --package-version 0.11.0
)
```

Reduce `-j 8` if the host runs out of memory. The SDK describes Android cross-compilation as experimental; use the [Scenario Runner build documentation](https://github.com/arm/ai-ml-sdk-scenario-runner/tree/v0.11.0) to diagnose build failures.

Set the generated APK path and confirm that the file exists:

```bash
export APK="$SDK_PATH/sw/scenario-runner/apk_package/app/build/outputs/apk/debug/ai-ml-sdk-scenario-runner-0.11.0-debug.apk"
test -s "$APK"
```

Don't continue if the build failed or the APK is missing. The explicit package version gives the APK a predictable filename; the debug build permits the `run-as` commands used for capture.

## Generate a scenario for your model

Build the host `vgf_dump` tool from the same manifest checkout:

```bash
python "$SDK_PATH/sw/vgf-lib/scripts/build.py" -j 8
export VGF_DUMP="$SDK_PATH/sw/vgf-lib/build/vgf_dump/vgf_dump"
"$VGF_DUMP" --help
cd "$NX_WORKSPACE"
```

The help output should list `--input`, `--output`, and `--scenario-template`. Generate a scenario from the exact model copied on the previous page:

```bash
"$VGF_DUMP" \
    --input workload/model.vgf \
    --output workload/scenario.json \
    --scenario-template
```

Open `workload/scenario.json` in VS Code. In its tensor resources, remove only the `src` and `dst` properties whose values are placeholders such as `TEMPLATE_PATH_TENSOR_INPUT_0` and `TEMPLATE_PATH_TENSOR_OUTPUT_0`. Fix any trailing commas after removing a property.

Keep the graph's `src: "model.vgf"`, the generated tensor dimensions and formats, resource identifiers, bindings, and commands. The scenario generator derives these from the exported artifact; copying MobileNet's scenario or assuming Python tensor layouts would describe a different workload.

An input tensor without `src` is initialized to zero by Scenario Runner. An output without `dst` isn't written to a file. These settings are sufficient to exercise the graph and capture statistics. To measure representative inference later, supply matching input tensors instead of zeros.

Check that the edited file is valid JSON and inspect the resources and dispatch command:

```bash
python -m json.tool workload/scenario.json
```

Confirm that no `TEMPLATE_PATH` values remain and that every referenced resource file is in `workload/`. JSON parsing checks syntax; successful execution on the device will check the workload itself.

## Install the debug APK and capture layer

Install Scenario Runner and confirm that ADB can access its application identity:

```bash
export PACKAGE=com.arm.ai_ml_sdk_scenario_runner
adb install -r "$APK"
adb shell run-as "$PACKAGE" id
```

Installation should report `Success`; `run-as` should print the application's UID. If it reports `package not debuggable`, install the debug APK built above. Unlock the device and approve any install-over-USB prompt.

Download and extract the Android Arm64 capture layer:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
    -o "$NX_WORKSPACE/neural-statistics-layer.tar.gz"
tar -xzf "$NX_WORKSPACE/neural-statistics-layer.tar.gz" -C "$NX_WORKSPACE"
export LAYER_LIB="$NX_WORKSPACE/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so"
test -s "$LAYER_LIB"
```

This layer archive is separate from the SDK checkout. The next page copies it into the application's private storage, where Android's Vulkan loader can find it without root access.

## What you've accomplished and what's next

You've built a debug runner, generated a scenario from your model, verified `run-as` access, and downloaded the capture layer. Next, you'll execute the workload with the layer enabled and retrieve a complete capture.
