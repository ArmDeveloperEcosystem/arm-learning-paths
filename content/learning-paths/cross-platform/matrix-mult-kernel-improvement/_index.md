---
title: GenAI LLM Matrix Multiplication acceleration on Linux
draft: true
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers deploying LLMs on a Linux machine who want to speed up their application.

learning_objectives: 
    - Understand the basic math operations that power Large Language Models.
    - Learn how the KleidiAI micro-kernels uniquely speed up Generative AI inference performance.
    - Run a basic C++ matrix multiplication example to showcase the speedup the KleidiAI micro-kernels deliver.
    
prerequisites:
    - A Linux machine; this example uses an AWS Graviton 3 instance.
    - A basic understanding of linear algibra termenology such as dot product and matrix multiplication.

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
