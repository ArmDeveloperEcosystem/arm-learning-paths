---
title: Run an optimized vision-language model from the Arm AI Portal on Android
description: Run the Arm-optimized Qwen3-VL model locally with llama.cpp to generate text from an image and prompt on Android.

minutes_to_complete: 35

who_is_this_for: This Learning Path is for Android and machine learning developers who want to run an optimized vision-language model locally on an Arm-based Android device.

learning_objectives:
    - Prepare the Android command-line tools and connect an Arm-based Android phone.
    - Download and run the supported Qwen3-VL model package from the Arm AI Portal.
    - Trace how Vision Chat validates and extracts the model package ZIP, prepares an image and prompt, runs llama.cpp, and generates text.
    - Interpret model-load, image-and-prompt, and token-generation measurements on a physical phone.

prerequisites:
    - A macOS, Linux, or Windows development machine
    - An Arm-based Android phone with Android 9 or later, `asimddp` and `i8mm` CPU features, and at least 4 GB of free storage
    - Basic familiarity with terminal commands and Android applications
    - Git installed on the development machine
    - Python 3 with the `venv` and `pip` modules on the machine
    - Java Development Kit (JDK) 17 or later on the machine, available on your `PATH`
    - A tool for downloading files and a tool for extracting ZIP archives on the machine
    - A data-capable USB cable
    - A Hugging Face account
    - Network access for the first Gradle build and model downloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-22T18:51:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 69d627a35fb1ebe0259bdf6e614a735170c01dbc1331043247a9c3e90f8c1c51
  summary_generated_at: '2026-09-22T18:51:54Z'
  summary_source_hash: 69d627a35fb1ebe0259bdf6e614a735170c01dbc1331043247a9c3e90f8c1c51
  faq_generated_at: '2026-09-22T18:51:54Z'
  faq_source_hash: 69d627a35fb1ebe0259bdf6e614a735170c01dbc1331043247a9c3e90f8c1c51
  summary: >-
    You'll prepare Android command-line tools, build Vision Chat, and run an Arm-optimized Qwen3-VL
    model locally on an Arm-based Android phone. First, you'll install the required SDK packages, connect a
    compatible phone, and build the application with llama.cpp. You'll then download and import the
    supported model package before generating text from an image and prompt. Finally, you'll trace
    package validation, multimodal inference, Arm CPU kernel selection, and timing measurements.
  faqs:
  - question: How do I confirm that my Android phone is connected and authorized for debugging?
    answer: >-
      Run `adb devices -l` and confirm that your phone appears as an authorized device. If you see
      `unauthorized`, unlock your phone, accept the USB debugging prompt, and run the command again.
      If your phone doesn't appear, see [Run apps on a hardware
      device](https://developer.android.com/studio/run/device).
  - question: Which model ZIP should I use with Vision Chat?
    answer: >-
      Use the supported Qwen3-VL 2B Instruct package from the Arm AI Portal. You'll get one GGUF file
      for the language model and one for the vision projector, both targeting llama.cpp. When you
      import the ZIP, Vision Chat validates both files before extracting them.
  - question: What do I need to provide to run a vision-language inference?
    answer: >-
      Provide one image and a text prompt. After you import the model package, select **Choose a
      photo** and choose an image. Enter your prompt, then select **Ask Qwen3-VL** to generate text
      locally on your phone.
  - question: What result should I expect after running Vision Chat?
    answer: >-
      You'll receive generated text based on your selected image and prompt. You'll also see the
      model-load time, image-and-prompt evaluation time, output-token count, and decode speed
      measured on your phone.
  - question: Why does the model package contain two GGUF files?
    answer: >-
      The ZIP you import contains two GGUF files because llama.cpp separates the language model
      from the vision encoder and projector. When you run inference, Vision Chat loads the `Q4_K_M`
      language-model GGUF and the matching `Q8_0` `mmproj` GGUF together.
# END generated_summary_faq

author: Matt Cossins

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
    - Java
    - C++
    - llama.cpp
    - KleidiAI
    - Arm AI Portal
    - Hugging Face
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: Arm AI Portal model catalog
        link: https://developer.arm.com/ai/models
        type: documentation
    - resource:
        title: Qwen3-VL 2B Instruct model package
        link: https://huggingface.co/Arm/qwen3-vl-2b-instruct-q4-k-m-ggml-llama-cpp-vivo-x300
        type: documentation
    - resource:
        title: llama.cpp multimodal documentation
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/mtmd
        type: documentation
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
