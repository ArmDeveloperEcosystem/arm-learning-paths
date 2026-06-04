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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:17:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  summary_generated_at: '2026-06-01T22:11:42Z'
  summary_source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  faq_generated_at: '2026-06-02T23:17:05Z'
  faq_source_hash: 4069c5bce1ce4b689a7a67d740fc077dc55c9b0bfbab392f5984ba0bdd9e59c3
  summary: >-
    This Learning Path shows how to use Arm64EC on Windows 11 on Arm to build native Arm applications
    and begin migrating existing x86 or x64 code. Working on a Windows on Arm computer (for example,
    a Lenovo ThinkPad X13s) with Visual Studio 2022 or later, you will configure projects to target
    the Arm64EC application binary interface, build and run on-device, and compare the performance
    of a simple application across different build configurations. The topic is introductory and
    focused on practical steps developers can follow on Windows, with no additional prerequisites
    explicitly listed beyond the required hardware and Visual Studio installation.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer such as a Lenovo ThinkPad X13s running Windows 11 and
      Visual Studio 2022 or higher installed. No other prerequisites are explicitly listed.
  - question: Which option should I use to migrate an existing x86 or x64 application?
    answer: >-
      Use Arm64EC to migrate existing x86 or x64 applications to devices using the Arm architecture.
      The path also covers building new native Arm applications so you can compare configurations.
  - question: What should I check if I do not see Arm64EC options in Visual Studio?
    answer: >-
      Verify that you are using Visual Studio 2022 or higher on a Windows 11 on Arm computer.
      The Learning Path does not list additional components beyond installing Visual Studio.
  - question: How do I compare performance across build configurations?
    answer: >-
      Build the same simple application using different configurations and then run them to observe
      differences. The steps guide you through creating those builds and comparing the results;
      no specific performance targets are stated.
  - question: How do I verify that my build was successful?
    answer: >-
      After building in Visual Studio, you should get a runnable application on your Windows 11
      on Arm device. Launch it and proceed to the comparison step to confirm it behaves as expected
      in the selected configuration.
# END generated_summary_faq

author: Pareena Verma

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

