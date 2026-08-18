---
title: Run ExecuTorch Llama 3.2 1B Instruct on a Vivo X300 Pro with Vulkan

draft: true
cascade:
    draft: true

description: Learn how to export Llama 3.2 1B Instruct with ExecuTorch, build the Android Vulkan runtime, and run the model on a Vivo X300 Pro.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to export a Llama 3.2 model with ExecuTorch and run it on an Android phone through the Vulkan backend.

learning_objectives:
  - Set up a Linux host for Android cross-compilation, ADB deployment, and Vulkan-backed ExecuTorch builds.
  - Export Meta Llama 3.2 1B Instruct to a Vulkan-enabled `.pte` with the exact quantization settings used in the guide.
  - Build, deploy, measure, and validate the Android `llama_main` runner on a Vivo X300 Pro.

prerequisites:
  - A Linux host with enough disk space for the ExecuTorch source tree, Android SDK and NDK, Vulkan SDK, and the Llama checkpoint.
  - A Vivo X300 Pro or a similar Android phone with USB debugging enabled.
  - A Hugging Face account.
  - Working familiarity with the shell, Python virtual environments, and Android ADB workflows.

author: Ash Naik

test_maintenance: false

skilllevels: Advanced

subjects: ML

operatingsystems:
  - Linux
  - Android

tools_software_languages:
  - ExecuTorch
  - PyTorch
  - Python
  - Android
  - Vulkan
  - glslc
  - Hugging Face
armips:
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
