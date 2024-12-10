---
title: Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers interested in running LLMs on Arm-based servers. 

learning_objectives:
    - Download and build llama.cpp on your Arm server.
    - Download a pre-quantized Llama 3.1 model from Hugging Face.
    - Run the pre-quantized model on your Arm CPU and measure the performance.

prerequisites:
    - An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

author_primary: Pareena Verma, Jason Andrews, and Zach Lasiuk

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - GenAI
    - Python


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
