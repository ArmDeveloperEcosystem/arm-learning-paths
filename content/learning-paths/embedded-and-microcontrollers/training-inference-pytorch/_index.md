---
title: Edge AI with PyTorch & ExecuTorch - Tiny Rock-Paper-Scissors on Arm

minutes_to_complete: 90

who_is_this_for: This learning path is for machine learning engineers, embedded AI developers, and researchers interested in deploying TinyML models on Arm-based edge devices. You will learn how to train and deploy a machine learning model for the classic game "Rock-Paper-Scissors" on edge devices. We'll use PyTorch and ExecuTorch, a framework designed for efficient on-device inference, to build and run a small-scale computer vision model.


learning_objectives: 
    - Train a small Convolutional Neural Network (CNN) for image classification using PyTorch.
    - Understand how to use synthetic data generation for training a model when real-world data is limited.
    - Optimize and convert a PyTorch model into an ExecuTorch program (.pte) for Arm-based devices.
    - Run the trained model on a local machine to play an interactive mini-game, demonstrating model inference.


prerequisites:
   - A basic understanding of machine learning concepts.
   - Familiarity with Python and the PyTorch library. 
   - It is advised to first complete [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) before starting this learning path. 
   - A Linux host machine or VM running Ubuntu 22.04 or higher.
   - An Arm license to run the examples on the Corstone-320 Fixed Virtual Platform (FVP), for hands-on deployment.  


author: Dominica Abena O. Amanfo

### Tags
skilllevels: Intermediate 
subjects: ML
armips:
    - Cortex-M
tools_software_languages:
    - tinyML 
    - Computer Vision
    - Edge AI Game
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
