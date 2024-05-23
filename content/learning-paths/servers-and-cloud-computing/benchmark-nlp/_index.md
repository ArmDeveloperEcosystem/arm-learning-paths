---
title: Accelerate Natural Language Processing (NLP) models from Hugging Face on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run and accelerate the performance of Natural Language Processing (NLP) models on Arm-based servers. 

learning_objectives:
    - Deploy PyTorch NLP Sentiment Analysis models from Hugging Face on Arm servers. 
    - Evaluate the performance of three NLP models using the Sentiment Analysis pipeline.
    - Measure the performance uplift of these models by enabling support for BFloat16 fast math kernels on Arm Neoverse-based AWS Graviton3 Processors.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

author_primary: Pareena Verma

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse 
operatingsystems:
    - Linux 
tools_software_languages:
    - Python
    - PyTorch
    
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
