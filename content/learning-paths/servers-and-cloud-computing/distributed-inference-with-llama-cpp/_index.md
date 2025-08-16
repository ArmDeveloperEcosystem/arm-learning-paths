---
title: Distributed inference using llama.cpp

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers with some experience using llama.cpp who want to learn distributed inference.

learning_objectives: 
    - Set up a main host and worker nodes with llama.cpp
    - Run a large quantized model (for example, Llama 3.1 405B) with distributed CPU inference on Arm machines

prerequisites:
    - Three AWS c8g.16xlarge instances with at least 2 TB of EBS storage
    - Python 3 installed on each instance
    - Access to Meta's gated repository for the Llama 3.1 model family and a Hugging Face token to download models
    - Familiarity with [Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers](/learning-paths/servers-and-cloud-computing/llama-cpu)
    - Familiarity with AWS

author: Aryan Bhusari

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - LLM
    - GenAI
    - AWS
operatingsystems:
    - Linux



further_reading:
    - resource:
        title: llama.cpp RPC server code
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/rpc
        type: Code



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
