---
title: Trace measured costs to Python source
description: Connect NX performance overlays to Python modules and code stacks, resolve source paths, and inspect synchronized heatmaps and CodeLens values.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check that the source locations are available

Keep the completed profiling run selected in **Analysis Runs**. Expand its performance result's **Source mappings** in **Current Analysis Run**.

Expand **Accessible locally**, find `quantize_and_export_vgf.py`, and select a reported line to open the source that produced your VGF.

If no source locations are reported, return to the model export and check both debug settings. A path mapping can't recreate metadata omitted during export. If you re-export the VGF, generate a new scenario and collect a matching capture before repeating the analysis.

If locations exist but your Python file is inaccessible, [resolve its moved path](#optional-resolve-moved-source-files), then return here. Missing framework files need not block navigation to your model, but you need at least one accessible, mapped model-source location to complete the exercise.

## Follow a costly group into the Python model

Open VS Code **Settings**, search for `vscode-mlia.syncModelExplorerSelectionToCode`, and enable **Sync Model Explorer Selection To Code**. Return to the group and measured cycle overlay you recorded:

1. Expand the group to an operation. In the side panel, inspect its `spv id`, opcode, and **debug info**. Record the Python module path from `nn_module_stack` and your model-file location from `stack_trace`, when present.
2. Switch to **Source Model** and search for the recorded opcode. Select the operation with the matching `spv id` in the same graph segment; use its attributes and connections to distinguish it from other instances of that opcode.
3. Switch to **nn_module** and locate the module path from the debug information. Expand it and confirm the operation's `spv id`. If this representation is absent, proceed directly to **code_stack**.
4. In **code_stack**, find the recorded model filename and line, expand that call-stack group, and confirm it contains the operation. Select the group with that single local source location to open and highlight the Python line.

For the supplied `SmallUpscalerModel`, module paths `net.0`, `net.2`, and `net.4` identify its first, middle, and final convolutions. For example, a mapped operation under `net.2` belongs to the middle 32-channel convolution. A source frame at `x = self.net(x)` identifies the call to the entire sequence; use the module path to distinguish the convolutions that share this call site. Your measured overlay determines which group merits investigation.

Keep the same overlay selected across views. Their groupings can change the reported aggregate, so match operations by their attributes and source metadata rather than by equal costs.

If **code_stack** is absent or a group has several source locations, use the file and line recorded from **debug info** to select the matching entry in **Source mappings**. If neither view provides a model-source location for the operation, check the export debug settings before claiming a source match.

<!-- Publication: verify and illustrate this sequence with the actual upscaler capture. Record the execution group, operation spv id, module path, source line, and measured value; add a screenshot of the mapped graph beside SmallUpscalerModel. -->

## Read source heatmaps and CodeLens

With your model source open, select the measured cycle overlay in **Current Analysis Run**. Inspect its source presentation:

- Numeric heatmap colors show relative values across mapped lines. They help locate regions to inspect; red doesn't by itself establish a performance defect.
- CodeLens displays the selected value and, when it can be calculated safely, its percentage of the model total.
- Selecting a metric CodeLens entry selects its associated node in Model Explorer.

Follow a CodeLens entry back to the graph and confirm that the same overlay remains selected. Several source lines can refer to shared execution work, so their values are not additive model totals.

If source presentation is missing, check these settings and inputs:

| Check | Expected state |
| --- | --- |
| Current run | The completed profiling analysis is selected. |
| Overlay | A measured metric is selected rather than **None**. |
| Source file | The matching file appears under **Accessible locally** and is open in the editor. |
| `vscode-mlia.showHeatmap` | Enabled. |
| `vscode-mlia.showCodeLens` and `editor.codeLens` | Both enabled. |
| Metric mapping | The selected overlay reports a value for that source location. |

For unavailable values, read the CodeLens hover explanation. The extension's [source visualization guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-visualisation.md) explains the presentation controls.

## Record your investigation

Copy this table into `$RUN_DIR/run-notes.md`, replacing the guidance in the second column with your values and artifact paths:

| Record | Where to find it |
| --- | --- |
| Capture directory, VGF checksum, and source revision or unchanged source copy | `$CAPTURE_ROOT`, `$NX_WORKSPACE/model.sha256`, and your Python project |
| Device, Android version, and driver | `$RUN_DIR/device-model.txt`, `$RUN_DIR/android-version.txt`, and `$NX_WORKSPACE/device-vulkan.json` |
| Extension and MLIA package versions | The MLIA extension's details page, and **Show MLIA Information** in the **New Analysis** title bar |
| SDK revisions | `$NX_WORKSPACE/sdk-manifest.xml` |
| Capture configuration | Mode `1`, filter `0`, one scenario execution, zero-filled input |
| Model result | Metric name, full value, unit, and the selected VGF's scope |
| Candidate and reason | Representation, group, metric value, and the comparison that led you to it |
| Source connection | Operation `spv id` and segment, module path, and Python file and line |

For a performance comparison, first establish a new baseline with representative inputs and repeated captures. Then change one model operation and repeat under the same input, frequency, and thermal conditions. Validate model quality as well as performance.

Use **Open Analysis Run Folder** to retain the generated reports. Deleting a saved analysis through the extension also deletes that run's output directory.

## Optional: resolve moved source files

Use this section only if the embedded paths no longer resolve. In **Source mappings**, expand **Distinct source locations**, inspect the old paths, and select **Configure source file mapping**. This opens the setting in VS Code. To enter JSON, run **Preferences: Open Workspace Settings (JSON)** from the Command Palette.

If export embedded `/home/export/upscaler` and the unchanged project is now in `/home/developer/upscaler`, add this property, replacing both paths with yours:

```json
{
    "vscode-mlia.sourceFileMap": {
        "/home/export/upscaler": "/home/developer/upscaler"
    }
}
```

Merge the property into the existing settings object. The extension preserves the path suffix after the matched prefix and refreshes mappings automatically. Recheck **Accessible locally** and open a source line. Path remapping cannot correct changed source contents or line numbers. See the [source-file mapping guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-file-mapping.md) for more complex layouts.

## Optional: reopen a saved analysis

Close the analysis tab, then select the completed entry in **Analysis Runs**. Its graph views and saved overlay should reopen without another capture. Open the mapped source again to inspect its heatmap and CodeLens. The [analysis guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/analyses.md) describes saved-run management.

## What you've accomplished

You've captured NX statistics for the selected VGF, analyzed its measured costs in VS Code, and traced a candidate through model graphs to Python source. Your next task is to establish a representative baseline before testing a model change.
