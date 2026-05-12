---
title: Inspect the model in Model Explorer
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Model Explorer and adapters

Use the following commands in your active virtual environment:

```bash
pip install torch ai-edge-model-explorer
pip install pte-adapter-model-explorer
pip install tosa-adapter-model-explorer
pip install vgf-adapter-model-explorer
```

## Launch Model Explorer

Run:

```bash
model-explorer --extensions=pte_adapter_model_explorer,tosa_adapter_model_explorer,vgf_adapter_model_explorer
```

When the web UI opens, start with the `.vgf` artifacts in `executorch-model/` or the generated `as-vgf.pte` file. If you later inspect the optional TOSA artifacts, you can use the same Model Explorer flow to compare the intermediate representation with the deployable output.

![Photo of model-explorer](images/model-explorer-home.png)

## What to check

Start by confirming:
- The graph contains the expected add and sigmoid flow
- Input/output tensor shapes match your exported model
- No unexpected decompositions are introduced

![Photo of model with operations](images/model-ops.png)

This same inspection approach is used in [Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/) and [quantization workflows](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/). If you want to go deeper after this point, inspect the TOSA artifacts to understand the intermediate lowering step.
