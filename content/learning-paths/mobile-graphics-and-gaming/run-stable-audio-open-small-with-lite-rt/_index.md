---
title: Generate audio with Stable Audio Open Small on LiteRT

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers looking to deploy the Stable Audio Open Small text-to-audio model using LiteRT on an Android™ device or on a reasonably modern platform with macOS®.

learning_objectives:
    - Download and test the Stable Audio Open Small model. 
    - Convert the Stable Audio Open Small model to the LiteRT (.tflite) format.
    - Compile the application for an Arm CPU.
    - Create a simple application that generates audio. 
    - Run the application on an Android smartphone and generate an audio snippet.

prerequisites:
    - A Linux-based x86 or macOS development machine with at least 8 GB of RAM and 50 GB of disk space (tested on Ubuntu 22.04 with x86_64).
    - A [HuggingFace](https://huggingface.co/) account.
    - An Android phone in [developer mode](https://developer.android.com/studio/debug/dev-options) and a cable to connect it to your development machine.

author:
    - Nina Drozd
    - Gian Marco Iodice
    - Adnan AlSinan
    - Aude Vuilliomenet
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-X

tools_software_languages:
    - CPP
    - Python
    - Hugging Face

operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: Stability AI and Arm Collaborate to Release Stable Audio Open Small, Enabling Real-World Deployment for On-Device Audio Generation
        link: https://stability.ai/news/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control
        type: blog
    - resource:
        title: "Unlocking audio generation on Arm CPUs to all: Running Stable Audio Open Small with KleidiAI"
        link: https://community.arm.com/arm-community-blogs/b/ai-blog/posts/audio-generation-arm-cpus-stable-audio-open-small-kleidiai
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
