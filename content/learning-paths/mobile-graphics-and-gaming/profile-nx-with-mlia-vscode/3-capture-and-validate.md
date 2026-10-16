---
title: Capture and validate NX profiling data
description: Collect one dispatch with the Neural Statistics layer, retrieve its complete capture tree, and restore the Android device settings.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Record the existing device settings

Continue in the same Bash terminal, with the device selected and Scenario Runner installed. Create a unique name for this execution and a host directory for its settings and capture archive:

```bash
cd "$NX_WORKSPACE"
export RUN_NAME="nx-$(date +%Y%m%d-%H%M%S-%N)"
export RUN_DIR="$NX_WORKSPACE/runs/$RUN_NAME"
export CAPTURE_NAME="capture-$RUN_NAME"
export STAGING="/data/local/tmp/$RUN_NAME"
mkdir -p "$RUN_DIR"
```

The layer rejects an existing capture directory. Use a new run name every time you collect data, including retries after a failed capture.

Android's GPU debug-layer settings are global. Save the four values you will change and the layer-settings property before enabling capture:

```bash
for key in enable_gpu_debug_layers gpu_debug_app gpu_debug_layer_app gpu_debug_layers; do
    adb shell settings get global "$key" > "$RUN_DIR/$key.before"
done
adb shell getprop debug.vulkan.khronos_profiles.settings_path > "$RUN_DIR/settings-path.before"
adb shell getprop ro.product.model > "$RUN_DIR/device-model.txt"
adb shell getprop ro.build.version.release > "$RUN_DIR/android-version.txt"
```

Keep these files for restoration at the end of this page.

## Stage the workload and layer

Copy the workload through a fresh staging directory, make it readable, and transfer it into the application's private storage:

```bash
adb push "$NX_WORKSPACE/workload" "$STAGING"
adb shell chmod -R a+rX "$STAGING"
adb shell run-as "$PACKAGE" mkdir -p "files/$RUN_NAME"
adb shell run-as "$PACKAGE" cp -r "$STAGING/." "files/$RUN_NAME/"
```

Stage the Android layer library and copy it into the application's private directory:

```bash
adb push "$LAYER_LIB" "$STAGING/libVkLayerNeuralStatistics.so"
adb shell chmod a+r "$STAGING/libVkLayerNeuralStatistics.so"
adb shell run-as "$PACKAGE" cp "$STAGING/libVkLayerNeuralStatistics.so" .
```

The Vulkan loader can load the library from the app's private directory. `run-as` gives access as the debuggable application without root access; shared storage such as `/sdcard` can restrict library loading.

## Select one dispatch to capture

Create the layer settings on the host:

```bash
cat > "$RUN_DIR/vk_layer_settings.txt" <<EOF
lgl_neural_statistics.capture_folder = /data/data/$PACKAGE/files/$CAPTURE_NAME
lgl_neural_statistics.statistics_mode = 1
lgl_neural_statistics.dispatch_filter = 0
EOF
```

Mode `1` requests neural statistics. Filter `0` selects the first executed dispatch occurrence, using zero-based numbering. It is an occurrence filter, not a model-operation index. This example runs the generated scenario once.

The capture path is an absolute application-private path. Keep the `/data/data/$PACKAGE/files/` form used here; the application might not be able to write under `/data/local/tmp`.

Push the settings file, enable the layer for Scenario Runner, and force-stop the application so the next launch loads the configuration:

```bash
export SETTINGS_PATH="$STAGING/vk_layer_settings.txt"
adb push "$RUN_DIR/vk_layer_settings.txt" "$SETTINGS_PATH"
adb shell chmod a+r "$SETTINGS_PATH"
adb shell setprop debug.vulkan.khronos_profiles.settings_path "$SETTINGS_PATH"
adb shell settings put global enable_gpu_debug_layers 1
adb shell settings put global gpu_debug_app "$PACKAGE"
adb shell settings put global gpu_debug_layer_app "$PACKAGE"
adb shell settings put global gpu_debug_layers VK_LAYER_LGL_neural_statistics
adb shell am force-stop "$PACKAGE"
```

## Execute the scenario

Launch Scenario Runner's foreground service with the scenario and output paths in application-private storage:

```bash
DEVICE_DIR="/data/data/$PACKAGE/files/$RUN_NAME"
RUN_ARGS="--scenario,$DEVICE_DIR/scenario.json,--output,$DEVICE_DIR,--repeat,1,--log-level,debug"
adb shell am start-foreground-service -n "$PACKAGE/.Main" --esa args "$RUN_ARGS"
adb logcat -v time -s ScenarioService ScenarioRunner VkLayerNeuralStatistics vulkan AndroidRuntime
```

Check timestamps in the log so that you inspect the launch you just made.

The expected output for a successful run includes:

```output
native exit code=0
```

Wait for this message from the current run, then stop `adb logcat` with **Ctrl+C**. A nonzero exit code or `runScenarioRunner failed` indicates a runner failure. Successful runner completion alone doesn't prove that the statistics layer captured data; check the capture separately.

## Retrieve and validate the capture

Ordinary `adb pull` cannot traverse the private capture directory. Stream its complete tree through `run-as`, then extract it on the host:

```bash
adb exec-out run-as "$PACKAGE" tar -C files -cf - "$CAPTURE_NAME" > "$RUN_DIR/capture.tar"
tar -xf "$RUN_DIR/capture.tar" -C "$NX_WORKSPACE/captures"
export CAPTURE_ROOT="$NX_WORKSPACE/captures/$CAPTURE_NAME"
printf 'Profiling data: %s\n' "$CAPTURE_ROOT"
```

Preserve the complete directory hierarchy. MLIA needs the related metadata and binary payloads, not just the statistics file. A typical single-dispatch capture has this structure:

```text
capture-<run-name>/
  capture.json
  pipeline_000000/
    pipeline.json
    debug_database.bin
    neural_statistics_info.bin
    session_000000/
      session.json
      dispatch_000000/
        dispatch.json
        statistics_mode1.bin
```

Open `capture.json` and confirm that `status` is `complete`, `capture.statistics_mode` is `1`, and there are no unexpected warnings. Check that the capture includes pipeline and dispatch directories with statistics files. MLIA validates the capture files when it loads the directory.

Keep the printed **Profiling data** path for the next page. This is `$CAPTURE_ROOT`, the extracted directory directly containing `capture.json`. Keep the capture terminal open so you can reuse the variable when selecting the analysis inputs.

If you encounter a problem, preserve the available files and use these checks before analysis:

| Symptom | Check |
| --- | --- |
| `run-as` fails | Install the debuggable APK and use the same package name throughout. |
| The layer cannot be found | Confirm the Arm64 library is in the application's private directory, the layer name matches, and the application was force-stopped before launch. |
| The capture is missing | Check the settings-file property, its readability, the application package, and the app-private capture path. |
| The capture is incomplete or empty | Check driver support, runner errors, dispatch filter `0`, and whether the workload finished. |
| The capture directory already exists | Start again with a new run name and settings file. |

See the [capture-layer troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting) for further diagnostics.

## Restore the device settings

After retrieving the capture, stop Scenario Runner and restore the device's previous GPU debug-layer configuration. Do this after a failed capture too, before using the device for other work.

If the four saved settings are `null` and `settings-path.before` is empty, the device had no previous configuration. Use these cleanup commands from the [capture guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#restore-the-device):

```bash
adb shell am force-stop "$PACKAGE"

adb shell settings delete global enable_gpu_debug_layers
adb shell settings delete global gpu_debug_app
adb shell settings delete global gpu_debug_layer_app
adb shell settings delete global gpu_debug_layers
adb shell "setprop debug.vulkan.khronos_profiles.settings_path ''"
```

If the backups show an existing configuration, force-stop Scenario Runner and use `adb shell settings put global` to restore the saved setting values. Use `adb shell setprop debug.vulkan.khronos_profiles.settings_path` to restore the saved settings-file path. Delete only settings that were previously unset, and clear the property only if its saved value was empty.

If ADB reports an error, reconnect the same device and complete restoration before continuing.

Keep the host capture and backup files. The application-private workload and library can remain for another capture; they aren't active when their layer configuration is disabled. If you remove the library later, first confirm that no restored configuration still needs it.

To repeat the exercise, return to **Record the existing device settings** and create a new run name. If another GPU debugging application was configured before this capture, relaunch it and confirm its previous layer configuration works.

## What you've accomplished and what's next

You've collected a structured NX capture, checked its completion and statistics payloads, copied it to the host, and restored the device settings. Next, you'll import the capture and its matching VGF into MLIA for VS Code.
