---
title: Deploy Phi-4-mini model with ONNX Runtime on Azure Cobalt 100

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, ML engineers, and cloud practitioners looking to deploy Microsoft's Phi Models on Arm-based servers using ONNX Runtime.

learning_objectives:
    - Quantize and run the Phi-4-mini model with ONNX Runtime on Azure.
    - Analyze performance on Arm Neoverse N2 based Azure Cobalt 100 VMs.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate cloud service provider. This Learning Path has been tested on an Azure Cobalt 100 virtual machine.
    - Basic understanding of Python and machine learning concepts.
    - Familiarity with ONNX Runtime and Azure cloud services.
    - Knowledge of Large Language Model (LLM) fundamentals.


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:42:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a9e547c4a9f99e1c7bfbfe582032ede11eb8ff5a74dbb7a93bada275ac435220
  summary_generated_at: '2026-06-02T04:40:35Z'
  summary_source_hash: a9e547c4a9f99e1c7bfbfe582032ede11eb8ff5a74dbb7a93bada275ac435220
  faq_generated_at: '2026-06-03T01:42:17Z'
  faq_source_hash: a9e547c4a9f99e1c7bfbfe582032ede11eb8ff5a74dbb7a93bada275ac435220
  summary: >-
    This advanced Learning Path guides you through quantizing and deploying Microsoft’s Phi-4-mini
    model with ONNX Runtime on Arm-based Azure Cobalt 100 virtual machines running Ubuntu 24.04
    LTS. You will build and configure ONNX Runtime, convert and quantize the model, and create
    a minimal Python chatbot server (phi4.py) using onnxruntime_genai. You will run prompts and
    analyze performance on Neoverse N2–based Cobalt 100 instances, observing metrics such as tokens
    per second and time to first token. Prerequisites include an Arm-based cloud instance (tested
    on an Azure Cobalt 100 VM), familiarity with Python, ONNX Runtime, Azure services, and LLM
    fundamentals. By the end, you can interactively serve Phi-4-mini inference on Azure Arm CPUs.
  faqs:
  - question: What kind of Azure instance should I use to follow this path?
    answer: >-
      Use an Arm-based instance. The steps were tested on an Azure Cobalt 100 Dpls_v6 VM with
      32 cores, 64GB of RAM, and 32GB of disk space.
  - question: Which operating system and environment are the instructions written for?
    answer: >-
      The procedures target Linux and were validated on Ubuntu 24.04 LTS running on Azure Cobalt
      100 servers.
  - question: Do I need to quantize the Phi-4-mini model before running inference?
    answer: >-
      Yes. The setup includes quantizing and converting Phi-4-mini before deploying it with ONNX
      Runtime.
  - question: How do I run the chatbot server and which arguments matter?
    answer: >-
      Create the provided phi4.py script and run it with a model path (args.model_path) to your
      converted Phi-4-mini model. You can also set an execution provider (args.execution_provider)
      and enable verbose or timing output if needed.
  - question: How do I know the deployment worked and what results should I expect?
    answer: >-
      After starting the server, send a text prompt and check the terminal for generated tokens
      and performance metrics. You should see tokens/second and time to first token; the example
      output shows about 57 tokens/s and ~0.2 s to first token.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
cloud_service_providers:
  - Microsoft Azure
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - ONNX Runtime


further_reading:
    - resource:
        title: ONNX Runtime Docs
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-Based Inference
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has a weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths use this wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

