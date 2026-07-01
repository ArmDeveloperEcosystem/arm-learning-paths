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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:36:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  summary_generated_at: '2026-06-30T21:36:51Z'
  summary_source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  faq_generated_at: '2026-06-30T21:36:51Z'
  faq_source_hash: a4cf1d9161b3a32e29694415762eda419752e1c3144662d5e131b6553f0a58e3
  summary: >-
    You'll deploy Hugging Face Sentiment Analysis models
    with PyTorch on Arm servers and measure how they perform. Starting from a working Ubuntu
    22.04 Arm environment, you'll run three NLP models with the Sentiment Analysis
    pipeline, record baseline results, and then enable BFloat16 fast math kernels to assess the
    impact on inference performance. The workflow is validated on Arm Neoverse-based AWS Graviton3
    (c7g) instances and remains applicable to Arm servers meeting the stated requirements. By
    the end, you'll compare before-and-after measurements to confirm the effect of BFloat16
    on this workload.
  faqs:
  - question: Which environment do the instructions assume?
    answer: >-
      The instructions target an Arm server running Ubuntu 22.04 LTS. They've been tested on
      AWS Graviton3 (c7g) instances.
  - question: What system resources should I provision before running the steps?
    answer: >-
      Use an Arm server instance with at least four CPU cores and 8GB of RAM. This capacity supports
      running the three sentiment analysis models and collecting measurements.
  - question: Which framework and model source are used in this path?
    answer: >-
      The path uses PyTorch to run Natural Language Processing models sourced from Hugging Face.
      The examples use the Sentiment Analysis pipeline.
  - question: How should I measure the performance uplift from BFloat16 fast math kernels?
    answer: >-
      First, run the models to collect a baseline using the same Sentiment Analysis pipeline.
      Then enable BFloat16 fast math kernels on supported Arm Neoverse-based AWS Graviton3 processors,
      rerun the same workload, and compare measurements.
  - question: Which models are evaluated and what should I have at the end?
    answer: >-
      The path evaluates three NLP models with the Sentiment Analysis pipeline. By the end, you
      should have deployed the models on your Arm server and recorded baseline and BFloat16-enabled
      performance results for comparison.
# END generated_summary_faq

author: Pareena Verma

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

