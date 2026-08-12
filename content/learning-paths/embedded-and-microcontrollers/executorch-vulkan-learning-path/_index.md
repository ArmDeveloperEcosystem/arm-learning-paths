---
title: Run ExecuTorch Llama 3.2 1B Instruct on a Vivo X300 Pro with Vulkan

description: Learn how to export Llama 3.2 1B Instruct with ExecuTorch, build the Android Vulkan runtime, and run the model on a Vivo X300 Pro.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for developers who want to export a Llama 3.2 model with ExecuTorch and run it on an Android phone through the Vulkan backend.

learning_objectives:
  - Set up a Linux host for Android cross-compilation, ADB deployment, and Vulkan-backed ExecuTorch builds.
  - Pin the host Python and PyTorch environment required by the ExecuTorch 1.4 release branch.
  - Export Meta Llama 3.2 1B Instruct to a Vulkan-enabled `.pte` with the exact quantization settings used in the guide.
  - Build, deploy, validate, and troubleshoot the Android `llama_main` runner on a Vivo X300 Pro.

prerequisites:
  - A Linux host with enough disk space for the ExecuTorch source tree, Android SDK and NDK, Vulkan SDK, and the Llama checkpoint.
  - A Vivo X300 Pro or a similar Android phone with USB debugging enabled.
  - Access to the gated Hugging Face repository `meta-llama/Llama-3.2-1B-Instruct`.
  - Working familiarity with the shell, Python virtual environments, and Android ADB workflows.

author: Ash Naik

skilllevels:
  - Advanced

subjects:
  - ML

operatingsystems:
  - Linux
  - Android

tools_software_languages:
  - ExecuTorch
  - PyTorch
  - Python
  - Android SDK
  - Android NDK
  - ADB
  - Vulkan
  - glslc
  - Hugging Face
armips:
  - Cortex-A
  - Mali

further_reading:
  - resource:
      title: ExecuTorch repository
      link: https://github.com/pytorch/executorch
      type: documentation
  - resource:
      title: ExecuTorch Llama documentation
      link: https://github.com/pytorch/executorch/blob/main/docs/source/llm/llama.md
      type: documentation
  - resource:
      title: ExecuTorch Android Vulkan documentation
      link: https://github.com/pytorch/executorch/blob/main/docs/source/android-vulkan.md
      type: documentation

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

## About this Learning Path

This Learning Path turns the material from `ExecuTorch_Llama32_Vivo_X300Pro_End_to_End_Guide.docx` into an Arm-style walkthrough. It keeps the exact versions, commands, and measured results from the successful run, while reorganizing them into a sequence you can follow from environment setup through validation.

### Who is this for?

This topic is for developers targeting Android Arm64 devices who want to run an LLM locally with ExecuTorch and the Vulkan backend instead of CPU-only inference.

### What will you learn?

Upon completion of this Learning Path, you will be able to:

- Prepare the Android SDK, NDK, ADB, and host Vulkan toolchain required for cross-compiling ExecuTorch.
- Fix the PyTorch version mismatch that can break ExecuTorch 1.4 builds on the host.
- Export Llama 3.2 1B Instruct to a Vulkan-ready `.pte` using the same `8da4w` and KV-cache settings as the measured run.
- Build the Android runtime and `llama_main`, deploy them to the phone, and confirm Vulkan-backed execution.

### Prerequisites

Before starting, you will need the following:

- A Linux machine that can build native and Android targets.
- Android Studio or an equivalent Android SDK and NDK installation path.
- A phone connected over USB with developer mode and USB debugging enabled.
- Hugging Face access to download `meta-llama/Llama-3.2-1B-Instruct`.
- Sufficient storage for a multi-gigabyte checkpoint and exported `.pte`.
