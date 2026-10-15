---
title: Analyze measured performance in VS Code
description: Import an NX capture and its matching VGF into MLIA for VS Code, verify measured results, and distinguish model totals from graph-level values.
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
3. Select `nx-profile/workload/model.vgf` in **Source model**. This matching VGF supplies the graph and Python source mappings.
4. Select `neural-technology` as the target profile.
5. Enable **Performance**.
6. Select **Run Analysis**.

<!-- Publication: add a screenshot from this walkthrough showing Profiling, its capture root, model.vgf, neural-technology, and Performance. -->

![MLIA New Analysis with Profiling selected, the capture directory and model.vgf entered, neural-technology selected, and Performance enabled.#center](images/nx-profiling-capture.png "Configure the NX profiling analysis")

Model Explorer opens with a loading view while MLIA analyzes the capture. Wait for completion before inspecting the metrics.

## Verify that the result uses measurements

In **Current Analysis Run**, confirm that:

- The run completed successfully.
- **Mode** is **Profiling** and **Checks** includes **Performance**.
- The profiling-data directory and source model match the inputs you selected.
- The target profile is `neural-technology`.
- A performance result is available under **Model metrics**.

The selected entry in **Analysis Runs** determines which analysis you're inspecting. **Current Analysis Run** shows its configuration and **Model metrics** for the selected VGF. Model Explorer displays its graphs and details for the selected node or group in its side panel. Keep this profiling run selected as you explore its results.

Select **Open Analysis Run Folder** on the completed entry in **Analysis Runs**, then open `mlia-output/model-explorer/standardized-output.json`. Within its `results` array, find the object whose `kind` is `performance`. Confirm these fields; the excerpt omits the other result fields:

```json
{
    "kind": "performance",
    "status": "ok",
    "mode": "measured"
}
```

The `measured` mode confirms that the result uses capture data.

If the run fails, inspect its error summary and the **MLIA** output log, then check the inputs:

| Problem | Action |
| --- | --- |
| Missing or invalid capture files | Recheck `capture.json`, its completion status, and the complete extracted directory tree. |
| Model and captured pipelines don't match | Select the exact VGF deployed to the device and verify its recorded checksum. |
| Capture selection is ambiguous | Recreate this example with one scenario execution and dispatch filter `0`; consult the profiling documentation before combining captures. |
| No profiling target profile is available | Refresh the managed MLIA environment and inspect its setup log. |

## Read the model-level metrics first

Expand the performance result's **Model metrics** and find `total_cycles`, with unit `cycles`. It summarizes the cycle cost attributed to the captured VGF. The mode-1 profiling backend derives both `total_cycles` and `compute_cycles` from the reported NX-active cycle counts.

These counts describe accelerator work for the captured dispatch, excluding application work such as CPU preprocessing and presentation. They are not elapsed application latency. Use representative inputs and repeated measurements before drawing application-performance conclusions.

In the example below we can see that the `total_cycles` is 25,543 and the utilization is 100%. The other metrics aren't available through the "Profiling" route, just "Estimation", but we will look into the cycles in more detail in the model view, in the next few sections. Record the model’s total_cycles value before exploring the graph.

![MLIA Model metrics showing total_cycles and compute_cycles of 25,543 cycles, target_utilization of 100%, and unavailable metrics with explanatory messages.#center](images/current-analysis.png "Inspect model-level profiling metrics")

## Explore the model graph

In Model Explorer, select **Source Model** in the graph selector to inspect the original VGF graph. Use the navigation controls to find your way around the model:

1. Select **Fit to screen** on the toolbar, or press **Space** while the graph has focus, to show the whole graph.
2. Drag the graph to pan.
3. Use a group's expand control to reveal its contents. Collapse it when you want to return to a broader view.
4. Use the search box to find a node by name. Select a result to locate it in the graph, then inspect its attributes, inputs, and outputs in the side panel.

Next, select **segment_cascade_chain**. It groups operations into the segments, cascades, and chains used for hardware execution. Expand a segment to its cascades and chains to inspect increasingly specific execution groups.

The [Model Explorer representation guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/model-explorer-representations.md) explains the views available for different model metadata and results.

## Compare measured values within a cascade

Lets look into the results in more detail. In the example we can see that `Cascade 249` is darker green than the rest, indicating that the total cycle count is greater than other cascades in the graph. If we click on this we can see the cycle count for this `12471`. This is a combination of the `CONV2D` and `RESCALE` operators. Also this highlights the two operators in the `Source Model` on the left.

If source model mapping is also setup, it will point to the line of code from your model that represents these layers, but we will look at that in the next page.

![Model Explorer showing Cascade 249 selected in segment_cascade_chain with total_cycles of 12,471. The corresponding CONV2D and RESCALE operations are highlighted in Source Model.#center](images/profiling-result.png "Inspect Cascade 249 and its source operations")

## Inspect group statistics and change the overlay

With the group selected, inspect **Aggregated stats in selected layer**. The table summarizes available numeric node values within that group. Minimum and maximum help you find the range of mapped costs; average and sum summarize those values when the result exposes them. This is more useful when there are multiple runs, in this example we have only executed the workload once.

![Model Explorer's Aggregated stats in selected layer table showing minimum, maximum, sum, and average values for the selected group's available node metrics.#center](images/aggregated-stats.png "Inspect aggregated node metrics")

In Node data providers (descendants), select the eye icon beside a metric to display its overlay on the graph. In this example, total_cycles is selected, which is enabled by default.

![Model Explorer's Node data providers list with total_cycles highlighted and its eye icon active, indicating the metric selected for the graph overlay.#center](images/view-options.png "Select the metric displayed on the graph")

## Choose a group to investigate

Choose a group with a higher reported cycle cost than a comparable group in the same view, like in the sample above. Record the comparison that makes it worth investigating. If only one group has a value, record that limitation and use it to practice source tracing without claiming it is the dominant cost.

Before moving to the Python source, record:

- The graph representation and group name.
- The selected measured cycle metric, its value, and its unit.
- The model-level metric and value you recorded earlier, keeping its scope distinct from the group's value.

Keep that group and cycle overlay selected for the next page. A high reported cost identifies a candidate to inspect; it does not establish that changing the operation will improve application performance.

## What you've accomplished and what's next

You've run a measured profiling analysis, checked its origin, and inspected model totals. You've also explored the graph, compared mapped values and group statistics, and chosen an execution group to investigate. Next, you'll connect that evidence to the Python source that produced the graph.
