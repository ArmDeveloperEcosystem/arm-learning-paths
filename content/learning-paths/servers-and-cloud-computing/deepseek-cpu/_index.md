---
title: Deploy DeepSeek-R1 models on Arm servers

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers interested in running DeepSeek-R1 on Arm-based servers. 

learning_objectives:
    - Download and build llama.cpp on your Arm-based server.
    - Download a pre-quantized DeepSeek-R1 model from Hugging Face.
    - Run the pre-quantized model on your Arm CPU and measure the performance.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server. This Learning Path was tested on an AWS Graviton4 r8g.24xlarge instance.

author:
    - Tianyu Li

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


further_reading:
    - resource:
        title: Getting started with DeepSeek-R1
        link: https://huggingface.co/deepseek-ai/DeepSeek-R1
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-based inference 
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog
    - resource: 
        title: DeepSeek-R1-GGUF
        link: https://huggingface.co/bartowski/DeepSeek-R1-GGUF 
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
