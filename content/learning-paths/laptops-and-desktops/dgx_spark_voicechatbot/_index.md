---
title: Build an offline voice chatbot with faster-whisper and vLLM on DGX Spark

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers and ML engineers who want to build private, offline voice assistant systems on Arm-based servers such as DGX Spark.

learning_objectives:
  - Explain the architecture of an offline voice chatbot pipeline combining speech-to-text (STT) and vLLM
  - Capture and segment real-time audio using PyAudio and Voice Activity Detection (VAD)
  - Transcribe speech using faster-whisper and generate replies using vLLM
  - Tune segmentation and prompt strategies to improve latency and response quality
  - Deploy and run the full pipeline on Arm-based systems such as DGX Spark

prerequisites:
    - An NVIDIA DGX Spark system with at least 15 GB of available disk space
    - A USB microphone for audio input

author: Odin Shen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - Python
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: NVIDIA DGX Spark website
        link: https://www.nvidia.com/en-gb/products/workstations/dgx-spark/
        type: website
    - resource:
        title: NVIDIA DGX Spark Playbooks GitHub repository
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: documentation
    - resource:
        title: Spark RAG Pipeline Tutorial
        link: /learning-paths/laptops-and-desktops/dgx_spark_rag/
        type: website
    - resource:
        title: Build and Run vLLM on Arm Servers
        link: /learning-paths/servers-and-cloud-computing/vllm/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
