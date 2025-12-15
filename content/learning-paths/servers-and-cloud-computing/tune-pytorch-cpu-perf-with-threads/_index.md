---
title: Fine Tune LLM performance on CPU with multithreading

minutes_to_complete: 20

who_is_this_for: ML Engineers looking to fine tune the inference performance of LLMs running on CPU 

learning_objectives: 
    - Understand how PyTorch uses multiple threads for CPU inference and the various tradeoffs involved
    - Tune the thread count to improve performance for specific models and systems

prerequisites:
    - Intermediate understanding of Python and PyTorch
    - Access to an Arm-based system

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - Python
    - PyTorch
    - Bash
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Arm Tool Solutions
        link: https://github.com/ARM-software/Tool-Solutions/tree/main
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
