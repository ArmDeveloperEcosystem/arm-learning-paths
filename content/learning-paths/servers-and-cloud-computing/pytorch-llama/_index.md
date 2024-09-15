---
title: Run a Large Language Model (LLM) chatbot with PyTorch using KleidiAI on Arm servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in running LLMs using PyTorch on Arm-based servers. 

learning_objectives:
    - Download the Meta Llama 3.1 model from the Meta Hugging Face repository.
    - 4-bit quantize the model using optimized INT4 KleidiAI Kernels for PyTorch.
    - Run an LLM inference using PyTorch on an Arm-based CPU.
    - Expose an LLM inference as a browser application with Streamlit as the frontend and Torchchat framework in PyTorch as the LLM backend server.
    - Measure performance metrics of the LLM inference running on an Arm-based CPU.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) with at least 16 CPUs from a cloud service provider or an on-premise Arm server.

author_primary: Nikhil Gupta, Pareena Verma, Nobel Chowdary Mandepudi, Ravi Malhotra

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
    - PyTorch


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
