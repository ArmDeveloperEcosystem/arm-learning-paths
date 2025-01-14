---
title: Accelerate Generative AI workloads using KleidiAI 

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to learn how to use KleidiAI to accelerate the execution of Generative AI workloads on hardware.

learning_objectives: 
    - Describe how basic math operations power Large Language Models.
    - Describe how the KleidiAI micro-kernels speed up Generative AI inference performance.
    - Run a basic C++ matrix multiplication example to showcase the speedup that KleidiAI micro-kernels can deliver.
    
prerequisites:
    - An Arm-based Linux machine that implements the Int8 Matrix Multiplication (*i8mm*) architecture feature. The example in this Learning Path is run on an AWS Graviton 3 instance. Instructions on setting up an Arm-based server are [found here](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/aws/).
    - A basic understanding of linear algebra terminology, such as dot product and matrix multiplication.

author_primary: Zach Lasiuk
### Tags
skilllevels: Introductory 
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C++
    - GenAI
    - Coding
    - NEON
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
