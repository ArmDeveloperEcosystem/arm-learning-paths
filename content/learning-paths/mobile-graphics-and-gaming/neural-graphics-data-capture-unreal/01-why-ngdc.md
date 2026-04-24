---
title: Benefits of Neural Graphics Data Capture for game developers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

The Neural Graphics Data Capture plugin helps you create structured datasets directly from Unreal Engine gameplay. This is useful when you want to train or evaluate neural graphics workloads, such as [Neural Super Sampling (NSS)](/learning-paths/mobile-graphics-and-gaming/nss-unreal/) and other temporal upscalers, with real scene motion, geometry, and camera behavior from your own content.

## Benefits of capturing data from your game content

Capturing from your own gameplay is useful when you want to:

- Fine-tune NSS on your specific game content to improve image quality.
- Evaluate NSS output quality on your own scenes, motion, materials, and camera behavior.
- Train NSS variants, or your own model architecture from scratch, using representative project data.

With this setup, you can create capture data inside Unreal Engine 5.5 without extra graphics API environment configuration. For teams iterating on model experiments, this lowers setup friction and shortens time-to-first-dataset.

## Common workflow for neural graphics data capture

A common workflow is:

- Capture representative gameplay clips from your project.
- Export frames and metadata to a dataset folder.
- Use those datasets as input to Model Gym's [NSS data generation step](https://github.com/arm/neural-graphics-model-gym/blob/main/docs/nss/nss_data_generation.md), which converts captured data into `safetensors` for training.
- Tune rendering/capture settings (for example supersampling, upscaling ratio, fixed frame rate) and capture again.

## Learning Path objectives

You will:

- Install the plugin into a UE 5.5 C++ project.
- Enable and compile the module in Visual Studio.
- Add Level Blueprint nodes to start capture (`C`) and stop capture (`V`).
- Run in Standalone Game mode and verify output in `Saved/NeuralGraphicsDataset`.
