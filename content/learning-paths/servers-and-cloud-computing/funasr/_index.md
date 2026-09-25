---
title: Deploy ModelScope FunASR Model on Arm Servers
description: Learn how to deploy the ModelScope FunASR Chinese automatic speech recognition model on Arm-based servers with real-time transcription and sentiment analysis.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in learning how to deploy the ModelScope FunASR Chinese Automatic Speech Recognition (ASR) model on Arm-based servers.

learning_objectives:
    - Leverage open-source large language models and tools to build Chinese ASR applications.
    - Deploy real-time Chinese speech recognition, punctuation restoration, and sentiment analysis using FunASR.
    - Describe how to accelerate ModelScope models on Arm-based servers for enhanced performance and efficiency.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or a local Arm Linux computer with at least 8 CPUs and 16GB of RAM

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:01:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5a07ef6da46ab992765c534ff2d1d8b37c5adc92e412bcd105fe931e606de14b
  summary_generated_at: '2026-09-10T22:01:50Z'
  summary_source_hash: 5a07ef6da46ab992765c534ff2d1d8b37c5adc92e412bcd105fe931e606de14b
  faq_generated_at: '2026-09-10T22:01:50Z'
  faq_source_hash: 5a07ef6da46ab992765c534ff2d1d8b37c5adc92e412bcd105fe931e606de14b
  summary: >-
    You'll deploy a Chinese speech-recognition workflow on Arm-based Linux servers with ModelScope and FunASR. First, you'll prepare an Arm Ubuntu environment, install the pinned FunASR release, load a pretrained model, and run speech-to-text. Next, you'll optionally enable punctuation restoration and sentiment analysis, then review the transcription and analysis output from the completed pipeline.
  faqs:
  - question: Which FunASR version should I use for the examples?
    answer: >-
      Use `funasr==1.2.3`. Results
      might vary with other versions.
  - question: What should I check on my server before installing anything?
    answer: >-
      Verify that you're on an Arm-based machine running Ubuntu 22.04 LTS or later with at least
      8 cores, 16GB RAM, and 30GB of free disk space.
  - question: What result should I expect when the ASR pipeline runs successfully?
    answer: >-
      You should see Chinese speech transcribed to text, with optional punctuation restoration
      and sentiment analysis outputs.
  - question: Where do the models used in the examples come from?
    answer: >-
      The models are pre-trained and come from ModelScope, an open-source platform designed to simplify the integration of AI models into applications.
  - question: Which Python version does the optimized PyTorch setup require?
    answer: >-
      Use Python 3.10. If your current version is lower or higher, install `python3.10`, configure
      the `python3` alternatives, and confirm the active version with `python --version`.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - ModelScope
    - FunASR
    - LLM
    - Generative AI
    - Python

further_reading:
    - resource:
        title: ModelScope GitHub Repository
        link: https://github.com/modelscope/modelscope
        type: github
    - resource:
        title: FunASR GitHub Repository
        link: https://github.com/modelscope/FunASR
        type: github
    - resource:
        title: FunASR tutorial
        link: https://modelscope.cn/models/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch
        type: documentation
    - resource:
        title: Kleidi improves ASR on Arm Neoverse N2
        link: https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/neoverse-n2-delivers-leading-price-performance-on-asr
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
