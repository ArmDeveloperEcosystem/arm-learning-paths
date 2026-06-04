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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:16:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  summary_generated_at: '2026-06-02T03:05:06Z'
  summary_source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  faq_generated_at: '2026-06-03T00:16:57Z'
  faq_source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  summary: >-
    This Learning Path guides you through deploying Arcee’s AFM-4.5B small language model on Arm-based
    Google Cloud Axion instances using Llama.cpp. You will provision a Linux Compute Engine VM
    (c4a-standard-16 or larger), install system and Python dependencies, build Llama.cpp from
    source, download the model from Hugging Face, quantize it, and run inference. You will also
    evaluate model quality by measuring perplexity. It targets developers and ML engineers and
    is scoped to about 30 minutes. Prerequisites include a Google Cloud account with permission
    and quota to launch Axion instances, at least 128 GB of available storage, and basic familiarity
    with Linux and SSH.
  faqs:
  - question: What do I need in my Google Cloud project before launching the VM?
    answer: >-
      You need permission and sufficient quota to launch a Google Cloud Axion instance of type
      c4a-standard-16 (or larger). Ensure at least 128 GB of available storage for the model and
      dependencies.
  - question: Which Llama.cpp repository should I clone for AFM-4.5B support?
    answer: >-
      Use the standard Llama.cpp repository: git clone https://github.com/ggerganov/llama.cpp.
      AFM-4.5B support is available because Arcee AI contributed the necessary modeling code upstream.
  - question: Do I need a Hugging Face account or token to download AFM-4.5B?
    answer: >-
      The Learning Path states that you will download the AFM-4.5B model from Hugging Face, but
      it does not explicitly list whether a Hugging Face account or token is required. Follow
      the steps as provided in the path.
  - question: Why create a Python virtual environment for Llama.cpp, and how is it set up here?
    answer: >-
      A virtual environment isolates dependencies and prevents conflicts. In this path, you create
      one with virtualenv env-llama-cpp before installing the required Python packages.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will have built Llama.cpp on a Google Cloud Axion Arm64 VM, downloaded and quantized
      AFM-4.5B, and run inference. You will also evaluate model quality by measuring perplexity.
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

