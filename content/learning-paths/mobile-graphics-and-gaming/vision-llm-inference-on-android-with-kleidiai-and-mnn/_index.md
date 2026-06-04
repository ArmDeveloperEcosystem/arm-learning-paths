---
title: Run Vision LLM inference on Android with KleidiAI and MNN
description: Learn how to download, convert, and deploy Vision Transformers using the Mobile Neural Network framework on Android with KleidiAI micro-kernels for optimized performance.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to run Vision Transformers (ViT) efficiently on Android.

learning_objectives:
    - Download a Vision Large Language Model (LLM) from Hugging Face.
    - Convert the model to the Mobile Neural Network (MNN) framework.
    - Install an Android demo application using the model to run an inference.
    - Compare inference performance with and without KleidiAI Arm-optimized micro-kernels.


prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed.
    - A smartphone running Android with support for `i8mm` and `dotprod` instructions.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:11:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e7d95c8e7210be2fe4520fe94ccbaa3e437cd0edfa5caca549afaee22fb8b377
  summary_generated_at: '2026-06-02T03:01:36Z'
  summary_source_hash: e7d95c8e7210be2fe4520fe94ccbaa3e437cd0edfa5caca549afaee22fb8b377
  faq_generated_at: '2026-06-03T00:11:12Z'
  faq_source_hash: e7d95c8e7210be2fe4520fe94ccbaa3e437cd0edfa5caca549afaee22fb8b377
  summary: >-
    This Learning Path guides you through running Vision Transformer (ViT) inference on Android
    using the Mobile Neural Network (MNN) framework and KleidiAI micro-kernels. You will download
    a Vision LLM from Hugging Face, prepare the Qwen vision model, convert it to MNN, and build
    a demo Android app from the Vision Language Models repository in Android Studio to create
    an APK. You also compile command-line binaries, push an example image to the device with adb,
    and run inference. Finally, you benchmark runs with and without KleidiAI kernels to compare
    performance. Prerequisites include Android Studio and an Android smartphone with i8mm and
    dotprod support. The path is introductory and takes about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Android Studio installed on your development machine and a smartphone running Android
      that supports i8mm and dotprod instructions. No other prerequisites are explicitly listed.
  - question: Which NDK and CMake versions are used, and how do I install them?
    answer: >-
      This path was tested with NDK 28.0.12916984 and CMake 4.0.0-rc1. Install the NDK via Android
      Studio (Tools > SDK Manager > SDK Tools > NDK (Side by side)), and on Ubuntu/Debian install
      CMake and git‑lfs with: sudo apt update and sudo apt install cmake git-lfs -y.
  - question: Where do I get the source code for the Android demo app?
    answer: >-
      Clone the examples repository with: git clone https://gitlab.arm.com/kleidi/kleidi-examples/vision-language-models.
      Open the project in Android Studio and build to generate an APK.
  - question: How is the model prepared for use with MNN?
    answer: >-
      You will download a Vision LLM from Hugging Face and convert it to the MNN format. The setup
      steps prepare the Qwen vision model as part of this process.
  - question: How do I run the benchmark and what input image should I use?
    answer: >-
      Build the command-line ViT demo and prepare an example image named example.png. Push it
      to the device with adb push example.png /data/local/tmp, then follow the steps to compare
      inference runs with and without KleidiAI micro-kernels.
# END generated_summary_faq

author:
    - Shuheng Deng
    - Yiyang Fan

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - KleidiAI
operatingsystems:
    - Android



further_reading:
    - resource:
        title: "MNN: A Universal and Efficient Inference Engine"
        link: https://arxiv.org/pdf/2002.12418
        type: documentation
    - resource:
        title: MNN-Doc
        link: https://mnn-docs.readthedocs.io/en/latest/
        type: blog
    - resource:
        title: Vision transformer
        link: https://en.wikipedia.org/wiki/Vision_transformer
        type: website
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

