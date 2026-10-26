---
title: Run and benchmark vLLM mixture of experts models on Arm CPUs

description: Learn how to run and benchmark BF16 and INT8/W8A8 mixture of experts models with vLLM on Arm CPUs.
    
minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers interested in running and benchmarking mixture of experts (MoE) models with vLLM on Arm CPUs.

learning_objectives:
- Install and verify vLLM for CPU inference on an Arm server.
- Serve BF16 and INT8/W8A8 MoE models and validate a response.
- Benchmark MoE serving performance with vLLM bench serve.
- Compare BF16 and INT8/W8A8 MoE performance using relative speedups.

prerequisites:
- An Arm-based Linux server running Ubuntu 24.04 LTS, with enough CPU cores, memory, and disk space for large MoE models
- CPU support for BF16 and I8MM instructions
- Python 3.12 and basic familiarity with Hugging Face models and vLLM serving

author:
- Gauri Sahnan
- Fadi Arafeh

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
  title: Run vLLM inference with quantized models and benchmark on Arm servers
  link: /learning-paths/servers-and-cloud-computing/vllm-benchmark-quantisation/
  type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
