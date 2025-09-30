---
title: "Edge AI on Arm: PyTorch and ExecuTorch Rock Paper Scissors"

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for machine learning developers who want to deploy TinyML models on Arm-based edge devices using PyTorch and ExecuTorch.

learning_objectives:
  - Train a small Convolutional Neural Network (CNN) for image classification using PyTorch
  - Use synthetic data generation for training a model when real data is limited
  - Convert and optimize a PyTorch model to an ExecuTorch program (`.pte`) for Arm-based devices
  - Run the trained model locally as an interactive mini-game to demonstrate inference

prerequisites:
  - Basic understanding of machine learning concepts
  - Familiarity with Python and the PyTorch library
  - Completion of the Learning Path [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/)
  - An x86 Linux host machine or VM running Ubuntu 22.04 or later

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
      title: ExecuTorch examples
      link: https://github.com/pytorch/executorch/blob/main/examples/README.md
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
