---
title: Inspect the graph with Model Explorer
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

If you use `.vgf` as an intermediate artifact, it helps to inspect the exported graph before you integrate it into your runtime.

## Install the Model Explorer

Install and launch Model Explorer with the VGF adapter:

```bash
pip install vgf-adapter-model-explorer
pip install torch ai-edge-model-explorer
model-explorer --extensions=vgf_adapter_model_explorer
```

Open the `.vgf` file from `./output/` and `./output_qat/`.

When you review the graph, look for unexpected layout conversions (for example, extra transpose operations), operators that you did not intend to run on your GPU path, and model I/O shapes that do not match your integration.

## Advanced: connect the model to an ML Extensions for Vulkan workflow

The fastest way to understand the integration constraints is to start from a known-good sample and then replace the model.

Use the Learning Path [Get started with neural graphics using ML Extensions for Vulkan](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/) and focus on how the sample loads and executes `.vgf` artifacts. This is where you validate assumptions about input and output tensor formats and where any required color-space or layout conversions happen.

## Wrap-up

You now have a complete reference workflow for quantizing an image-to-image model with TorchAO and exporting INT8 `.vgf` artifacts using the ExecuTorch Arm backend. You also have a practical baseline you can use to debug export issues before you switch to your production model and data.

When you move from the CIFAR-10 proxy model to your own model, keep these constraints in mind:

- Treat calibration data as part of your model contract. If PTQ quality drops, start by fixing the representativeness of calibration inputs.
- Use QAT when PTQ introduces visible artifacts or regressions that matter to your visual quality bar.
- Validate early by inspecting the exported graph so you can catch unexpected layouts, operators, or tensor shapes before runtime integration.

Continue to the last page to go deeper on further resources.
