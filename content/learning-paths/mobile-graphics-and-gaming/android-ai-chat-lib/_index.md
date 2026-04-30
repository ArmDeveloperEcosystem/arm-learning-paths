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
