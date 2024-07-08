---
title: KleidiAI basics - Improving AI/ML workloads from servers to phones

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for people wanting to learn how Generative AI workloads execute on hardware, and how KleidiAI accelerates it.

learning_objectives: 
    - Understand how basic math operations power Large Language Models.
    - Learn how the KleidiAI micro-kernels speed up Generative AI inference performance.
    - Run a basic C++ matrix multiplication example to showcase the speedup the KleidiAI micro-kernels deliver.
    
prerequisites:
    - An Arm Linux machine that implements the Int8 Matrix Multiplication (*i8mm*) architecture feature; this example uses an AWS Graviton 3 instance. Instructions on setting up an Arm-based server are [found here](https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/aws/).
    - A basic understanding of linear algebra terminology such as dot product and matrix multiplication.

author_primary: Zach Lasiuk
### Tags
skilllevels: Introductory 
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
tools_software_languages:
    - C++
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - smartphones-and-mobile



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
