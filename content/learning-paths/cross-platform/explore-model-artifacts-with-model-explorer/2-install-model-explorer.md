---
title: Install Model Explorer and the Arm extensions
description: Download pre-generated model artifacts and install Model Explorer with Arm extensions in a Python virtual environment.

weight: 3

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Clone the repository of example models

You'll download the example model artifacts and install Model Explorer with the Arm extensions in a clean Python virtual environment. In the next section, you'll confirm the installation by opening a Cortex-M `.pte` file.

First, clone the repository of example models that you'll use.

Use a machine capable of displaying a browser. For example, a laptop.

The repository uses Git Large File Storage (LFS) for model artifacts. Install and configure Git LFS for your operating system:

{{% notice Note %}}
- If you use WSL on Windows, follow the Linux commands. 
- You need to run `git lfs install` only once for your user account.
{{% /notice %}}

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

Use a separate Python 3.10, 3.11, or 3.12 environment to avoid dependency conflicts with any ExecuTorch build, notebook, or application environment that you already use:

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
If Windows PowerShell blocks `Activate.ps1`, allow local activation scripts for your user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
{{% /notice %}}

## Install Arm extensions with TOSA and VGF adapters

Install the combined ExecuTorch extension with the separate Tensor Operator Set Architecture (TOSA) and VGF adapters:

```bash
python -m pip install executorch-extension-model-explorer tosa-adapter-model-explorer vgf-adapter-model-explorer
```

The ExecuTorch extension provides the PTE adapter, ETRecord adapter, and ETDump profiling data provider. The separate TOSA and VGF adapters open standalone `.tosa` and `.vgf` files.

{{% notice Note %}}
For component development or focused debugging, install the ExecuTorch components separately as `pte-adapter-model-explorer`, `etrecord-adapter-model-explorer`, and `etdump-data-provider-model-explorer`. For this Learning Path, use the combined `executorch-extension-model-explorer` package.
{{% /notice %}}

## What you've accomplished and what's next

You've downloaded the example model artifacts, created a Python virtual environment, and installed Model Explorer with the combined ExecuTorch extension and separate TOSA and VGF adapters.

Next, you'll launch Model Explorer and confirm the installation by opening and inspecting a Cortex-M `.pte` artifact.
