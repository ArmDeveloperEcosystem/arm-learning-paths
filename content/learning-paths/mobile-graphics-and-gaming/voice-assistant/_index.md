---
title: Accelerate multimodal Voice Assistant performance with KleidiAI and SME2
description: Learn how to build and optimize a multimodal Voice Assistant application on Android using KleidiAI and SME2 for accelerated performance.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to implement a multimodal pipeline for a Voice Assistant application and accelerate the performance on Android devices using KleidiAI and SME2.

learning_objectives:
    - Learn about the multimodal Voice Assistant pipeline and different components used.
    - Learn about the functionality of ML components used and how these can be built and benchmarked on various platforms.
    - Compile and run a multimodal Voice Assistant example based on Android OS.
    - Optimize performance of multimodal Voice Assistant using KleidiAI and SME2.

prerequisites:
    - An Android phone that supports the i8mm Arm architecture feature (8-bit integer matrix multiplication).
    - An Android phone with support for SME (Scalable Matrix Extension) instructions, required for SME performance checking
    - This Learning Path was tested on a Vivo X300 Pro.
    - A development machine with [Android Studio](https://developer.android.com/studio) installed.
    - Arm Performance Studio installed. Follow the [Arm Performance Studio install guide](/install-guides/ams/) for instructions.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:32:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8e6a05c4319dc6172fc36446a8bc4e64a67790d6da2b4bbe05f36df5169e1ec9
  summary_generated_at: '2026-08-21T17:32:43Z'
  summary_source_hash: 8e6a05c4319dc6172fc36446a8bc4e64a67790d6da2b4bbe05f36df5169e1ec9
  faq_generated_at: '2026-08-21T17:32:43Z'
  faq_source_hash: 8e6a05c4319dc6172fc36446a8bc4e64a67790d6da2b4bbe05f36df5169e1ec9
  summary: >-
    You'll build and run a multimodal Voice Assistant on an Android device, then compare and profile its
    LLM performance with KleidiAI and SME2. First, you'll install Android Studio and command-line dependencies,
    clone and build the app, and deploy it to your phone. Then, you'll use its speech-to-text, local LLM,
    and Android text-to-speech pipeline, benchmark LLMs with and without SME2, and use Arm Streamline
    to inspect performance.
  faqs:
  - question: How do I know Android Studio can deploy the app to my phone?
    answer: >-
      Enable developer mode, connect your phone with USB, and confirm that it appears as a running
      device in the Android Studio toolbar. Select the device, then select **Run** to install and
      launch the Voice Assistant.
  - question: What should I check if the build
      fails?
    answer: >-
      If the build fails while downloading, verify that `python3` version 3.9 or later and `git`
      are installed, then try the Android Studio build again. The first build might take longer
      while it downloads additional dependencies.
  - question: What result should I expect when I run the Voice Assistant?
    answer: >-
      Tap **Press to talk** in Chat mode and speak your request. The app transcribes your audio,
      sends the text to its LLM, and displays the response. To hear the response, enable **Speech
      generation**, which is disabled by default.
  - question: Do I need to change any settings to use KleidiAI in this project?
    answer: >-
      On Arm platforms, the default build includes KleidiAI support. To compare against a build
      without it, add `-PkleidiAI=false` to `./gradlew build` or set `kleidiAI=false` in `gradle.properties`.
  - question: How can I check SME2-related behavior or performance on my device?
    answer: >-
      To compare SME2 performance, build the LLM benchmark once with `-DMNN_SME2=OFF` and again
      without that setting, which enables SME instructions by default. You can also capture a
      profile in Arm Streamline to confirm SME2 kernel activity during LLM execution.
# END generated_summary_faq

author:
    - Arnaud de Grandmaison
    - Nina Drozd

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - Java
    - Kotlin
    - CPP
    - SME2
    - Arm Performance Studio
operatingsystems:
    - Android
    - Linux
    - macOS

further_reading:

    - resource:
        title: Accelerate Generative AI workloads using KleidiAI
        link: /learning-paths/cross-platform/kleidiai-explainer
        type: website

    - resource:
        title: LLM inference on Android with KleidiAI, MediaPipe, and XNNPACK
        link: /learning-paths/mobile-graphics-and-gaming/kleidiai-on-android-with-mediapipe-and-xnnpack/
        type: website

    - resource:
        title: Vision LLM inference on Android with KleidiAI and MNN
        link: /learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
