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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:12:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2d8fca8838e759c3098358f131fb4b0884b0d80d5fdb2fd68719bd09fa4c3d32
  summary_generated_at: '2026-06-02T03:02:45Z'
  summary_source_hash: 2d8fca8838e759c3098358f131fb4b0884b0d80d5fdb2fd68719bd09fa4c3d32
  faq_generated_at: '2026-06-03T00:12:36Z'
  faq_source_hash: 2d8fca8838e759c3098358f131fb4b0884b0d80d5fdb2fd68719bd09fa4c3d32
  summary: >-
    Build an end-to-end, on-device voice assistant on Arm that understands both speech and emotion.
    You will set up an isolated Python environment (Linux, Windows, or macOS), install dependencies
    including ffmpeg for Whisper, and create a baseline pipeline that records from a microphone,
    transcribes with Whisper, and queries a locally hosted LLM via llama.cpp. You then train a
    HuBERT-based sentiment classifier on the RAVDESS dataset (neutral, happy, angry), export the
    model to ONNX, and apply post-training quantization for on-device inference with ONNX Runtime.
    Finally, you integrate sentiment inference into the voice-to-LLM flow to generate context-aware
    responses. Prerequisites include Python 3.9+, a working microphone, and basic Python/CLI skills.
    Estimated time: 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Python 3.9 or later, a working microphone, and basic Python and command-line knowledge.
      No other prerequisites are explicitly listed.
  - question: Which operating systems are supported, and how should I set up the environment?
    answer: >-
      The instructions support Ubuntu, macOS, and Windows. You will create a project workspace
      and use an isolated UV environment, and install required system tools first; ffmpeg is required
      by Whisper for audio decoding.
  - question: What result should I expect when the baseline voice-to-LLM pipeline is working?
    answer: >-
      After recording audio from your microphone, Whisper transcribes it to text and sends the
      text to a locally hosted LLM. You should see the model’s response displayed.
  - question: Which dataset and sentiment labels are used for training the classifier?
    answer: >-
      Training uses the RAVDESS dataset with three sentiment classes: neutral, happy, and angry.
      The same approach can be extended to more classes or other datasets.
  - question: How do I verify the ONNX conversion and quantization steps?
    answer: >-
      You should obtain an exported ONNX model and a quantized version with reduced file size
      for on-device inference with ONNX Runtime. If export fails, ensure the trained HuBERT checkpoint
      from the previous section exists and can be loaded; ONNX export may take a few seconds.
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

