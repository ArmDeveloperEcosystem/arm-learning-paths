---
title: Choose the right Arm tooling path
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Model Gym vs manual lowering with ExecuTorch

You now have two practical ways to prepare neural graphics models:

- Model Gym: higher-level workflow for training, evaluation, and export
- Manual ExecuTorch flow: low-level control over VGF export, TOSA inspection, and runtime validation

## When to use Model Gym

Use [Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/) when you want to:
- Fine-tune NSS quickly
- Work through notebook-based training and evaluation
- Standardize export pipelines with less backend-level tuning

## When to use manual lowering

Use the manual flow from this Learning Path when you need to:
- Debug export correctness at the TOSA level
- Control backend partitioning and artifact generation
- Validate backend/runtime behavior with custom test graphs
- Build confidence with a toy model before moving to Scenario Runner or engine-level validation

## Recommended next learning paths

- [Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/)
- [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/)
- [Enable neural graphics using ML Extensions for Vulkan](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/)
- [Running a test with the Scenario Runner](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/4-scenario-runner/)
- [Enable Neural Super Sampling in Unreal Engine with ML Extensions](/learning-paths/mobile-graphics-and-gaming/nss-unreal/)
