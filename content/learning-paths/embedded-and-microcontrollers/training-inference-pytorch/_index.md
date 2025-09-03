---
title: Edge AI with PyTorch & ExecuTorch - Tiny Sentiment Analysis on Arm

draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This topic is for machine learning engineers, embedded AI developers, and researchers interested in deploying TinyML models for NLP on Arm-based edge devices using PyTorch and ExecuTorch.

learning_objectives:
    - Train a custom CNN-based sentiment classification model implemented in PyTorch.
    - Optimize and convert the model using ExecuTorch for Arm-based edge devices.
    - Deploy and run inference on the Corstone-320 FVP.

prerequisites:
   - Basic knowledge of machine learning concepts.
   - It is advised to complete The Learning Path, [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm) before starting this learning path.
   - Familiarity with Python and PyTorch.
   - A Linux host machine or VM running Ubuntu 22.04 or higher.
   - An Arm license to run the examples on the Corstone-320 Fixed Virtual Platform (FVP), for hands-on deployment.


author: Dominica Abena O. Amanfo

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - tinyML
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
