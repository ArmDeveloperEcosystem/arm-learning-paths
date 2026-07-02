---
title: Deploy an AI Agent on Arm with llama.cpp and llama-cpp-agent using KleidiAI
description: Learn how to build and deploy an AI agent application on Arm servers using llama.cpp and llama-cpp-agent with KleidiAI optimization for efficient LLM inference and function calling.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers and ML engineers looking to deploy an optimized AI agent application.

learning_objectives:
    - Set up llama-cpp-python optimized for Arm servers.
    - Run optimized Large Language Models (LLMs).
    - Create custom functions for LLMs.
    - Deploy optimized AI agents for applications.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.
    - Basic understanding of Python and prompt engineering.
    - Understanding of LLM fundamentals.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:17:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 275878b5aa4c27dee394da12ad8b80e4c0d0235b3ddce66b1fe3f0e056ef3da9
  summary_generated_at: '2026-06-26T17:17:51Z'
  summary_source_hash: 275878b5aa4c27dee394da12ad8b80e4c0d0235b3ddce66b1fe3f0e056ef3da9
  faq_generated_at: '2026-06-26T17:17:51Z'
  faq_source_hash: 275878b5aa4c27dee394da12ad8b80e4c0d0235b3ddce66b1fe3f0e056ef3da9
  summary: >-
    You'll build and run a function-calling AI agent on Arm servers using
    `llama.cpp` and the `llama-cpp-agent` framework with KleidiAI optimizations. After preparing
    an Arm-based Ubuntu environment and obtaining a quantized Llama 3.1 8B model, you'll create
    `agent.py` to connect the model to tool functions and structured outputs. You'll learn how the
    agent selects functions based on input intent, then test the end-to-end workflow to observe
    tool invocation and responses. By the end, you'll run an AI agent backed by an optimized
    LLM, verify that the model loads, and inspect outputs that demonstrate function selection
    and result handling.
  faqs:
  - question: Which operating system and instance setup do the steps target?
    answer: >-
      The steps are designed for Arm servers running Ubuntu 22.04 LTS. They were tested on an
      Amazon EC2 `m7g.xlarge` instance powered by Graviton3, and expect at least four cores, 16 GB of memory, and
      32 GB of disk.
  - question: What should be ready before running the `agent.py` script?
    answer: >-
      Build `llama.cpp` and download the quantized Llama 3.1 8B model. Ensure the Python dependencies,
      including `llama-cpp-agent` and `llama-cpp-python`, are installed in the active environment.
  - question: Where should the model file be placed for the script to find it?
    answer: >-
      Place the downloaded model at the path referenced by `model_path` in `agent.py`. Keep the directory
      structure consistent with the code so the model loads without modification.
  - question: How do I know the agent used a function call rather than replying directly?
    answer: >-
      Check the script’s output for a selected tool/function name and its arguments, followed
      by the function’s return data. If the agent replies directly, you will see a model-generated
      response without a function invocation.
  - question: How are functions exposed to the LLM in this application?
    answer: >-
      Functions are declared in `agent.py` and registered through `llama-cpp-agent`. The LLM analyzes
      the input and selects among the predefined functions based on intent and context.
# END generated_summary_faq

author: Andrew Choi

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
tools_software_languages:
    - Python
    - AWS Graviton
    - AI
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: llama.cpp
        link: https://github.com/ggml-org/llama.cpp
        type: documentation
    - resource:
        title: llama-cpp-agent
        link: https://llama-cpp-agent.readthedocs.io/en/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
