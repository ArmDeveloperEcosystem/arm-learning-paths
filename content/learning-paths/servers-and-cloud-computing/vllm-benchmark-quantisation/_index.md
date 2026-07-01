---
title: Run vLLM inference with quantized models and benchmark on Arm servers

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in running inference on quantized models. In this Learning Path, you'll learn how to run inference on Llama 3.1-8B and Whisper with and without quantization. You'll then benchmark Llama performance and accuracy with vLLM's bench CLI and the LM Evaluation Harness.

learning_objectives: 
    - Install a recent release of vLLM
    - Run both quantized and non-quantized variants of Llama3.1-8B and Whisper using vLLM
    - Evaluate and compare model performance and accuracy using vLLM's bench CLI and the LM Evaluation Harness

prerequisites:
    - An Arm-based Linux server (Ubuntu 22.04+ recommended) with a minimum of 32 vCPUs, 96 GB RAM, and 64 GB free disk space
    - Python 3.12 and basic familiarity with Hugging Face Transformers and quantization schemes

description: Learn how to run Llama 3.1 8B and Whisper inference with BF16 and W8A8 quantized models on Arm servers, then compare throughput and accuracy with vLLM benchmark tools.

author:
  - Anna Mayne
  - Nikhil Gupta
  - Marek Michałowski

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - vLLM
    - Python
    - PyTorch
    - Hugging Face
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: vLLM Documentation
        link: https://docs.vllm.ai/
        type: documentation
    - resource:
        title: vLLM GitHub Repository
        link: https://github.com/vllm-project/vllm
        type: website
    - resource:
        title: Hugging Face Model Hub
        link: https://huggingface.co/models
        type: website
    - resource:
        title: Build and Run vLLM on Arm Servers
        link: /learning-paths/servers-and-cloud-computing/vllm/
        type: website
    - resource:
        title: LM Evaluation Harness (GitHub)
        link: https://github.com/EleutherAI/lm-evaluation-harness
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
