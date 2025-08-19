---
title: Distributed inference using llama.cpp

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This learning path is for developers with some experience using llama.cpp who want to learn about distributed inference.

learning_objectives: 
    - Set up the main host and worker nodes using llama.cpp
    - Run a large quantized model (e.g., Llama 3.1 70B) on CPUs in a distributed manner on Arm machines

prerequisites:
    - Three AWS c8g.4xlarge instances with at least 500GB EBS space.
    - Python installed on the AWS instances.
    - Access to Meta’s gated repository for the Llama 3.1 model family, with a Hugging Face token generated for downloading the models.
    - Familiarity with -> [Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers](/learning-paths/servers-and-cloud-computing/llama-cpu)
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
        title: Llama.cpp rpc-server code
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/rpc
        type: Code



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
