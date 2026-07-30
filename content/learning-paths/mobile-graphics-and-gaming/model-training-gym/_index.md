---
title: Fine-tune neural graphics models using Model Gym
description: Learn how to train, evaluate, quantize, and export Neural Super Sampling (NSS) models using PyTorch and Arm's Model Gym API.
   
minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying upscaling models like Neural Super Sampling (NSS) using PyTorch and Arm’s hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it’s applied to game performance
    - Learn how to fine-tune and evaluate a neural network for Neural Super Sampling (NSS)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Fine-tune an NSS model with quantization-aware training (QAT) and export it to .vgf
    - Inspect the graph of exported .vgf models using Model Explorer

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04 or later, with a CUDA-capable NVIDIA® GPU
    - CUDA Toolkit v13.1.1 or later

author: Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - PyTorch
    - Jupyter Notebook
    - Vulkan
    - NX
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Model Gym GitHub Repository
        link: https://github.com/arm/neural-graphics-model-gym
        type: code
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
    - resource:
        title: NSS Fine-Tuning Guide
        link: https://developer.arm.com/documentation/111141/latest
        type: documentation
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: NSS on HuggingFace
        link: https://huggingface.co/Arm/neural-super-sampling
        type: website
    - resource:
        title: Vulkan Samples Learning Path
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
