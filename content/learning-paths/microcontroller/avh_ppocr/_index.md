---
title: Deploy PaddlePaddle on Arm Cortex-M55 with Corstone-300 FVP

description: Learn how to deploy a PP-OCRv3 English text recognition model on Arm Cortex-M55 processor using the Corstone-300 FVP.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in using PaddlePaddle for Arm Cortex-M processors.

learning_objectives: 
    - Train an English text recognition model with PaddleOCR
    - Export Paddle inference model
    - Compile Paddle inference model with TVMC
    - Deploy on the Corstone-300 FVP with Arm Cortex-M55

prerequisites:
    - Some familiarity with embedded programming 
    - Some familiarity with AI/ML software development

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
    - GCC
    - TVM
    - PaddleOCR

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
