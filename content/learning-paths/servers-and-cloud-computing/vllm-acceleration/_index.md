---
title: High throughput LLM serving using vLLM on Arm Servers

minutes_to_complete: 60

who_is_this_for: This learning path is for software developers and AI engineers who want to build an optimized vLLM for Arm servers, quantize models to INT4, and serve them through an OpenAI‑compatible API.

learning_objectives:
    - Build an optimized vLLM for aarch64 with oneDNN + Arm Compute Library.
    - Set up dependencies including PyTorch and llmcompressor dependencies.
    - Quantize an LLM (DeepSeek‑V2‑Lite) to 4‑bit weights.
    - Run and serve the quantized model using vLLM & test BF16 non‑quantized serving.
    - Use OpenAI‑compatible endpoints and understand sequence and batch limits.

prerequisites:
    - An Arm-based Linux server (Ubuntu 22.04+ recommended) with 32+ vCPUs, 64+ GB RAM, and 32+ GB free disk.
    - Python 3.12 and basic familiarity with Hugging Face Transformers and quantization.
    - Optional: a Hugging Face token to access gated models.

author:
   - Nikhil Gupta

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
    - Generative AI
    - Python
    - PyTorch
    - llmcompressor

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
    - resource:
        title: Build and Run vLLM on Arm Servers
        link: /learning-paths/servers-and-cloud-computing/vllm/
        type: website

### Notes
This path focuses on CPU inference on Arm servers using an optimized vLLM build with oneDNN and the Arm Compute Library (ACL), 4‑bit quantization accelerated by Arm KleidiAI microkernels, and OpenAI‑compatible serving. You can apply these steps to many LLMs; the examples use `deepseek-ai/DeepSeek-V2-Lite` for concreteness. As vLLM’s CPU support matures, manual builds will be replaced by a simple `pip install` flow.

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
