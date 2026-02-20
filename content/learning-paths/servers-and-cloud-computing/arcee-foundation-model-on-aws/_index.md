---
title: Deploy Arcee AFM-4.5B on Arm-based AWS Graviton4 with Llama.cpp

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

author: Julien Simon

# Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
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
