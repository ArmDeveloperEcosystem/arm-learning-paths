---
title: Prepare your model and VS Code workspace
description: Export SmallUpscalerModel with Python debug information and set up MLIA for VS Code.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the NX profiling workflow

You'll run `SmallUpscalerModel` on an Android device with an Arm neural accelerator (NX) and capture one execution with Scenario Runner. Then you'll inspect cycle costs and follow an operation to its Python source.

The MLIA for VS Code extension runs Arm ML Inference Advisor (MLIA) and presents the results in Model Explorer. The example uses zero-filled input to exercise the graph; it doesn't assess image quality.

## Prepare a compatible VGF export

MLIA needs VGF 0.4.3 from Model Converter v0.10.0, as specified in the extension's [VGF preparation guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/creating-vgf-model.md). Use ExecuTorch v1.5.1, which selects that converter.

In a new project directory, create an export environment:

```bash
python3.12 -m venv export-venv
source export-venv/bin/activate
python -m pip install \
    'executorch[vgf]==1.5.1' \
    'torch==2.14.0+cpu' \
    'torchvision==0.29.0+cpu' \
    --extra-index-url https://download.pytorch.org/whl/cpu
```

Keep this environment active so that Model Converter stays on `PATH`.

Save the complete `SmallUpscalerModel` post-training quantization (PTQ) example from [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/3-run-ptq-and-export-vgf/#run-the-end-to-end-ptq-example) as `quantize_and_export_vgf.py` in your project directory. Run it in the export environment:

```bash
python quantize_and_export_vgf.py
```

The script downloads CIFAR-10, trains for one epoch, applies PTQ, and exports `output/output_tag0.tosa.vgf`.

The sample includes both debug options needed for source navigation:

- `compiler_flags=["--emit-debug-info"]` in `VgfCompileSpec` preserves debug information when Model Converter converts TOSA to VGF.
- `.dump_debug_info(VgfCompileSpec.DebugMode.TOSA)` embeds ExecuTorch stack traces and module metadata in the intermediate TOSA graph.

Keep the Python file unchanged and in this directory so its paths and line numbers match the exported debug information.

## Create a profiling workspace

Open the directory containing `quantize_and_export_vgf.py` in VS Code using **File > Open Folder**. Open **Terminal > New Terminal** and use Bash for the remaining commands.

Copy the exported model into the profiling workspace:

```bash
export NX_WORKSPACE="$PWD/nx-profile"
export MODEL_VGF="$PWD/output/output_tag0.tosa.vgf"
mkdir -p "$NX_WORKSPACE/workload" "$NX_WORKSPACE/captures"
cp "$MODEL_VGF" "$NX_WORKSPACE/workload/model.vgf"
cd "$NX_WORKSPACE"
```

Keep this terminal open for the preparation and capture commands. Leave the Python source in the project directory.

## Prepare the extension's managed environment

Install MLIA for VS Code v0.1.1 using the [extension installation instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md#install-the-extension).

In VS Code:

1. Select **MLIA** in the Activity Bar.
2. In **New Analysis**, select **Refresh MLIA Environment** and wait for setup to finish.

    <img src="/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/images/refresh-environment.png" width="360" style="max-width: 100%; height: auto;" alt="MLIA's New Analysis view prompts you to set up the environment. Select Refresh MLIA Environment to begin setup." title="Initialize the managed MLIA environment" class="content-uploaded-image centered" />
    <span class="content-image-caption centered">Initialize the managed MLIA environment</span>

The extension manages its own Python and MLIA installation separately from your export environment. For setup problems, see the [MLIA environment troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/troubleshooting.md#environment-refresh-fails).

## What you've accomplished and what's next

You've exported the model and initialized MLIA in VS Code. Next, prepare the Android workload.
