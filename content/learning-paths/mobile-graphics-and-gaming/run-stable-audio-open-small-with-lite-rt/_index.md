---
title: Generate audio with Stable Audio Open Small on LiteRT
description: Learn how to convert and deploy the Stable Audio Open Small text-to-audio model to LiteRT format for audio generation on Android devices and macOS.

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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 388cab0dcb284c29fe2ad82f2b2934d9243c6356b2885d26db0a97c1a1d4d393
  summary: >-
    Learn how to convert and deploy the Stable Audio Open Small text-to-audio model to LiteRT
    format for audio generation on Android devices and macOS. It is designed for developers looking
    to deploy the Stable Audio Open Small text-to-audio model using LiteRT on an Android™ device
    or on a reasonably modern platform with macOS®. By the end, you will be able to download and
    test the Stable Audio Open Small model, convert the Stable Audio Open Small model to the LiteRT
    (.tflite) format, and compile the application for an Arm CPU. It focuses on tools and technologies
    such as CPP, Python, and Hugging Face, Linux and Android environments, and Arm platforms including
    Cortex-A and Cortex-X. The main steps cover Set up your development environment, Download
    and test the model, Convert Stable Audio Open Small model to LiteRT, Build LiteRT, and Create
    a simple program for Android target.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will download and test the Stable Audio Open Small model, convert the Stable Audio Open
      Small model to the LiteRT (.tflite) format, and compile the application for an Arm CPU.
      Learn how to convert and deploy the Stable Audio Open Small text-to-audio model to LiteRT
      format for audio generation on Android devices and macOS.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers looking to deploy the Stable Audio Open Small
      text-to-audio model using LiteRT on an Android™ device or on a reasonably modern platform
      with macOS®.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A Linux-based x86 or macOS development
      machine with at least 8 GB of RAM and 50 GB of disk space (tested on Ubuntu 22.04 with x86_64).;
      A [HuggingFace](https://huggingface.co/) account.; An Android phone in [developer mode](https://developer.android.com/studio/debug/dev-options)
      and a cable to connect it to your development machine.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CPP, Python, and Hugging Face, Linux and Android
      environments, and Arm platforms such as Cortex-A and Cortex-X.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your development environment, Download and
      test the model, Convert Stable Audio Open Small model to LiteRT, Build LiteRT, and Create
      a simple program for Android target.
# END generated_summary_faq

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

