---
title: Run an LLM chatbot with rtp-llm on Arm-based servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in running a Large Language Model (LLM) with rtp-llm on Arm-based servers. 

learning_objectives:
    - Build rtp-llm on an Arm-based server.
    - Download a Qwen model from Hugging Face.
    - Run a Large Language Model with rtp-llm.

prerequisites:
    - Any Arm Neoverse N2-based or Arm Neoverse V2-based instance running Ubuntu 22.04 LTS from a cloud service provider or an on-premise Arm server. 
    - For the server, at least four cores and 16GB of RAM, with disk storage configured up to at least 32 GB. 

author: Tianyu Li

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - Generative AI
    - Python
    - Hugging Face

further_reading:
    - resource: 
        title: Qwen2-0.5B-Instruct
        link: https://huggingface.co/Qwen/Qwen2-0.5B-Instruct
        type: website
    - resource:
        title: Getting started with RTP-LLM
        link: https://github.com/alibaba/rtp-llm
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
        title: Get started with Arm-based cloud instances
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: website
     



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
