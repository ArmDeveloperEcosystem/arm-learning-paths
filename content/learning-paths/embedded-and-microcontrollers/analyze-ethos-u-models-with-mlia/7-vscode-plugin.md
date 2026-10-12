---
title: (Optional) Use the MLIA & Model Explorer VS Code Extension

description: Set up MLIA in VS Code, analyze a MobileNet model for Ethos-U, and inspect compatibility, performance metrics, and advice in Model Explorer.

weight: 8

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

The MLIA VS Code extension allows you to move from a CLI view, to using MLIA within your IDE, and also supports visualizing models in Model Explorer, with data from MLIA overlaid onto the model graphs.

## Open your model workspace in VS Code

Ensure you have [VS Code](https://code.visualstudio.com/download?_exp_download=d53503e735) 1.100 or newer on your local machine.

If you completed the earlier steps on that same local machine, open VS Code, select **File > Open Folder**, open your `ml-model-artifacts` directory, and continue to **Install the MLIA extension and prepare its environment**.

If you completed the earlier steps on a remote Linux machine, connect to it using [VS Code Remote - SSH](https://code.visualstudio.com/docs/remote/ssh). Use the same SSH connection details you used for the CLI steps:

1. Install the **Remote - SSH** extension on the machine running VS Code.
2. Open the Command Palette with **Ctrl+Shift+P** on Windows or Linux, or **Cmd+Shift+P** on macOS. Select **Remote-SSH: Add New SSH Host**.
3. Enter your existing SSH command, including any key-file option such as `-i`. For example, enter `ssh ubuntu@YOUR_HOST`, replacing the user and host with your connection details. Select an SSH configuration file when prompted.

![VS Code prompts for an SSH connection command. Enter the user and host of the Linux machine containing your models.#center](images/vscode-ssh-connection.png "Add your Linux host to Remote - SSH")

4. Run **Remote-SSH: Connect to Host** and select the host you added.
5. Confirm that the VS Code status bar shows your SSH host.
6. In the connected window, select **File > Open Folder** and open the remote `ml-model-artifacts` directory.

With Remote - SSH, the MLIA extension and analysis run on the remote host.

## Install the MLIA extension and prepare its environment

Download the `.vsix` package from the latest [MLIA VS Code extension release](https://github.com/arm/vscode-mlia/releases) to your local machine.

In VS Code:

1. If you’re using a remote Linux machine, connect to it with **Remote - SSH** first.
2. Open the **Extensions** view.
3. Select the **...** menu at the top of the view, then **Install from VSIX...**.
4. Select the `.vsix` file you downloaded to your local machine and install it.
5. If you’re connected over SSH, confirm that MLIA is installed and enabled on the SSH host, as shown below.

<img src="/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/images/vscode-mlia-installed.png" width="1088" style="max-width: min(70%, 1088px); height: auto;" alt="The MLIA extension page identifies Arm as the publisher and confirms that the extension is enabled on an SSH host." title="MLIA installed on the remote host" class="content-uploaded-image centered" />
<span class="content-image-caption centered">MLIA installed on the remote host</span>

Select **MLIA** in the Activity Bar. In **New Analysis**, select **Refresh MLIA Environment** and wait for setup to finish.

<img src="/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/images/vscode-refresh-environment.png" width="426" style="max-width: min(70%, 426px); height: auto;" alt="The MLIA New Analysis view shows Refresh MLIA Environment before setup. Select this button to prepare the extension&#x27;s runtime." title="Create the managed MLIA environment" class="content-uploaded-image centered" />
<span class="content-image-caption centered">Create the managed MLIA environment</span>

The extension installs and manages `uv`, Python, and MLIA in its own environment. You don't need to activate `mlia_env` or install MLIA again for the extension. Its packages and backends are separate from the CLI environment you created earlier.

Setup is complete when **New Analysis** shows the **Estimation** and **Profiling** tabs, a source-model field, and target-profile selection.

<img src="/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/images/vscode-new-analysis.png" width="419" style="max-width: min(70%, 419px); height: auto;" alt="The initialized New Analysis view shows Estimation and Profiling tabs, a Source model field, target selection, and check options." title="Analysis options after environment setup" class="content-uploaded-image centered" />
<span class="content-image-caption centered">Analysis options after environment setup</span>

## Run an Ethos-U estimation for a TFLite model

In **New Analysis**:

1. Select **Estimation**.
2. Use the **...** button next to **Source model** to select `tflite/mv2_int8.tflite` in your model-artifacts folder.
3. Select **ethos-u85-256** as the target profile.
4. Enable both **Performance** and **Compatibility**, by ticking each box.
5. Select **Run Analysis**.

<img src="/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/images/vscode-analysis-settings.png" width="613" style="max-width: min(70%, 613px); height: auto;" alt="The estimation form selects mv2_int8.tflite and ethos-u85-256 with both Performance and Compatibility enabled, ready to run both checks." title="Select the model, target, and checks" class="content-uploaded-image centered" />
<span class="content-image-caption centered">Select the model, target, and checks</span>

Model Explorer opens with a loading view while the analysis runs. When it finishes, **Current Analysis Run** shows **Complete**, the model path, target profile, and selected checks. The completed-run screenshot confirms **Performance + Compatibility**.

![Current Analysis Run shows Complete for mv2_int8.tflite on ethos-u85-256, with both Performance and Compatibility checks recorded.#center](images/vscode-completed-run.png "Confirm the analysis completed")

## Inspect compatibility and model performance

Expand **Result 1 · compatibility > Model metrics**. For this INT8 model, expect `accelerator_operator_percentage` to be **100%**, matching the earlier CLI check.

![The compatibility result reports accelerator_operator_percentage as 100 percent, confirming that the INT8 model's operators map to the accelerator.#center](images/vscode-compatibility-metrics.png "Inspect the compatibility result")

Expand **Result 2 · performance > Model metrics** to inspect model-level cycle estimates, memory use, and estimated inference time.

![The performance result lists NPU cycles, SRAM and DRAM access cycles, total cycles, estimated inference time, and model memory sizes.#center](images/vscode-performance-metrics.png "Inspect whole-model performance estimates")

These LiteRT results come from Vela compiler estimates. The displayed inference time is an estimate, rather than latency measured on a board.

## Explore operation metrics in Model Explorer

In Model Explorer, pan, zoom, and expand the model's groups to inspect operations. Use the search box to locate a node by name.

Select a performance metric in the **Overlay** selector under **Current Analysis Run**. The corresponding values and colours appear on the graph. You can also select this in Model Explorer, and this is synchronized with the sidebar. `op_cycles` are shown in the image below.

![Model Explorer displays the MobileNet source graph alongside completed compatibility and performance results. The selected op_cycles provider adds cycle values to the graph.#center](images/vscode-model-explorer.png "View analysis metrics on the source graph")

Select a model group and inspect **Node data in selected layer**. Compare operation placement, `npu_cycles`, `op_cycles`, and memory-access metrics. Use the table's filter to narrow the operations you inspect.

![The node-data table shows NPU placement and coloured performance metrics for convolution and depthwise convolution operations, allowing operation costs to be compared.#center](images/vscode-node-metrics.png "Compare metrics across operations")

The **Aggregated stats in selected layer** table summarizes the available numeric metrics with minimum, maximum, sum, and average values. These summaries describe the selected graph group; use **Model metrics** for the whole-model result.

![Aggregated stats in selected layer shows minimum, maximum, sum, and average values for the selected group's numeric metrics.#center](images/vscode-aggregated-metrics.png "Inspect metrics for a selected group")

You can zoom in on the graph to see specific operators, with associated data overlaid. For example, to investigate memory cost, select the `dram_access_cycles` overlay. Expand a group and compare the values attached to its operations.

![Model Explorer shows dram_access_cycles on expanded MobileNet groups, with different cycle values and colours identifying operations to investigate.#center](images/vscode-dram-overlay.png "Explore DRAM access cycle estimates")

## Find advice on the model graph

Select **advice** as the overlay in **Current Analysis Run** or Model Explorer to highlight operations with MLIA advice. Select a highlighted operation to inspect its advice.

![The selected softmax node has NPU placement and advice about a suboptimal SOFTMAX activation, showing that a supported operation can still receive performance advice.#center](images/vscode-softmax-advice.png "Locate the Softmax performance advice")

The advice identifies `SOFTMAX` as a suboptimal activation for NPU performance. The operation is supported, so the model can still map fully to the NPU, but it is a candidate for optimization. You could choose to change the model, after which you can rerun MLIA to compare compatibility and performance estimates, and check that prediction accuracy and any required probability outputs still meet your application's needs.

## What you've accomplished

You've set up the MLIA extension, analyzed a model for Ethos-U, and inspected compatibility, model metrics, operation overlays, and advice in Model Explorer. You can now use the same workflow to compare other supported model artifacts or investigate a revised model.
