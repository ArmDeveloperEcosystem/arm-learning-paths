---
title: Run a PyTorch LLM chatbot with KleidiAI on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in running large language models (LLMs) using PyTorch on Arm-based servers. 

learning_objectives:
    - Download the Meta Llama 3.1 model from the Meta Hugging Face repository.
    - 4-bit quantize the model using optimized INT4 KleidiAI Kernels for PyTorch.
    - Run an LLM inference using PyTorch on an Arm-based CPU.
    - Expose an LLM inference as a browser application with Streamlit as the frontend and Torchchat framework in PyTorch as the LLM backend server.
    - Measure performance metrics of the LLM inference running on an Arm-based CPU.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) with at least 16 CPUs from a cloud service provider, or an on-premise Arm server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T15:58:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: de0c91f69925ca664abbb3d7383c52a0196ecf72864260599ef6afbf4032319c
  summary_generated_at: '2026-11-19T15:58:37Z'
  summary_source_hash: de0c91f69925ca664abbb3d7383c52a0196ecf72864260599ef6afbf4032319c
  faq_generated_at: '2026-11-19T15:58:37Z'
  faq_source_hash: de0c91f69925ca664abbb3d7383c52a0196ecf72864260599ef6afbf4032319c
  summary: >-
    You'll run a PyTorch chatbot with KleidiAI INT4 kernels on an Arm server. First, you'll prepare
    a Python environment and download Meta Llama 3.1 from Hugging Face. You'll quantize the model
    to four bits and run CPU inference. Then, you'll start the Torchchat backend and Streamlit
    frontend, test a prompt in the browser, and capture basic inference performance
    measurements.
  faqs:
  - question: What Arm server do I need before starting?
    answer: >-
      Use an Arm server with Ubuntu 24.04 LTS, at least 16 cores, 64 GB of memory, and 50 GB
      of storage. You can use the tested AWS Graviton4 `r8g.4xlarge` setup as reference.
  - question: Which model do I download?
    answer: >-
      Download Meta Llama 3.1 from its Meta repository on Hugging Face. 
  - question: Which Python environment do I activate for the frontend?
    answer: >-
      Run `source torch_env/bin/activate` before you install the frontend dependencies.
  - question: How do I resolve the httpx proxies error?
    answer: >-
      Install `httpx==0.27.2`, then restart the
      frontend.
  - question: How do I check that the chatbot works end to end?
    answer: >-
      Start the Torchchat backend and Streamlit frontend. Open the web interface, enter a
      prompt, and check that you receive a model response.
# END generated_summary_faq

author:
    - Nikhil Gupta
    - Pareena Verma
    - Nobel Chowdary Mandepudi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: AI/ML
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - Generative AI
    - Python
    - PyTorch
    - Hugging Face

further_reading:
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: PyTorch Inference Performance Tuning on AWS Graviton Processors
        link: https://pytorch.org/tutorials/recipes/inference_tuning_on_aws_graviton.html
        type: documentation
    - resource:
        title: ML inference on Graviton CPUs with PyTorch
        link: https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md
        type: documentation
    - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

