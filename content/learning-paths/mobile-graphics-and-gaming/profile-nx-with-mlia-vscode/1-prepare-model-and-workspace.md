---
title: Prepare your model and VS Code workspace
description: Preserve Python debug information in a compatible VGF export and prepare the managed MLIA environment for device profiling.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the NX profiling workflow

The MLIA for VS Code extension lets you analyze model performance within your editor. It runs Arm ML Inference Advisor (MLIA) and presents the results in Model Explorer.

You'll run a small neural upscaler on an Android device with an Arm neural accelerator (NX) and capture its execution. Then you'll use the extension to inspect measured performance and trace costly parts of the model back to Python source.

The workflow has three parts:

| Stage | Tool | Result |
| --- | --- | --- |
| Execute and capture | Scenario Runner and the Neural Statistics Vulkan layer on Android | A directory containing capture metadata and driver statistics |
| Analyze | MLIA for VS Code extension on your Linux host | A saved profiling analysis with measured performance results |
| Investigate | Model Explorer and the source editor within VS Code | Graph overlays, source navigation, heatmaps, and CodeLens |

Capture requires a compatible NX Android device. You can run the Android tools from VS Code's integrated terminal, then copy the capture to your Linux host and load it into the extension for analysis.

The exercise uses one dispatch and zero-filled input to establish the capture and analysis workflow. It doesn't measure application frame time, establish sustained performance, or validate the upscaler's image quality.

{{% notice Draft validation %}}
This draft has not yet been validated from model export through device capture and VS Code source navigation. The device walkthrough and screenshots must be checked before publication.
{{% /notice %}}

## Prepare a compatible VGF export

Use the `SmallUpscalerModel` PTQ example in [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/3-run-ptq-and-export-vgf/). Keep its `quantize_and_export_vgf.py` source file alongside the exported artifacts. Complete that path's environment and PTQ steps; you don't need the QAT example.

Apply the following version requirement **before** running the installation scripts in the [environment setup page](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/2-set-up-your-environment/): after cloning ExecuTorch, select its compatible release:

```bash
cd executorch
git checkout v1.5.1
```

Continue with the installation scripts from that page. The extension's [VGF preparation guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/creating-vgf-model.md) specifies Model Converter v0.10.0 and VGF 0.4.3; ExecuTorch v1.5.1 selects that converter. A newer SDK used to build Scenario Runner later in this path doesn't change the VGF version accepted by MLIA.

Retain both debug options already present in the PTQ example:

- `compiler_flags=["--emit-debug-info"]` in `VgfCompileSpec` embeds ExecuTorch stack traces and module metadata.
- `.dump_debug_info(VgfCompileSpec.DebugMode.TOSA)` preserves the corresponding TOSA debug information during lowering.

Keep the Python file that produced the export unchanged during this exercise. Changing its line numbers or moving it can make source navigation misleading or require path remapping. Debug information and matching source are required for the final page, even though other MLIA workflows can operate without them.

## Create a profiling workspace

Open the directory containing `quantize_and_export_vgf.py` in VS Code using **File > Open Folder**. Open **Terminal > New Terminal** and use Bash for the remaining commands.

From that project directory, list the exported VGF files:

```bash
find output -type f -name '*.vgf'
```

Select the VGF produced by the PTQ example. Replace `<exported-model>.vgf` with its actual filename, then copy it to a stable workload path:

```bash
export NX_WORKSPACE="$PWD/nx-profile"
export MODEL_VGF="$PWD/output/<exported-model>.vgf"
test -s "$MODEL_VGF"
mkdir -p "$NX_WORKSPACE/workload" "$NX_WORKSPACE/captures"
cp "$MODEL_VGF" "$NX_WORKSPACE/workload/model.vgf"
sha256sum "$NX_WORKSPACE/workload/model.vgf" > "$NX_WORKSPACE/model.sha256"
cd "$NX_WORKSPACE"
```

Stop if `test -s` fails: the selected model must exist and contain data. If export produced several partitions, use the artifact corresponding to the graph you intend to capture; the measurements will describe that artifact, not every partition in the original Python program.

Keep this terminal open across the capture pages. `NX_WORKSPACE` identifies the host working directory; later pages also define `SDK_PATH`, `PACKAGE`, and a unique run name. The original Python source stays in the project directory so its embedded locations remain available.

## Prepare the extension's managed environment

Follow the [MLIA extension installation instructions](https://github.com/arm/vscode-mlia/blob/main/docs/users/installation.md). If you use a release VSIX, install it with **Extensions > ... > Install from VSIX...**.

In VS Code:

1. Select **MLIA** in the Activity Bar.
2. In **New Analysis**, select **Refresh MLIA Environment** and wait for setup to finish.
3. Confirm that **Estimation** and **Profiling** are available.
4. Select **Profiling** and confirm that the `neural-technology` target profile is available.

The extension manages its own `uv`, Python, and MLIA installation. Your model-export environment and the SDK build environment are separate. You don't need a command-line MLIA installation for this path.

If setup fails or the profile is absent, select **Show Log** and resolve the environment error before proceeding. See the extension's [environment troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/troubleshooting.md).

## What you've accomplished and what's next

You've prepared a debug-enabled VGF, retained the source that produced it, and initialized MLIA in VS Code. Next, you'll prepare Scenario Runner and generate the Android workload for this exact artifact.
