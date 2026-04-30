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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: d82aa4faeb599a3a1ac12d477204ebe0a4ddb99564bedced86ca0fc4851e17b9
  summary: >-
    Serve the llama.cpp chatbot through an OpenAI-compatible API, enabling existing OpenAI-style
    clients and applications to run against a persistent Arm-hosted LLM. It is designed for developers
    interested in running LLMs on Arm-based servers. By the end, you will be able to download
    and build llama.cpp on your Arm server, download a pre-quantized Llama 3.1 model from Hugging
    Face, and run the pre-quantized model on your Arm CPU and measure the performance. It focuses
    on tools and technologies such as LLM, Generative AI, Python, Demo, and Hugging Face, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as AWS. The main
    steps cover Run a Large Language model (LLM) chatbot on Arm servers and Access the chatbot
    using the OpenAI-compatible API.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will download and build llama.cpp on your Arm server, download a pre-quantized Llama
      3.1 model from Hugging Face, and run the pre-quantized model on your Arm CPU and measure
      the performance. Serve the llama.cpp chatbot through an OpenAI-compatible API, enabling
      existing OpenAI-style clients and applications to run against a persistent Arm-hosted LLM.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers interested in running LLMs on Arm-based servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AWS Graviton4 r8g.16xlarge instance
      to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/)
      from a cloud service provider or an on-premise Arm server.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including LLM, Generative AI, Python, Demo, and Hugging Face,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Run a Large Language model (LLM) chatbot on Arm servers
      and Access the chatbot using the OpenAI-compatible API.
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

