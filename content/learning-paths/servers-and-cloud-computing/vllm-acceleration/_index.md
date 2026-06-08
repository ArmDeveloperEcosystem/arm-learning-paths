---
title: Run vLLM inference with INT4 quantization on Arm servers
    
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in building and optimizing vLLM for Arm-based servers. This Learning Path shows you how to quantize large language models (LLMs) to INT4, serve them using an OpenAI-compatible API, and benchmark model accuracy with the LM Evaluation Harness.

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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:16:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 487e9829c6e08798ad01be7a01f192e10e99cb06b71108575f1919c134eece02
  summary_generated_at: '2026-06-02T05:25:49Z'
  summary_source_hash: 487e9829c6e08798ad01be7a01f192e10e99cb06b71108575f1919c134eece02
  faq_generated_at: '2026-06-03T02:16:14Z'
  faq_source_hash: 487e9829c6e08798ad01be7a01f192e10e99cb06b71108575f1919c134eece02
  summary: >-
    This Learning Path shows how to build an aarch64-optimized vLLM with oneDNN and the Arm Compute
    Library on an Arm-based Linux server, set up runtime dependencies (including PyTorch and llmcompressor),
    quantize the DeepSeek‑V2‑Lite model to INT4, and serve both INT4 and BF16 variants through
    OpenAI‑compatible endpoints. You will configure key vLLM batching parameters (max_model_len
    and max_num_batched_tokens) and evaluate accuracy using the LM Evaluation Harness to compare
    BF16 and INT4 deployments. Prerequisites include an Arm-based Ubuntu 22.04+ server with at
    least 32 vCPUs, 64 GB RAM, 64 GB free disk space, and Python 3.12 with basic Hugging Face
    and quantization familiarity. Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm-based Linux server (Ubuntu 22.04+ recommended) with at least 32 vCPUs, 64 GB
      RAM, and 64 GB free disk space. Install Python 3.12 and be comfortable with Hugging Face
      Transformers and basic quantization concepts.
  - question: How do I build and verify vLLM is optimized for aarch64 with oneDNN and ACL?
    answer: >-
      Follow the build step to target aarch64 and include oneDNN and the Arm Compute Library.
      You validate the build by running inference as described in the path to confirm the binary
      loads and serves a model.
  - question: Which packages do I install to quantize the model, and why are they needed?
    answer: >-
      Install compressed-tensors and llmcompressor as shown in the quantization step. compressed-tensors
      provides tensor storage and compression utilities for quantized formats, and llmcompressor
      supplies quantization utilities compatible with Hugging Face Transformers and vLLM to quantize
      deepseek-ai/DeepSeek‑V2‑Lite to INT4.
  - question: How should I set vLLM batch sizing parameters when serving the model?
    answer: >-
      Use max_model_len to cap tokens per request and max_num_batched_tokens to bound total tokens
      across concurrent requests. These parameters determine memory usage and how effectively
      CPU threads are saturated; choose values based on expected prompt/generation lengths and
      concurrency on your server.
  - question: How do I evaluate accuracy for BF16 vs INT4 with LM Evaluation Harness?
    answer: >-
      Install the LM Evaluation Harness with vLLM support, then run benchmarks against your BF16
      and INT4 models served by vLLM. Compare the reported metrics across precisions; results
      vary based on your CPU, datasets, and runtime settings.
# END generated_summary_faq

author:
   - Nikhil Gupta

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

