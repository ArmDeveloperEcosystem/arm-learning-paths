---
title: Inspect the model graph with Model Explorer
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Model Explorer?

Model Explorer is a visualization tool for inspecting neural network structures and execution graphs. Arm provides a VGF adapter for Model Explorer, allowing you to inspect the graph of a `.vgf` model created by the export pipeline.

This lets you inspect model architecture, tensor shapes, and graph connectivity before deployment. It does not visualize or evaluate rendered output quality; use the evaluation notebook to compare model output with the ground truth.

## Set up the VGF adapter

The VGF adapter extends Model Explorer to support `.vgf` files exported from the Model Gym toolchain.

## Install the VGF adapter with pip

Run:

```bash
pip install vgf-adapter-model-explorer
```

The VGF adapter model explorer source code is available on [GitHub](https://github.com/arm/vgf-adapter-model-explorer).

## Install Model Explorer

The next step is to make sure the Model Explorer itself is installed. Use pip to set it up:

```bash
pip install torch ai-edge-model-explorer
```

## Launch the viewer

Once installed, launch the explorer with the VGF adapter:

```bash
model-explorer --extensions=vgf_adapter_model_explorer
```

Use the file browser to open the `.vgf` model exported by the QAT notebook from:

```output
neural-graphics-model-gym-examples/tutorials/output/vgf
```

You have now trained, evaluated, quantized, and exported an NFRU model, then inspected its graph with Model Explorer. Continue to Next Steps for more neural graphics resources.
