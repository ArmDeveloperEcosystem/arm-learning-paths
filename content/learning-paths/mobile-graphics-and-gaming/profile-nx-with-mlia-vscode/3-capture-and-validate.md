---
title: Capture NX profiling data
description: Capture one NX dispatch with the supplied helper and load the resulting directory into MLIA.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the capture helper

Continue in the same Bash terminal. Save the [capture helper](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/files/capture_nx.py) as `capture_nx.py` in `$NX_WORKSPACE`.

The helper runs the scenario once and captures the first dispatch with statistics mode `1`. It retrieves and validates the capture, then restores the device's previous GPU debug settings, including after a failed or interrupted run. Keep the device connected until restoration finishes.

## Execute and retrieve one capture

Run the helper with the workspace and Android Arm64 layer from the previous page:

```bash
cd "$NX_WORKSPACE"
python3.12 capture_nx.py --workspace "$NX_WORKSPACE" --layer "$LAYER_LIB"
```

On success, the helper reports **Device settings restored and verified** and **Complete mode-1 capture**. It saves logs and settings backups in the printed **Run directory** beneath `runs/`.

After a successful run, set the analysis input from the saved capture path:

```bash
export CAPTURE_ROOT="$(cat "$NX_WORKSPACE/last-capture.txt")"
printf 'Profiling data: %s\n' "$CAPTURE_ROOT"
```

`CAPTURE_ROOT` is the directory containing `capture.json` and the captured statistics. Select this directory as **Profiling data** in MLIA.

For capture failures, see the [MLIA capture troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting). If device restoration fails, reconnect the same device and run the recovery command printed by the helper. Wait for **Device settings restored and verified** before using the device for other work.

## What you've accomplished and what's next

You've captured one dispatch and restored the device settings. Next, open the capture and its matching VGF in MLIA for VS Code.
