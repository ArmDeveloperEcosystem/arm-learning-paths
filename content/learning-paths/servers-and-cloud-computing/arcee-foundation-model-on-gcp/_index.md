---
title: Deploy Arcee AFM-4.5B on Arm-based Google Cloud Axion with Llama.cpp
description: Learn how to build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference on Google Cloud Axion instances with perplexity-based quality evaluation.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers and ML engineers who want to deploy Arcee's AFM-4.5B small language model on Google Cloud Axion instances using Llama.cpp.

learning_objectives:
    - Launch an Arm-based Compute Engine instance on Google Cloud Axion
    - Build and install Llama.cpp from source
    - Download and quantize the AFM-4.5B model from Hugging Face
    - Run inference on the quantized model using Llama.cpp
    - Evaluate model quality by measuring perplexity

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with permission to launch Axion (`c4a-standard-16` or larger) instances
    - Basic familiarity with Linux and SSH

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  summary: >-
    Learn how to build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference
    on Google Cloud Axion instances with perplexity-based quality evaluation. It is designed for
    developers and ML engineers who want to deploy Arcee's AFM-4.5B small language model on Google
    Cloud Axion instances using Llama.cpp. By the end, you will be able to launch an Arm-based
    Compute Engine instance on Google Cloud Axion, build and install Llama.cpp from source, and
    download and quantize the AFM-4.5B model from Hugging Face. It focuses on tools and technologies
    such as Google Cloud, Hugging Face, Python, and Llama.cpp, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Google Cloud. The main steps cover AFM-4.5B
    deployment on Google Cloud Axion with Llama.cpp, Provision a Google Cloud Axion Arm64 environment,
    Configure your Google Cloud Axion Arm64 environment, Build Llama.cpp on Google Cloud Axion
    Arm64, and Install Python dependencies for Llama.cpp.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will launch an Arm-based Compute Engine instance on Google Cloud Axion, build and install
      Llama.cpp from source, and download and quantize the AFM-4.5B model from Hugging Face. Learn
      how to build llama.cpp, quantize the Arcee AFM-4.5B model, and run optimized inference on
      Google Cloud Axion instances with perplexity-based quality evaluation.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for developers and ML engineers who want to deploy Arcee's AFM-4.5B
      small language model on Google Cloud Axion instances using Llama.cpp.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud account](https://console.cloud.google.com/)
      with permission to launch Axion (`c4a-standard-16` or larger) instances; Basic familiarity
      with Linux and SSH.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Google Cloud, Hugging Face, Python, and Llama.cpp,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around AFM-4.5B deployment on Google Cloud Axion with Llama.cpp,
      Provision a Google Cloud Axion Arm64 environment, Configure your Google Cloud Axion Arm64
      environment, Build Llama.cpp on Google Cloud Axion Arm64, and Install Python dependencies
      for Llama.cpp.
# END generated_summary_faq

author: Julien Simon

# Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - Google Cloud
armips:
    - Neoverse
tools_software_languages:
    - Google Cloud
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
      title: Google Cloud Axion instances
      link: https://cloud.google.com/products/axion
      type: documentation
  - resource:
      title: Google Cloud Compute Engine Documentation
      link: https://cloud.google.com/compute/docs
      type: documentation

# FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

