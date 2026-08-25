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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:32:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5a896c3cf2c7ba600a260e444bd4d7d1725490c8b3f9e1f53bd9868e918ba03d
  summary_generated_at: '2026-08-21T17:32:04Z'
  summary_source_hash: 5a896c3cf2c7ba600a260e444bd4d7d1725490c8b3f9e1f53bd9868e918ba03d
  faq_generated_at: '2026-08-21T17:32:04Z'
  faq_source_hash: 5a896c3cf2c7ba600a260e444bd4d7d1725490c8b3f9e1f53bd9868e918ba03d
  summary: >-
    You'll run the Qwen2.5-VL-3B-Instruct-MNN vision model on an Android device with MNN and KleidiAI.
    First, you'll install the Android tools, download a pre-quantized MNN model, and build the Android Studio
    demo. Then, you'll prepare an image, build and run the MNN command-line demo, enable KleidiAI,
    rebuild the binaries, and compare the reported benchmark timings.
  faqs:
  - question: Which NDK and CMake do I need, and how do I install them?
    answer: >-
      To match the tested setup, use Android NDK `28.0.12916984` and CMake `4.0.0-rc1`. In Android
      Studio, select **Tools > SDK Manager**, open **SDK Tools**, then select **NDK (Side by side)**
      and **CMake**. On Ubuntu or Debian, install `cmake` and `git-lfs` with the provided command.
  - question: How do I clone and open the project in Android Studio?
    answer: >-
      Run `git clone https://gitlab.arm.com/kleidi/kleidi-examples/vision-language-models`. In Android
      Studio, select **File > Open**, choose the `vision-language-models` directory, and select
      **Open**. Android Studio then builds the project.
  - question: Where should I put the example image and what name should it have?
    answer: >-
      Rename the image to `example.png`, then run `adb push example.png /data/local/tmp/` to copy
      it to your device.
  - question: How do I compare inference with and without KleidiAI micro-kernels?
    answer: >-
      Build and run the MNN command-line demo without KleidiAI first. Then add the
      `CPU_ENABLE_KLEIDIAI` runtime hint, rebuild the binaries, replace them on your device, and
      run the same inference command again to compare the reported timings.
  - question: When is the model converted to MNN, and how do I know it worked?
    answer: >-
      Model conversion is optional. By default, you download the pre-quantized
      `Qwen2.5-VL-3B-Instruct-MNN` model. If you convert the model with `llmexport`, verify that
      the `Qwen2.5-VL-3B-Instruct-convert-4bit-64qblock` directory is at least 2 GB.
# END generated_summary_faq

author:
    - Shuheng Deng
    - Yiyang Fan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
