---
title: Deploy Arcee AFM-4.5B on Arm-based AWS Graviton4 with Llama.cpp
description: Learn how to build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference on AWS Graviton4 instances with perplexity-based quality evaluation.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers and ML engineers who want to deploy Arcee's AFM-4.5B small language model on AWS Graviton4 instances using Llama.cpp.

learning_objectives:
    - Launch an Arm-based EC2 instance on AWS Graviton4
    - Build and install Llama.cpp from source
    - Download and quantize the AFM-4.5B model from Hugging Face
    - Run inference on the quantized model using Llama.cpp
    - Evaluate model quality by measuring perplexity

prerequisites:
    - An [AWS account](https://aws.amazon.com/) with permission to launch Graviton4 (`c8g.4xlarge` or larger) instances
    - Basic familiarity with Linux and SSH

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:23:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  summary_generated_at: '2026-06-26T17:23:15Z'
  summary_source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  faq_generated_at: '2026-06-26T17:23:15Z'
  faq_source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  summary: >-
    You'll provision an Arm-based Amazon EC2 instance powered by AWS Graviton4, prepare a Linux
    environment, and build the `llama.cpp` inference engine from source. With a dedicated Python
    virtual environment, you'll retrieve Arcee's AFM-4.5B model from Hugging Face, perform quantization,
    and run inference using `llama.cpp` on Graviton4. You'll learn to make practical choices, including
    instance sizing, storage, dependency setup, and repository selection, so the model compiles
    and executes cleanly on Arm. By the end, you'll perform a perplexity-based quality check to validate that the quantized model runs, and interpret the reported perplexity
    as an objective signal of model quality.
  faqs:
  - question: Which EC2 instance type and storage size should I choose when launching?
    answer: >-
      Use a `c8g.4xlarge` (or larger) EC2 instance powered by Graviton4 and allocate at least 128 GB of available
      storage. Configure the volume size during instance launch in the EC2 service so the space
      is available before you build and run the model.
  - question: When should I create the SSH key pair and what is it used for?
    answer: >-
      Create the SSH key pair in the AWS Management Console before launching the instance. You
      will use it to connect to the Graviton4 host over SSH for setup, building, and running inference.
  - question: Which `llama.cpp` repository should I clone, and why build from source here?
    answer: >-
      Clone the upstream repository at `https://github.com/ggerganov/llama.cpp` as shown in the
      steps. Build from source because AFM-4.5B support was contributed upstream, so the
      standard repo contains the necessary modeling code.
  - question: Do I need a Python virtual environment for this workflow?
    answer: >-
      Yes. Creating a virtual environment, such as `env-llama-cpp`, isolates the Python interpreter
      and packages required for the model workflow and avoids conflicts with system packages.
  - question: How do I know that quantization and perplexity evaluation worked?
    answer: >-
      After downloading AFM-4.5B and completing quantization, run the `llama.cpp` steps that load
      the quantized model and perform evaluation. Expect the program to load the model without
      errors and print a perplexity value you can use to compare quality across runs.
# END generated_summary_faq

author: Julien Simon

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

# Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - AWS
    - Hugging Face
    - Python
    - Llama.cpp
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Arcee AI
      link: https://www.arcee.ai
      type: website
  - resource:
      title: Announcing the Arcee Foundation Model family
      link: https://www.arcee.ai/blog/announcing-the-arcee-foundation-model-family
      type: blog
  - resource:
      title: Deep Dive - AFM-4.5B, the first Arcee Foundation Model
      link: https://www.arcee.ai/blog/deep-dive-afm-4-5b-the-first-arcee-foundational-model
      type: blog
  - resource:
      title: Amazon EC2 Graviton instances
      link: https://aws.amazon.com/ec2/graviton/
      type: documentation
  - resource:
      title: Amazon EC2 User Guide
      link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/
      type: documentation

# FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
