---
title: Build a RAG application using Zilliz Cloud on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to create a Retrieval-Augmented Generation (RAG) application on Arm servers.

description: Build a Retrieval-Augmented Generation (RAG) application on Arm servers using Zilliz Cloud for vector search and llama.cpp for LLM inference.

learning_objectives: 
    - Create a simple RAG application using Zilliz Cloud
    - Launch an LLM service on Arm servers

prerequisites:
    - A basic understanding of a RAG pipeline.
    - An AWS Graviton3 C7g.2xlarge instance, or any [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.
    - A [Zilliz account](https://zilliz.com/cloud?utm_source=partner&utm_medium=referral&utm_campaign=2024-10-24_web_arm-dev-hub-data-loading_arm), which you can sign up for with a free trial.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:50:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2969ffbecd9365d45d5d154d6892a7030b142c70e8143e73d18ff09e88811d45
  summary_generated_at: '2026-09-28T19:50:15Z'
  summary_source_hash: 2969ffbecd9365d45d5d154d6892a7030b142c70e8143e73d18ff09e88811d45
  faq_generated_at: '2026-09-28T19:50:15Z'
  faq_source_hash: 2969ffbecd9365d45d5d154d6892a7030b142c70e8143e73d18ff09e88811d45
  summary: >-
    Build a retrieval-augmented generation (RAG) workflow on Arm with Zilliz Cloud and llama.cpp.
    You create a dedicated Zilliz Cloud cluster on Arm-based machines, then build a local llama.cpp
    server with an OpenAI-compatible API. You use Python to create and inspect an embedding, connect
    to the local model endpoint, and issue test requests. Finally, you validate vector search in
    Zilliz Cloud and local model inference on your Arm server.
  faqs:
  - question: Which Zilliz Cloud cluster should I create?
    answer: >-
      Create a **Dedicated** cluster on AWS using Arm-based machines. You can also use self-hosted
      Milvus, although its setup is more involved.
  - question: How do I know my Zilliz Cloud cluster is ready before I continue?
    answer: >-
      After you select **Create Cluster**, check that the cluster appears in your **Default Project**
      with a running status. Continue after it reports that it’s running.
  - question: Do I need an API key to call the LLM service from my script?
    answer: >-
      No. You run the llama.cpp server locally, so the OpenAI SDK can connect without a real API
      key. The example passes `no-key` as the client value.
  - question: How do I confirm the embedding model is working correctly?
    answer: >-
      Run the provided test code and confirm that it prints an embedding dimension and several
      floating-point values. The example reports a dimension of `384`.
  - question: What do I need before I use the Llama 3.1 model with llama.cpp?
    answer: >-
      Request access to Llama 3.1 through the Llama website. After you receive access, follow the
      instructions to host the model with llama.cpp on your Arm-based server.
# END generated_summary_faq

author: Chen Zhang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - Python
    - Generative AI
    - RAG
    - Hugging Face

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Zilliz Documentation
        link: https://zilliz.com/cloud
        type: documentation
    - resource:
        title: Milvus Documentation
        link: https://milvus.io/
        type: documentation
    - resource:
        title: llama.cpp repository
        link: https://github.com/ggerganov/llama.cpp
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
