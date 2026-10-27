---
title: Analyze measured performance in VS Code
description: Load an NX capture in MLIA for VS Code, inspect a cascade's measured cycle cost, and follow a graph operation to Python source.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select the capture and matching model

Return to the Visual Studio Code (VS Code) window containing your Python model project. Print the Scenario Runner neural accelerator (NX) capture and model paths from the capture terminal:

```bash
printf 'Profiling data: %s\nSource model: %s\n' "$CAPTURE_ROOT" "$NX_WORKSPACE/workload/model.vgf"
```

For an existing-application capture, use its capture directory and matching VGF instead.

In **MLIA > New Analysis**:

1. Select **Profiling**.
2. Add the printed **Profiling data** directory, which directly contains `capture.json`.
3. Select `nx-profile/workload/model.vgf` in **Source model**. Use the same VGF deployed to the device.
4. Select `neural-technology` as the target profile.
5. Enable **Performance**.
6. Select **Run Analysis**.

![MLIA New Analysis with Profiling selected, the capture directory and model.vgf entered, neural-technology selected, and Performance enabled.#center](images/nx-profiling-capture.png "Configure the NX profiling analysis")

Model Explorer opens when the analysis completes. For analysis errors, see the [Arm ML Inference Advisor (MLIA) analysis troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/troubleshooting.md#an-analysis-fails).

## Inspect a cascade's cycle cost

In Model Explorer, set **Left graph** to **Source Model** and **Right graph** to **segment_cascade_chain**. The latter groups operations into the segments, cascades, and chains used for hardware execution. Expand a segment to see its cascades.

The `total_cycles` overlay is selected by default. It shows accelerator cycle counts for the captured dispatch.

Select a cascade with a reported cycle value. In the example screenshot, `Cascade 249` has 12,471 cycles for its combined `CONV2D` and `RESCALE` work. Selecting the cascade highlights the corresponding operations in **Source Model**.

![Model Explorer showing Cascade 249 selected in segment_cascade_chain with total_cycles of 12,471. The corresponding CONV2D and RESCALE operations are highlighted in Source Model.#center](images/profiling-result.png "Inspect Cascade 249 and its source operations")

Keep the cascade selected. For other graph views, see the [MLIA Model Explorer representation guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/model-explorer-representations.md).

## Follow an operation to Python

Keep the completed profiling run selected in **Analysis Runs** and the `total_cycles` overlay selected in Model Explorer.

Expand the selected cascade and select a mapped operation node in **Source Model**. VS Code opens `quantize_and_export_vgf.py` and highlights the corresponding line. For a convolution in `SmallUpscalerModel`, this is `x = self.net(x)`, which calls the `nn.Sequential` block of the model.

When source cycle values are available, VS Code displays them above the mapped lines. In this screenshot, `x = self.net(x)` accounts for 22,506 cycles, or 88% of the model total.

![VS Code showing SmallUpscalerModel with source heatmaps and CodeLens values. The self.net(x) call is mapped to 22,506 cycles, or 88% of the model total, while interpolation is mapped to 3,037 cycles, or 12%.#center](images/python-model.png "Inspect measured cycles mapped to Python source")

Select a displayed cycle count (CodeLens) to highlight the corresponding graph operations. The screenshot shows **Source Model** on the left and **code_stack** on the right.

![Model Explorer showing synchronized Source Model and code_stack views beside the Python source. The selected code_stack group maps three CONV2D and RESCALE pairs to x = self.net(x), with total_cycles of 22,506.#center](images/code-mapping.png "Trace a Python source line to its mapped operations")

Source navigation is enabled by default. If the file doesn't open, see the [MLIA source-navigation troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/troubleshooting.md#source-files-do-not-open). For a moved source file, use the [source-file mapping guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-file-mapping.md).

## What you've accomplished

You've captured an NX dispatch, inspected cycle cost of a cascade, and followed a mapped operation to the Python model.

You can extend the Learning Path steps to capture and analyze performance of a model of your choice on an NX device.
