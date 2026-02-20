---
title: Deploy Arcee AFM-4.5B on Arm-based Google Cloud Axion with Llama.cpp

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

author: Julien Simon

# Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
arm_ips:
    - Neoverse
cloud_service_providers:
  - Google Cloud
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
