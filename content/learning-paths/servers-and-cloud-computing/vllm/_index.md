---
title: Build and Run vLLM on Arm Servers
description: Build vLLM from source on an Arm Linux server, run batch inference with a Hugging Face model, and expose the model through an OpenAI-compatible API.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers and AI engineers interested in learning how to use the vLLM library on Arm servers.

learning_objectives:
    - Build vLLM from source on an Arm server.
    - Use a Qwen LLM from Hugging Face.
    - Run local batch inference using vLLM.
    - Create and interact with an OpenAI-compatible server provided by vLLM on your Arm server.

prerequisites:
    - An [Arm-based Linux instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or a local Arm Linux computer running Ubuntu 24.04 with at least 8 CPUs, 16 GB RAM, and 50 GB of disk storage.
    - A system that includes support for BFloat16.

author: Jason Andrews

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

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
    - vLLM
    - LLM
    - Generative AI
    - Python
    - Hugging Face

further_reading:
    - resource:
        title: vLLM Documentation
        link: https://docs.vllm.ai/
        type: documentation
    - resource:
        title: vLLM GitHub Repository
        link: https://github.com/vllm-project/vllm
        type: github
    - resource:
        title: Hugging Face Model Hub
        link: https://huggingface.co/models
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
