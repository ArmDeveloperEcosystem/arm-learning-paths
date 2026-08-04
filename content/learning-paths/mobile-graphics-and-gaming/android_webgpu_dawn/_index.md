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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:14:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  summary_generated_at: '2026-08-04T22:14:57Z'
  summary_source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  faq_generated_at: '2026-08-04T22:14:57Z'
  faq_source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  summary: >-
    You set up an Android C++ Game Activity project, integrate
    the Dawn WebGPU implementation, and using WebGPU APIs to render a simple 3D object on an Android
    device. You learn core WebGPU concepts, including the device’s single command queue and
    the workflow for submitting GPU work after obtaining the queue with wgpuDeviceGetQueue. You
    restructure the stock project, add a dedicated WebGPU renderer, build, deploy, and verify
    on a physical device. You then profile the running app using Arm Streamline
    from Arm Performance Studio and review the collected data to validate rendering
    behavior and inspect GPU activity for the sample.
  faqs:
  - question: Which Android Studio template should I use to create the project?
    answer: >-
      Select Game Activity (C++) when creating the new project. Use the provided project name
      and defaults as instructed in the steps.
  - question: When preparing the C++ sources, which default files should I remove and which should
      I add?
    answer: >-
      Delete all files in the top-level cpp directory except CMakeLists.txt. Then add main.cpp
      and the WebGPU renderer sources (webgpuRenderer.cpp and webgpuRenderer.h).
  - question: How do I know the WebGPU device and queue are initialized correctly?
    answer: >-
      Initialization is correct when the app builds and runs without errors and you can obtain
      a valid queue from the device using wgpuDeviceGetQueue. If initialization fails, review
      the integration and file changes from the previous step.
  - question: Which Android SDK Platform should I install during setup?
    answer: >-
      Install Android 14.0 (UpsideDownCake) from the Android SDK Platforms tab. Also follow the
      steps to install the required NDK from the SDK Tools tab.
  - question: What should I check before profiling the app with Streamline?
    answer: >-
      Confirm the app runs on your Android device in developer mode and that Arm Performance Studio
      is installed. Launch the app first, then start a Streamline capture to collect profiling
      data.
# END generated_summary_faq

author:
    - Varun Chari
    - Albin Bernhardsson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
