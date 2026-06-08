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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:16:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  summary_generated_at: '2026-06-02T03:04:42Z'
  summary_source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  faq_generated_at: '2026-06-03T00:16:17Z'
  faq_source_hash: 964c1e6a87810dca686a7b3218433ce09d31bd92882db10af355e8c50bb6091c
  summary: >-
    Follow a concise workflow to deploy Arcee’s AFM-4.5B small language model on Arm-based AWS
    Graviton4 using Llama.cpp. You will launch a Graviton4 EC2 instance (c8g.4xlarge or larger),
    configure a Linux environment with system packages and a Python virtual environment, build
    Llama.cpp from source, download the AFM-4.5B model from Hugging Face, quantize it, and run
    inference. The path includes evaluating model quality using perplexity. Prerequisites are
    an AWS account with permission to launch Graviton4 instances, at least 128 GB of available
    storage, and basic Linux and SSH familiarity. The estimated time to complete is about 30 minutes.
  faqs:
  - question: Do I need specific AWS access or resources before starting?
    answer: >-
      Yes. You need an AWS account with permission to launch Graviton4 EC2 instances and at least
      128 GB of available storage. Basic familiarity with Linux and SSH is also expected.
  - question: Which EC2 instance type should I launch for this workflow?
    answer: >-
      Use an Arm-based AWS Graviton4 instance of type c8g.4xlarge or larger. The steps assume
      a Linux environment on this instance.
  - question: How do I connect to the EC2 instance?
    answer: >-
      Create an SSH key pair in the EC2 console as part of the provisioning steps. You will use
      this key pair to establish an SSH connection to your Graviton4 instance.
  - question: Which Llama.cpp repository should I use for AFM-4.5B?
    answer: >-
      Use the standard upstream repository at https://github.com/ggerganov/llama.cpp. Arcee AI
      has contributed the necessary modeling code upstream, so no custom fork is required.
  - question: What are the main steps after provisioning the instance?
    answer: >-
      Install system packages and a Python environment, then build Llama.cpp from source. Next,
      download the AFM-4.5B model from Hugging Face, quantize it, run inference with Llama.cpp,
      and evaluate quality by measuring perplexity.
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

