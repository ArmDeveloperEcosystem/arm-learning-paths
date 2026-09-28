---
title: Prepare ExecuTorch and build the VGF runner
description: Set up the DeiT example dependencies and ML SDK for Vulkan, then build a VGF-enabled ExecuTorch runner on your Linux host.
weight: 3
layout: "learningpathall"
---

## Get the ExecuTorch source

The commands use public ExecuTorch revision `9dfe4086846ad372b8b78976586ee1857a0c6d13`. This keeps the example, exporter, and runtime source aligned.

Create a new workspace, then clone the source and select that revision:

```bash
mkdir deit-vgf-workspace
cd deit-vgf-workspace
git clone https://github.com/pytorch/executorch.git executorch
cd executorch
git checkout 9dfe4086846ad372b8b78976586ee1857a0c6d13
git submodule sync --recursive
git submodule update --init --recursive
```

Keep the repository directory named `executorch`: the build checks this name at the pinned revision. Run all remaining commands from this repository root, in the same shell.

## Install the Python dependencies

Create a Python 3.12 environment and install the current source checkout with VGF dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
./install_executorch.sh --optional-dependency vgf
```

Install the example's training and evaluation dependencies after the main installer:

```bash
python -m pip install -r examples/arm/image_classification_example_vgf/requirements.txt
```

The example pins Transformers 5.3.0. The ExecuTorch installer supplies the matching PyTorch stack, Datasets, and CMake dependencies.

## Configure the ML SDK for Vulkan

Read the tooling's license terms before accepting them. Install the ML SDK components and Vulkan SDK, then load the generated environment:

```bash
./examples/arm/setup.sh \
  --i-agree-to-the-contained-eula \
  --disable-ethos-u-deps \
  --enable-mlsdk-deps
source examples/arm/arm-scratch/setup_path.sh
```

This revision uses ML SDK packages version `0.10.0`. The setup script configures the model converter, VGF library, and Vulkan emulation layers. Your GPU driver must already be installed and working.

{{% notice Note %}}
This flow uses the packaged emulation layer, which needs `shaderFloat64` support at this revision. If setup reports missing support, use a compatible Linux host for these commands. The [ML SDK source-build helper](https://github.com/pytorch/executorch/blob/9dfe4086846ad372b8b78976586ee1857a0c6d13/backends/arm/scripts/setup-mlsdk-from-source.sh) documents the separate source-build route for other configurations.
{{% /notice %}}

## Check the environment

Check export prerequisites and confirm that the Vulkan tools can see your GPU:

```bash
python -m executorch.backends.arm.vgf.check_env --aot
command -v model-converter
command -v glslc
vulkaninfo --summary
```

Resolve any `FAIL` entries before continuing. The tool paths should belong to this environment, and the Vulkan summary should identify your GPU and driver.

## Build the host runner

Keep the Python environment active and the generated `setup_path.sh` sourced. Configure a separate build directory for the VGF runner:

```bash
cmake -S . -B cmake-out-deit-vgf \
  -DCMAKE_BUILD_TYPE=Release \
  -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
  -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
  -DEXECUTORCH_BUILD_XNNPACK=OFF \
  -DEXECUTORCH_BUILD_VULKAN=ON \
  -DEXECUTORCH_BUILD_VGF=ON \
  -DEXECUTORCH_ENABLE_LOGGING=ON \
  -DPython3_EXECUTABLE="$(command -v python)"

cmake --build cmake-out-deit-vgf --target executor_runner --parallel 4
```

`EXECUTORCH_BUILD_VGF` includes the Arm VGF delegate. The Vulkan option enables the associated runtime components. The build produces `cmake-out-deit-vgf/executor_runner` for your host architecture.

## Save the Learning Path helper

Create a directory for your artifacts, and preserve failures when logging command output:

```bash
mkdir -p arm_test/deit_vgf
set -o pipefail
```

Download the [DeiT-Tiny Learning Path helper](../deit_vgf_helper.py) and save it as `arm_test/deit_vgf/deit_vgf_helper.py` in your ExecuTorch checkout. If your browser displays the source, use **Save as** to save it with the `.py` extension. Review the file before running it.

The helper belongs to this Learning Path, not the ExecuTorch example. It handles checkpoint compatibility, image preparation, and result decoding without changing the example. Training, export, and inference still use ExecuTorch's existing scripts and runner.

## What you've accomplished

You have prepared the tools, built the VGF runner, and saved the helper. Next, you will fine-tune the classifier and prepare its checkpoint for export.
