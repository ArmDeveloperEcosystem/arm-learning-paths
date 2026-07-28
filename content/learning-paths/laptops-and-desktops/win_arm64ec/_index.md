---
title: Use Arm64EC with Windows 11 on Arm

description: Learn how to build native Arm applications and migrate x86/x64 applications to Arm using Arm64EC on Windows on Arm devices.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to use Arm64EC with Windows on Arm devices. 

learning_objectives:
    - Build native Arm applications and migrate x86 or x64 applications to Arm using Arm64EC
    - Compare the performance of a simple application using different build configurations

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:28:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  summary_generated_at: '2026-07-28T16:28:23Z'
  summary_source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  faq_generated_at: '2026-07-28T16:28:23Z'
  faq_source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  summary: >-
    This Learning Path shows how to use Arm64EC with Visual Studio on Windows 11 on Arm to build
    a simple application and explore migration from existing x86 or x64 code. Learners create
    and build the project using Arm64EC, run the resulting binaries on a Windows on Arm device,
    and compare results across build configurations to observe differences in behavior and execution
    time. The path introduces Arm64EC as the application binary interface for Windows 11 on Arm
    and highlights practical considerations that influence migration decisions, including dependency
    integration. By the end, learners validate builds on hardware and practice a basic workflow
    to build, run, and compare an application that targets Arm using Arm64EC.
  faqs:
  - question: How do I know my device is ready to build with Arm64EC?
    answer: >-
      Use a Windows 11 on Arm computer and install Visual Studio 2022 or higher. The Lenovo Thinkpad
      X13s is one example of suitable hardware.
  - question: Which Visual Studio version should I install for this path?
    answer: >-
      Install Visual Studio 2022 or higher. Earlier versions are not listed for this workflow.
  - question: Which option should I choose for a new project versus migrating an existing x86/x64
      project?
    answer: >-
      For new code, build a native application targeting Arm using Arm64EC. For existing x86 or
      x64 code, follow the steps to migrate the project using Arm64EC on Windows 11 on Arm.
  - question: What result should I expect after building and running the sample with Arm64EC?
    answer: >-
      You should get a Windows application that runs on the Arm device and produces the expected
      output for the simple example. Successful execution confirms the build and configuration
      are correct.
  - question: What should I record to compare performance across build configurations?
    answer: >-
      Use the same simple application, run each build on the device, and note observed runtime
      behavior and timing. Keep the test conditions consistent so differences reflect the build
      configuration.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - Arm64EC
    - Visual Studio

further_reading:
    - resource:
        title: Get started with Arm64EC
        link: https://learn.microsoft.com/en-us/windows/arm/arm64ec-build
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

