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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:03:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  summary_generated_at: '2026-06-01T22:04:24Z'
  summary_source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  faq_generated_at: '2026-06-02T23:03:30Z'
  faq_source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  summary: >-
    This advanced Learning Path guides you through building a private, offline voice chatbot on
    Arm-based DGX Spark running Linux. You will capture real-time audio from a USB microphone
    using PyAudio with Voice Activity Detection, transcribe speech locally using faster-whisper
    on CPU, and generate responses with vLLM for on-device inference. The steps cover installing
    and validating faster-whisper, constructing a real-time STT pipeline, fine-tuning segmentation
    parameters, and integrating vLLM to complete the end-to-end system. By the end, you will deploy
    and run the full pipeline on DGX Spark, with a focus on adjusting segmentation and prompt
    strategies to balance latency and response quality. Prerequisites include a DGX Spark system
    with at least 15 GB free disk space and a USB microphone, using Docker and Python.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an NVIDIA DGX Spark system with at least 15 GB of available disk space, a USB microphone,
      and a Linux environment. The path uses Python and Docker.
  - question: Which components run on CPU versus GPU in this workflow?
    answer: >-
      The path builds a real-time speech-to-text pipeline on the CPU using faster-whisper. It
      then adds vLLM for local language generation, which runs on GPU.
  - question: How do I verify that faster-whisper is installed correctly?
    answer: >-
      The setup step focuses on confirming that faster-whisper can reliably transcribe audio.
      Run a short recording or sample through the tool and check that you get accurate text output
      before proceeding.
  - question: How is audio captured and segmented for transcription?
    answer: >-
      You capture real-time audio with PyAudio and apply VAD-based segmentation and smart turn
      detection. The path evolves from a simple 10-second recorder to a multithreaded, VAD-enhanced
      STT engine.
  - question: What result should I expect when the full pipeline is running?
    answer: >-
      Speaking into the microphone yields transcribed text from faster-whisper, and vLLM generates
      a local response. You can fine-tune segmentation and prompt strategies to improve latency
      and response quality.
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

