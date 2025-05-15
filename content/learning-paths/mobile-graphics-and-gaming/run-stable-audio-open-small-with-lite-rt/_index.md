---
title: Generate audio with Stable Audio Open Small on LiteRT

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers looking to deploy the Stable Audio Open Small text-to-audio model using LiteRT on an Android device.

learning_objectives:
    - Download  and learn about the Stable Audio Open Small.
    - Create a simple application to generate audio.
    - Compile the application for an Arm CPU.
    - Run the application on an Android smartphone and generate an audio snippet.

prerequisites:
    - A Linux-based x86 or macOS development machine with at least 8 GB of RAM (tested on Ubuntu 20.04.4 LTS with x86_64).
    - A [HuggingFace](https://huggingface.co/) account.
    - An Android phone and a cable to connect it to your development machine.

author:
    - Nina Drozd
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X

tools_software_languages:
    - C++
    - Python

operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: Stability AI and Arm Collaborate to Release Stable Audio Open Small, Enabling Real-World Deployment for On-Device Audio Generation
        link: https://stability.ai/news/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control
        type: blog
    - resource:
        title: Stability AI optimized its audio generation model to run on Arm chips
        link: https://techcrunch.com/2025/03/03/stability-ai-optimized-its-audio-generation-model-to-run-on-arm-chips/
        type: blog
    - resource:
        title: Fast Text-to-Audio Generation with Adversarial Post-Training
        link: https://arxiv.org/abs/2505.08175
        type: website




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
