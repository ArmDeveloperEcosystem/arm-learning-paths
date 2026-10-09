---
title: Understand MLIA and the NX Performance Estimator
description: Learn how MLIA converts models and uses the NX Performance Estimator to advise on Arm Neural Technology compatibility and performance.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Estimate performance before deployment

Arm ML Inference Advisor (MLIA) helps you evaluate a model for an Arm target before you build a deployment pipeline or tune an application on a device. You provide a model and a target profile, then inspect compatibility checks, performance metrics, and advice.

In this Learning Path, you'll use the `mlia-neural-technology` package to evaluate two pretrained, quantized MobileNet V1 image classifiers from TensorFlow's public model catalog. You'll compare a baseline with a smaller-input variant under the same Neural Technology configuration. You don't need a model stored in this repository or a device to run the estimator.

The tested example reduces estimated total cycles from `136,962` to `79,824`. These are compiler estimates, not device measurements or an accuracy result. The model comparison section explains the model and configuration assumptions behind this comparison.

If you have an NX-capable Android device and a compatible native Vulkan driver, the [optional device section](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/7-run-on-nx-device/) shows how to execute the model and bring a measured capture back to MLIA.

## Connect the NX and Ethos-U workflows

The [Analyze Ethos-U models with MLIA Learning Path](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/) applies the same workflow to Arm Ethos-U: select a target profile, check compatibility, inspect performance, and use the advice to guide your next change. It uses Vela for compiler estimates and Corstone for whole-model NPU performance counters. Here, you'll use the Neural Technology plugin and NX Performance Estimator, with optional measurements from an Android device.

The report-reading approach carries across targets, but their backends, supported operators, and performance metrics differ. Don't compare cycle counts across targets as though they describe the same hardware configuration. For a visual workflow, see the [Ethos-U VS Code and Model Explorer walkthrough](/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/7-vscode-plugin/).

## Understand the conversion and analysis flow

The Neural Accelerator (NX) Performance Estimator backend evaluates Arm Neural Technology targets. In this workflow, the tools perform the following steps:

1. Download a public LiteRT model in `.tflite` format.
2. Convert it to Tensor Operator Set Architecture (TOSA) MLIR with the public LiteRT-to-TOSA converter.
3. Check TOSA operator compatibility with MLIA and the ML SDK Model Converter.
4. Convert the TOSA graph to a Vulkan Graph Format (VGF) artifact and run the NX Performance Estimator.
5. Write standardized JSON results and detailed estimator artifacts.

You'll convert the models before analysis so that you can distinguish a conversion failure from an estimator failure. With the `mlia-converters-litert` plugin installed, MLIA can also perform that conversion automatically when you pass a `.tflite` file directly.

## Select a target profile

The Neural Technology plugin supplies `neural-technology`, `NX-peak-12SC-8NX-600MHz`, and `NX-sustained-12SC-8NX-350MHz` profiles. Each profile selects system and compiler configuration files. Use the same profile and configuration when comparing model variants; changing both the model and the target makes the result harder to interpret.

## What you've learned and what's next

You've learned how model conversion, compatibility analysis, and performance estimation fit together. Next, you'll install the public packages and verify that the Neural Technology profiles are available.
