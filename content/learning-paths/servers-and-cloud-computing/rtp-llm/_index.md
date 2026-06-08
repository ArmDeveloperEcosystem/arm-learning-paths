---
title: Run an LLM chatbot with rtp-llm on Arm-based servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in running a Large Language Model (LLM) with rtp-llm on Arm-based servers. 

learning_objectives:
    - Build rtp-llm on an Arm-based server.
    - Download a Qwen model from Hugging Face.
    - Run a Large Language Model with rtp-llm.

prerequisites:
    - Any Arm Neoverse N2-based or Arm Neoverse V2-based instance running Ubuntu 22.04 LTS from a cloud service provider or an on-premise Arm server. 
    - For the server, at least four cores and 16GB of RAM, with disk storage configured up to at least 32 GB. 

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:02:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 27e17ea322cc7dc117f24d9d2007fbc0e6b498840b4097b859b1f376b8d8c9a6
  summary_generated_at: '2026-06-02T05:05:13Z'
  summary_source_hash: 27e17ea322cc7dc117f24d9d2007fbc0e6b498840b4097b859b1f376b8d8c9a6
  faq_generated_at: '2026-06-03T02:02:59Z'
  faq_source_hash: 27e17ea322cc7dc117f24d9d2007fbc0e6b498840b4097b859b1f376b8d8c9a6
  summary: >-
    This introductory Learning Path guides you through running a Large Language Model (LLM) chatbot
    on an Arm-based CPU using rtp-llm. You will build rtp-llm, set up Python 3.10 with micromamba,
    install Bazelisk and build tools, then download the Qwen2-0.5B-Instruct model from Hugging
    Face. You will start the rtp-llm server and send OpenAI-compatible API requests so applications
    can interact with the model locally or over the network. The target environment is an Arm
    Neoverse N2- or V2-based Ubuntu 22.04 LTS server with at least 4 CPU cores, 16 GB RAM, and
    32 GB storage. By the end, you will have a working LLM chatbot service running on an Arm server.
  faqs:
  - question: What hardware and OS do I need before running the steps?
    answer: >-
      Use an Arm Neoverse N2- or V2-based server running Ubuntu 22.04 LTS with at least four cores,
      16GB of RAM, and 32GB of disk. This can be a cloud instance or an on-premise Arm server.
  - question: Which Python version and location does the rtp-llm build expect?
    answer: >-
      The build expects Python 3.10 installed at /opt/conda310. The steps use micromamba to create
      this environment.
  - question: Which tools do I need to build rtp-llm?
    answer: >-
      Install bazelisk to build rtp-llm, and install git, gcc, g++, and build-essential. These
      packages are used to fetch sources and compile the project.
  - question: Which model will I run and how is it obtained?
    answer: >-
      You will run the Qwen2-0.5B-Instruct model. It is downloaded from Hugging Face in the steps.
  - question: How do I interact with the model after starting the server?
    answer: >-
      Use the rtp-llm server program and submit requests through its OpenAI-compatible API. Install
      jq to follow the API examples in the steps. The server can be accessed over the network
      from another machine.
# END generated_summary_faq

author: Tianyu Li

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

