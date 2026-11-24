---
title: Run an LLM chatbot with rtp-llm on Arm-based servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in running a Large Language Model (LLM) with rtp-llm on Arm-based servers. 

learning_objectives:
    - Build rtp-llm on an Arm-based server.
    - Download a Qwen model from Hugging Face.
    - Run a Large Language Model with rtp-llm.

prerequisites:
    - An Arm Neoverse N2-based or Arm Neoverse V2-based instance running Ubuntu 22.04 LTS from a cloud service provider, or an on-premise Arm server
    - At least four cores and 16GB of RAM for the server, with disk storage configured up to at least 32 GB

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:56:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ba5fd2e55679ffb0aaef44f0c32c8e47478610f5f6362925b43a671d33e1c791
  summary_generated_at: '2026-11-23T20:56:52Z'
  summary_source_hash: ba5fd2e55679ffb0aaef44f0c32c8e47478610f5f6362925b43a671d33e1c791
  faq_generated_at: '2026-11-23T20:56:52Z'
  faq_source_hash: ba5fd2e55679ffb0aaef44f0c32c8e47478610f5f6362925b43a671d33e1c791
  summary: You'll build and run an rtp-llm chatbot on an Arm-based server. First, you'll install build
    tools and prepare Python 3.10 with `micromamba`, then build the project with `bazelisk`. You'll then
    run a local inference test using Qwen2-0.5B-Instruct. Next, you'll download the model for the
    server and start it on port `8088`. Finally, you'll send requests to its OpenAI-compatible API with `curl`.
  faqs:
  - question: Which model should I use?
    answer: Download and use Qwen2-0.5B-Instruct from Hugging Face.
  - question: How do I select Python 3.10 for the build?
    answer: Install Python 3.10 in the `micromamba` root at `/opt/conda310`, then enter its shell before building rtp-llm.
  - question: How can I test the model before starting the server?
    answer: Run the local inference example with the downloaded Qwen2-0.5B-Instruct model and
      check that it generates a response to the sample prompt.
  - question: How do I check the server API?
    answer: Start the server, which listens on port `8088`. In another terminal, run the
      `curl-test.sh` request to `http://localhost:8088/v1/chat/completions` and inspect the JSON
      response.
  - question: Does the API request's `model` value select a different model?
    answer: No. The server loads only one model, so it does not use the request's `model` value.
      You can enter any value in that field for this example.
# END generated_summary_faq

author: Tianyu Li

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
    - Hugging Face

further_reading:
    - resource: 
        title: Qwen2-0.5B-Instruct
        link: https://huggingface.co/Qwen/Qwen2-0.5B-Instruct
        type: website
    - resource:
        title: Getting started with RTP-LLM
        link: https://github.com/alibaba/rtp-llm
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
        title: Get started with Arm-based cloud instances
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

