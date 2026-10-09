---
title: Run an optimized text-to-speech model from the Arm AI Portal on an Arm Neoverse-based instance
description: Run an optimized text-to-speech model with ONNX Runtime on an Arm Neoverse-based machine.
minutes_to_complete: 40

who_is_this_for: This Learning Path is for developers and ML engineers who want to run text-to-speech generation from a browser interface or the terminal with an Arm-optimized Qwen3-TTS model on an Arm Neoverse Linux machine.

learning_objectives:
- Prepare an Arm Neoverse Linux machine and download a model from the Arm AI Portal.
- Generate speech through a browser interface and optionally run the model from the terminal.
- Identify how the web application prepares reference audio, invokes the server runner, and returns WAV audio.

prerequisites:
- An Arm Neoverse-based Linux machine, such as an AWS `r8g.xlarge` instance, running Ubuntu 24.04 LTS and Python 3.11 or later
- At least 32 GB of memory on the Linux machine
- A local development machine with SSH access
- Access to a microphone or an existing voice recording
- Basic familiarity with Linux command-line tools and Python

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-03T17:25:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: false
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3bb4119d064226ffb9f5b2ab798a51bdea84f4d5ebd0f8573ce9ea74ed4a374d
  summary_generated_at: '2026-09-03T17:25:16Z'
  summary_source_hash: 3bb4119d064226ffb9f5b2ab798a51bdea84f4d5ebd0f8573ce9ea74ed4a374d
  faq_generated_at: '2026-09-03T17:25:16Z'
  faq_source_hash: 3bb4119d064226ffb9f5b2ab798a51bdea84f4d5ebd0f8573ce9ea74ed4a374d
  summary: >-
    You'll run an optimized text-to-speech model with ONNX Runtime on an Arm Neoverse-based machine. First, you'll install the required Python dependencies and
    download application files and the Qwen3-TTS ONNX package from the Arm AI Portal. Next, you'll start
    the FastAPI browser application, connect through an SSH tunnel, and record or upload reference audio
    before generating a WAV file from text. You'll learn an optional terminal-based workflow and trace how the application normalizes audio, calls
    the ONNX runner, and returns the result.
  faqs:
  - question: How do I know that the web application started correctly?
    answer: >-
      Check the startup output for the runner, cascade driver, text-path files, FFmpeg, and thread
      count checks. When the service is ready, it listens on `127.0.0.1:8000`.
  - question: How do I provide a reference voice sample?
    answer: >-
      Use the browser application to record a sample or upload an existing reference recording. The
      application converts the audio to the format expected by the server runner.
  - question: What result will I get after generating speech?
    answer: >-
      The server returns a WAV file that speaks the provided text using characteristics of the
      reference voice. You can play the file in the browser or download it.
  - question: How do I access the browser application on the instance?
    answer: >-
      Create an SSH tunnel that forwards port `8000` from the instance to your local computer.
      Then, open `http://127.0.0.1:8000` in your local browser. The application remains bound to the
      instance loopback interface and isn't exposed on a public network interface.
  - question: Can I run the model from the terminal instead of using the browser?
    answer: >-
      Yes. The browser application is a FastAPI wrapper around `onnx_tts_runner.py`. You can invoke
      the runner directly from the terminal with the required inputs and model directory.
# END generated_summary_faq

author: Kwashie Andoh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
- Neoverse
cloud_service_providers:
- AWS
- Google Cloud
- Microsoft Azure
operatingsystems:
- Linux
tools_software_languages:
- Python
- ONNX Runtime
- Hugging Face
- FastAPI
- KleidiAI
- Arm AI Portal
- Generative AI
- Text-to-Speech

further_reading:
- resource:
  title: Arm models on Hugging Face
  link: https://huggingface.co/Arm/models
  type: website
- resource:
  title: ONNX Runtime documentation
  link: https://onnxruntime.ai/docs/
  type: documentation
- resource:
  title: Download files from the Hugging Face Hub
  link: https://huggingface.co/docs/huggingface_hub/guides/download
  type: documentation
- resource:
  title: Qwen3-TTS-12Hz-0.6B-Base model
  link: https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base
  type: website
- resource:
  title: KleidiAI project
  link: https://github.com/ARM-software/kleidiai
  type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
