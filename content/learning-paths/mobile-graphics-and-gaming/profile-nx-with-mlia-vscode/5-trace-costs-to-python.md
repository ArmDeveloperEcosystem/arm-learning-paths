---
title: Follow graph operations to Python source
description: Follow a profiled graph operation to SmallUpscalerModel's original Python source in VS Code.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Follow an operation to Python

Keep the completed profiling run selected in **Analysis Runs** and the `total_cycles` overlay selected in Model Explorer.

Expand the cascade you selected on the previous page and select a mapped operation node in **Source Model**. VS Code opens `quantize_and_export_vgf.py` and highlights the corresponding line. For a convolution in `SmallUpscalerModel`, this is `x = self.net(x)`, which calls the model's `nn.Sequential` block.

Source navigation is enabled by default. If the file doesn't open, see the [MLIA source-navigation troubleshooting guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/troubleshooting.md#source-files-do-not-open). For a moved source file, use the [source-file mapping guide](https://github.com/arm/vscode-mlia/blob/main/docs/users/source-file-mapping.md).

## What you've accomplished

You've captured an NX dispatch, inspected a cascade's cycle cost, and followed a mapped operation to the Python model.
