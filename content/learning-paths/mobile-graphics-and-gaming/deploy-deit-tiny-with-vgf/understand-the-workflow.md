---
title: Understand the DeiT-Tiny deployment workflow
description: Follow a pet classifier from DeiT-Tiny fine-tuning through quantization and VGF export to inference with the ML SDK for Vulkan.
weight: 2
layout: "learningpathall"
---

## How you'll classify a pet image with VGF

You'll fine-tune a Data-efficient Image Transformer (DeiT) model called DeiT-Tiny to recognize 37 cat and dog breeds. You'll then export the classifier with the Arm VGF backend and run a pet image through ExecuTorch. The classifier selects one of the 37 breed labels for the image.

You'll use the training and export scripts from the [ExecuTorch 1.5.1 example](https://github.com/pytorch/executorch/tree/v1.5.1/examples/arm/image_classification_example_vgf). You'll then run inference with `executor_runner`. A downloadable helper handles checkpoint compatibility, image preparation, and breed decoding, so you don't need to edit the example.

### Follow the model through the pipeline

Follow these stages:

1. Prepare the Linux environment and build `executor_runner` to execute the exported model.
2. Fine-tune DeiT-Tiny on Oxford-IIIT Pet images to produce a checkpoint for 37 breeds.
3. Quantize and export the checkpoint to produce a VGF-backed ExecuTorch `.pte` program.
4. Run the program on a pet image to obtain a breed prediction and confirm VGF execution.

The exporter uses `VgfCompileSpec("TOSA-1.0+INT")`. Tensor Operator Set Architecture (TOSA) describes the model graph for the ML SDK model converter. The converter compiles the graph into VGF delegate data. The exporter then embeds that data in the `.pte` program for the VGF runtime to execute.

The model uses the following tensor interfaces:

| Tensor | Shape | Data |
|---|---|---|
| Input | `[1, 3, 224, 224]` | Preprocessed RGB image, float32 |
| Output | `[1, 37]` | One float32 class score per breed |

Quantization applies inside the model. You still supply the normalized floating-point image expected by its exported input.

### Understand the execution target

The ML SDK for Vulkan supplies emulation layers for the Arm tensor and data graph extensions. These layers let you develop the VGF workflow on a compatible host GPU before integrating it with a device application.

You'll validate host execution and a breed prediction. Timing from this emulation workflow doesn't establish performance on an Arm GPU, and this example doesn't deploy an Android application.

{{% notice Note %}}
Allow additional time for dependency downloads, builds, and three training epochs. CPU training can take substantially longer than the estimated reading and setup time.
{{% /notice %}}

## What you've learned and what's next

You've learned how the fine-tuned model becomes a VGF-backed ExecuTorch program and what the host run demonstrates.

Next, you'll prepare the development environment.
