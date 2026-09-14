---
title: Upscale an image with Swin2SR and Arm VGF

draft: true
cascade:
    draft: true

description: Export Swin2SR with ExecuTorch and run it through Arm VGF on your Linux host to upscale a low-resolution image and reconstruct finer detail.

minutes_to_complete: 60
lastmod: 2026-09-14

who_is_this_for: This is an introductory topic for machine learning and graphics developers who want to run image super-resolution with ExecuTorch and Arm VGF.

learning_objectives:
    - Prepare ExecuTorch, the Arm ML SDK for Vulkan, and a sample image
    - Export a pretrained Swin2SR model as a VGF-backed ExecuTorch program
    - Build the host runner and upscale a 64 × 64 image to 128 × 128
    - Check the output dimensions and compare the result with the high-resolution reference

prerequisites:
    - A 64-bit Linux host (AArch64 or x86_64) with a Vulkan 1.3 GPU and driver that support shaderFloat64, as required by the packaged ML SDK emulation layer
    - Python 3.12 with development headers and venv support, Git, curl, xz-utils, CMake 3.24–3.x, and a C++17 compiler
    - An internet connection to download ExecuTorch, model weights, and the Arm ML SDK dependencies
    - Basic familiarity with Python and command-line tools

author: Usamah Zaheer

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Python
    - Vulkan
    - VGF
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Swin2SR VGF example source
        link: https://github.com/pytorch/executorch/tree/32a86b69388b5a5208e367a96b0f5b7cb39df8e2/examples/arm/super_resolution_example_vgf
        type: code
    - resource:
        title: Swin2SR pretrained model
        link: https://huggingface.co/caidas/swin2SR-classical-sr-x2-64
        type: website
    - resource:
        title: Arm ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-for-vulkan
        type: documentation
    - resource:
        title: Prepare models for neural graphics with Arm neural technology
        link: /learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/
        type: learningpath
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
