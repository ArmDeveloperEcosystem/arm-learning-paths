---
title: Prepare your environment and image
description: Install the Swin2SR example and Arm ML SDK, then prepare a 64 × 64 input image and its high-resolution reference.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you'll build

You will upscale a low-resolution image using Swin2SR, a pretrained image super-resolution model. It predicts finer detail as it doubles the image's width and height.

You export the model with ExecuTorch, then run it through the Arm Vulkan Graph Format (VGF) backend. The result is a PNG image you can open and compare with a high-resolution reference.

![Equal-size views compare a 64 by 64 low-resolution input with its 128 by 128 Swin2SR output. The input is enlarged for display only; labels show actual pixel dimensions. ExecuTorch and Arm VGF run the model on the host.#center](swin2sr-image-flow.svg "Images shown at the same display size to compare detail; labels show actual resolution")

This workflow runs on your Linux host using the Arm ML SDK's Vulkan emulation layer. It introduces the model execution flow used by Arm neural graphics; it doesn't deploy an application to a phone or measure Mali GPU performance.

## Prepare the Linux host

Use a 64-bit Linux system (AArch64 or x86_64) with a working Vulkan 1.3 GPU driver. The packaged ML SDK checks for the `shaderFloat64` feature, even though you export a floating-point 32-bit model. The setup script stops if your GPU doesn't support it. Apple Silicon with MoltenVK needs a separate source-built SDK, which isn't covered here.

On Ubuntu 24.04, install Python 3.12, the build tools, and the Vulkan development files:

```bash
sudo apt-get update
sudo apt-get install -y \
  ca-certificates curl git build-essential pkg-config \
  python3.12 python3.12-venv python3.12-dev \
  libvulkan1 libvulkan-dev vulkan-tools unzip xz-utils
```

These packages don't install your GPU's vendor-specific driver. The Python installation step installs CMake 3.31.10.

## Get the ExecuTorch release

Use [ExecuTorch 1.5.1](https://github.com/pytorch/executorch/releases/tag/v1.5.1) for both the Python package and native source. From a path without spaces or an existing `executorch` folder, clone the matching release. Keep the checkout folder named `executorch`; the build requires this exact name:

```bash
git clone --branch v1.5.1 --single-branch --depth 1 \
  https://github.com/pytorch/executorch.git executorch
cd executorch
test "$(git rev-parse HEAD)" = 3b60683923245cf472b7323426920e15623ba361
git submodule sync --recursive
git submodule update --init --recursive
```

Run the remaining commands from this repository root, in the same terminal.

## Configure the Arm ML SDK

Create a fresh Python environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Review the [ML SDK license terms](https://github.com/arm/ai-ml-sdk-for-vulkan/tree/main/LICENSES) and the Vulkan SDK terms. Use the setup script included in the release to install the SDK tools:

```bash
bash examples/arm/setup.sh --disable-ethos-u-deps --enable-mlsdk-deps
```

The setup script also installs three developer packages that this example doesn't use. Remove them from the fresh environment before resolving the example's dependencies:

```bash
python -m pip uninstall -y \
  tosa-adapter-model-explorer ai-edge-model-explorer pytest-timeout
```

## Install the release packages

Install the released CPU PyTorch stack, VGF packages, build tools, and Swin2SR dependencies:

```bash
python -m pip install \
  --index-url https://pypi.org/simple \
  --extra-index-url https://download.pytorch.org/whl/cpu \
  'executorch[vgf]==1.5.1' \
  'torch==2.14.0+cpu' 'torchvision==0.29.0+cpu' 'torchao==0.18.0+cpu' \
  'cmake==3.31.10' 'zstd==1.5.7.2' \
  -r examples/arm/super_resolution_example_vgf/requirements.txt \
  -r backends/arm/requirements-arm-vgf-runtime.txt
python -m pip check
```

The example pins Transformers 4.56.1, NumPy 2.1.3, and Pillow 12.0.0. The `+cpu` packages avoid a CUDA dependency during export; the host runner still uses Vulkan.

Run this installation after SDK setup to resolve its older FlatBuffers dependency. `pip check` should report `No broken requirements found.` Don't run `install_executorch.sh`, which uses nightly package indexes. If you rerun SDK setup, repeat the package removal and release installation.

## Check the tools

Activate the SDK paths, check export prerequisites, and confirm that Vulkan can see your GPU:

```bash
source examples/arm/arm-scratch/setup_path.sh
python -m executorch.backends.arm.vgf.check_env --aot
python -c "import executorch.exir; from executorch.extension.pybindings import portable_lib; print('ExecuTorch is ready')"
command -v model-converter
command -v glslc
vulkaninfo --summary
vulkaninfo | grep shaderFloat64
```

Resolve any `FAIL` entries before continuing. Confirm `shaderFloat64 = true` for your device, and keep this terminal open for the remaining steps.

## Prepare the input image

Create the example images from a screenshot included in ExecuTorch:

```bash
python examples/arm/super_resolution_example_vgf/model_export/prepare_demo_assets.py \
  --output-dir swin2sr-work
```

The script creates a 128 × 128 crop and downsizes a copy to 64 × 64. You use these two files:

| File in `swin2sr-work/runtime/` | What it is |
| --- | --- |
| `demo_lr_64.png` | Small image you give to the model |
| `demo_hr_128.png` | High-resolution reference: the original crop before downsampling |

The helper also prepares calibration and evaluation folders. You don't need them for this floating-point walkthrough.

## What you've accomplished and what's next

You have the example, its tools, and a small input image with a high-resolution reference. Next, export Swin2SR as an ExecuTorch program.
