---
title: Deploy Phi-3.5 Vision with ONNX Runtime on Azure Cobalt 100 on Arm



draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, ML engineers, and cloud practitioners looking to deploy Microsoft's Phi Models on Arm-based servers using ONNX Runtime.

learning_objectives:
    - Quantize and run the Phi-3.5 vision model with ONNX Runtime on Azure.
    - Analyze performance on Arm Neoverse-N2 based Azure Cobalt 100 VMs.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate cloud service provider. This Learning Path has been tested on a Microsoft Azure Cobalt 100 virtual machine with 32 cores, 8GB of RAM, and 32GB of disk space.
    - Basic understanding of Python and machine learning concepts.
    - Familiarity with ONNX Runtime and Azure cloud services.
    - Knowledge of Large Language Model (LLM) fundamentals.


author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
cloud_service_providers: Microsoft Azure
armips:
    - Neoverse
subjects: ML
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime
   

further_reading:
    - resource:
        title: ONNX Runtime Docs
        link: https://onnxruntime.ai/docs/
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
