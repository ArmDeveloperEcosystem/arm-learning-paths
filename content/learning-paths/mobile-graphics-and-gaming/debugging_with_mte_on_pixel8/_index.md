---
title: Debug with MTE on Google Pixel 8
description: Learn how to detect and debug memory safety bugs in Android applications using Arm Memory Tagging Extension (MTE) on a Google Pixel 8 smartphone.

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for developers interested in learning how to use the Arm Memory Tagging Extension (MTE) to detect memory safety bugs with Android Studio on a Google Pixel 8 smartphone. 

learning_objectives: 
    - Recognize common memory safety bugs in Android applications.
    - Describe how you can use an Android MTE Test app to implement common memory bugs. 
    - Build the MTE Test app in Android Studio.
    - Enable and disable MTE in the Android Manifest.
    - Debug the MTE Test app in Android Studio on a Google Pixel 8 smartphone.

prerequisites:
    - A Google Pixel 8 smartphone.
    - Android Studio installed on your development computer.
    - A USB cable to connect your computer to your Google Pixel 8.
    - Android Debug Bridge (adb) installed on your device. If needed, follow the steps in the [Android Debug Bridge](https://developer.android.com/tools/adb) documentation.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:02:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4a6a656497613a34dd17e6afbdd31e7a491b75e6ecb1befaee650a4d02fd6976
  summary_generated_at: '2026-08-17T22:02:08Z'
  summary_source_hash: 4a6a656497613a34dd17e6afbdd31e7a491b75e6ecb1befaee650a4d02fd6976
  faq_generated_at: '2026-08-17T22:02:08Z'
  faq_source_hash: 4a6a656497613a34dd17e6afbdd31e7a491b75e6ecb1befaee650a4d02fd6976
  summary: >-
    You'll use Arm Memory Tagging Extension (MTE) on a Google Pixel 8 to find memory-safety bugs
    in an Android app. Clone and open the MTE Test app in Android Studio, edit `AndroidManifest.xml`
    to control MTE, and start a debug session on the connected device. Then exercise built-in
    memory-bug scenarios and investigate them with MTE.
  faqs:
  - question: How do I get the MTE Test app into Android Studio?
    answer: >-
      Clone the repository with git clone https://github.com/rlopez3d/mte_test_app, then open
      the cloned Android project in Android Studio. The project opens in the default Android view.
  - question: Which project view helps me find AndroidManifest.xml to enable MTE?
    answer: >-
      Switch to the Project Files view. Expand app -> src -> main -> res and open AndroidManifest.xml.
  - question: How do I confirm Android Studio is targeting my Google Pixel 8 before debugging?
    answer: >-
      Check that your device name appears in the device selector next to the Run/Debug controls.
      If it isn’t listed, ensure the phone is connected over USB and the project is open.
  - question: What should I expect on the phone when I start debugging the app?
    answer: >-
      The app shows a message on the screen when it starts. Wait until the application interface
      appears before proceeding.
  - question: Where do I enable or disable MTE for this app?
    answer: >-
      Use the application manifest to control MTE. The steps show how to edit AndroidManifest.xml
      to enable or disable MTE for the project.
# END generated_summary_faq

author: Roberto Lopez Mendez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - MTE
operatingsystems:
    - Android

further_reading:
    - resource:
        title: MTE User Guide for Android OS
        link: https://developer.arm.com/documentation/108035/latest/
        type: documentation
    - resource:
        title: Arm Memory Tagging Extension
        link: https://developer.android.com/ndk/guides/arm-mte
        type: website
    - resource:
        title: AArch64 TAGGED ADDRESS ABI
        link: https://www.kernel.org/doc/Documentation/arm64/tagged-address-abi.rst
        type: documentation
    - resource:
        title: Enhanced Security Through MTE
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/enhanced-security-through-mte
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
