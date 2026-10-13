---
title: (Optional) Run and profile the model on an NX device
description: Prepare a VGF scenario, execute it on an NX-capable Android device, capture neural statistics, and analyze measured performance with MLIA.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Run the quantized MobileNet V1 0.25, 224 × 224 model on your NX device and inspect its measured cycles in MLIA. Scenario Runner executes the graph through the ML Extensions for Vulkan. The Neural Statistics layer captures accelerator counters for MLIA to analyze.

Use `baseline.vgf` from the [baseline performance check](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/5-performance-check/) and the supplied MobileNet scenario. The constant input exercises the graph; it doesn't test image-classification accuracy.

## Verify ADB and build Scenario Runner

Verify that Android Debug Bridge (ADB) is available on your development host:

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

The output is similar to this shortened example, with your device's serial:

```output
List of devices attached
<device-serial>  device
```

Your device should appear with the status `device`. If several devices are connected, set the `ANDROID_SERIAL` environment variable with `export ANDROID_SERIAL="your-device-serial"`, replacing the value with your device's serial.

Follow the [Scenario Runner 0.11.0 Android build instructions](https://github.com/arm/ai-ml-sdk-scenario-runner/tree/release/v0.11.0#building-with-the-script) to build a debuggable Android arm64 APK. This experimental build needs the Android NDK, Android SDK, Gradle, and public SDK source dependencies. Use Scenario Runner and VGF Library `release/v0.11.0` for this example.

Run the Android build command from `mlia-demo` and add `--package-version 0.11.0` so the generated APK has the fixed filename used below.

The following steps configure the public Neural Statistics layer for the unmodified runner. They turn on **Enable GPU debug layers**, select the runner application, and activate `VK_LAYER_LGL_neural_statistics` through ADB.

## Prepare the baseline scenario on the host

Run the remaining host commands from `mlia-demo` in the same Bash shell. Create a separate environment for NumPy, copy the compiled model as `baseline.vgf`, and download the [ready-made MobileNet scenario](mobilenet-scenario.json):

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

Create the synthetic input tensor, filled with the value `128`:

```bash
python - <<'PY'
import numpy as np

input_data = np.full((1, 224, 224, 3), 128, dtype=np.uint8)
np.save("nx-demo/input.npy", input_data)
print(f"Input shape: {input_data.shape}; dtype: {input_data.dtype}")
PY
```

The expected final output is:

```output
Input shape: (1, 224, 224, 3); dtype: uint8
```

## Install the APK and transfer the workload

From `mlia-demo`, install the debug APK from the generated `apk_package` directory:

```bash
adb install -r apk_package/app/build/outputs/apk/debug/ai-ml-sdk-scenario-runner-0.11.0-debug.apk
```

The expected final output is:

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

## Download and install the capture layer

Download the public Android arm64 layer release used for this example:

```bash
curl -fL https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz -o nx-demo/neural-statistics-layer.tar.gz
tar -xzf nx-demo/neural-statistics-layer.tar.gz -C nx-demo
```

Copy the library into the runner's application-owned data directory:

```bash
adb shell -T "run-as $PACKAGE sh -c 'cat > libVkLayerNeuralStatistics.so'" < nx-demo/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so
```

Android loads this library from the runner's data directory.

## Configure one measured dispatch

Mode `1` collects neural statistics, and filter `0` selects the first executed dispatch. Configure the layer for the runner application:

{{% notice Good practice %}}
Each capture needs a new directory; the timestamp supplies one. GPU debug-layer settings persist and can affect later app runs. Preserve any existing debug configuration you need, and restore it or disable the layer when you're finished.
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

The layer writes the capture into the runner's application-owned storage. The [public layer settings and capture format](https://github.com/arm/vulkan-layer-neural-statistics) describe the generated files.

## Execute the graph with capture enabled

Start the runner's foreground service. Android's `--esa args` option passes the comma-separated `RUN_ARGS` values as the runner's command-line arguments. The profiling file collects Vulkan timestamps separately from the neural statistics capture:

```bash
DEVICE_DIR="/data/data/$PACKAGE/files/nx-demo"
RUN_ARGS="--scenario,$DEVICE_DIR/scenario.json,--profiling-dump-path,$DEVICE_DIR/profiling.json,--repeat,1"
adb shell am force-stop "$PACKAGE"
adb shell am start-foreground-service -n "$PACKAGE/.Main" --esa args "$RUN_ARGS"
adb logcat -s ScenarioService ScenarioRunner VkLayerNeuralStatistics vulkan AndroidRuntime
```

The successful run includes this log message:

```output
native exit code=0
```

Stop `adb logcat` with **Ctrl+C** after this message appears. A nonzero code or a `runScenarioRunner failed` message means the run failed. Exit code zero confirms runner completion; the capture checks that the layer collected neural statistics from the driver.

After the workload completes, retrieve its timestamp profiling and complete capture tree:

```bash
adb exec-out run-as "$PACKAGE" cat files/nx-demo/profiling.json > nx-demo/profiling.json
adb exec-out run-as "$PACKAGE" tar -C files -cf - "$CAPTURE_NAME" > nx-demo/neural-statistics-capture.tar
mkdir -p nx-demo/captures
tar -xf nx-demo/neural-statistics-capture.tar -C nx-demo/captures
```

Ordinary `adb pull` can't traverse application-owned capture storage. Streaming a tar archive through `run-as` preserves the hierarchy and its metadata without root access.

## Check capture completion

Inspect the capture metadata and locate the nonempty mode-1 statistics file:

```bash
python -m json.tool "nx-demo/captures/$CAPTURE_NAME/capture.json"
find "nx-demo/captures/$CAPTURE_NAME" -name statistics_mode1.bin -size +0c
```

In `capture.json`, check that `schema_version` is `2`, `status` is `complete`, and `capture.statistics_mode` is `1`. Review any `warnings`. For this single-dispatch scenario, the `find` command should print one path, similar to:

```output
nx-demo/captures/<capture-name>/pipeline_000000/session_000000/dispatch_000000/statistics_mode1.bin
```

A completed capture with a nonempty statistics file shows that the layer intercepted the dispatch and the driver returned neural statistics. If the capture is missing, incomplete, or has no statistics payload, check the layer configuration and driver diagnostics before continuing.

## Analyze measured data with MLIA

Return to the MLIA environment and pass the same VGF with the complete capture directory. Add `--model-explorer open` to view the measured results on the graph:

```bash
source mlia-venv/bin/activate
mlia check nx-demo/baseline.vgf \
  --target-profile neural-technology \
  --performance \
  --profiling-data "nx-demo/captures/$CAPTURE_NAME" \
  --output-dir runs/baseline-measured \
  --model-explorer open
```

The following abbreviated output comes from a device capture of this MobileNet scenario. Your cycle counts will depend on the device and its configuration:

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

`Status ok` confirms that MLIA analyzed the capture. The full results are saved in `runs/baseline-measured/mlia-output/mlia-output.json`.


## (Optional) Explore measured performance and TOSA operations

The MLIA command opens Model Explorer with the capture's results already loaded. The plugin installed during setup includes the VGF adapter, so you don't need a separate installation or launch command.

### View measured cycle counts

In the generated MLIA hierarchy, select a cycle metric from the measured performance result using the node-data controls. Expand the hierarchy and select an entity to inspect its reported cycle count. Follow the source mapping, where available, to see the related operations in **Source Model**.

These overlays show the capture's measurements, not the estimates from the earlier performance check. Use them to locate costly parts of the workload. Only entities with reported metrics have values; a missing value doesn't mean zero cycles. The `951,154` cycles shown in the CLI output are the whole-model result, not the cost of the selected convolution.

MLIA saves the visualization in `runs/baseline-measured/mlia-output/model-explorer/bundle/index.html`. Open this self-contained file to revisit or share the results without rerunning the capture or starting a server.

### Inspect a TOSA convolution

In **Source Model**, inspect `nx-demo/baseline.vgf`. The baseline graph contains 103 nodes. Expand `graph_segment_0` and select the first `CONV2D` node, between two `RESCALE` nodes.

This view exposes the TOSA operations in the VGF graph. You can see how the original MobileNet layer is represented after MLIA's LiteRT-to-TOSA conversion and VGF generation. The screenshot shows the operation's attributes, rather than a performance overlay.

![Model Explorer showing a TOSA CONV2D operation between two RESCALE nodes in baseline.vgf. The Attributes panel links to the TOSA CONV2D specification and shows the MobileNet source location, connecting the converted operation to its definition and original model.#center](model-explorer-conv2d.png "Inspect a TOSA convolution in the VGF graph")

In **ATTRIBUTES**, **opcode** identifies the TOSA operation as `CONV2D`. Select **TOSA spec: CONV2D** in the **spec** field to open the [TOSA operator definition](https://www.mlplatform.org/tosa/tosa_spec_1_0_1.html#_conv2d), including its tensor shapes, padding, stride, and dilation arguments. Compare these with the values shown for this node:

| Field | Value in this example | What it tells you |
| --- | --- | --- |
| **result type** | `uint32[1, 112, 112, 8]` | The convolution produces an intermediate tensor with a batch size of one, 112 × 112 spatial dimensions, and eight channels. |
| **arg1 stride** | `int32[2, 2]` | A stride of two reduces the 224 × 224 input to 112 × 112. |
| **debug info** | `MobilenetV1/MobilenetV1/Conv2d_0/Relu6` | Relates this TOSA operation to its source location in MobileNet. Expand the field to read the full name. |

Select the following `RESCALE` node to inspect how TOSA scales the convolution's intermediate integer result into the output's quantized range. You can also search for `DEPTHWISE_CONV2D` and follow its specification link to compare the two convolution operators.

For the editor workflow, follow the [MLIA and Model Explorer VS Code walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/). The same tools support Ethos-U analysis, with different target-specific metrics.

## Use the measurements

`mlia-output.json` shows accelerator cycles; `benchmark.json` shows graph execution times. Use both when comparing your next model version on the same device. Check its predictions on real images too—a faster model isn't useful if it misses your accuracy target.


## What you've accomplished

You've learned how to run the VGF on an NX-capable device, validate output, collect a structured neural statistics capture, and return it to MLIA for measured analysis. Use this evidence alongside model accuracy tests and end-to-end application profiling before making deployment decisions.
