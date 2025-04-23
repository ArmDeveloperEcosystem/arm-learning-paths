---
title: Quantize and Run a Large Language Model using vLLM on Arm Servers


minutes_to_complete: 45

who_is_this_for: This learning path is intended for software developers and AI engineers interested in optimizing and deploying large language models using vLLM on Arm-based servers. It’s ideal for those looking to explore CPU-based inference and model quantization techniques.

learning_objectives:
    - Build and configure OpenBLAS to optimize LLM performance.
    - Set up vLLM and PyTorch using builds optimized for Arm CPUs.
    - Download and quantize a large language model using INT8 techniques.
    - Launch a vLLM server to serve the quantized model.
    - Run single-prompt and batch inference using the vLLM OpenAI-compatible API.

    
prerequisites:
    - An Arm-based server or cloud instance running with at least 32 CPU cores, 64 GB RAM and 32 GB of available disk space.
    - Familiarity with Python and machine learning concepts.
    - An active Hugging Face account with access to the target model.

author: Rani Chowdary Mandepudi
	Phalani Paladugu

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - vLLM
    - LLM
    - GenAI
    - Python


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
