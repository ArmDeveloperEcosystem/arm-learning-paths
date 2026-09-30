---
title: Classify pet images with DeiT-Tiny and Arm VGF using ExecuTorch
description: Fine-tune DeiT-Tiny for pet breed classification, export a quantized ExecuTorch program with Arm VGF, and run inference on a Linux host.

draft: true
cascade:
    draft: true

minutes_to_complete: 120

who_is_this_for: This Learning Path is for machine learning developers who want to deploy an image classifier with ExecuTorch and Arm VGF using the ML SDK for Vulkan's host emulation layers.

learning_objectives:
    - Prepare ExecuTorch, the ML SDK for Vulkan, and a VGF runner on a Linux host
    - Fine-tune DeiT-Tiny on the Oxford-IIIT Pet dataset and export a quantized VGF-backed ExecuTorch program
    - Classify a pet image with the VGF-backed ExecuTorch program
    - Compare the predicted breed with the dataset label and confirm VGF execution on the host

prerequisites:
    - An Arm Linux development machine
    - A working Vulkan 1.3 or later GPU driver with shaderFloat64 support for the packaged ML emulation layer
    - Internet access and sufficient disk space for the source code, SDK, Oxford-IIIT Pet dataset, and model checkpoints

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
        link: https://github.com/pytorch/executorch/tree/v1.5.1/examples/arm/image_classification_example_vgf
        type: website
    - resource:
        title: ExecuTorch Arm VGF backend documentation
        link: https://github.com/pytorch/executorch/blob/v1.5.1/docs/source/backends/arm-vgf/arm-vgf-overview.md
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
