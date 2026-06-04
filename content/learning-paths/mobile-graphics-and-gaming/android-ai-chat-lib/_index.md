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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:42:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e63ac917c218aa5e5981f96a9821567d0f8ba9761d5ce6e4c9d7b6dea7ed5c5f
  summary_generated_at: '2026-06-02T02:41:57Z'
  summary_source_hash: e63ac917c218aa5e5981f96a9821567d0f8ba9761d5ce6e4c9d7b6dea7ed5c5f
  faq_generated_at: '2026-06-02T23:42:41Z'
  faq_source_hash: e63ac917c218aa5e5981f96a9821567d0f8ba9761d5ce6e4c9d7b6dea7ed5c5f
  summary: >-
    Build a simple Android chatbot app that runs a local LLM on-device using Arm’s AI Chat library.
    You will create a new Android Studio project, verify google() and mavenCentral() repositories,
    add the library dependency, design a basic chat UI, and implement MainActivity in Kotlin to
    load a GGUF model and stream chat responses. The library wraps llama.cpp with Arm CPU optimizations
    for GGUF models. You will download a mobile-friendly GGUF, such as google_gemma-3-4b-it-Q4_0.gguf,
    sized for your device and run the app on a physical Android phone in Developer Mode. Prerequisites
    include Android Studio, a USB-connected Android phone, and basic familiarity with Kotlin and
    Android app development. Reference implementations include the Arm AI Chat app on Google Play.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Install Android Studio, have an Android phone in Developer Mode with a USB cable, and be
      comfortable with basic Kotlin and Android app development. No other prerequisites are explicitly
      listed.
  - question: Which repositories should be in settings.gradle.kts to resolve the AI Chat library?
    answer: >-
      Ensure the top-level repositories include google() and mavenCentral(). This allows Gradle
      to find the AI Chat library from Maven Central.
  - question: Where do I add the AI Chat dependency and what is the coordinate?
    answer: >-
      Add the dependency in the app module’s build file (app/build.gradle.kts), not the project-level
      file. Use implementation "com.arm:ai-chat:0.1.0".
  - question: How do I choose a mobile-compatible GGUF model, and is there an example?
    answer: >-
      Pick a model that is significantly smaller than your device’s RAM to leave room for the
      OS and other apps. A good example provided is google_gemma-3-4b-it-Q4_0.gguf.
  - question: What result should I expect when I run the app, and how do I know it’s working?
    answer: >-
      The app should load your selected GGUF model on-device and produce streamed chat responses
      in the UI. If the build cannot resolve the library, re-check that google() and mavenCentral()
      are configured and that the dependency was added to app/build.gradle.kts.
# END generated_summary_faq

author: Ben Clark

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

