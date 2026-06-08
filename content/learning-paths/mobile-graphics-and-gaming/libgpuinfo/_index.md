---
title: Query Arm GPU configuration information
description: Learn how to build the libGPUInfo library using Android NDK and query configuration details of Arm Mali or Immortalis GPUs on Android devices.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for Android developers who want to adjust application complexity to match device performance. 

learning_objectives: 
    - Build the libGPUInfo library using the Android NDK
    - Run an example application to query the configuration details of an Arm Mali or Arm Immortalis GPU
    
prerequisites:
    - A development machine running Ubuntu or Debian Linux with `x86_64` architecture
    - An Android device with an Arm GPU

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:55:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 68cdc7315795b6ffa794c0a1fd4cf325ab39ebb65e23efd27b7760ece76a2ec9
  summary_generated_at: '2026-06-02T02:51:15Z'
  summary_source_hash: 68cdc7315795b6ffa794c0a1fd4cf325ab39ebb65e23efd27b7760ece76a2ec9
  faq_generated_at: '2026-06-02T23:55:55Z'
  faq_source_hash: 68cdc7315795b6ffa794c0a1fd4cf325ab39ebb65e23efd27b7760ece76a2ec9
  summary: >-
    Learn to build the libGPUInfo C++ library with the Android NDK and run an example application
    on an Android device to query configuration details of Arm Mali or Arm Immortalis GPUs. Working
    from a Debian or Ubuntu x86_64 host, you will install the Android NDK, use adb to deploy and
    run the sample, and read GPU feature and performance-level information reported by the device.
    The outcome is the ability to retrieve device-specific GPU configuration at runtime to inform
    application settings. Prerequisites are a development machine running Ubuntu or Debian Linux
    and an Android device with an Arm GPU; no additional prerequisites are explicitly listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a development machine running Ubuntu or Debian Linux with x86_64 architecture and
      an Android device with an Arm GPU. The steps use the Android NDK and adb.
  - question: Which Android GPUs and devices does this target?
    answer: >-
      The example targets Arm Mali and Arm Immortalis GPUs on Android. Use an Android device that
      includes an Arm GPU.
  - question: Does this Learning Path include installing the Android NDK and using adb?
    answer: >-
      Yes. You download and install the Android NDK and use adb as part of building libGPUInfo
      and running the example on a connected device.
  - question: What result should I expect from the example application?
    answer: >-
      The example queries the device to read Arm GPU hardware configuration information. The results
      identify available features and performance levels.
  - question: How would I use libGPUInfo in my own application?
    answer: >-
      libGPUInfo is a C++ library that can be integrated into applications to gather Arm GPU configuration
      details at runtime. You can use this information to guide runtime settings and application
      complexity choices.
# END generated_summary_faq

author: Jason Andrews

##### Tags

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Mali
    - Immortalis
operatingsystems:
    - Android
tools_software_languages:
    - Android NDK
    - adb

further_reading:
    - resource:
        title: Arm Total Compute
        link: https://www.arm.com/solutions/mobile-computing/total-compute
        type: website
    - resource:
        title: Arm Total Compute (Developer)
        link: https://developer.arm.com/Tools%20and%20Software/Total%20Compute
        type: website
    - resource:
        title: Arm Reference Solutions
        link: https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/tree/master/docs/totalcompute
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

