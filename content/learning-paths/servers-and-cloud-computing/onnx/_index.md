---
title: Running Phi-3.5 Vision Model with ONNX Runtime on Cobalt 100

minutes_to_complete: 30

who_is_this_for:
    - Software developers, ML engineers, and cloud practitioners looking to deploy Microsoft Phi Models on Arm-based servers using ONNX Runtime.

learning_objectives:
    - Install ONNX Runtime, download and quantize the Phi-3.5 vision model.
    - Run the Phi-3.5 model with ONNX Runtime on Azure.
    - Analyze performance on Neoverse N2-based Cobalt 100 servers.

prerequisites:
    - Access to an Azure Cobalt 100 (or other Arm-based) compute instance with at least 16 cores, 8GB of RAM, and 32GB of disk space.
    - Basic understanding of Python and machine learning concepts.
    - Familiarity with ONNX Runtime and Azure cloud services.
    - Knowledge of LLM (Large Language Model) fundamentals.


author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: Machine Learning
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime
    - Microsoft Azure

further_reading:
    - resource:
        title: Getting Started with Llama
        link: https://llama.meta.com/get-started
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-Based Inference
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has a weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths use this wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---