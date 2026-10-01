---
title: Prepare ExecuTorch and build the VGF runner
description: Set up the DeiT example dependencies and ML SDK for Vulkan, then build a VGF-enabled ExecuTorch runner on your Linux host.
weight: 3
layout: "learningpathall"
---

## Prepare a Linux host

Use Python 3.12 on Linux. On Ubuntu 24.04, install the system tools and Vulkan development files:

```bash
sudo apt-get update
sudo apt-get install -y \
  ca-certificates curl git build-essential pkg-config \
  python3.12 python3.12-venv python3.12-dev \
  libvulkan1 libvulkan-dev vulkan-tools unzip xz-utils
```

Your GPU's Vulkan driver must also be installed and working. These packages don't install a vendor-specific driver.

## Clone the ExecuTorch release

Use the [ExecuTorch 1.5.1 release](https://github.com/pytorch/executorch/releases/tag/v1.5.1) for both the Python package and native source. This release uses stable PyTorch and TorchAO packages. The instructions don't depend on a dated nightly wheel.

Create a new workspace in a path without spaces, then clone the matching source:

```bash
mkdir deit-vgf-workspace
cd deit-vgf-workspace
git clone --branch v1.5.1 --single-branch --depth 1 \
  https://github.com/pytorch/executorch.git executorch
cd executorch
test "$(git rev-parse HEAD)" = 3b60683923245cf472b7323426920e15623ba361
git submodule sync --recursive
git submodule update --init --recursive
```

Keep the repository directory named `executorch`. The build checks this name. Run all remaining commands from this repository root in the same shell.

The source checkout provides the example and C++ runner. Export uses the matching released Python package.

## Create the Python environment

Create a fresh Python 3.12 environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
mkdir -p arm_test/deit_vgf
set -o pipefail
```

The directory holds your model, images, and logs. `pipefail` preserves command failures when you save logs with `tee` later.

## Configure the ML SDK for Vulkan

Review the [ML SDK license terms](https://github.com/arm/ai-ml-sdk-for-vulkan/tree/main/LICENSES) and the Vulkan SDK terms before using the tooling. Use the setup script already included in ExecuTorch:

```bash
bash examples/arm/setup.sh --disable-ethos-u-deps --enable-mlsdk-deps
```

The script downloads the Vulkan SDK and configures the packaged ML emulation layers. It also installs three developer-only packages that you don't need for this Learning Path. Remove them from the fresh virtual environment before resolving the example's dependencies:

```bash
python -m pip uninstall -y \
  tosa-adapter-model-explorer ai-edge-model-explorer pytest-timeout
```

## Install the Python dependencies

Install the release's CPU-only PyTorch stack, VGF packages, build tools, and example dependencies from PyPI and the stable PyTorch CPU index:

```bash
python -m pip install \
  --index-url https://pypi.org/simple \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  'executorch[vgf]==1.5.1' \
  'torch==2.14.0+cpu' 'torchvision==0.29.0+cpu' 'torchao==0.18.0+cpu' \
  'cmake==3.31.10' 'zstd==1.5.7.2' 'scikit-learn==1.9.1' \
  -r examples/arm/image_classification_example_vgf/requirements.txt \
  -r backends/arm/requirements-arm-vgf-runtime.txt
python -m pip check
```

The expected output is:

```output
No broken requirements found.
```

This installs Transformers 5.3.0 and ML SDK packages 0.10.0. Scikit-learn supplies the training script's accuracy metric.

The `+cpu` wheels still support the VGF runner's Vulkan execution. They make the Python training and export environment independent of CUDA.

The dependency installation resolves the older FlatBuffers version installed by the SDK setup script. Don't run `install_executorch.sh`; you'll use released wheels instead of its nightly indexes. If you rerun the SDK setup, remove the developer-only packages and repeat the dependency installation.

Load the generated SDK environment:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

In a new shell, return to the repository root, activate `.venv`, source `setup_path.sh`, and enable `set -o pipefail` again.

{{% notice Note %}}
You'll use the packaged emulation layer, which needs `shaderFloat64` support at this release. Use a compatible Linux host for these commands. For a separate source-build route for other configurations, see the [ML SDK source-build helper](https://github.com/pytorch/executorch/blob/v1.5.1/backends/arm/scripts/setup-mlsdk-from-source.sh).
{{% /notice %}}

## Check the environment

Check export prerequisites and confirm that the Vulkan tools can see your GPU:

```bash
python -m executorch.backends.arm.vgf.check_env --aot
python -m pip check
command -v model-converter
command -v glslc
vulkaninfo --summary
vulkaninfo | grep shaderFloat64
```

Resolve any `FAIL` entries before continuing. The tool paths should belong to this environment, and the Vulkan summary should identify your GPU and driver. Confirm `shaderFloat64 = true` for the device that you'll use.

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

## What you've accomplished and what's next

You've prepared the release-based environment and built the VGF runner.

Next, you'll fine-tune the classifier and prepare its checkpoint for export.
