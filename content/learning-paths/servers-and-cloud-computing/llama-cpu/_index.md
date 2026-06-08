---
title: Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers
description: Serve the llama.cpp chatbot through an OpenAI-compatible API, enabling existing OpenAI-style clients and applications to run against a persistent Arm-hosted LLM.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers interested in running LLMs on Arm-based servers. 

learning_objectives:
    - Download and build llama.cpp on your Arm server.
    - Download a pre-quantized Llama 3.1 model from Hugging Face.
    - Run the pre-quantized model on your Arm CPU and measure the performance.

prerequisites:
    - An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:21:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d82aa4faeb599a3a1ac12d477204ebe0a4ddb99564bedced86ca0fc4851e17b9
  summary_generated_at: '2026-06-02T04:16:47Z'
  summary_source_hash: d82aa4faeb599a3a1ac12d477204ebe0a4ddb99564bedced86ca0fc4851e17b9
  faq_generated_at: '2026-06-03T01:21:51Z'
  faq_source_hash: d82aa4faeb599a3a1ac12d477204ebe0a4ddb99564bedced86ca0fc4851e17b9
  summary: >-
    Deploy a pre-quantized Llama‑3.1‑8B chatbot on an Arm server using llama.cpp with KleidiAI,
    and expose it through an OpenAI‑compatible API. You will download and build llama.cpp, fetch
    the pre‑quantized model from Hugging Face, run it on your Arm CPU, and measure performance.
    The path targets Ubuntu 24.04 LTS on Arm with a minimum of 4 CPU cores, 8 GB RAM, and 32 GB
    disk; it was tested on an AWS Graviton4 r8g.16xlarge instance but can run on other Arm‑based
    instances or on‑prem Arm servers. You will also install jq and start the llama.cpp server,
    which listens on port 8080 and can be accessed by OpenAI‑style clients over the network.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm server running Ubuntu 24.04 LTS with at least four cores, 8 GB RAM, and 32 GB
      of disk. The instructions were tested on an AWS Graviton4 r8g.16xlarge instance, but any
      Arm-based instance or on-prem Arm server meeting these resources is acceptable.
  - question: Which LLM model should I download for this setup?
    answer: >-
      Download a pre-quantized Llama 3.1 model from Hugging Face. The Learning Path guides you
      to use that model with llama.cpp on your Arm CPU.
  - question: How do I start and access the OpenAI-compatible server?
    answer: >-
      After building llama.cpp (via make in a prior step), start the server binary; it listens
      on port 8080. You can submit requests using an OpenAI-compatible API from the same machine
      or over the network.
  - question: Is any extra package required to interact with the API responses?
    answer: >-
      Yes. Install jq to work with JSON responses (for example, using sudo apt install jq -y on
      Ubuntu). This helps format and inspect the server’s OpenAI-compatible output.
  - question: Can I measure performance during inference, and how is it covered?
    answer: >-
      Yes. The Learning Path includes running the pre-quantized model on your Arm CPU and measuring
      performance as part of the procedure; it does not list additional tools beyond those in
      the steps.
# END generated_summary_faq

author:
    - Pareena Verma
    - Jason Andrews
    - Zach Lasiuk

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - Generative AI
    - Python
    - Demo
    - Hugging Face

further_reading:
    - resource:
        title: Getting started with Llama
        link: https://llama.meta.com/get-started
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
        title: Llama-2-7B-Chat-GGUF
        link: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

