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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: 487e9829c6e08798ad01be7a01f192e10e99cb06b71108575f1919c134eece02
  summary: >-
    Run vLLM inference with INT4 quantization on Arm servers walks you through an end-to-end Arm
    software workflow. It is designed for developers interested in building and optimizing vLLM
    for Arm-based servers. This Learning Path shows you how to quantize large language models
    (LLMs) to INT4, serve them using an OpenAI-compatible API, and benchmark model accuracy with
    the LM Evaluation Harness. By the end, you will be able to build an optimized vLLM for aarch64
    with oneDNN and the Arm Compute Library (ACL), set up all runtime dependencies including PyTorch,
    llmcompressor, and Arm-optimized libraries, and quantize an LLM (DeepSeek‑V2‑Lite) to 4-bit
    integer (INT4) precision. It focuses on tools and technologies such as vLLM, LM Evaluation
    Harness, LLM, Generative AI, and Python, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps
    cover Build and validate vLLM for inference, Quantize an LLM to INT4, Serve high throughput
    inference with vLLM, and Evaluate accuracy with LM Evaluation Harness.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build an optimized vLLM for aarch64 with oneDNN and the Arm Compute Library (ACL),
      set up all runtime dependencies including PyTorch, llmcompressor, and Arm-optimized libraries,
      and quantize an LLM (DeepSeek‑V2‑Lite) to 4-bit integer (INT4) precision.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers interested in building and optimizing vLLM
      for Arm-based servers. This Learning Path shows you how to quantize large language models
      (LLMs) to INT4, serve them using an OpenAI-compatible API, and benchmark model accuracy
      with the LM Evaluation Harness.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based Linux server (Ubuntu 22.04+
      recommended) with a minimum of 32 vCPUs, 64 GB RAM, and 64 GB free disk space; Python 3.12
      and basic familiarity with Hugging Face Transformers and quantization.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including vLLM, LM Evaluation Harness, LLM, Generative AI,
      and Python, Linux environments, Arm platforms such as Neoverse, and cloud platforms such
      as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and validate vLLM for inference, Quantize an
      LLM to INT4, Serve high throughput inference with vLLM, and Evaluate accuracy with LM Evaluation
      Harness.
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

