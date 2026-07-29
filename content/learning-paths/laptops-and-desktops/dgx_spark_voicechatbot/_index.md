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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:15:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  summary_generated_at: '2026-07-28T16:15:38Z'
  summary_source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  faq_generated_at: '2026-07-28T16:15:38Z'
  faq_source_hash: 4ccde526ec4dd9fc18672e162e067108c7251161c1da0375a0bb0374a2f3a4ea
  summary: >-
    You'll build a local voice chatbot on an Arm-based NVIDIA DGX Spark with `faster-whisper` for
    speech-to-text and vLLM for response generation. You'll capture microphone audio with PyAudio,
    add voice and turn detection, tune segmentation for stable low-latency transcription, and
    connect the CPU STT pipeline to GPU-backed vLLM. You'll validate segmented transcripts followed
    by local replies.
  faqs:
  - question: What result should I expect after installing `faster-whisper`?
    answer: >-
      After a successful installation, you can transcribe a short audio sample or live microphone input
      with readable text and no runtime errors. Use this to confirm the installation before moving
      on to pipeline changes.
  - question: When should I upgrade the speech model in the CPU STT pipeline?
    answer: >-
      Upgrade after you confirm baseline transcription works. The build step adds a more accurate
      model and VAD. If latency increases, proceed to segmentation tuning.
  - question: How do I know VAD and turn detection are working correctly?
    answer: >-
      Transcriptions should arrive as sentence-like chunks, and pauses should start new segments.
      If long monologues merge into one block or speech is cut mid-sentence, adjust the segmentation
      parameters.
  - question: What should I verify before integrating vLLM with the STT engine?
    answer: >-
      Ensure the CPU-based STT runs in real time on your DGX Spark and produces stable, segmented
      text. A clean, timely text stream simplifies downstream integration with vLLM.
  - question: What behavior confirms the end-to-end offline chatbot is running?
    answer: >-
      Speak into the microphone and watch for segmented transcriptions from `faster-whisper`, followed
      by a locally generated reply from vLLM. Seeing this sequence consistently indicates the
      pipeline is integrated and running on the system.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
