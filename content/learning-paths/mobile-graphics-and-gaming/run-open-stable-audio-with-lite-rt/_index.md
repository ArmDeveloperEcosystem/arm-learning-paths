---
title: Generate audio with Open Stable Audio using LiteRT runtime

minutes_to_complete: 30

who_is_this_for: This is an introductory topic on how to convert the  text-to-audio model Open Stable Audio to LiteRT (Lite Runtime) and deploying it on an Android device.

learning_objectives:
    - Convert Open Stable Audio to LiteRT
    - Create a simple program to generate audio
    - Compile the application and accelerate it on Arm CPU
    - Run the application on an Android smartphone and generate an audio snippet


prerequisites:
    - A Linux x86 development machine with at least 8 GB of RAM
    - A [HuggingFace](https://huggingface.co/) account
    - An Android phone and a cable to connect it to your development machine

author: Nina Drozd, TODO - add linkedIn, add more involved in the creation?

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
        title: Introducing Stable Audio 2.0
        link: https://stability.ai/news/stable-audio-2-0
        type: documentation
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
