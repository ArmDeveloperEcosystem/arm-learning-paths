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
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:11:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  summary_generated_at: '2026-08-04T22:11:34Z'
  summary_source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  faq_generated_at: '2026-08-04T22:11:34Z'
  faq_source_hash: f9af4e5e63763a06e375e9f1d3198a4dd613f236d3cda874e7422899b73a262e
  summary: >-
    You build a minimal Android chatbot that runs a local
    GGUF model using Arm’s AI Chat library. You create a new Android Studio project, verify repository
    configuration, and add the library from Maven Central. You then replace the default layout
    with a simple chat UI and implement MainActivity to initialize the library and handle streamed
    chat inference. After downloading a mobile-friendly GGUF model, such as a small Gemma 3 variant,
    you run the app on a device and send prompts to verify end-to-end behavior. You use the library's
    llama.cpp wrapper with Arm CPU optimizations to evaluate on-device chat with a compact, responsive
    interface.
  faqs:
  - question: Where do I add the AI Chat dependency in Gradle?
    answer: >-
      Add the dependency in the app module’s build.gradle.kts file, not the project-level file.
      After saving, sync Gradle to download the library.
  - question: How do I confirm Maven Central is configured so my dependency resolves?
    answer: >-
      Open settings.gradle.kts and ensure the repositories include google() and mavenCentral().
      Sync the project and check that no unresolved dependency errors appear.
  - question: How do I know my layout is set up correctly before I write code?
    answer: >-
      Replace activity_main.xml with the provided layout and run the app. You should see a status
      area, a scrolling message list, and a text input with a Send button.
  - question: Which GGUF model should I download for my phone, and how large can it be?
    answer: >-
      Use a mobile-compatible GGUF model that is significantly smaller than your device’s RAM
      to leave headroom for the system and apps. An example is google_gemma-3-4b-it-Q4_0.gguf.
  - question: What result should I expect after I load the model and send a message?
    answer: >-
      The status area should indicate that the model is ready, and the message list should populate
      with streamed responses. If nothing appears, confirm the model file is accessible and loaded
      without errors.
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
