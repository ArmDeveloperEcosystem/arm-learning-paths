---
title: Deploy ModelScope FunASR Model on Arm Servers

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in learning how to deploy the ModelScope FunASR Chinese Automatic Speech Recognition (ASR) model on Arm-based servers.

learning_objectives:
    - Leverage open-source large language models and tools to build Chinese ASR applications.
    - Deploy real-time Chinese speech recognition, punctuation restoration, and sentiment analysis using FunASR.
    - Describe how to accelerate ModelScope models on Arm-based servers for enhanced performance and efficiency.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or a local Arm Linux computer with at least 8 CPUs and 16GB of RAM.

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
