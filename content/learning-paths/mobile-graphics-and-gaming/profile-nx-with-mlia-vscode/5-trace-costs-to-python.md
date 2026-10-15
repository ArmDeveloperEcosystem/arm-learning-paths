---
title: Trace measured costs to Python source
description: Connect NX performance overlays to Python modules and code stacks, resolve source paths, and inspect synchronized heatmaps and CodeLens values.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check that the source locations are available

Keep the completed profiling run selected in **Analysis Runs**. Expand its performance result's **Source mappings** in **Current Analysis Run**.

The view distinguishes reported code stacks, code stacks mapped to Model Explorer, distinct source locations, and locations **Accessible locally**. Find entries for the `quantize_and_export_vgf.py` file that produced your VGF, then select an accessible line to open it.

If no source locations are reported, return to the model export and check both debug settings. A path mapping can't recreate metadata omitted during export. If you re-export the VGF, generate a new scenario and collect a matching capture before repeating the analysis.

If locations exist but your Python file is inaccessible, use the source-mapping steps below. Missing framework files don't necessarily prevent navigation to your own model file, but you need at least one accessible, mapped model-source location to complete this exercise.

## Resolve moved source files

Skip this section if the model's source locations already open correctly.

1. Expand **Distinct source locations** and inspect the embedded file paths.
2. Select **Configure source file mapping**.
3. Map the embedded project prefix to the location of the same source files on this host.

For example, if export embedded `/home/export/upscaler` but the unchanged project is now in `/home/developer/upscaler`, add this workspace setting, replacing both paths with yours:

```json
{
    "vscode-mlia.sourceFileMap": {
        "/home/export/upscaler": "/home/developer/upscaler"
    }
}
```

If the workspace settings already contain other entries, merge this property into the existing JSON object. The extension preserves the suffix after a matching prefix, so the example maps `quantize_and_export_vgf.py` under the old directory to the same filename under the new directory.

After saving, the mapping index refreshes automatically. Recheck **Accessible locally** and open a source line. The file's contents must still match the exported version; remapping paths doesn't correct changed line numbers. See the [source-file mapping guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-file-mapping.md) for more complex directory layouts.

## Follow a costly group into the Python model

Use the execution group and cycle overlay you recorded on the previous page:

1. Inspect the group's mapped operations in **Source Model**.
2. Switch to **nn_module**, when available, to inspect costs grouped by the PyTorch module hierarchy. Locate the `SmallUpscalerModel` modules associated with those operations.
3. Switch to **code_stack** to inspect their source call stacks. Expand to a node referring to your model file.
4. Select a node with one unambiguous local source location. With **Sync Model Explorer Selection To Code** enabled, VS Code opens that file and highlights the line.

These views regroup the analysis; they aren't separate device captures. Keep the same overlay selected and inspect the reported values rather than assuming a graph node's cost remains identical under every grouping.

Some nodes map to multiple source locations or have no usable file and line. In those cases, automatic navigation is unavailable. Use **Source mappings** to inspect the reported locations instead of expecting every node to open one line.

<!-- Publication: add a screenshot from this walkthrough showing a measured overlay on a code_stack or nn_module graph beside the matching SmallUpscalerModel source. -->

## Read source heatmaps and CodeLens

With your model source open, select the measured cycle overlay in **Current Analysis Run**. Mapped source lines receive heatmap colors, and CodeLens entries can show the metric above those lines.

- Numeric heatmap colors show relative values across mapped lines. They help locate regions to inspect; red doesn't by itself establish a performance defect.
- CodeLens displays the selected value and, when it can be calculated safely, its percentage of the model total.
- Selecting a metric CodeLens entry selects its associated node in Model Explorer. Caller and called-source actions navigate related source locations when available.

Follow a CodeLens entry back to the graph and confirm that the same overlay remains selected. A source line can represent work shared by several operations, and multiple lines can refer to related execution work. Don't add all line values to obtain an independent model total.

If source presentation is missing, check these settings and inputs:

| Check | Expected state |
| --- | --- |
| Current run | The completed profiling analysis is selected. |
| Overlay | A measured metric is selected rather than **None**. |
| Source file | The matching file appears under **Accessible locally** and is open in the editor. |
| `vscode-mlia.showHeatmap` | Enabled. |
| `vscode-mlia.showCodeLens` and `editor.codeLens` | Both enabled. |
| Metric mapping | The selected overlay reports a value for that source location. |

An unavailable value is different from zero. Read any explanation provided by MLIA or the CodeLens hover. The extension's [source visualization guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-visualisation.md) explains the presentation controls.

## Reopen and record the analysis

Close the analysis tab, then select the completed entry in **Analysis Runs**. Confirm that its Model Explorer views and saved overlay reopen without collecting another capture. Open the mapped model source again to inspect its heatmap and CodeLens.

Before finishing, record:

- The capture directory, VGF checksum, and source revision or unchanged source copy.
- The device, Android and driver versions, extension version, MLIA package versions, and resolved SDK manifest.
- The capture configuration: mode `1`, filter `0`, one scenario execution, and zero-filled input.
- One measured model total and one expensive group, with their units and a mapped Python location worth investigating.

This gives you evidence for choosing the next experiment. For example, investigate whether a costly operation can be changed, then validate model quality and collect a new capture with representative input. Keep the device and measurement conditions consistent, change one meaningful variable at a time, and distinguish model changes from changes in frequency, thermal state, or workload.

Use the run's output folder to retain its generated reports. Deleting a saved analysis through the extension also deletes that run's output directory.

## What you've accomplished

You've captured NX statistics on Android, analyzed measured performance in VS Code, and followed reported execution costs through model graphs to Python source. You can now identify a model region to investigate and collect comparable evidence for a later change.

For compiler estimates before deployment, see the [NX performance estimation Learning Path proposal](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/pull/3876). For a different target, the [Ethos-U VS Code walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/) applies MLIA and Model Explorer to compatibility checks and estimates, with different metrics and backends.
