---
title: Build and profile a simple WebGPU Android Application
description: Learn how to integrate Dawn WebGPU in an Android application, render 3D objects, and profile the application using Streamline.
cascade:
minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who are building GPU-based Android applications and are interested in experimenting with WebGPU. 

learning_objectives: 
    - Describe the benefits of WebGPU.
    - Describe the benefits of using Dawn.
    - Set up a WebGPU development environment.
    - Integrate Dawn in an Android Application.
    - Use Dawn WebGPU APIs in the application.
    - Describe the changes required to upgrade to WebGPU to render a simple 3D object.
    - Build and run a WebGPU Android Application.
    - Profile the application using Streamline.
    - Analyze the profiling data.
       
prerequisites:
    - Basic knowledge of graphics APIs and experience in developing Android graphics applications.
    - A development machine with Android Studio, Blender, and Arm Streamline installed.
    - An Android phone in developer mode.
    - Android Studio.
    - Arm Performance Studio.
    - Python 3.10 or later.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:47:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8f58429f12e40b53e8a2e0d7eb260f22fbb7ac869ca64554a906ddcd28c9fd75
  summary_generated_at: '2026-06-02T02:44:35Z'
  summary_source_hash: 8f58429f12e40b53e8a2e0d7eb260f22fbb7ac869ca64554a906ddcd28c9fd75
  faq_generated_at: '2026-06-02T23:47:07Z'
  faq_source_hash: 8f58429f12e40b53e8a2e0d7eb260f22fbb7ac869ca64554a906ddcd28c9fd75
  summary: >-
    This Learning Path shows how to integrate Dawn WebGPU into a C++-based Android Game Activity,
    render a simple 3D object using WebGPU APIs, and profile the application with Arm Streamline.
    You will set up a development environment on macOS, Linux, or Windows with Android Studio
    (including the NDK), Arm Performance Studio, Blender, and Python 3.10, and use an Android
    phone in developer mode. The steps introduce WebGPU fundamentals, create and configure the
    Android Studio project, add Dawn and renderer sources, build and run the app, and capture
    and analyze profiling data. By the end, you have a working WebGPU Android application and
    a Streamline capture to review.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need Android Studio, Arm Performance Studio, Python 3.10 or later, and Blender installed
      on your development machine. You also need an Android phone in developer mode. Basic knowledge
      of graphics APIs and experience developing Android graphics applications are expected.
  - question: Which Android Studio project template should I start with?
    answer: >-
      Create a new project using the Game Activity (C++) template. Name the project dawnwebgpu
      and accept the default selections until the project is created in ~/AndroidStudioProjects.
  - question: How should I set up the Android SDK and NDK for this project?
    answer: >-
      Install the latest Android Studio and the Android NDK. In Settings > Languages & Frameworks
      > Android SDK, enable the Android 14.0 (UpsideDownCake) platform, then use the SDK Tools
      tab to install the required tools including the NDK.
  - question: After integrating Dawn, which project files do I keep or add?
    answer: >-
      Delete all files from the top-level cpp directory except CMakeLists.txt. Add webgpuRenderer.cpp
      and webgpuRenderer.h, and use the provided commands to copy in a new main.cpp and the WebGPU
      renderer files.
  - question: When should I profile the app with Streamline and what is the expected outcome?
    answer: >-
      After the application builds and runs on your Android device, use Arm Performance Studio’s
      Streamline to profile it. You will capture and analyze profiling data to understand the
      app’s behavior as described in the steps.
# END generated_summary_faq

author:
    - Varun Chari
    - Albin Bernhardsson

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Cortex-A
tools_software_languages:
    - Java
    - Kotlin
    - CPP
    - Python
operatingsystems:
    - macOS
    - Linux
    - Windows
    - Android


further_reading:
    - resource:
        title: WebGPU example application
        link: https://github.com/varunchariArm/Android_DawnWebGPU
        type: website
    - resource:
        title: WebGPU working draft
        link: https://www.w3.org/TR/webgpu/
        type: website
    - resource:
        title: Dawn Github repository
        link: https://github.com/google/dawn
        type: website
    - resource:
        title: WebGPU API
        link: https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API
        type: website
    - resource:
        title: WebGPU fundamentals 2
        link: https://webgpufundamentals.org/
        type: website
    - resource:
        title: Learn WebGPU 
        link: https://eliemichel.github.io/LearnWebGPU/index.html
        type: website
    - resource:
        title: WebGPU examples 2
        link: https://github.com/samdauwe/webgpu-native-examples
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

