---
title: (Optional) Run and profile the model on an NX device
description: Prepare a VGF scenario, execute it on an NX-capable Android device, capture neural statistics, and analyze measured performance with MLIA.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

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

Your device should appear with the status `device`. If several devices are connected, set `ANDROID_SERIAL` to the intended serial. This workflow assumes that ADB can install APKs and configure GPU debug-layer settings on your device.

Follow the [Scenario Runner Android build instructions](https://github.com/arm/ai-ml-sdk-scenario-runner#building-with-the-script) to build a debuggable Android arm64 APK. This experimental build needs the Android NDK, Android SDK, Gradle, and public SDK source dependencies. Use VGF Library `release/v0.11.0` to match the host tools used here.

Use the unmodified runner with the public Neural Statistics layer. The capture setup enables **Enable GPU debug layers**, selects the runner application, and activates `VK_LAYER_LGL_neural_statistics` through ADB.

## Prepare the baseline scenario on the host

Run the remaining host commands from `mlia-demo` in the same Bash shell, and stop if any command fails. Create a separate environment for the public VGF tools and LiteRT CPU runtime. This keeps their packages separate from the tested MLIA installation:

```bash
python3.12 -m venv nx-tools-venv
source nx-tools-venv/bin/activate
python -m pip install \
  ai-ml-sdk-vgf-library==0.11.0 \
  ai-edge-litert==2.3.0
python -m pip check
mkdir -p nx-demo
cp runs/baseline/mlia-output/ml-sdk-model-converter/baseline.vgf \
  nx-demo/baseline.vgf
vgf_dump --input nx-demo/baseline.vgf \
  --output nx-demo/scenario-template.json \
  --scenario-template
```

The dump tool generates tensor bindings and shapes from the VGF, following the SDK's [scenario preparation workflow](https://github.com/arm/ai-ml-sdk-for-vulkan/blob/main/docs/source/vgf_run_tutorial.rst). The baseline has one unsigned eight-bit input with shape `[1, 224, 224, 3]` and one unsigned eight-bit output with shape `[1, 1001]`.

Replace the template placeholders, create a synthetic input, and compute a CPU reference from the original LiteRT model:

```bash
python - <<'PY'
from pathlib import Path
import numpy as np
from ai_edge_litert.interpreter import Interpreter, OpResolverType

folder = Path("nx-demo")
template = (folder / "scenario-template.json").read_text()
assert "TEMPLATE_PATH_TENSOR_INPUT_0" in template
assert "TEMPLATE_PATH_TENSOR_OUTPUT_0" in template
scenario = template.replace("TEMPLATE_PATH_TENSOR_INPUT_0", "input.npy")
scenario = scenario.replace("TEMPLATE_PATH_TENSOR_OUTPUT_0", "output.npy")
assert "TEMPLATE_PATH_" not in scenario, "Resolve every scenario placeholder."
(folder / "scenario.json").write_text(scenario)

input_data = np.full((1, 224, 224, 3), 128, dtype=np.uint8)
np.save(folder / "input.npy", input_data)
interpreter = Interpreter(
    model_path="mlia-demo-models/mobilenet_v1_0.25_224_quant.tflite",
    experimental_op_resolver_type=OpResolverType.BUILTIN_REF,
)
interpreter.allocate_tensors()
model_input = interpreter.get_input_details()[0]
model_output = interpreter.get_output_details()[0]
assert tuple(model_input["shape"]) == input_data.shape
assert model_input["dtype"] == input_data.dtype
interpreter.set_tensor(model_input["index"], input_data)
interpreter.invoke()
reference = interpreter.get_tensor(model_output["index"])
np.save(folder / "reference.npy", reference)
print(f"Reference shape: {reference.shape}; dtype: {reference.dtype}")
PY
```

The expected final output is:

```output
Reference shape: (1, 1001); dtype: uint8
```

This synthetic tensor is a smoke-test input, not a representative image or an accuracy test. For real evaluation, reproduce the model's resizing, layout, normalization, and input quantization. Use exactly the same input tensor for the CPU reference and device execution.

`BUILTIN_REF` explicitly selects LiteRT's [reference CPU kernels](https://developers.google.com/edge/api/tflite/python/tf/lite/experimental/OpResolverType) for this validation. During device testing, the default XNNPACK-delegated CPU run differed by one quantization level in 19 of 1001 outputs; the reference and non-delegated CPU kernels both matched the device exactly. The example retains strict equality against the reference kernels rather than relaxing the comparison tolerance.

## Install the APK and transfer the workload

Set `NX_RUNNER_APK` to the debug APK you built and install it with ADB:

```bash
export NX_RUNNER_APK=/absolute/path/to/ai-ml-sdk-scenario-runner-debug.apk
test -f "$NX_RUNNER_APK"
adb install -r "$NX_RUNNER_APK"
```

The expected final output is:

```output
Success
```

After installation, transfer the workload into the application's own storage and confirm that the host and device checksums match:


```bash
export PACKAGE=com.arm.ai_ml_sdk_scenario_runner
adb shell run-as "$PACKAGE" mkdir -p files/nx-demo
for filename in baseline.vgf scenario.json input.npy; do
  adb shell -T "run-as $PACKAGE sh -c 'cat > files/nx-demo/$filename'" \
    < "nx-demo/$filename"
  HOST_SHA=$(sha256sum "nx-demo/$filename" | cut -d ' ' -f 1)
  DEVICE_SHA=$(adb shell run-as "$PACKAGE" sha256sum "files/nx-demo/$filename" \
    | tr -d '\r' | cut -d ' ' -f 1)
  test "$HOST_SHA" = "$DEVICE_SHA" || exit 1
  printf "Transferred and verified %s\n" "$filename"
done
```

The expected output is:

```output
Transferred and verified baseline.vgf
Transferred and verified scenario.json
Transferred and verified input.npy
```


## Download and install the capture layer

Download the public Android arm64 layer release used for this example:

```bash
curl --fail --location \
  https://github.com/arm/vulkan-layer-neural-statistics/releases/download/v1.0.0/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
  --output nx-demo/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz
tar -xzf nx-demo/VkLayerNeuralStatistics-android-arm64-v8a.tar.gz \
  -C nx-demo
export LAYER_LIB="$PWD/nx-demo/VkLayerNeuralStatistics-android-arm64-v8a/libVkLayerNeuralStatistics.so"
test -f "$LAYER_LIB"
```

Copy the library into the runner's application-owned data directory and verify the transfer:

```bash
adb shell -T "run-as $PACKAGE sh -c 'cat > libVkLayerNeuralStatistics.so'" \
  < "$LAYER_LIB"
HOST_SHA=$(sha256sum "$LAYER_LIB" | cut -d ' ' -f 1)
DEVICE_SHA=$(adb shell run-as "$PACKAGE" sha256sum libVkLayerNeuralStatistics.so \
  | tr -d '\r' | cut -d ' ' -f 1)
test "$HOST_SHA" = "$DEVICE_SHA" || exit 1
printf "Capture layer transferred and verified.\n"
```

The expected final output is:

```output
Capture layer transferred and verified.
```

Android loads this library from the runner's data directory.

## Configure one measured dispatch

Mode `1` collects neural statistics, and filter `0` selects the first executed dispatch. Configure the layer for the runner application:

{{% notice Good practice %}}
Each capture needs a new directory; the timestamp supplies one. GPU debug-layer settings persist and can affect later app runs. Preserve any existing debug configuration you need, and restore it or disable the layer when you're finished.
{{% /notice %}}

```bash
export CAPTURE_NAME="neural-statistics-capture-$(date +%Y%m%d-%H%M%S)"
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
adb shell setprop debug.vulkan.khronos_profiles.settings_path \
  "$SETTINGS_PATH"
```

The layer writes the capture into the runner's application-owned storage. The [public layer settings and capture format](https://github.com/arm/vulkan-layer-neural-statistics) describe the generated files.

## Execute the graph with capture enabled

Start the runner's foreground service. The profiling file collects Vulkan timestamps separately from the structured neural statistics capture:

```bash
DEVICE_DIR="/data/data/$PACKAGE/files/nx-demo"
adb shell am force-stop "$PACKAGE"
adb shell am start-foreground-service \
  -n "$PACKAGE/.Main" \
  --esa args "--scenario,$DEVICE_DIR/scenario.json,--profiling-dump-path,$DEVICE_DIR/profiling.json,--repeat,1"
adb logcat -s ScenarioService ScenarioRunner VkLayerNeuralStatistics vulkan AndroidRuntime
```

The successful run includes this log message:

```output
native exit code=0
```

Stop `adb logcat` with **Ctrl+C** after this message appears. Confirm that the statistics layer loaded and the workload used the intended native NX backend. A nonzero code or a `runScenarioRunner failed` message means you need to inspect the runner and driver diagnostics.

After the workload completes, retrieve its output, timestamp profiling, and complete capture tree:

```bash
adb exec-out run-as "$PACKAGE" cat files/nx-demo/output.npy \
  > nx-demo/output.npy
adb exec-out run-as "$PACKAGE" cat files/nx-demo/profiling.json \
  > nx-demo/profiling.json
adb exec-out run-as "$PACKAGE" tar -C files -cf - "$CAPTURE_NAME" \
  > nx-demo/neural-statistics-capture.tar
mkdir -p nx-demo/captures
tar -xf nx-demo/neural-statistics-capture.tar -C nx-demo/captures
```

Ordinary `adb pull` can't traverse application-owned capture storage. Streaming a tar archive through `run-as` preserves the hierarchy and its metadata without root access.

## Validate output and capture completion

First, check the device's output against the CPU reference:

```bash
python - <<'PY'
from pathlib import Path
import numpy as np

folder = Path("nx-demo")
actual = np.load(folder / "output.npy", allow_pickle=False)
reference = np.load(folder / "reference.npy", allow_pickle=False)
assert actual.shape == reference.shape, "Output shape mismatch."
assert actual.dtype == reference.dtype, "Output data type mismatch."
np.testing.assert_array_equal(actual, reference)
print("Device output matches the CPU reference for this input.")
PY
```

The expected output is:

```output
Device output matches the CPU reference for this input.
```

Verify that the neural statistics capture completed:

```bash
python - <<'PY'
import json
import os
from pathlib import Path

folder = Path("nx-demo")
capture_dir = folder / "captures" / os.environ["CAPTURE_NAME"]
metadata = json.loads((capture_dir / "capture.json").read_text())
assert metadata["schema_version"] == 2, "Check the capture format and MLIA versions."
assert metadata["status"] == "complete", "The capture didn't finish successfully."
assert metadata["capture"]["statistics_mode"] == 1, "Expected a mode-1 capture."
assert metadata["pipelines"], "No pipeline was captured."
dispatches = list(capture_dir.glob("pipeline_*/session_*/dispatch_*/dispatch.json"))
assert dispatches, "No dispatch was captured."
for dispatch in dispatches:
    statistics = dispatch.parent / "statistics_mode1.bin"
    assert statistics.is_file() and statistics.stat().st_size > 0, "Missing statistics payload."
print(f"Capture complete; statistics mode: {metadata['capture']['statistics_mode']}")
print(f"Captured dispatches: {len(dispatches)}; warnings: {metadata.get('warnings', [])}")
PY
```

For this baseline model, the output is similar to:

```output
Capture complete; statistics mode: 1
Captured dispatches: 1; warnings: []
```

The equality check is deliberately strict. If it fails, investigate conversion, bindings, preprocessing, and your driver's documented numerical behavior. Don't silently relax it to make the test pass; assess any accepted tolerance with representative data and application accuracy requirements. Review capture warnings before using the measurements.

## Analyze measured data with MLIA

Return to the MLIA environment and pass the same VGF with the complete capture directory:

```bash
source mlia-venv/bin/activate
mlia check nx-demo/baseline.vgf \
  --target-profile neural-technology \
  --performance \
  --profiling-data "nx-demo/captures/$CAPTURE_NAME" \
  --output-dir runs/baseline-measured
```

The output is similar to this abbreviated result. The `<measured ...>` placeholders are numeric cycle counts in your run; their values depend on your device and workload:

```output
Result 1: Performance
Status   ok
Producer neural-technology-profiling-data
Mode     measured
Metrics:
┌────────────────┬────────────────────┬────────┐
│ Metric         │ Value              │ Unit   │
╞════════════════╪════════════════════╪════════╡
│ total_cycles   │ <measured total>   │ cycles │
├────────────────┼────────────────────┼────────┤
│ compute_cycles │ <measured compute> │ cycles │
└────────────────┴────────────────────┴────────┘
```

`Status ok` confirms that MLIA analyzed the capture. `Mode measured` and the `neural-technology-profiling-data` producer distinguish these results from the compiler estimates. The command also prints per-entity breakdowns. Some metrics, such as inference time and throughput, can be unavailable; don't interpret a missing value as zero.

The full results are saved in `runs/baseline-measured/mlia-output/mlia-output.json`. Supplying `--profiling-data` selects the measured backend automatically, so don't add `--backend nx-performance-estimator`. Use the complete schema-version-2 capture hierarchy, not the runner's timestamp JSON or a statistics file alone.

This synthetic-input run validates execution and profiling, not model accuracy or representative performance. For benchmarks, follow the [SDK performance guidance](https://github.com/arm/ai-ml-sdk-for-vulkan/blob/main/docs/source/performance.rst) and collect repeated runs under controlled conditions.

## What you've accomplished

You've learned how to run the VGF on an NX-capable device, validate output, collect a structured neural statistics capture, and return it to MLIA for measured analysis. Use this evidence alongside model accuracy tests and end-to-end application profiling before making deployment decisions.
