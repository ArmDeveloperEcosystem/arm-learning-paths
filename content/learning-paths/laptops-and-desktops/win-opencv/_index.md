---
title: Create OpenCV applications on Windows on Arm

description: Learn how to build the OpenCV library for Windows on Arm devices and develop computer vision applications using OpenCV.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to build and develop applications on Windows on Arm devices using OpenCV.

learning_objectives: 
    - Build the OpenCV library for Windows on Arm devices.
    - Develop applications using OpenCV.

prerequisites:
    - A Windows on Arm machine such as the Lenovo Thinkpad X13s, or an [Azure virtual machine](/learning-paths/cross-platform/woa_azure/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:13:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d24bf30aef690451942789bb66df63b7a3483ecc3cd2c4b3e60ce15fad90cb91
  summary_generated_at: '2026-06-01T22:10:09Z'
  summary_source_hash: d24bf30aef690451942789bb66df63b7a3483ecc3cd2c4b3e60ce15fad90cb91
  faq_generated_at: '2026-06-02T23:13:24Z'
  faq_source_hash: d24bf30aef690451942789bb66df63b7a3483ecc3cd2c4b3e60ce15fad90cb91
  summary: >-
    This Learning Path shows how to build the OpenCV library from source on Windows on Arm and
    create a small test application using either MSVC or Clang. You will work on a Windows on
    Arm machine or an Azure virtual machine, install CMake and Git, and, for the MSVC route, use
    Visual Studio 2022 or higher. The steps clone the OpenCV repository and build version 4.10.0
    with CMake from the command line. By the end, you will have a working OpenCV build on Windows
    on Arm and a C++ application linked against it. No additional prerequisites are explicitly
    listed. The estimated time to complete is about 90 minutes.
  faqs:
  - question: What do I need before building OpenCV on Windows on Arm?
    answer: >-
      You need a Windows on Arm machine such as the Lenovo Thinkpad X13s, or an Azure virtual
      machine. Install CMake (tested with 3.28.1) and Git for Windows on Arm. For the MSVC flow,
      install Visual Studio 2022 or higher; Clang is used in the alternative flow.
  - question: Which compiler should I use, MSVC or Clang?
    answer: >-
      This Learning Path includes separate sections for MSVC and Clang. Choose one compiler and
      follow the corresponding steps to build OpenCV and the test application.
  - question: Where do I run the commands to fetch and configure OpenCV?
    answer: >-
      Open a Windows PowerShell, clone the OpenCV repository, and check out the 4.10.0 tag. Then
      use CMake from the command line to run the pre-build configuration.
  - question: Can I use a newer OpenCV version than 4.10.0?
    answer: >-
      The instructions have been tested with OpenCV 4.10.0. You might be able to use a later version,
      but 4.10.0 is the version verified by this path.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will have a built OpenCV library for Windows on Arm and a test application that uses
      the library. This provides a working base to start developing OpenCV applications on your
      device or Azure VM.
# END generated_summary_faq

author: Koki Mitsunami

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
tools_software_languages:
    - Visual Studio
    - Clang
    - OpenCV
    - CPP
operatingsystems:
    - Windows


further_reading:
    - resource:
        title: OpenCV website
        link: https://opencv.org/
        type: website
    - resource:
        title: Arm Kleidi Libraries
        link: https://www.arm.com/products/development-tools/embedded-and-software/kleidi-libraries
        type: website
    - resource:
        title: Evolution of SIMD architecture with SVE2 
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/sve2
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

