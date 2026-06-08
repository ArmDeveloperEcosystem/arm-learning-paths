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
    - An AWS Graviton3 C7g.2xlarge instance, or any [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp) from a cloud service provider or an on-premise Arm server.
    - A [Zilliz account](https://zilliz.com/cloud?utm_source=partner&utm_medium=referral&utm_campaign=2024-10-24_web_arm-dev-hub-data-loading_arm), which you can sign up for with a free trial.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:30:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2eb252b19b7535fbb776a3153bfc9f70b6217088e5b4b55deb56d01393abaf3b
  summary_generated_at: '2026-06-02T04:25:25Z'
  summary_source_hash: 2eb252b19b7535fbb776a3153bfc9f70b6217088e5b4b55deb56d01393abaf3b
  faq_generated_at: '2026-06-03T01:30:54Z'
  faq_source_hash: 2eb252b19b7535fbb776a3153bfc9f70b6217088e5b4b55deb56d01393abaf3b
  summary: >-
    Build a Retrieval-Augmented Generation application on Arm-based servers using Zilliz Cloud
    for vector search and llama.cpp for LLM inference. You will create a Dedicated Zilliz Cloud
    cluster on AWS using Arm-based machines, then build and run a local llama.cpp server that
    exposes an OpenAI-compatible API with the Llama‑3.1‑8B model. In Python, prepare embeddings
    and call the local LLM to perform an online RAG query, validating by printing the embedding
    dimension and sample values. Prerequisites: basic RAG knowledge, access to an Arm-based instance
    (for example, an AWS Graviton3 C7g.2xlarge or other Arm server), a Zilliz account, and Linux.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a basic understanding of a RAG pipeline, access to an Arm-based server (for example,
      an AWS Graviton3 C7g.2xlarge or any Arm-based instance from a cloud provider or on-prem),
      and a Zilliz Cloud account. The environment is Linux.
  - question: Which Zilliz Cloud cluster should I create for this path?
    answer: >-
      Create a Dedicated cluster deployed in AWS using Arm-based machines. You can alternatively
      use self-hosted Milvus, but this is more complicated to set up.
  - question: Do I need to request access to the Llama 3.1 model before launching llama.cpp?
    answer: >-
      Yes. Before using the Llama 3.1-8B model, visit the Llama website and fill in the form to
      request access.
  - question: Do I need an OpenAI API key when using the OpenAI SDK with the local llama.cpp server?
    answer: >-
      No. Because the LLM service is running locally via llama.cpp, you do not need to provide
      an API key.
  - question: What output should I see when I test the embedding model in the Python script?
    answer: >-
      The script prints the embedding dimension and the first few elements. The example output
      shows 384 followed by several floating-point values.
# END generated_summary_faq

author: Chen Zhang

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

