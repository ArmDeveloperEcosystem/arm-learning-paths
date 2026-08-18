---
title: Overview
description: Review the target architecture, host responsibilities, and end-to-end flow for running ExecuTorch with Vulkan on Android.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Goal

The goal is to run Meta Llama 3.2 1B Instruct directly on a Vivo X300 Pro with ExecuTorch, using the phone GPU through the Vulkan backend.

The Linux host is used for:

- model export
- quantization
- graph lowering and partitioning
- Android cross-compilation
- ADB deployment

The Linux host does not need CUDA, ROCm, or a working Vulkan GPU.

## Linux host architecture

![Diagram showing the Linux host architecture for the ExecuTorch Vulkan workflow, including PyTorch and ExecuTorch 1.4, export and quantization stages, and the generated Vulkan-enabled program artifact#center](linux-host-architecture.png "Linux host architecture for the ExecuTorch Vulkan workflow")

## Android device architecture

![Diagram showing the Android device architecture for the ExecuTorch Vulkan workflow, with llama_main calling the ExecuTorch runtime, which uses the Vulkan backend on the Mali GPU inside the Vivo X300 Pro#center](android-device-architecture.png "Android device architecture for the ExecuTorch Vulkan workflow")

## What you will build

By the end of this Learning Path you will have:

- a working ExecuTorch host environment
- a Vulkan-enabled Llama `.pte` model
- an Android `llama_main` binary
- the model, tokenizer, and runner deployed under `/data/local/tmp/llama` on your Android device
- a reproducible validation flow for checking that Vulkan is actually in use
