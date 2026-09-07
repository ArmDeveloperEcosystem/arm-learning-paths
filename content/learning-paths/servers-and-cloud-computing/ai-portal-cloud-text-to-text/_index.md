---
title: Run Optimized LLMs from the Arm AI Portal on Arm Neoverse Cloud Instances

description: Download and run an Arm-optimized LLM using the supplied ONNX Runtime GenAI workflow, or use a coding agent to adapt the application for a compatible alternative model runtime or format.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for developers and ML engineers running Arm-optimized LLMs on Arm Neoverse Linux machines. It provides a tested ONNX Runtime GenAI workflow and an optional coding-agent workflow for compatible text-to-text packages that use alternative runtimes or formats.

learning_objectives:
    - Prepare an Arm Neoverse Linux machine and download a model from the Arm AI Portal.
    - Generate text from the terminal and optionally serve the model through a local web application.
    - Explain how the shared application calls the supplied ONNX Runtime GenAI adapter.
    - Compare runtime and model-format choices, and optionally use a coding agent to replace the supplied adapter for another compatible text-to-text package.

prerequisites:
    - An Arm Neoverse Linux machine running Ubuntu 24.04 LTS, with Python 3.11 or later, for example an AWS m8g.xlarge instance
    - At least 16 GB of memory if you plan to use one of the 8B models
    - Basic familiarity with Linux command-line tools and Python
    - (Optional) Access to a coding agent if you want to generate an adapter for another runtime

author: Matt Cossins

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
cloud_service_providers:
  - AWS
  - Google Cloud
  - Microsoft Azure
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
    - Generative AI
    - LLM
    - Agent

further_reading:
    - resource:
        title: ONNX Runtime GenAI documentation
        link: https://onnxruntime.ai/docs/genai/
        type: documentation
    - resource:
        title: Arm models on Hugging Face
        link: https://huggingface.co/Arm/models
        type: website
    - resource:
        title: Download files from the Hugging Face Hub
        link: https://huggingface.co/docs/huggingface_hub/guides/download
        type: documentation
    - resource:
        title: ONNX Runtime execution providers
        link: https://onnxruntime.ai/docs/execution-providers/
        type: documentation
    - resource:
        title: KleidiAI project
        link: https://github.com/ARM-software/kleidiai
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
