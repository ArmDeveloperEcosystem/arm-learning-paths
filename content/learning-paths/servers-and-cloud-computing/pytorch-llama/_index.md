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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:55:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1c5be7bfc7785ae3b06c60210c06324f00aed7ba75145a0fa65425e6005d4f06
  summary_generated_at: '2026-06-02T04:51:34Z'
  summary_source_hash: 1c5be7bfc7785ae3b06c60210c06324f00aed7ba75145a0fa65425e6005d4f06
  faq_generated_at: '2026-06-03T01:55:09Z'
  faq_source_hash: 1c5be7bfc7785ae3b06c60210c06324f00aed7ba75145a0fa65425e6005d4f06
  summary: >-
    Learn how to run a Meta Llama 3.1 LLM chatbot on Arm-based servers using PyTorch and KleidiAI
    INT4 kernels. You will use an Ubuntu 24.04 LTS Arm instance with at least 16 cores, 64 GB
    RAM, and 50 GB disk; the steps were tested on an AWS Graviton4 r8g.4xlarge. The path covers
    downloading the model from the Meta Hugging Face repository, applying 4-bit quantization,
    running CPU inference with PyTorch, and exposing the service through a Streamlit frontend
    backed by the Torchchat framework. You will also measure performance metrics for the inference
    run. Estimated time to complete is about 30 minutes. No additional explicit prerequisites
    are listed beyond access to an Arm-based server.
  faqs:
  - question: What infrastructure and OS should I use to follow this path?
    answer: >-
      Use an Arm server running Ubuntu 24.04 LTS with at least 16 cores, 64 GB of RAM, and around
      50 GB of disk space. The instructions were tested on an AWS Graviton4 r8g.4xlarge instance.
  - question: Do I need a GPU to run the example?
    answer: >-
      No. The Learning Path runs LLM inference on an Arm-based CPU using PyTorch.
  - question: Where do I obtain the model used in the example?
    answer: >-
      Download the Meta Llama 3.1 model from the Meta Hugging Face repository as shown in the
      steps.
  - question: How is quantization performed, and what role does KleidiAI play?
    answer: >-
      The model is 4-bit quantized using optimized INT4 KleidiAI Kernels for PyTorch. This setup
      is used to run the LLM on Arm-based CPUs.
  - question: Which packages are required for the frontend, and how do I avoid HTTP client issues?
    answer: >-
      Activate the torch_env virtual environment, install openai version 1.45.0, and roll back
      httpx to a version before 0.28. Then start the backend server and launch the Streamlit app
      to access the chatbot in your browser.
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

