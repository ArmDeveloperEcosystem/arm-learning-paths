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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  summary: >-
    Learn how to build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference
    on AWS Graviton4 instances with perplexity-based quality evaluation. It is designed for developers
    and ML engineers who want to deploy Arcee's AFM-4.5B small language model on AWS Graviton4
    instances using Llama.cpp. By the end, you will be able to launch an Arm-based EC2 instance
    on AWS Graviton4, build and install Llama.cpp from source, and download and quantize the AFM-4.5B
    model from Hugging Face. It focuses on tools and technologies such as AWS, Hugging Face, Python,
    and Llama.cpp, Linux environments, Arm platforms including Neoverse, and cloud platforms such
    as AWS. The main steps cover Overview, Provision your Graviton4 environment, Configure your
    Graviton4 environment, Build Llama.cpp, and Install Python dependencies.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will launch an Arm-based EC2 instance on AWS Graviton4, build and install Llama.cpp
      from source, and download and quantize the AFM-4.5B model from Hugging Face. Learn how to
      build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference on AWS Graviton4
      instances with perplexity-based quality evaluation.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for developers and ML engineers who want to deploy Arcee's AFM-4.5B
      small language model on AWS Graviton4 instances using Llama.cpp.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [AWS account](https://aws.amazon.com/)
      with permission to launch Graviton4 (`c8g.4xlarge` or larger) instances; Basic familiarity
      with Linux and SSH.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including AWS, Hugging Face, Python, and Llama.cpp, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Provision your Graviton4 environment, Configure
      your Graviton4 environment, Build Llama.cpp, and Install Python dependencies.
# END generated_summary_faq

author: Julien Simon

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

