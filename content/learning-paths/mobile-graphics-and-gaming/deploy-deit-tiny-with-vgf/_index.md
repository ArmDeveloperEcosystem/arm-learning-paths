---
title: Classify pet images with DeiT-Tiny and Arm VGF using ExecuTorch
description: Fine-tune DeiT-Tiny, export a quantized model with the Arm VGF backend, and classify a pet image using ExecuTorch and the ML SDK for Vulkan.

draft: true
cascade:
    draft: true

minutes_to_complete: 120

who_is_this_for: This Learning Path is for machine learning developers who want to deploy an image classifier through the Arm VGF backend and run it with the ML SDK for Vulkan.

learning_objectives:
    - Prepare ExecuTorch, the ML SDK for Vulkan, and a VGF runner on a Linux host
    - Fine-tune DeiT-Tiny on the Oxford-IIIT Pet dataset and export a quantized VGF program
    - Classify a pet image with the VGF-backed ExecuTorch program
    - Inspect the predicted breed and confirm VGF execution

prerequisites:
    - A Linux development machine with an aarch64 or x86_64 processor
    - A working Vulkan 1.3 or later GPU driver with shaderFloat64 support for the packaged ML emulation layer
    - Python 3.12, Git, a C++ compiler, and Make
    - Familiarity with Python virtual environments, PyTorch, and model training
    - Internet access and disk space for the source code, SDK, Oxford-IIIT Pet dataset, and model checkpoints

author: Usamah Zaheer

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Python
    - VGF
    - Vulkan
    - CMake
    - Hugging Face
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: ExecuTorch VGF image classification example
        link: https://github.com/pytorch/executorch/tree/9dfe4086846ad372b8b78976586ee1857a0c6d13/examples/arm/image_classification_example_vgf
        type: website
    - resource:
        title: ExecuTorch Arm VGF backend documentation
        link: https://github.com/pytorch/executorch/blob/9dfe4086846ad372b8b78976586ee1857a0c6d13/docs/source/backends/arm-vgf/arm-vgf-overview.md
        type: documentation
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-for-vulkan
        type: website
    - resource:
        title: DeiT-Tiny model card
        link: https://huggingface.co/facebook/deit-tiny-patch16-224
        type: documentation
    - resource:
        title: Oxford-IIIT Pet dataset on Hugging Face
        link: https://huggingface.co/datasets/timm/oxford-iiit-pet
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
