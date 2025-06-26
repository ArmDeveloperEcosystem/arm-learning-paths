---
title: Deploy Arcee AFM-4.5B on Google Axion

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers and engineers who want to deploy the Arcee AFM-4.5B small language model on a Google Cloud Axion c4a instance. AFM-4.5B is a 4.5-billion-parameter frontier model that delivers excellent accuracy, strict compliance, and very high cost-efficiency. It was trained on almost 7 trillion tokens of clean, rigorously filtered data, and has been tested across a wide range of languages, including Arabic, English, French, German, Hindi, Italian, Korean, Mandarin, Portuguese, Russian, and Spanish

learning_objectives:
    - Launch and set up an Arm-based Axion c4a virtual machine on Google Cloud

    - Build llama.cpp from source

    - Download AFM-4.5B from Hugging Face

    - Quantize AFM-4.5B with llama.cpp

    - Deploy the model and run inference with llama.cpp

    - Evaluate the quality of quantized models by measuring perplexity

prerequisites:
    - A Google Cloud account, with quota for c4a instances

    - Basic familiarity with SSH

author: Julien Simon

### Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: ML
arm_ips:
    - Neoverse

tools_software_languages:
    - Google Cloud

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
        title: Google Cloud c4a Instances
        link: https://cloud.google.com/blog/products/compute/try-c4a-the-first-google-axion-processor 
        type: Documentation

    - resource:
        title: Google Cloud Compute Engine
        link: https://cloud.google.com/compute/docs
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
