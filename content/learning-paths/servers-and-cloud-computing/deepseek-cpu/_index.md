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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:39:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  summary_generated_at: '2026-06-02T03:31:44Z'
  summary_source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  faq_generated_at: '2026-06-03T00:39:18Z'
  faq_source_hash: f600fcba0adea12ff1b8b092e75de553577d940dc3bf632e9a247cec22d364a4
  summary: >-
    This Learning Path shows how to deploy and run the DeepSeek-R1 671B language model on Arm-based
    servers using llama.cpp with quantization for CPU inference. You will clone and build llama.cpp,
    download a pre-quantized DeepSeek-R1 model from Hugging Face, start the llama.cpp server,
    and access it via an OpenAI-compatible API. The instructions target Ubuntu 24.04 LTS on an
    Arm server with at least 64 cores, 512 GB RAM, and 400 GB of disk space; they were tested
    on an AWS Graviton4 r8g.24xlarge instance. By the end, you will have a running chatbot on
    your Arm CPU and benchmark its performance. Prerequisite: an Arm-based instance from a cloud
    provider or an on-prem Arm server.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm-based server running Ubuntu 24.04 LTS with at least 64 CPU cores, 512 GB RAM,
      and 400 GB of disk space. An Arm-based instance from a cloud provider or an on-prem Arm
      server is suitable; the instructions were tested on an AWS Graviton4 r8g.24xlarge instance.
  - question: Where do I get the DeepSeek-R1 model and what format is expected?
    answer: >-
      Download a pre-quantized DeepSeek-R1 model from Hugging Face as directed in the Learning
      Path. The steps assume a pre-quantized artifact appropriate for llama.cpp.
  - question: How do I start and access the model server during this Learning Path?
    answer: >-
      After building llama.cpp, start its server mode as shown in the steps. The server provides
      an OpenAI-compatible API and can be accessed locally or over the network from another machine.
  - question: Do I need any extra tools to query or work with the API responses?
    answer: >-
      Yes. The steps require jq for this section; install it with: sudo apt install jq -y.
  - question: What should I check if the llama.cpp server binary is missing?
    answer: >-
      The server executable is built when you run make in the previous section. Ensure you completed
      the llama.cpp build step before attempting to start the server.
# END generated_summary_faq

author:
    - Tianyu Li

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

