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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:33:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4c689371fcca5a0bdf2d9750733f6c8f70e73ddaee8d26c612d5534e3b37618d
  summary_generated_at: '2026-08-21T17:33:32Z'
  summary_source_hash: 4c689371fcca5a0bdf2d9750733f6c8f70e73ddaee8d26c612d5534e3b37618d
  faq_generated_at: '2026-08-21T17:33:32Z'
  faq_source_hash: 4c689371fcca5a0bdf2d9750733f6c8f70e73ddaee8d26c612d5534e3b37618d
  summary: >-
    You'll build a sentiment-aware voice assistant that runs on-device on Arm. First, you'll prepare a UV-managed
    Python environment, build `llama.cpp`, and create a Gradio pipeline that transcribes microphone
    audio with Whisper and sends it to a local LLM. You'll train a HuBERT classifier on selected
    RAVDESS sentiments, export and quantize it to ONNX, then add its prediction to the LLM prompt
    and user interface.
  faqs:
  - question: How do I know the baseline voice-to-LLM pipeline is working?
    answer: >-
      Record audio and confirm that the interface displays both a transcript and the local LLM
      response. This verifies that Whisper transcription and the LLM request are working.
  - question: Do I need `ffmpeg` installed before using Whisper?
    answer: >-
      Yes. Install `ffmpeg` before running the transcription step because Whisper needs it to decode audio.
  - question: Where do I save the trained HuBERT model and feature extractor?
    answer: >-
      After training, save the HuBERT model and its feature extractor in `models/hubert_vsa_ravdess`.
      Train it on the selected RAVDESS classes: neutral, happy, and angry. You use those files
      in the ONNX export step.
  - question: How is sentiment used with the LLM, and how can I verify it’s included?
    answer: >-
      Add the predicted sentiment to the prompt in `handle_audio` before sending it to the local
      LLM. To verify the integration, run `app.py` and confirm that you see a transcript, predicted
      sentiment, and LLM response.
  - question: What should I check if ONNX export or quantization fails?
    answer: >-
      Ensure the trained model from the previous step exists and loads correctly; ONNX export
      can take a few seconds. After success, you should have an exported ONNX model and a quantized
      version ready for on-device inference.
# END generated_summary_faq

author: Bhanu Arya

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
