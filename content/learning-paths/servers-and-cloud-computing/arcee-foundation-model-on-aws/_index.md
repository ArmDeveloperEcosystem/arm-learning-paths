---
title: Deploy Arcee AFM-4.5B on AWS Graviton4

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers and engineers who want to deploy the Arcee AFM-4.5B small language model on an AWS Arm-based instance. AFM-4.5B is a 4.5-billion-parameter frontier model that delivers excellent accuracy, strict compliance, and very high cost-efficiency. It was trained on almost 7 trillion tokens of clean, rigorously filtered data, and has been tested across a wide range of languages, including Arabic, English, French, German, Hindi, Italian, Korean, Mandarin, Portuguese, Russian, and Spanish

learning_objectives:
    - Deploy an Arm-based Graviton4 virtual machine on Amazon Web Services
    - Connect to the virtual machine using SSH
    - Download the AFM-4.5B model from Hugging Face
    - Quantize the model with llama.cpp
    - Deploy the model and run inference with llama.cpp

prerequisites:
    - An Amazon Web Services account, with quota for c8g instances
    - Basic familiarity with SSH

author: Julien Simon

### Tags
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
        type: Website
    - resource:
        title: Announcing Arcee Foundation Models
        link: https://www.arcee.ai/blog/announcing-the-arcee-foundation-model-family
        type: Blog
    - resource:
        title: AFM-4.5B, the First Arcee Foundation Model
        link: https://www.arcee.ai/blog/deep-dive-afm-4-5b-the-first-arcee-foundational-model
        type: Blog
    - resource:
        title: Amazon EC2 Graviton Instances
        link: https://aws.amazon.com/ec2/graviton/
        type: Documentation
    - resource:
        title: Amazon EC2 Documentation
        link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
