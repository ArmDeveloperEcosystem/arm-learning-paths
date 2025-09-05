---
title: Fine-Tuning Neural Graphics Models with Model Gym

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers exploring neural graphics and interested in training and deploying upscaling models like Neural Super Sampling (NSS) using PyTorch and Arm’s hardware-aware backend.

learning_objectives:
    - Understand the principles of neural graphics and how it’s applied to game performance
    - Learn how to fine-tune and evaluate a neural network for Neural Super Sampling (NSS)
    - Use the Model Gym Python API and CLI to configure and train neural graphics models
    - Visualize and inspect models using the Model Explorer tool

prerequisites:
    - Basic understanding of PyTorch and machine learning concepts
    - A development machine running Ubuntu 22.04, with a CUDA-capable NVIDIA® GPU
    - CUDA Toolkit version 11.8 or later

author: Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML, Graphics, Upscaling, PyTorch
armips:
    - Mali
tools_software_languages:
    - PyTorch
    - Jupyter Notebook
    - Vulkan
operatingsystems:
    - Linux
further_reading:
    - resource:
        title: Model Gym GitHub Repository
        link: https://github.com/arm/neural-graphics-model-gym
        type: code
    - resource:
        title: How Arm Neural Super Sampling works
        link: https://community.arm.com/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-arm-neural-super-sampling-works
        type: blog
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: NSS Use Case Guide
        link: https://developer.arm.com/documentation/111009/latest/
        type: documentation


### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---