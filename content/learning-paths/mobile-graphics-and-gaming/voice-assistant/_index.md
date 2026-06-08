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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:11:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 192f5919261cfef88c107576dc444d2db3a07fbad98100d9c758bb75670a5a00
  summary_generated_at: '2026-06-02T03:02:05Z'
  summary_source_hash: 192f5919261cfef88c107576dc444d2db3a07fbad98100d9c758bb75670a5a00
  faq_generated_at: '2026-06-03T00:11:41Z'
  faq_source_hash: 192f5919261cfef88c107576dc444d2db3a07fbad98100d9c758bb75670a5a00
  summary: >-
    Build and run a multimodal Voice Assistant on Android and explore how KleidiAI and SME2 can
    accelerate its performance. You will set up Android Studio and supporting command-line tools
    (cmake, python3, git, adb), clone the Real-Time-Voice-Assistant repository, compile the project
    in Android Studio, and deploy it to a USB-connected phone in developer mode. The application
    implements a Speech-to-Text → LLM (via Llama.cpp) → Text-to-Speech pipeline, with KleidiAI
    micro-kernels and SME2 highlighted for Arm-specific acceleration on supported hardware. Prerequisites
    include an Android phone with i8mm and SME support and a development machine with Android
    Studio. This introductory path takes about 30 minutes and results in a working app and a clear
    understanding of the acceleration points.
  faqs:
  - question: What do I need before starting?
    answer: >-
      An Android phone that supports the i8mm Arm architecture feature and SME (Scalable Matrix
      Extension) instructions, and a development machine with Android Studio installed. This path
      was tested on a Vivo X300 Pro and uses a USB connection to deploy via adb.
  - question: Which command-line tools should I install and why?
    answer: >-
      Install cmake, python3, git, and adb. Python is used by the project to fetch dependencies
      and models, and adb is required to communicate with and control the Android device.
  - question: How do I build the app in Android Studio?
    answer: >-
      Open the downloaded project in Android Studio and click the Make Module VoiceAssistant.app
      button (hammer icon). Android Studio will build the application with the default settings.
  - question: How do I install and run the app on my phone?
    answer: >-
      Enable developer mode on the Android device, connect it via USB, and select it as the target
      in Android Studio. Click Run to transfer and start the application on the phone.
  - question: How are KleidiAI, SME2, and Llama.cpp used in this application?
    answer: >-
      The application combines local LLM inference and speech recognition optimized for Arm CPUs
      using Llama.cpp and the KleidiAI library of tuned micro-kernels. SME support is required
      for SME performance checking, and the path focuses on using KleidiAI and SME2 to accelerate
      the workload on supported devices.
# END generated_summary_faq

author:
    - Arnaud de Grandmaison
    - Nina Drozd

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

