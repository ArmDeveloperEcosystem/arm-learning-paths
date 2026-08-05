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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:55:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  summary_generated_at: '2026-08-05T14:55:05Z'
  summary_source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  faq_generated_at: '2026-08-05T14:55:05Z'
  faq_source_hash: 3450df73511aba125edf46829af77bf3b2303ae89ad761b6492a2b3342bedde2
  summary: >-
    You'll add Dawn WebGPU to a C++ Game Activity project and replace the starter code with a minimal
    renderer. First, you'll create a device and command queue, submit GPU work, and render a 3D object.
    Then, you'll build and run the app on an Android phone, and capture its performance with Streamline to
    verify on-device rendering.
  faqs:
  - question: Which Android Studio template should I choose to start the project?
    answer: >-
      Use the **Game Activity (C++)** template when creating the new project. This template sets up the native
      C++ scaffolding used by the WebGPU renderer.
  - question: Which Android SDK Platform should I install before building?
    answer: >-
      Install Android 14.0 ("UpsideDownCake") from the SDK Platforms tab. 
  - question: After integrating Dawn, which default C++ files should I remove and which new files
      should be present?
    answer: >-
      Delete all files from the top `cpp` directory except `CMakeLists.txt`. Add `webgpuRenderer.cpp`,
      `webgpuRenderer.h`, and the provided `main.cpp` for the WebGPU application.
  - question: How do I get the WebGPU command queue in code?
    answer: >-
      Retrieve the device’s single queue with `wgpuDeviceGetQueue()`, then submit work using
      methods such as `wgpuQueueSubmit`.
  - question: When should I start profiling with Streamline, and what indicates I’m ready?
    answer: >-
      Start a Streamline capture after the app builds and renders the simple 3D object on your
      Android device. When you see the object render without runtime errors, you're ready to
      profile and analyze the data.
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
