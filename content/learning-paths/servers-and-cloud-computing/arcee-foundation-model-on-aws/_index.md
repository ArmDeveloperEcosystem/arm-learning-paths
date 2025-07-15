---
title: Deploy Arcee AFM-4.5B on AWS Graviton4

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers and engineers who want to deploy the Arcee AFM-4.5B small language model on an Arm-based AWS instance

learning_objectives:
    - Launch and set up an Arm-based Graviton4 virtual machine on Amazon Web Services
    - Build Llama.cpp from source
    - Download AFM-4.5B from Hugging Face
    - Quantize AFM-4.5B using Llama.cpp
    - Deploy the model and run inference with Llama.cpp
    - Evaluate the quality of quantized models by measuring perplexity

prerequisites:
    - Access to launch an EC2 instance of type c8g.4xlarge (or larger) with 128 GB of storage
    - An [AWS account](https://aws.amazon.com/) with permission to launch c8g (Graviton4) instances
    - Basic familiarity with SSH

author: Julien Simon

# Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
arm_ips:
    - Neoverse
tools_software_languages:
    - Amazon Web Services
    - Linux
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
      title: Announcing Arcee Foundation Models
      link: https://www.arcee.ai/blog/announcing-the-arcee-foundation-model-family
      type: blog
  - resource:
      title: AFM-4.5B, the first Arcee Foundation Model
      link: https://www.arcee.ai/blog/deep-dive-afm-4-5b-the-first-arcee-foundational-model
      type: blog
  - resource:
      title: Amazon EC2 Graviton instances
      link: https://aws.amazon.com/ec2/graviton/
      type: documentation
  - resource:
      title: Amazon EC2 documentation
      link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/
      type: documentation

# FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
