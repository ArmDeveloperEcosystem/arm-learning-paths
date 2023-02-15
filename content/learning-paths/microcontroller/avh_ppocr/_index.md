---
title: Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware

description: Learn how to deploy a PP-OCRv3 English text recognition model on Arm Cortex-M55 processor with Arm Virtual Hardware.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in using PaddlePaddle for Arm Cortex-M processors.

learning_objectives: 
    - Train an English text recognition model with PaddleOCR
    - Export Paddle inference model
    - Compile Paddle inference model with TVMC
    - Deploy on the AVH Corstone-300 platform with Arm Cortex-M55

prerequisites:
    - Some familiarity with embedded programing is assumed
    - Some familiarity with AI/ML software development is assumed
    - An AWS account to subscribe [Arm Virtual Hardware](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g) Amazon Machine Image(AMI). Refer to [this guide](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) to create an AWS account.

author_primary: Liliya Yu

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - C
    - Python
    - AWS EC2
    - GCC
    - TVM
    - PaddleOCR

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
