---
title: Edge AI with PyTorch & ExecuTorch - Tiny Rock-Paper-Scissors on Arm

minutes_to_complete: 60

who_is_this_for: This learning path is for machine learning developers interested in deploying TinyML models on Arm-based edge devices. You will learn how to train and deploy a machine learning model for the classic game "Rock-Paper-Scissors" on edge devices. You'll use PyTorch and ExecuTorch, frameworks designed for efficient on-device inference, to build and run a small-scale computer vision model.


learning_objectives:
    - Train a small Convolutional Neural Network (CNN) for image classification using PyTorch.
    - Understand how to use synthetic data generation for training a model when real-world data is limited.
    - Optimize and convert a PyTorch model into an ExecuTorch program (.pte) for Arm-based devices.
    - Run the trained model on a local machine to play an interactive mini-game, demonstrating model inference.


prerequisites:
   - A basic understanding of machine learning concepts.
   - Familiarity with Python and the PyTorch library.
   - Having completed [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm).
   - An x86 Linux host machine or VM running Ubuntu 22.04 or higher.

author: Dominica Abena O. Amanfo

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - tinyML
    - Computer Vision
    - Edge AI
    - CNN
    - PyTorch
    - ExecuTorch

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Run Llama 3 on a Raspberry Pi 5 using ExecuTorch
        link: /learning-paths/embedded-and-microcontrollers/rpi-llama3
        type: website
    - resource:
        title: ExecuTorch Examples
        link: https://github.com/pytorch/executorch/blob/main/examples/README.md
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---