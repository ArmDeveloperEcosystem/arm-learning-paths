---
title: Build a Sentiment-Aware Voice Assistant with On-Device LLMs

description: Build an end-to-end, on-device voice assistant that understands both speech and emotion using Whisper, HuBERT, ONNX Runtime, and a local LLM with llama.cpp on Arm.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers, ML practitioners, and game developers interested in building on-device AI applications, including voice interfaces, real-time interactions with non-player characters (NPCs), and edge AI systems powered by LLMs on Arm platforms.


learning_objectives:
    - Build a voice-to-LLM pipeline using Whisper and llama.cpp.
    - Train a voice sentiment classification model using HuBERT on the RAVDESS dataset.
    - Quantize the model and convert into ONNX Runtime for on-device inference.
    - Integrate sentiment classification model with voice-to-LLM pipeline to generate context-aware LLM responses.

prerequisites:
    - Python 3.9 or later for programming.
    - A working microphone for voice input.
    - Basic Python and command-line knowledge.

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 2d8fca8838e759c3098358f131fb4b0884b0d80d5fdb2fd68719bd09fa4c3d32
  summary: >-
    Build an end-to-end, on-device voice assistant that understands both speech and emotion using
    Whisper, HuBERT, ONNX Runtime, and a local LLM with llama.cpp on Arm. It is designed for developers,
    ML practitioners, and game developers interested in building on-device AI applications, including
    voice interfaces, real-time interactions with non-player characters (NPCs), and edge AI systems
    powered by LLMs on Arm platforms. By the end, you will be able to build a voice-to-LLM pipeline
    using Whisper and llama.cpp, train a voice sentiment classification model using HuBERT on
    the RAVDESS dataset, and quantize the model and convert into ONNX Runtime for on-device inference.
    It focuses on tools and technologies such as Python, Transformers, ONNX Runtime, llama.cpp,
    and Gradio, Linux, Windows, and macOS environments, and Arm platforms including Cortex-A.
    The main steps cover Understand voice sentiment analysis for on-device AI, Set up your environment,
    Build the voice-to-LLM pipeline, Train the voice sentiment classification model, and Convert
    and quantize the model.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build a voice-to-LLM pipeline using Whisper and llama.cpp, train a voice sentiment
      classification model using HuBERT on the RAVDESS dataset, and quantize the model and convert
      into ONNX Runtime for on-device inference. Build an end-to-end, on-device voice assistant
      that understands both speech and emotion using Whisper, HuBERT, ONNX Runtime, and a local
      LLM with llama.cpp on Arm.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for developers, ML practitioners, and game developers interested in
      building on-device AI applications, including voice interfaces, real-time interactions with
      non-player characters (NPCs), and edge AI systems powered by LLMs on Arm platforms.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Python 3.9 or later for programming.;
      A working microphone for voice input.; Basic Python and command-line knowledge.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, Transformers, ONNX Runtime, llama.cpp, and
      Gradio, Linux, Windows, and macOS environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand voice sentiment analysis for on-device
      AI, Set up your environment, Build the voice-to-LLM pipeline, Train the voice sentiment
      classification model, and Convert and quantize the model.
# END generated_summary_faq

author: Bhanu Arya

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
    - Windows
    - macOS
tools_software_languages:
    - Python
    - Transformers
    - ONNX Runtime
    - llama.cpp
    - Gradio

further_reading:
    - resource:
        title: Whisper model docs
        link: https://github.com/openai/whisper
        type: documentation
    - resource:
        title: llama.cpp
        link: https://github.com/ggml-org/llama.cpp
        type: documentation
    - resource:
        title: ONNX Runtime quantization
        link: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
        type: documentation
    - resource:
        title: "Multimodal Sentiment Analysis: A Survey"
        link: https://arxiv.org/abs/2305.07611
        type: research paper

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

