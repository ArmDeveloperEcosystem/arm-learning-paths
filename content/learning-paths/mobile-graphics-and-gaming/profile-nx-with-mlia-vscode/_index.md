---
title: Capture and analyze NX profiling data with MLIA for VS Code

draft: true
cascade:
    draft: true

description: Capture neural accelerator statistics on an Android device and use MLIA for VS Code to trace measured performance through Model Explorer to your Python model.

minutes_to_complete: 90

who_is_this_for: >-
    You're a machine learning or graphics developer investigating model performance on Arm neural accelerators (NX).

learning_objectives:
    - Prepare a debug-enabled VGF model and an Android Scenario Runner workload
    - Capture and validate NX neural statistics from a device
    - Analyze measured performance in MLIA for VS Code and Model Explorer
    - Trace reported costs to Python source using graph mappings, heatmaps, and CodeLens

prerequisites:
    - An x86-64 Ubuntu 24.04 LTS host with internet access and permission to install development tools
    - Visual Studio Code 1.100 or later on the host
    - An Arm64 Android device with USB debugging and a driver supporting Vulkan data-graph execution and VK_ARM_data_graph_neural_accelerator_statistics; check the documented r56p0 driver on the [Android preparation page](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/2-prepare-android-workload/#check-the-host-tools-and-device)
    - Familiarity with Bash, ADB, and PyTorch model export
    - The PTQ model and Python source from [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/); read the [version requirements](/learning-paths/mobile-graphics-and-gaming/profile-nx-with-mlia-vscode/1-prepare-model-and-workspace/#prepare-a-compatible-vgf-export) before installing its tools or exporting the model

author: Matthew Sloyan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - MLIA
    - NX
    - Visual Studio Code
    - Model Explorer
    - ExecuTorch
    - Python
    - VGF
    - Vulkan
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
    - resource:
        title: MLIA for VS Code user guide
        link: https://github.com/arm/vscode-mlia/blob/main/docs/users/README.md
        type: documentation
    - resource:
        title: Neural Statistics Vulkan layer
        link: https://github.com/arm/vulkan-layer-neural-statistics
        type: repository
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-manifest
        type: repository
    - resource:
        title: NX performance estimation Learning Path proposal
        link: https://github.com/ArmDeveloperEcosystem/arm-learning-paths/pull/3876
        type: documentation
    - resource:
        title: Analyze Ethos-U models with MLIA
        link: /learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
