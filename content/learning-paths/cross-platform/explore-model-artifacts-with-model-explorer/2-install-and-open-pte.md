---
title: Install Model Explorer extensions and view a Cortex-M model graph
description: Install Model Explorer and Arm extensions, then open a Cortex-M PTE file to inspect its graph and ExecuTorch metadata.

weight: 3

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Clone the repo of example models

You'll install Model Explorer and the Arm extensions in a clean Python virtual environment. Then, you'll confirm the installation by opening a Cortex-M `.pte` file. 

First, clone the repository of example models that you'll use.

Use a machine capable of displaying a browser. For example, a laptop.

The repository uses Git Large File Storage (LFS) for model artifacts. Install and configure Git LFS for your operating system. You need to run `git lfs install` only once for your user account:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
sudo apt update
sudo apt install -y git-lfs
git lfs install
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
brew install git-lfs
git lfs install
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
winget install -e --id GitHub.GitLFS
git lfs install
  {{< /tab >}}
{{< /tabpane >}}

Clone the artifacts repository, then use `git lfs pull` to download the model files:

```bash
git clone https://github.com/arm-education/ml-model-artifacts.git
cd ml-model-artifacts
git lfs pull
```

## Create a virtual environment

Use a separate environment to avoid dependency conflicts with any ExecuTorch build, notebook, or application environment that you already use:

Use Python 3.10, 3.11, or 3.12 for this environment.

If you use WSL on Windows, follow the Linux or macOS commands.

{{< tabpane code=true >}}
  {{< tab header="Linux or macOS" language="bash">}}
python3 -m venv model_explorer_env
source model_explorer_env/bin/activate
python -m pip install --upgrade pip
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
py -m venv model_explorer_env
.\model_explorer_env\Scripts\Activate.ps1
python -m pip install --upgrade pip
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}
On Windows, if PowerShell blocks `Activate.ps1`, allow local activation scripts for your user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
{{% /notice %}}

## Install Model Explorer and the Arm extensions

Install the combined ExecuTorch extension with the separate Tensor Operator Set Architecture (TOSA) and VGF adapters:

```bash
python -m pip install executorch-extension-model-explorer tosa-adapter-model-explorer vgf-adapter-model-explorer
```

The ExecuTorch extension provides the PTE adapter, ETRecord adapter, and ETDump profiling data provider. The separate TOSA and VGF adapters open standalone `.tosa` and `.vgf` files.

{{% notice Note %}}
For component development or focused debugging, install the ExecuTorch components separately as `pte-adapter-model-explorer`, `etrecord-adapter-model-explorer`, and `etdump-data-provider-model-explorer`. For this Learning Path, use the combined `executorch-extension-model-explorer` package.
{{% /notice %}}

## Launch Model Explorer

Launch Model Explorer with all the extensions that you'll use. The combined ExecuTorch extension opens `.pte` and `.etrecord` files and adds `.etdp` profiling data. The separate TOSA and VGF extensions open `.tosa` and `.vgf` files.

Launching Model Explorer opens a webpage in your browser.

{{< tabpane code=true >}}
  {{< tab header="All Learning Path extensions" language="bash">}}
model-explorer --extensions=executorch_extension_model_explorer,tosa_adapter_model_explorer,vgf_adapter_model_explorer
  {{< /tab >}}
  {{< tab header="ExecuTorch extension" language="bash">}}
model-explorer --extensions=executorch_extension_model_explorer
  {{< /tab >}}
  {{< tab header="No adapters" language="bash">}}
model-explorer
  {{< /tab >}}
{{< /tabpane >}}

Use `CTRL + C` to stop Model Explorer.

{{% notice Note %}}
If you're interested in a specific model format or a particular target, skip to the appropriate section.
{{% /notice %}}

## Open the Cortex-M PTE

You'll start with a `.pte` generated for the Cortex-M backend. This `.pte` was generated for the MobileNetV2 model, a typical Convolutional Neural Network (CNN) used in embedded ML.

The ExecuTorch Cortex-M backend prepares models for Arm Cortex-M microcontrollers, where memory and compute resources are much more limited than on application-class CPUs. The backend rewrites supported quantized operators so they can use CMSIS-NN, an Arm library of optimized neural network kernels for Cortex-M processors.

CMSIS-NN exists to make common ML operations such as convolutions, fully connected layers, activations, and quantization-related operations run efficiently on small embedded CPUs. Treat this first `.pte` as a good way to learn the Model Explorer interface while seeing how an ExecuTorch graph can reflect Cortex-M-specific lowering.

{{% notice Note %}}
The Cortex-M backend is a work-in-progress proof of concept. It's not intended for production use, and APIs might change without notice. However, the `.pte` is pre-generated for you in the provided repository. To learn more about the Cortex-M backend, see the [Cortex-M Backend Documentation](https://docs.pytorch.org/executorch/1.2/backends/arm-cortex-m/arm-cortex-m-overview.html), which also links to a Jupyter Notebook.
{{% /notice %}}

In the Model Explorer UI, open `ml-model-artifacts/pte/mv2_cortex_m.pte`.

Your view in the browser should appear as follows:

![Screenshot of Model Explorer with Arm Adapters and a loaded Cortex-M PTE.#center](model_explorer.png "Model Explorer with Arm Adapters")

Select `View selected models`, and your view should appear as follows:

![Screenshot of top-level view in Model Explorer of a loaded Cortex-M PTE.#center](cortex_m_top.png "Typical top-level graph view in Model Explorer")

A right-hand bar tells you the graph info, including the `op node count` and the `layer count`. The `op node count` is the number of operator nodes in the graph. The `layer count` is the number of hierarchical graph components represented in the current view, not necessarily the number of neural network layers in the original model.

Double click the `forward` layer to see the various operators comprising the layer. Click a specific operator — for example, `cortex_m::quantize_per_tensor` — to see various attributes, as well as inputs and outputs, in the right-hand bar.

![Screenshot of examining a specific Cortex-M operator in Model Explorer.#center](cortex_m_inspect.png "Inspecting specific operators with Model Explorer")

When you inspect a `.pte` for the first time, focus on the higher-level graph information first:

- **Operator names** show the work the ExecuTorch program will perform.
- **Inputs and outputs** show how tensors flow through the graph.
- **Tensor shapes and types** help you check whether the model was exported and quantized as expected.
- **Hierarchical layers** let you expand or collapse parts of the graph so you can move between an overview and individual operators.
- **Delegate or backend-specific names** show where a backend flow has changed the graph. In this Cortex-M example, names such as `cortex_m::...` indicate operators affected by the Cortex-M backend flow.

You might also see lower-level `.pte` execution fields in the node attributes. These fields come from the serialized ExecuTorch program:

| Field | What it means |
| --- | --- |
| `instruction type: KernelCall` | The instruction calls an ExecuTorch operator kernel. A kernel is the code that executes a model operator for a runtime or backend. |
| `instr_args_type: 1` | The internal FlatBuffer type tag for the instruction arguments. In this case, `1` identifies the arguments as a `KernelCall`. |
| `op_index` | An index into the `.pte` operator table. It tells ExecuTorch which operator this instruction calls. |
| `args: [471, 473, 474, ...]` | Indexes into the `.pte` values table. These entries identify the tensors or other values used as inputs and outputs by the instruction. |

You don't need to memorize these internal fields. Use the fields as clues when you want to connect a visible graph node to the underlying ExecuTorch program structure.

Select the `eye symbol` in the top left bar to select data to view on nodes and edges. Choose the data you want to see - for example, `op node id` and `op node attributes` — to include more data within the graph itself.

## What you've accomplished and what's next

You've installed Model Explorer, launched it with the Arm extensions, and opened your first `.pte` artifact. You've also learned how to inspect the graph overview, expand into the `forward` layer, read operator metadata, and interpret common low-level `.pte` fields such as `KernelCall`, `op_index`, and `args`.

Next, you'll keep the same browser tab open and compare portable and XNNPACK `.pte` artifacts to see how backend delegation changes the graph.
