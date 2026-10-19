---
title: (Optional) Run and profile the model on an NX device
description: Prepare a VGF scenario, run it on an NX-capable Android device, capture neural statistics, and analyze measured performance with MLIA.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Profile a MobileNet model with Scenario Runner

Run the quantized MobileNet V1 0.25, 224 × 224 model on your neural accelerator (NX) device and inspect its measured cycles in MLIA. Scenario Runner executes the graph through the ML Extensions for Vulkan. The Neural Statistics layer captures accelerator counters for Arm ML Inference Advisor (MLIA) to analyze.

Use `baseline.vgf` from the [baseline performance check](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/5-performance-check/) and the supplied MobileNet scenario. The constant input exercises the graph but doesn't test image-classification accuracy.

### Verify adb and build Scenario Runner

Verify that Android Debug Bridge (`adb`) is available on your development host:

```bash
adb version
```

The output is similar to:

```output
Android Debug Bridge version 1.0.41
Version 36.0.2-14143358
```

On your device, enable **Developer options** and **USB debugging**, or **Wireless debugging** if you use a wireless connection. Authorize your development host when prompted, then verify the connection:

```bash
adb devices -l
```

The output is similar to this shortened example, with the serial number for your device:

```output
List of devices attached
<device-serial>  device
```

Your device should appear with the status `device`. If several devices are connected, set the `ANDROID_SERIAL` environment variable with `export ANDROID_SERIAL="your-device-serial"`, replacing `"your-device-serial"` with the serial number for your device.

To build a debuggable Android arm64 APK, follow the [Scenario Runner 0.11.0 Android build instructions](https://github.com/arm/ai-ml-sdk-scenario-runner/tree/release/v0.11.0#building-with-the-script). This experimental build needs the Android NDK, Android SDK, Gradle, and public SDK source dependencies. Use Scenario Runner and VGF Library `release/v0.11.0` for this example.

Run the Android build command from `mlia-demo` and add `--package-version 0.11.0`. This ensures that the generated APK has the fixed filename used in subsequent commands.

The following steps configure the public Neural Statistics layer for the unmodified runner. They turn on **Enable GPU debug layers**, select the runner application, and activate `VK_LAYER_LGL_neural_statistics` through `adb`.

### Prepare the baseline scenario on the host

Run the remaining host commands from `mlia-demo` in the same Bash shell.

Create a separate environment for NumPy, copy the compiled model as `baseline.vgf`, and download the [ready-made MobileNet scenario](mobilenet-scenario.json):

```bash
python3.12 -m venv nx-tools-venv
source nx-tools-venv/bin/activate
python -m pip install numpy==2.2.6
python -m pip check
mkdir -p nx-demo
cp runs/baseline/mlia-output/ml-sdk-model-converter/baseline.tosa.vgf nx-demo/baseline.vgf
curl -fL https://learn.arm.com/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/mobilenet-scenario.json -o nx-demo/scenario.json
```

The scenario binds `baseline.vgf` to an unsigned eight-bit input with shape `[1, 224, 224, 3]` and an unsigned eight-bit output with shape `[1, 1001]`. It reads `input.npy`, executes one graph dispatch, and writes `output.npy`. These paths are relative to the scenario file, so keep the three workload files together.

Create the synthetic input tensor filled with the value `128`:

```bash
python - <<'PY'
import numpy as np

input_data = np.full((1, 224, 224, 3), 128, dtype=np.uint8)
np.save("nx-demo/input.npy", input_data)
print(f"Input shape: {input_data.shape}; dtype: {input_data.dtype}")
PY
```

The expected output is:

```output
Input shape: (1, 224, 224, 3); dtype: uint8
```

### Install the APK and transfer the workload

From `mlia-demo`, install the debug APK from the generated `apk_package` directory:

```bash
adb install -r apk_package/app/build/outputs/apk/debug/ai-ml-sdk-scenario-runner-0.11.0-debug.apk
```

The expected output is:

```output
Success
```

Pack the three workload files into an archive, then stream it into the application's storage. `run-as` accesses the debuggable runner's files without root:

```bash
PACKAGE=com.arm.ai_ml_sdk_scenario_runner
adb shell run-as "$PACKAGE" mkdir -p files/nx-demo
tar -cf nx-demo/workload.tar -C nx-demo baseline.vgf scenario.json input.npy
adb shell -T "run-as $PACKAGE tar -xf - -C files/nx-demo" < nx-demo/workload.tar
```

### Download and install the capture layer

Download the public Android arm64 layer release:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz -o nx-demo/neural-statistics-layer.tar.gz
tar -xzf nx-demo/neural-statistics-layer.tar.gz -C nx-demo
```

Copy the library into the runner's application-owned data directory:

```bash
adb shell -T "run-as $PACKAGE sh -c 'cat > libVkLayerNeuralStatistics.so'" < nx-demo/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so
```

Android loads this library from the runner's data directory.

### Configure one measured dispatch

Mode `1` collects neural statistics, and filter `0` selects the first executed dispatch. Configure the layer for the runner application:

{{% notice Note %}}
Each capture needs a new directory. The timestamp supplies one. GPU debug-layer settings persist and can affect later app runs. Preserve any existing debug configuration that you need, and restore it or disable the layer when you're finished.
{{% /notice %}}

```bash
CAPTURE_NAME="neural-statistics-capture-$(date +%Y%m%d-%H%M%S)"
cat > nx-demo/vk_layer_settings.txt <<EOF
lgl_neural_statistics.capture_folder = /data/data/$PACKAGE/files/$CAPTURE_NAME
lgl_neural_statistics.statistics_mode = 1
lgl_neural_statistics.dispatch_filter = 0
EOF
SETTINGS_PATH="/data/local/tmp/$CAPTURE_NAME-settings.txt"
adb push nx-demo/vk_layer_settings.txt "$SETTINGS_PATH"
adb shell chmod a+r "$SETTINGS_PATH"
adb shell settings put global enable_gpu_debug_layers 1
adb shell settings put global gpu_debug_app "$PACKAGE"
adb shell settings put global gpu_debug_layer_app "$PACKAGE"
adb shell settings put global gpu_debug_layers VK_LAYER_LGL_neural_statistics
adb shell setprop debug.vulkan.khronos_profiles.settings_path "$SETTINGS_PATH"
```

The layer writes the capture into the runner's application-owned storage. For more information about the format of the generated files, see the [public layer settings and capture format](https://github.com/arm/vulkan-layer-neural-statistics).

### Run the graph with capture enabled

Start the runner's foreground service. The Android `--esa args` option passes the comma-separated `RUN_ARGS` values as the runner's command-line arguments. The profiling file collects Vulkan timestamps separately from the neural statistics capture:

```bash
DEVICE_DIR="/data/data/$PACKAGE/files/nx-demo"
RUN_ARGS="--scenario,$DEVICE_DIR/scenario.json,--profiling-dump-path,$DEVICE_DIR/profiling.json,--repeat,1"
adb shell am force-stop "$PACKAGE"
adb shell am start-foreground-service -n "$PACKAGE/.Main" --esa args "$RUN_ARGS"
adb logcat -s ScenarioService ScenarioRunner VkLayerNeuralStatistics vulkan AndroidRuntime
```

The successful run includes the following log message:

```output
native exit code=0
```

Stop `adb logcat` with **Ctrl+C** after this message appears. A nonzero code or a `runScenarioRunner failed` message means that the run failed. Exit code `0` confirms runner completion. The capture checks that the layer collected neural statistics from the driver.

After the workload completes, retrieve its timestamp profiling and complete capture tree:

```bash
adb exec-out run-as "$PACKAGE" cat files/nx-demo/profiling.json > nx-demo/profiling.json
adb exec-out run-as "$PACKAGE" tar -C files -cf - "$CAPTURE_NAME" > nx-demo/neural-statistics-capture.tar
mkdir -p nx-demo/captures
tar -xf nx-demo/neural-statistics-capture.tar -C nx-demo/captures
```

Ordinary `adb pull` can't traverse application-owned capture storage. Streaming a `tar` archive through `run-as` preserves the hierarchy and its metadata without root access.

## Check capture completion

Inspect the capture metadata and locate the nonempty mode-1 statistics file:

```bash
python -m json.tool "nx-demo/captures/$CAPTURE_NAME/capture.json"
find "nx-demo/captures/$CAPTURE_NAME" -name statistics_mode1.bin -size +0c
```

In `capture.json`, check that `schema_version` is `2`, `status` is `complete`, and `capture.statistics_mode` is `1`. Review any `warnings`. For this single-dispatch scenario, the `find` command should print one path similar to:

```output
nx-demo/captures/<capture-name>/pipeline_000000/session_000000/dispatch_000000/statistics_mode1.bin
```

A completed capture with a nonempty statistics file shows that the layer intercepted the dispatch and the driver returned neural statistics. If the capture is missing, incomplete, or has no statistics payload, check the layer configuration and driver diagnostics before continuing.

## Analyze measured data with MLIA

Return to the MLIA environment and pass the same Vulkan Graph Format (VGF) file with the complete capture directory:

```bash
source mlia-venv/bin/activate
mlia check nx-demo/baseline.vgf \
  --target-profile neural-technology \
  --performance \
  --profiling-data "nx-demo/captures/$CAPTURE_NAME" \
  --output-dir runs/baseline-measured
```

The following abbreviated output comes from a device capture of this MobileNet scenario:

```output
Result 1: Performance
Status   ok
Producer neural-technology-profiling-data
Mode     measured
Metrics:
┌────────────────┬────────┬────────┐
│ Metric         │ Value  │ Unit   │
╞════════════════╪════════╪════════╡
│ total_cycles   │ 951154 │ cycles │
├────────────────┼────────┼────────┤
│ compute_cycles │ 951154 │ cycles │
└────────────────┴────────┴────────┘
```
Your cycle counts will depend on the device and its configuration.

`Status ok` confirms that MLIA analyzed the capture. The full results are saved in `runs/baseline-measured/mlia-output/mlia-output.json`.


## Use the measurements

`mlia-output.json` shows accelerator cycles and `benchmark.json` shows graph execution times. Use both when comparing your next model version on the same device.

Check the predictions on real images as well. A faster model isn't useful if it misses your accuracy target.


## What you've accomplished

You've run the VGF file on an NX-capable device, checked that Scenario Runner completed, and confirmed that the neural statistics capture contains data. You've also returned the capture to MLIA for measured analysis.

Use this evidence alongside model accuracy tests and end-to-end application profiling before making deployment decisions for your own use cases.
