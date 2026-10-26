---
title: Prepare model work for NX
description: Use public Arm workflows to train, evaluate, quantize, export, and validate a neural graphics model for deployment.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Customize only for a measured reason

Start with the published model. Customize it only when the runtime exposes a reproducible quality or performance gap. To know when to customize a model, see the model workflow in [Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/06-models-in-practice/).

## Design with NX in mind

Understand how the GPU Execution Engine and neural accelerator (NX) perform the following tasks:

- Divide a workload
- Choose precision and quantization deliberately
- Limit avoidable data movement and execution transitions
- Connect model design to measurement, conversion, and deployment

For more information, see [Neural Network Model Development Best Practices for GPUs with Neural Accelerator](https://developer.arm.com/documentation/112431/latest). Use the [Arm GPU Best Practices Developer Guide](https://support.arm.com/documentation/101897/latest/) alongside it to optimize the graphics workload that runs with your neural model.

## Use Model Gym for NSS and NFRU model workflows

[Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) supports Neural Super Sampling (NSS) and Neural Frame Rate Upscaling (NFRU) model workflows. The Model Gym covers the following workflows: 

- Training
- Fine-tuning
- Evaluation
- Quantization
- Export for ML extensions for Vulkan

Use Model Gym in four steps:

1. Reproduce the issue with a prebuilt model and fixed data.
2. Prepare a fixed training and evaluation dataset that represents the measured issue.
3. Follow [Train and evaluate NFRU models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym-nfru/) to train or fine-tune an NFRU model, then compare quality before and after quantization.
4. Follow [Prepare models for Arm Neural Technology](/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/) to export and validate the artifact.

## Connect model estimates to measured results

Compare each candidate against the same data. Record quality before and after quantization, and confirm the exported model runs. For a supported model input, use [MLIA compatibility checks and NX performance estimates](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/) to investigate model cost before deployment. Keep the target profile and configuration fixed when comparing candidates.

When you have supported NX hardware, follow [Profile Arm Neural Technology workloads with Streamline](/learning-paths/mobile-graphics-and-gaming/streamline-nx/) to measure the integrated workload. An estimator result doesn't establish image quality, frame pacing, power, or thermal behavior in your game.

Change one variable at a time, and validate each hardware-aware design choice against your workload.

## What you've learned

You now have a bounded model workflow, from a reproducible gap through training, quantization, and export. Next, use the model toolkit to connect compatibility checks and performance estimates to device evidence.
