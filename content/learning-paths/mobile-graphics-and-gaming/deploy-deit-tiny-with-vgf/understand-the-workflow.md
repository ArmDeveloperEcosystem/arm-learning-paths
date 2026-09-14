---
title: Understand the DeiT-Tiny deployment workflow
description: Follow a pet classifier from DeiT-Tiny fine-tuning through quantization and VGF export to inference with the ML SDK for Vulkan.
weight: 2
layout: "learningpathall"
---

## Classify a pet image with VGF

You will fine-tune DeiT-Tiny, a Data-efficient Image Transformer, to recognize 37 cat and dog breeds. You will then export the classifier with the Arm VGF backend and run a pet image through ExecuTorch.

You will use the [ExecuTorch example's](https://github.com/pytorch/executorch/tree/9dfe4086846ad372b8b78976586ee1857a0c6d13/examples/arm/image_classification_example_vgf) training and export scripts, then run inference with `executor_runner`. A downloadable Learning Path helper handles checkpoint compatibility, image preparation, and breed decoding. You don't need to edit the example.

## Follow the model through the pipeline

Follow these stages:

1. Prepare the Linux environment and build the VGF runner
2. Fine-tune DeiT-Tiny on Oxford-IIIT Pet images
3. Quantize the model and export a VGF-backed ExecuTorch `.pte` file
4. Classify a pet image and confirm VGF execution

The exporter uses `VgfCompileSpec("TOSA-1.0+INT")`. TOSA, the Tensor Operator Set Architecture, describes the graph that the ML SDK model converter compiles into VGF. The `.pte` includes this delegate data.

The model uses these tensor interfaces:

| Tensor | Shape | Data |
|---|---|---|
| Input | `[1, 3, 224, 224]` | Preprocessed RGB image, float32 |
| Output | `[1, 37]` | One float32 class score per breed |

Quantization applies inside the model. You still supply the normalized floating-point image expected by its exported input.

## Understand the execution target

The ML SDK for Vulkan supplies emulation layers for the Arm tensor and data graph extensions. These let you develop the VGF workflow on a compatible host GPU before integrating it with a device application.

You will validate host execution and a breed prediction. Timing from this emulation workflow does not establish performance on an Arm GPU, and this example does not deploy an Android application.

{{% notice Note %}}
Allow additional time for dependency downloads, builds, and three training epochs. CPU training can take substantially longer than the estimated reading and setup time.
{{% /notice %}}

## What you've learned

You know how the fine-tuned model becomes a VGF-backed ExecuTorch program and what the host run demonstrates. Next, you will prepare the development environment.
