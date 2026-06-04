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
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or a local Arm Linux computer with at least 8 CPUs and 16GB of RAM.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:57:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 410ec28d257ce7aa1308f11a741aa87baea80daf1acb113c4149761144269022
  summary_generated_at: '2026-06-02T03:56:56Z'
  summary_source_hash: 410ec28d257ce7aa1308f11a741aa87baea80daf1acb113c4149761144269022
  faq_generated_at: '2026-06-03T00:57:43Z'
  faq_source_hash: 410ec28d257ce7aa1308f11a741aa87baea80daf1acb113c4149761144269022
  summary: >-
    Deploy the ModelScope FunASR Chinese ASR model on Arm-based Linux servers to enable real-time
    transcription, punctuation restoration, and sentiment analysis. This introductory path walks
    you through the essentials of ModelScope and FunASR, including installing FunASR via pip and
    using it from Python to run speech recognition tasks. You will learn how to leverage open-source
    large language models and tools for Chinese ASR, and describe approaches to accelerate ModelScope
    models on Arm servers. The target environment is Ubuntu 22.04 LTS (or later) on an Arm-based
    instance or local Arm Linux machine with at least 8 CPUs, 16GB RAM, and 30GB disk. Estimated
    time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm-based server or a local Arm Linux computer running Ubuntu 22.04 LTS or later
      with at least 8 CPU cores, 16GB of RAM, and 30GB of disk space. This environment is required
      for the examples in the Learning Path.
  - question: Which FunASR version should I install and how?
    answer: >-
      Install FunASR version 1.2.3 using the command: pip3 install funasr==1.2.3. The examples
      in this Learning Path use 1.2.3, and results might vary with other versions.
  - question: Can I run this on a cloud provider and which ones are suitable?
    answer: >-
      Yes. Use an Arm-based instance from a cloud service provider; AWS, Microsoft Azure, Google
      Cloud, and Oracle are listed options, or use a local Arm Linux machine.
  - question: How do I know FunASR is working correctly after installation?
    answer: >-
      Run the speech recognition example provided in the Learning Path and confirm that an audio
      input produces transcribed text output. FunASR provides a simple interface for transcription
      that you can use to validate your setup.
  - question: What output should I expect from the deployment?
    answer: >-
      You should be able to perform real-time Chinese speech-to-text transcription with punctuation
      restoration and sentiment analysis using FunASR. The steps guide you through enabling these
      capabilities on an Arm-based server.
# END generated_summary_faq

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

