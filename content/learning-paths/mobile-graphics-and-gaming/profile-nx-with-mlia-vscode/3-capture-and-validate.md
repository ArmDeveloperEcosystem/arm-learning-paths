---
title: Capture NX profiling data
description: Capture one NX dispatch with the supplied helper and load the resulting directory into MLIA.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare the capture helper

Continue in the same Bash terminal. Save the [capture helper](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/files/capture_nx.py) as `capture_nx.py` in `$NX_WORKSPACE`.

The helper runs the scenario once. It captures the first dispatch with statistics mode `1`. Then, it retrieves and validates the capture, and restores the previous GPU debug settings. Keep the device connected until the helper finishes.

To run the capture steps manually, follow the [Arm ML Inference Advisor (MLIA) for Visual Studio Code capture instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#neural-technology). After retrieving the capture, set `CAPTURE_ROOT` to the extracted directory containing `capture.json`. Then, continue with [Analyze measured performance in VS Code](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/4-analyze-in-vscode/) using your capture and matching VGF model.

## Execute and retrieve one capture

Run the helper with the workspace and Android Arm64 layer from [earlier](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/2-prepare-android-workload/):

```bash
cd "$NX_WORKSPACE"
python3.12 capture_nx.py --workspace "$NX_WORKSPACE" --layer "$LAYER_LIB"
```

On success, the helper reports **Complete mode-1 capture**. It saves logs in the printed **Run directory** beneath `runs/`.

After a successful run, set the analysis input from the saved capture path:

```bash
export CAPTURE_ROOT="$(cat "$NX_WORKSPACE/last-capture.txt")"
printf 'Profiling data: %s\n' "$CAPTURE_ROOT"
```

`CAPTURE_ROOT` is the directory containing `capture.json` and the captured statistics. Select this directory as **Profiling data** in MLIA.

For capture failures, see the [MLIA capture troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/profiling-data.md#troubleshooting). If device restoration fails, reconnect the same device and run the recovery command printed by the helper.

## What you've accomplished and what's next

You've captured one dispatch.

Next, you'll open the capture and its matching VGF in MLIA for Visual Studio Code.
