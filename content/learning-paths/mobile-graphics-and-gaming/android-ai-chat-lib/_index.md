---
title: Add an LLM to your Android app with Arm's AI Chat library
description: Learn how to build an Android chatbot app using Arm's AI Chat library to run GGUF models on-device with optimized performance on Arm CPUs.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to add a local, on-device LLM chat experience using Arm's AI Chat library, Kotlin, and Android Studio.

learning_objectives: 
    - Create a simple Android chatbot app scaffold in Android Studio
    - Load a mobile-friendly GGUF model on-device and run streamed chat inference

prerequisites:
    - An Android development environment with Android Studio installed
    - An Android phone for testing, in Developer Mode, with USB cable for connection
    - Basic familiarity with Kotlin and Android app development

# START generated_summary_faq

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:51:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  summary_generated_at: '2026-08-05T14:51:09Z'
  summary_source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  faq_generated_at: '2026-08-05T14:51:09Z'
  faq_source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  summary: >-
    You'll build a minimal Android chatbot that runs a local `GGUF` model with Arm’s AI Chat library.
    First, you'll configure the Android Studio project, add the Maven dependency, and create a chat
    UI. Then, you'll connect the `MainActivity` class to load a mobile-friendly model and stream responses. Finally, you'll download
    a `GGUF` model file on the device and run the app to verify on-device output.
  faqs:
  - question: Which Gradle file should I edit to add the AI Chat dependency?
    answer: >-
      Add the dependency in the app module’s `build.gradle.kts`, not the project-level `build.gradle.kts`.
      Place the implementation for `com.arm:ai-chat:0.1.0` in the dependencies block.
  - question: How do I check my repository configuration so the library resolves?
    answer: >-
      Open `settings.gradle.kts` and confirm the top-level repositories include `google()` and `mavenCentral()`.
      With both present, you can resolve the AI Chat library from Maven Central.
  - question: Which layout file do I replace for the chat UI?
    answer: >-
      Replace `activity_main.xml` in `app/src/main/res/layout` with the provided XML. The XML defines a
      status area, a message list, and a text input with a send button.
  - question: How do I choose a GGUF model that fits my device?
    answer: >-
      Select a model that is significantly smaller than your phone’s available RAM. A mobile-friendly
      example is `google_gemma-3-4b-it-Q4_0.gguf`, a Q4_0‑quantized Gemma 3 4B model that works
      well with Arm’s KleidiAI and benefits devices with SME2, SVE2, or Neon capabilities.
  - question: What result should I expect when I run the app?
    answer: >-
      After you provide the `GGUF` file on the device, you should see the app load the model and stream
      chat responses into the message list. Check the status area during generation to confirm
      progress.
# END generated_summary_faq

author: Ben Clark

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Arm AI Chat library
tools_software_languages:
    - Kotlin
    - Neon
    - SVE2
    - SME2
    - LLM
operatingsystems:
    - Android

further_reading:
    - resource:
        title: AI Chat - Explore and evaluate LLMs on Android and ChromeOS
        link: https://developer.arm.com/community/arm-community-blogs/b/announcements/posts/ai-chat-explore-and-evaluate-llms-on-android-and-chromeos
        type: blog    
    - resource:
        title: Arm AI Chat LLM test app 
        link: https://play.google.com/store/apps/details?id=com.arm.aichat
        type: example app    
    - resource:
        title: AI Chat library @ Maven Central
        link: https://central.sonatype.com/artifact/com.arm/ai-chat
        type: documentation
    - resource:
        title: AI Chat library on GitHub
        link: https://github.com/arm/ai-chat
        type: website
    - resource:
        title: Arm KleidiAI - Helping AI frameworks elevate their performance on Arm CPUs
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/kleidiai
        type: blog
    - resource:
        title: SME2
        link: https://www.arm.com/technologies/sme2
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
