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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:16:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 25b6e3d5781c748e1bc8ab40039ab47f63e062592b5a282e2f9327479f1bdce9
  summary_generated_at: '2026-08-11T16:16:06Z'
  summary_source_hash: 25b6e3d5781c748e1bc8ab40039ab47f63e062592b5a282e2f9327479f1bdce9
  faq_generated_at: '2026-08-11T16:16:06Z'
  faq_source_hash: 25b6e3d5781c748e1bc8ab40039ab47f63e062592b5a282e2f9327479f1bdce9
  summary: >-
    You'll build OpenCV from source on Windows on Arm and create a minimal C++ application. First, you'll
    clone the OpenCV repository, check out the validated `4.10.0` tag, and configure CMake with
    either MSVC or Clang. Then, you'll compile OpenCV and a test program that links against its
    generated libraries to validate your toolchain and environment.
  faqs:
  - question: How do I prepare the OpenCV DLLs before running the test application?
    answer: >-
      Add the directory containing the OpenCV DLLs to your `PATH`, or place the DLLs beside the
      executable. This lets the test application find the required libraries at runtime.
  - question: Which OpenCV version should I check out for this path?
    answer: >-
      Use tag `4.10.0`. You might be able to use a later version, but if you
      run into issues, switch back to `4.10.0`.
  - question: Do I need a specific CMake version, and where should I run the commands?
    answer: >-
      Use CMake `3.28.1` and run the commands from Windows PowerShell using
      the CMake command-line interface.
  - question: How do I know my build worked, and where are the outputs?
    answer: >-
      A successful run shows CMake configuration and compilation completing without errors and
      produces OpenCV libraries plus a test application in the build directory you created. Building
      the test program against OpenCV confirms the environment is set up correctly.
  - question: If I follow the MSVC path, do I need Visual Studio installed?
    answer: >-
      Yes. Use Visual Studio 2022 or later for the MSVC flow; the instructions were tested with
      Visual Studio 2022. If you choose Clang, follow the Clang section and its tool setup.
# END generated_summary_faq

author: Koki Mitsunami

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
