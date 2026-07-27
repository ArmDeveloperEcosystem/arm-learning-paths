---
title: Deploy DeepSeek-R1 on Arm Servers with llama.cpp
description: Learn how to deploy and run the DeepSeek-R1 language model on Arm servers using llama.cpp with quantization for efficient CPU inference.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to run DeepSeek-R1 on Arm-based servers. 

learning_objectives:
    - Clone and build llama.cpp on your Arm-based server.
    - Download a pre-quantized DeepSeek-R1 model from Hugging Face.
    - Run the model on your Arm CPU and benchmark its performance.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud provider or an on-premise Arm server. This Learning Path was tested on an AWS Graviton4 r8g.24xlarge instance.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:48:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  summary_generated_at: '2026-07-27T18:48:20Z'
  summary_source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  faq_generated_at: '2026-07-27T18:48:20Z'
  faq_source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  summary: >-
    You'll build `llama.cpp` on an Arm-based Ubuntu server, download a pre-quantized DeepSeek-R1 model
    from Hugging Face, and run it for CPU inference. You'll launch a persistent `llama.cpp` server with
    an OpenAI-compatible API, deploy a chatbot with the DeepSeek-R1 671B LLM, and send requests from
    the same or another machine. You'll then confirm the setup with API responses and basic benchmarks.
  faqs:
  - question: What do I need before running the 671B model?
    answer: >-
      Use an Arm server running Ubuntu 24.04 LTS with at least 64 cores, 512 GB of RAM, and 400
      GB of disk space. The Learning Path was tested on an AWS Graviton4 `r8g.24xlarge` instance.
  - question: Which DeepSeek-R1 model should I download?
    answer: >-
      Download a pre-quantized DeepSeek-R1 model from Hugging Face.
      Quantization enables efficient CPU inference with `llama.cpp`.
  - question: How do I know the llama.cpp server binary is available?
    answer: >-
      Running `make` during the build step creates the server executable. If it's missing,
      repeat the build step before starting the server.
  - question: How do I access the model repeatedly without restarting it?
    answer: >-
      Start the `llama.cpp` server and use its OpenAI-compatible API to submit multiple requests.
      You can also send requests from another machine to the host running the server.
  - question: Why do I install jq?
    answer: >-
      The examples use `jq` to work with JSON. It helps format and parse responses returned
      by the OpenAI-compatible API calls.
# END generated_summary_faq

author:
    - Tianyu Li

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
    - LLM
    - Generative AI
    - Python

further_reading:
    - resource:
        title: Getting started with DeepSeek-R1
        link: https://huggingface.co/deepseek-ai/DeepSeek-R1
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-based inference 
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog
    - resource: 
        title: DeepSeek-R1-GGUF
        link: https://huggingface.co/bartowski/DeepSeek-R1-GGUF 
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
