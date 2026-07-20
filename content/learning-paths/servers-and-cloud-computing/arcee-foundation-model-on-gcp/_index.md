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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:24:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  summary_generated_at: '2026-06-26T17:24:59Z'
  summary_source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  faq_generated_at: '2026-06-26T17:24:59Z'
  faq_source_hash: b2f60d2c31ef380e6e6ef3028671ad9242dd51c98f4a192f2da32bb05b94e185
  summary: >-
    You'll deploy Arcee's AFM-4.5B model on Arm-based Google Cloud Axion using
    `llama.cpp`. First, you'll provision an Axion-based VM, prepare the system and Python environment, and build `llama.cpp`
    from source. Then, you'll download and quantize the model, and run inference. You'll make concrete choices
    about instance size and storage, manage packages in an isolated environment, and use the upstream
    `llama.cpp` repository that includes the required AFM support. By the end, you'll perform a perplexity run to assess model quality. A successful outcome includes a clean build, a loadable
    quantized model, token generation during a test prompt, and a reported perplexity value.
  faqs:
  - question: Which Axion machine type should I choose to follow the steps?
    answer: >-
      Use `c4a-standard-16` or larger, as specified. Smaller types are not listed for this workflow.
  - question: What should I check in my Google Cloud project before launching the Axion VM?
    answer: >-
      Confirm that your project has quota for Axion instances and that sufficient storage is available.
      The Learning Path calls for at least 128 GB to accommodate the model and dependencies.
  - question: Which `llama.cpp` repository should I clone for AFM-4.5B?
    answer: >-
      Clone the standard upstream repository from `ggerganov/llama.cpp`. Arcee AI has contributed
      the required modeling code upstream, so you don't need a custom fork.
  - question: How do I know the `llama.cpp` build on Axion completed successfully?
    answer: >-
      The build should finish without errors and produce binaries that run as shown in the steps.
      Invoking the tool to display its help or version is a quick validation before proceeding.
  - question: What result should I expect after quantization and a test inference?
    answer: >-
      Quantization produces a smaller model artifact that `llama.cpp` can load. A brief prompt should
      generate tokens without errors, and a perplexity run should complete with a numeric value.
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
