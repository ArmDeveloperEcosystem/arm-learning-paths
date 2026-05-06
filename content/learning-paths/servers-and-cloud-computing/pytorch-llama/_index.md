---
title: Run a Large Language Model (LLM) chatbot with PyTorch using KleidiAI on Arm servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in running LLMs using PyTorch on Arm-based servers. 

learning_objectives:
    - Download the Meta Llama 3.1 model from the Meta Hugging Face repository.
    - 4-bit quantize the model using optimized INT4 KleidiAI Kernels for PyTorch.
    - Run an LLM inference using PyTorch on an Arm-based CPU.
    - Expose an LLM inference as a browser application with Streamlit as the frontend and Torchchat framework in PyTorch as the LLM backend server.
    - Measure performance metrics of the LLM inference running on an Arm-based CPU.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) with at least 16 CPUs from a cloud service provider or an on-premise Arm server.

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 1c5be7bfc7785ae3b06c60210c06324f00aed7ba75145a0fa65425e6005d4f06
  summary: >-
    Run a Large Language Model (LLM) chatbot with PyTorch using KleidiAI on Arm servers walks
    you through an end-to-end Arm software workflow. It is designed for software developers interested
    in running LLMs using PyTorch on Arm-based servers. By the end, you will be able to download
    the Meta Llama 3.1 model from the Meta Hugging Face repository, 4-bit quantize the model using
    optimized INT4 KleidiAI Kernels for PyTorch, and run an LLM inference using PyTorch on an
    Arm-based CPU. It focuses on tools and technologies such as LLM, Generative AI, Python, PyTorch,
    and Hugging Face, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps cover Run a Large Language
    model (LLM) chatbot on Arm servers and Chatbot with Streamlit Frontend.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will download the Meta Llama 3.1 model from the Meta Hugging Face repository, 4-bit
      quantize the model using optimized INT4 KleidiAI Kernels for PyTorch, and run an LLM inference
      using PyTorch on an Arm-based CPU.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in running LLMs using PyTorch
      on Arm-based servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/)
      with at least 16 CPUs from a cloud service provider or an on-premise Arm server.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including LLM, Generative AI, Python, PyTorch, and Hugging
      Face, Linux environments, Arm platforms such as Neoverse, and cloud platforms such as AWS,
      Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Run a Large Language model (LLM) chatbot on Arm servers
      and Chatbot with Streamlit Frontend.
# END generated_summary_faq

author:
    - Nikhil Gupta
    - Pareena Verma
    - Nobel Chowdary Mandepudi

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

