---
title: Accelerate vllm inference on AWS Graviton processors
    
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in building and optimizing vLLM for Arm-based servers. This Learning Path shows you how to quantize large language models (LLMs) to INT4, serve them efficiently using an OpenAI-compatible API, and benchmark model accuracy with the LM Evaluation Harness.

learning_objectives:
    - Build an optimized vLLM for aarch64 with oneDNN and the Arm Compute Library (ACL)
    - Set up all runtime dependencies including PyTorch, llmcompressor, and Arm-optimized libraries
    - Quantize an LLM (DeepSeek‑V2‑Lite) to 4-bit integer (INT4) precision
    - Run and serve both quantized and BF16 (non-quantized) variants using vLLM
    - Use OpenAI‑compatible endpoints and understand sequence and batch limits
    - Evaluate accuracy using the LM Evaluation Harness on BF16 and INT4 models with vLLM

prerequisites:
    - An Arm-based Linux server (Ubuntu 22.04+ recommended) with a minimum of 32 vCPUs, 64 GB RAM, and 64 GB free disk space
    - Python 3.12 and basic familiarity with Hugging Face Transformers and quantization

author:
   - Nikhil Gupta

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers: AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - vLLM
    - LM Evaluation Harness
    - LLM
    - Generative AI
    - Python
    - PyTorch
    - Hugging Face
    
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
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
