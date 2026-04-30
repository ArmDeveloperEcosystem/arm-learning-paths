---
title: Build an offline voice chatbot with faster-whisper and vLLM on DGX Spark

description: Learn how to build an offline voice assistant combining speech-to-text via faster-whisper and text generation via vLLM on Arm-based DGX Spark for privacy-focused deployments.

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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:16Z'
  generator: template
  source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  summary: >-
    Learn how to build an offline voice assistant combining speech-to-text via faster-whisper
    and text generation via vLLM on Arm-based DGX Spark for privacy-focused deployments. It is
    designed for developers and ML engineers who want to build private, offline voice assistant
    systems on Arm-based servers such as DGX Spark. By the end, you will be able to explain the
    architecture of an offline voice chatbot pipeline combining speech-to-text (STT) and vLLM,
    capture and segment real-time audio using PyAudio and Voice Activity Detection (VAD), and
    transcribe speech using faster-whisper and generate replies using vLLM. It focuses on tools
    and technologies such as Docker and Python, Linux environments, and Arm platforms including
    Neoverse. The main steps cover Build an offline voice assistant with whisper and vLLM, Install
    faster-whisper for local speech recognition, Build a real-time STT pipeline on CPU, Fine-tune
    segmentation parameters, and Build a real-time offline voice chatbot using STT and vLLM.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain the architecture of an offline voice chatbot pipeline combining speech-to-text
      (STT) and vLLM, capture and segment real-time audio using PyAudio and Voice Activity Detection
      (VAD), and transcribe speech using faster-whisper and generate replies using vLLM. Learn
      how to build an offline voice assistant combining speech-to-text via faster-whisper and
      text generation via vLLM on Arm-based DGX Spark for privacy-focused deployments.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers and ML engineers who want to build private, offline
      voice assistant systems on Arm-based servers such as DGX Spark.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An NVIDIA DGX Spark system with at least
      15 GB of available disk space; A USB microphone for audio input.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Docker and Python, Linux environments, and Arm platforms
      such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build an offline voice assistant with whisper and
      vLLM, Install faster-whisper for local speech recognition, Build a real-time STT pipeline
      on CPU, Fine-tune segmentation parameters, and Build a real-time offline voice chatbot using
      STT and vLLM.
# END generated_summary_faq

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

