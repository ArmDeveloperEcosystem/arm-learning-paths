---
title: Analyze measured performance in VS Code
description: Import a validated NX capture and its matching VGF into MLIA for VS Code, then distinguish model totals from graph-level measurements.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select the capture and matching model

Return to the VS Code window containing your Python model project. The device can remain disconnected during analysis because the capture is now on the host.

Print the two input paths from the capture terminal:

```bash
printf 'Profiling data: %s\nSource model: %s\n' "$CAPTURE_ROOT" "$NX_WORKSPACE/workload/model.vgf"
sha256sum --check "$NX_WORKSPACE/model.sha256"
```

The checksum check should report `OK`. Use this same VGF for analysis; exporting the Python model again can change the artifact and break the match with the captured pipelines.

In **MLIA > New Analysis**:

1. Select **Profiling**.
2. Add the printed **Profiling data** directory. Select the directory directly containing `capture.json`, not `capture.tar`, the enclosing `captures` directory, or an individual `.bin` file.
3. Select `nx-profile/workload/model.vgf` in **Source model**.
4. Select `neural-technology` as the target profile.
5. Enable **Performance**. Measured Neural Technology profiling supports the performance check; an unavailable **Compatibility** option can remain disabled.
6. Select **Run Analysis**.

The extension permits profiling without a source model for some formats. Supply the matching VGF here because the exercise includes model graphs and Python source mappings.

<!-- Publication: add a screenshot from this walkthrough showing Profiling, its capture root, model.vgf, neural-technology, and Performance. -->

Model Explorer opens with a loading view while MLIA analyzes the capture. Wait for completion before inspecting the metrics. The [analysis guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/analyses.md) describes run management and the managed output directory.

## Verify that the result uses measurements

In **Current Analysis Run**, confirm that:

- The run completed successfully.
- **Mode** is **Profiling** and **Checks** includes **Performance**.
- The profiling-data directory and source model match the inputs you selected.
- The target profile is `neural-technology`.
- A performance result is available under **Model metrics**.

The selected entry in **Analysis Runs** determines which analysis you're inspecting. **Current Analysis Run** shows its configuration and results, including **Model metrics** for the whole model. Model Explorer displays the run's graphs, with details for the selected node or group in its own side panel. Keep this profiling run selected as you explore its results.

Select the run's output-folder action in **Analysis Runs**. Inside that folder, open `mlia-output/model-explorer/standardized-output.json`. Find the performance entry in `results` and confirm that `status` is `ok` and `mode` is `measured`. This establishes the origin of the reported metrics; selecting a target profile alone doesn't turn an estimate into a measurement.

If the run fails, inspect its error summary and the **MLIA** output log. Resolve the input problem before using another run's metrics:

| Problem | Action |
| --- | --- |
| Missing or invalid capture files | Recheck `capture.json`, its completion status, and the complete extracted directory tree. |
| Model and captured pipelines don't match | Select the exact VGF deployed to the device and verify its recorded checksum. |
| Capture selection is ambiguous | Recreate this example with one scenario execution and dispatch filter `0`; consult the profiling documentation before combining captures. |
| No profiling target profile is available | Refresh the managed MLIA environment and inspect its setup log. |

## Read the model-level metrics first

Expand the performance result's **Model metrics**. Look for reported cycle metrics such as `total_cycles` and `compute_cycles`, and read their units. Available metrics depend on the driver statistics and MLIA package version; only use values that this run actually reports.

Record a model-level metric and its value as the starting point for your investigation. Hover over a shortened value to see its full precision.

These results describe accelerator work for the captured dispatch. They don't include every part of an application, such as CPU preprocessing or presentation. Avoid treating an accelerator cycle count as measured application latency or comparing it directly with an estimator result that assumes a different hardware configuration.

The one-dispatch, zero-input example establishes that the tools work together. Use representative inputs and repeated measurements under controlled device conditions before drawing performance conclusions about your application.

<!-- Publication: add a screenshot from the successful measured run showing its inputs, Profiling mode, and model metrics. -->

## Explore the model graph

In Model Explorer, select **Source Model** in the graph selector to inspect the original VGF graph. Use the navigation controls to find your way around the model:

1. Select **Fit to screen** on the toolbar, or press **Space** while the graph has focus, to show the whole graph.
2. Drag the graph to pan. Hold **Ctrl** while scrolling, or pinch on a touchpad, to zoom.
3. Use a group's expand control to reveal its contents. Collapse it when you want to return to a broader view.
4. Use the search box to find a node by name. Select a result to locate it in the graph, then inspect its attributes, inputs, and outputs in the side panel.

Next, select **segment_cascade_chain** when it is available. This representation groups operations into the segments, cascades, and chains used for hardware execution. It helps you relate measured costs to the work the accelerator executes. Switching representations changes how you inspect the same analysis; it doesn't collect another capture.

The [Model Explorer representation guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/model-explorer-representations.md) explains the available views. Their presence depends on the model's metadata and the result.

## Compare measured values within a group

Use a measured overlay to locate a group with a high reported cost:

1. In **Current Analysis Run > Overlay**, choose an available cycle metric from the measured performance result.
2. Expand the graph and inspect the values and colors on its nodes. Read the values as well as the colors when comparing costs.
3. Select a group and inspect **Node data in selected layer** in Model Explorer's side panel. This table lets you compare mapped values without reading each label on the graph.
4. Use the table filter to narrow the entries by node name. Compare values for the same metric and unit, and check which execution unit each value describes.

Overlay selections synchronize between **Current Analysis Run** and Model Explorer. If you see no values, check that the overlay belongs to the measured result and that the selected representation contains mapped entities.

A scheduling group can contain several model operations. A cost mapped to those operations isn't an independent measurement of every operation. Missing values don't mean zero cycles. Use the execution grouping to understand what was measured before deciding which part of the model to investigate.

<!-- Publication: add an NX screenshot from this walkthrough showing the segment_cascade_chain representation, a measured cycle overlay, and the selected group. -->

## Interpret group statistics

With the group selected, inspect **Aggregated stats in selected layer**. The table summarizes available numeric node values within that group. Minimum and maximum help you find the range of mapped costs; average and sum summarize those values when the result exposes them.

Filtering the node-data table narrows the rows you inspect. The aggregated statistics still describe the selected group.

These statistics depend on the selected graph representation and its metric mappings. Shared or overlapping costs can appear on several nodes, so a sum of mapped values doesn't necessarily represent an independently measured group total. Use **Model metrics** for the reported whole-model result, and don't add summaries from different representations together.

<!-- Publication: add an NX screenshot from the same run showing Node data in selected layer and Aggregated stats in selected layer for the selected group. Include the metric labels and explanatory alt text and caption. -->

## Choose a group to investigate

Use the graph and tables to choose one execution group with a high reported cycle cost. If other measured overlays are available, inspect them to understand what else the capture reports about that group. Use the metric names and units provided by this run.

Before moving to the Python source, record:

- The graph representation and group name.
- The selected measured cycle metric, its value, and its unit.
- The operations associated with the group, where available.
- The model-level metric and value you recorded earlier, keeping its scope distinct from the group's value.

Keep that group and cycle overlay selected for the next page. Treat it as a candidate for investigation: a high cost alone doesn't establish that an operation is inefficient or that changing it will improve application performance.

## What you've accomplished and what's next

You've run a measured profiling analysis, checked its origin, and inspected model totals. You've also explored the graph, compared mapped values and group statistics, and chosen an execution group to investigate. Next, you'll connect that evidence to the Python source that produced the graph.
