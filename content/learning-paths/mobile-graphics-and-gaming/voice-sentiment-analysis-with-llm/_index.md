---
title: Build a Sentiment-Aware Voice Assistant with On-Device LLMs

draft: true
cascade:
    draft: true

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
