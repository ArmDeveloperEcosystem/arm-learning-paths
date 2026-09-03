---
title: Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch

draft: true
cascade:
    draft: true

description: Export, deploy, and validate a quantized MobileSAM prompt segmentation model on an Arm Ethos-U85 Fixed Virtual Platform using ExecuTorch.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for embedded machine learning developers who want to evaluate transformer-based image segmentation on an Arm Ethos-U85 NPU with ExecuTorch.

learning_objectives:
    - Explain how the MobileSAM example turns a fixed point prompt and an image into a quantized segmentation mask
    - Set up ExecuTorch and the Arm Ethos-U development tools
    - Export, build, and run the MobileSAM example on a Corstone-320 Fixed Virtual Platform
    - Validate quantization quality, Ethos-U delegation, and target mask agreement

prerequisites:
    - A Linux development machine or an Apple silicon Mac
    - Python 3.12, Git, CMake, and a C++ build tool such as Ninja
    - Familiarity with PyTorch model export and embedded cross-compilation
    - Internet access to download ExecuTorch dependencies, Arm development tools, the pinned MobileSAM source, and its checkpoint
    - On macOS, Docker Desktop and the [FVPs-on-Mac wrapper](https://github.com/Arm-Examples/FVPs-on-Mac)

author: Usamah Zaheer

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Ethos-U
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - MobileSAM
    - Python
    - CMake
    - GCC
    - FVP
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: ExecuTorch MobileSAM prompt segmentation example
        link: https://github.com/pytorch/executorch/tree/main/examples/arm/mobilesam_prompt_segmentation_example_ethos_u
        type: repository
    - resource:
        title: ExecuTorch Arm Ethos-U backend documentation
        link: https://docs.pytorch.org/executorch/stable/embedded-arm-ethos-u.html
        type: documentation
    - resource:
        title: MobileSAM source repository
        link: https://github.com/ChaoningZhang/MobileSAM
        type: repository
    - resource:
        title: Arm Ethos-U85 NPU
        link: https://developer.arm.com/Processors/Ethos-U85
        type: documentation
    - resource:
        title: FVPs-on-Mac
        link: https://github.com/Arm-Examples/FVPs-on-Mac
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
