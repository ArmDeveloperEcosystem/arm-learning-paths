---
title: Prepare model work for NX
description: Use public Arm workflows to train, evaluate, quantize, export, and validate a neural graphics model for deployment.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Customize only for a measured reason

Start with the published model. Customize it only when the runtime exposes a reproducible quality or performance gap. The [model workflow in Arm Neural Technology Playbook - Evaluate](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/06-models-in-practice/) explains when to make that move.

## Design with NX in mind

<!-- TODO: Link the guide title below when the public NX Best Practices URL is available. -->

Use the **Neural Network Model Development Best Practices for GPUs with Neural Accelerator** guide to understand how the GPU Execution Engine and NX divide a workload, choose precision and quantization deliberately, limit avoidable data movement and execution transitions, and connect model design to measurement, conversion, and deployment.

## Use Model Gym for NSS and NFRU model workflows

[Neural Graphics Model Gym](https://github.com/arm/neural-graphics-model-gym) supports NSS and NFRU model workflows. It covers training, fine-tuning, evaluation, quantization, and export for ML extensions for Vulkan.

Use it in four steps:

1. Reproduce the issue with a prebuilt model and fixed data.
2. Prepare a fixed training and evaluation dataset that represents the measured issue.
3. Follow [Train and evaluate NFRU models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym-nfru/) to train or fine-tune an NFRU model, then compare quality before and after quantization.
4. Export and validate the artifact with [Prepare models for Arm Neural Technology](/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/).

## Connect model estimates to measured results

Compare each candidate against the same data. Record quality before and after quantization, and confirm the exported model runs. For a supported model input, use [MLIA compatibility checks and NX performance estimates](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/) to investigate model cost before deployment. Keep the target profile and configuration fixed when comparing candidates.

When you have supported NX hardware, follow [Profile Arm Neural Technology workloads with Streamline](/learning-paths/mobile-graphics-and-gaming/streamline-nx/) to measure the integrated workload. An estimator result doesn't establish image quality, frame pacing, power, or thermal behavior in your game.

Change one variable at a time, and validate each hardware-aware design choice against your workload.

## What you've learned

You now have a bounded model workflow, from a reproducible gap through training, quantization, and export. Next, use the model toolkit to connect compatibility checks and performance estimates to device evidence.
