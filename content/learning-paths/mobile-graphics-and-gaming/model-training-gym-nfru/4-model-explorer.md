---
title: Visualize your model with Model Explorer
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What Model Explorer is

Model Explorer is a visualization tool for inspecting neural network structures and execution graphs. Arm provides a VGF adapter for Model Explorer, so you can visualize `.vgf` models created from your training and export pipeline.

With Model Explorer, you can inspect model architecture, tensor shapes, and graph connectivity before deployment. This can be a powerful way to debug and understand your exported neural graphics models.

## Set up the VGF adapter

The VGF adapter extends Model Explorer to support `.vgf` files exported from the Model Gym toolchain.

Install the VGF adapter with pip:

```bash
pip install vgf-adapter-model-explorer
```

The VGF adapter model explorer source code is available on [GitHub](https://github.com/arm/vgf-adapter-model-explorer).

## Install Model Explorer

The next step is to make sure the Model Explorer itself is installed. Use `pip` to set it up:

```bash
pip install torch ai-edge-model-explorer
```

## Launch Model Explorer

After installing Model Explorer, launch the tool with the VGF adapter:

```bash
model-explorer --extensions=vgf_adapter_model_explorer
```

Use the file browser to open the `.vgf` model exported earlier in your training workflow.

## What you've accomplished and what's mext

You've now learned about Model Explorer and installed the tool to visualize your model.

Next, you'll learn about bringing your own use cases to the Model Gym.


