---
title: Accelerate Natural Language Processing (NLP) models from Hugging Face on Arm servers
description: Learn how to deploy and accelerate PyTorch NLP sentiment analysis models from Hugging Face on Arm servers with BFloat16 fast math kernel optimization on Graviton3 processors.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run and accelerate the performance of Natural Language Processing (NLP) models on Arm-based servers. 

learning_objectives:
    - Deploy PyTorch NLP Sentiment Analysis models from Hugging Face on Arm servers. 
    - Evaluate the performance of three NLP models using the Sentiment Analysis pipeline.
    - Measure the performance uplift of these models by enabling support for BFloat16 fast math kernels on Arm Neoverse-based AWS Graviton3 Processors.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:24:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  summary_generated_at: '2026-06-02T03:11:52Z'
  summary_source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  faq_generated_at: '2026-06-03T00:24:45Z'
  faq_source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  summary: >-
    Learn to deploy and evaluate Hugging Face Sentiment Analysis models with PyTorch on Arm servers
    running Linux. You will run three NLP models using the Sentiment Analysis pipeline, then enable
    BFloat16 fast math kernels on Arm Neoverse-based AWS Graviton3 processors to measure performance
    uplift. The instructions target Ubuntu 22.04 LTS on an Arm server with at least four cores
    and 8GB of RAM, and have been tested on AWS Graviton3 (c7g). You will use Python, PyTorch,
    and Hugging Face to complete the workflow. Prerequisite: access to an Arm-based instance from
    a cloud provider or an on-premise Arm server.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need an Arm-based instance from a cloud service provider or an on-prem Arm server. The
      instructions assume Ubuntu 22.04 LTS with at least four cores and 8GB RAM and have been
      tested on AWS Graviton3 (c7g) instances.
  - question: Which platforms can I use for this path?
    answer: >-
      You can use an Arm-based instance from AWS, Microsoft Azure, Google Cloud, or Oracle, or
      an on-prem Arm server. The procedure is written for any Arm server running Ubuntu 22.04
      LTS.
  - question: What should I install first to follow the steps?
    answer: >-
      Install PyTorch on your Arm machine. PyTorch is the framework used to deploy and run the
      Hugging Face NLP models in this path.
  - question: How do I know the sentiment analysis models ran successfully?
    answer: >-
      You should be able to execute the Sentiment Analysis pipeline for three Hugging Face models
      in PyTorch and capture performance measurements. The path then has you compare results before
      and after enabling BFloat16 fast math kernels.
  - question: How do I enable and validate BFloat16 fast math kernels on Graviton3?
    answer: >-
      Follow the steps to enable support for BFloat16 fast math kernels on Arm Neoverse-based
      AWS Graviton3 processors. Validate by re-running the same workloads and comparing the measured
      performance uplift reported in the path.
# END generated_summary_faq

author: Pareena Verma

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

