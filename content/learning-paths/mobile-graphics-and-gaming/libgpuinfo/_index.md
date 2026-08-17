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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:06:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eb2e5e1a9169679ea5398b97026829f8747778cd097701a3ebd7e7be9ef961a1
  summary_generated_at: '2026-08-17T22:06:59Z'
  summary_source_hash: eb2e5e1a9169679ea5398b97026829f8747778cd097701a3ebd7e7be9ef961a1
  faq_generated_at: '2026-08-17T22:06:59Z'
  faq_source_hash: eb2e5e1a9169679ea5398b97026829f8747778cd097701a3ebd7e7be9ef961a1
  summary: >-
    This Learning Path shows how to build the libGPUInfo C++ library with the Android NDK and
    run an example on an Android device to query Arm GPU configuration. You compile on the development
    machine and use adb to deploy and execute the sample on hardware with a Mali or Immortalis
    GPU. The application retrieves configuration details that reveal available features and indicative
    performance levels, enabling data-driven runtime decisions for graphics or compute paths.
    Success is verified by viewing the GPU attributes printed by the example on the device.
  faqs:
  - question: How do I confirm the Android device is ready before running the example?
    answer: >-
      Make sure the device is connected and visible to adb. If the device is not discoverable
      by adb, reconnect it and try again.
  - question: What result should I expect when the example runs on the device?
    answer: >-
      The application queries the Arm GPU and prints configuration information that highlights
      available features and indicative performance levels. Use this output to confirm the device’s
      reported GPU capabilities.
  - question: Where do the build and run steps happen in this path?
    answer: >-
      You build libGPUInfo and the example with the Android NDK on the development machine. You
      then use adb to deploy and run the example on the Android device.
  - question: Can I integrate libGPUInfo into my own Android app after trying the example?
    answer: >-
      Yes. libGPUInfo is a C++ library that can be integrated into applications to gather Arm
      GPU hardware information on the device.
  - question: What should I check if the example fails to retrieve GPU information?
    answer: >-
      Verify the app is running on an Android device with an Arm GPU and that the device is accessible
      via adb. Re-deploy the example to the connected device and run it again.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

