---
title: Fine tune LLM CPU inference performance with multithreading

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic ML engineers optimizing LLM inference performance on Arm CPUs.

learning_objectives: 
    - Understand how PyTorch uses multiple threads for CPU inference
    - Measure performance impact of thread count on LLM inference
    - Tune thread count to optimize inference for specific models and systems

prerequisites:
    - An [Arm-based cloud instance](/learning-paths/servers-and-cloud-computing/csp/) or an Arm server with at least 16 cores
    - Basic understanding of Python and PyTorch
    - Ability to install Docker on your Arm system

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - Python
    - PyTorch
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: PyTorch CPU Threading Documentation
        link: https://docs.pytorch.org/docs/stable/notes/cpu_threading_torchscript_inference.html
        type: documentation
    - resource:
        title: Arm Tool Solutions Repository
        link: https://github.com/ARM-software/Tool-Solutions/tree/main/ML-Frameworks/pytorch-aarch64
        type: website
    - resource:
        title: Docker install guide
        link: /install-guides/docker/
        type: install-guide


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
