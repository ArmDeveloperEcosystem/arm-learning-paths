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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:25:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e881f6b35dd5bbe42675d28c6139a8482c0da74862eac9b8d5e787ecdeb18571
  summary_generated_at: '2026-09-15T21:25:36Z'
  summary_source_hash: e881f6b35dd5bbe42675d28c6139a8482c0da74862eac9b8d5e787ecdeb18571
  faq_generated_at: '2026-09-15T21:25:36Z'
  faq_source_hash: e881f6b35dd5bbe42675d28c6139a8482c0da74862eac9b8d5e787ecdeb18571
  summary: >-
    You'll deploy a persistent LLM chatbot on an Arm server with `llama.cpp` and a pre-quantized
    Llama 3.1 8B model from Hugging Face. First, you'll build `llama.cpp`, obtain the model, launch its
    OpenAI-compatible server, and expose it on port `8080`. You'll then access the chatbot using the OpenAI-compatible API.
  faqs:
  - question: What result should I expect when I start the llama.cpp server?
    answer: >-
      The server starts and listens on port `8080`. After the server starts running, you can send OpenAI-compatible
      requests without restarting the process between calls.
  - question: Do I need any extra tools to view API responses?
    answer: >-
      Yes. Install `jq` with `sudo apt install jq -y`. You'll use `jq` to process JSON
      returned by the API.
  - question: Can I access the chatbot from another machine?
    answer: >-
      Yes. The server exposes an OpenAI-compatible API over the network, so a remote client can
      call the host running the LLM if it can reach port `8080`.
  - question: Which model should I download before launching the server?
    answer: >-
      Use a pre-quantized Llama 3.1 8B model from Hugging Face. Download
      the model to the Arm server before starting the server.
  - question: How do I send a request to the running llama.cpp server?
    answer: >-
      Send a `curl` request to `http://localhost:8080/v1/chat/completions` with a JSON prompt, then
      pipe the response to `jq -C`. Save the request in `curl-test.sh` and run it with `bash ./curl-test.sh`.
# END generated_summary_faq

author:
    - Pareena Verma
    - Jason Andrews
    - Zach Lasiuk

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS Graviton
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
