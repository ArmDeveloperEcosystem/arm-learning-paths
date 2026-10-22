---
title: Capture and validate NX profiling data
description: Collect one dispatch with the Neural Statistics layer, retrieve its complete capture tree, and restore the Android device settings.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the capture helper

Continue in the same Bash terminal, with the device selected and Scenario Runner installed. Save the [capture helper](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/files/capture_nx.py) as `capture_nx.py` in `$NX_WORKSPACE`. You can inspect the script in VS Code before running it.

The helper performs the ADB staging, layer configuration, execution, and retrieval steps. It saves the current GPU debug settings before changing them and restores those values after capture, including when execution fails or you interrupt it with **Ctrl+C**.

It uses these capture settings:

| Setting | Value and purpose |
| --- | --- |
| `statistics_mode` | `1`, for neural statistics |
| `dispatch_filter` | `0`, to select the first executed dispatch occurrence, using zero-based numbering |
| Scenario repeat count | `1`, to execute this example once |
| Capture path | A unique directory under `/data/data/com.arm.ai_ml_sdk_scenario_runner/files/` |

The dispatch filter selects an execution occurrence, not a model-operation index. The application-private capture path permits the runner to write its files. The helper also places the layer library in the application's private directory so the Vulkan loader can load it without root access. The [capture guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md) describes the individual ADB operations.

Android's GPU debug-layer settings are global. Keep the selected device connected until the helper reports that restoration succeeded.

## Execute and retrieve one capture

Run the helper with the workspace and Android Arm64 layer from the previous page:

```bash
cd "$NX_WORKSPACE"
python3.12 capture_nx.py --workspace "$NX_WORKSPACE" --layer "$LAYER_LIB"
```

The helper prints a unique **Run directory** beneath `runs/`. It waits for the current Scenario Runner execution to report `native exit code=0`, retrieves the full capture tree through `run-as`, and checks that the capture is complete, uses statistics mode `1`, has no capture warnings, and includes statistics payloads.

On success, it reports **Device settings restored and verified** and **Complete mode-1 capture**. Keep the log and settings backups under the printed run directory. The workload and layer remain in application-private storage for another capture; the restored settings determine whether the layer is active.

After a successful run, set the analysis input from the saved capture path:

```bash
export CAPTURE_ROOT="$(cat "$NX_WORKSPACE/last-capture.txt")"
printf 'Profiling data: %s\n' "$CAPTURE_ROOT"
```

Each capture uses a new directory, including retries. The helper removes an earlier `last-capture.txt` when starting a run and writes it only after capture and restoration succeed, so a failed attempt cannot silently select the previous capture.

## Inspect the captured data

Open `$CAPTURE_ROOT/capture.json` in VS Code and confirm `status: complete`, `capture.statistics_mode: 1`, and an empty warnings list. The extracted directory directly containing this file is the **Profiling data** directory you will select in MLIA.

A typical single-dispatch capture has this structure:

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

Preserve the complete hierarchy. MLIA needs the related metadata and binary payloads, not just the statistics file. The helper also retains `capture.tar` in the run directory as a backup. Successful runner completion alone does not establish that the layer captured usable data; MLIA validates the capture files again when it loads the directory.

## Recover from a failed capture

If capture fails, inspect `logcat.txt` in the printed run directory before retrying:

| Symptom | Check |
| --- | --- |
| `run-as` fails | Install the debuggable APK and use the package from the previous page. |
| The layer cannot be found | Use the Android Arm64 library. Inspect the Vulkan messages in the run log. |
| Capture is missing or incomplete | Check driver support, runner errors, and layer messages in the run log. |
| Runner times out | Inspect the log. For a larger workload, increase the helper's `--timeout` value in seconds. |
| ADB disconnects or restoration fails | Reconnect the same device and complete restoration before using it for other work. |

The helper prints a recovery command if it cannot restore the previous settings. You can also retry restoration from a saved run directory. Replace the placeholder with the **Run directory** printed by your capture attempt:

```bash
python3.12 capture_nx.py --restore "$NX_WORKSPACE/runs/<run-name>"
```

This uses the device serial and settings backups saved with that run, including any previous configuration for another GPU debugging application. Wait for **Device settings restored and verified**. If ADB still reports an error, preserve the backups and resolve the connection before continuing. If another GPU debugging application was configured before capture, relaunch it and confirm its previous layer configuration works.

For additional diagnostics, see the [capture-layer troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting). After resolving the failure, rerun the capture command to create a fresh run.

## What you've accomplished and what's next

You've collected a structured NX capture, checked its completion and statistics payloads, copied it to the host, and restored the device settings. Next, you'll import the capture and its matching VGF into MLIA for VS Code.
