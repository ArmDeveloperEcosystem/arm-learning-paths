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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:51:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 95d4fb855552939d1a0e9cccfe46333692ea291ee85dd08b816321db29ceebdc
  summary_generated_at: '2026-06-02T02:48:04Z'
  summary_source_hash: 95d4fb855552939d1a0e9cccfe46333692ea291ee85dd08b816321db29ceebdc
  faq_generated_at: '2026-06-02T23:51:15Z'
  faq_source_hash: 95d4fb855552939d1a0e9cccfe46333692ea291ee85dd08b816321db29ceebdc
  summary: >-
    This Learning Path shows how to detect and debug memory safety bugs in Android applications
    using Arm Memory Tagging Extension (MTE) on a Google Pixel 8. You will clone an Android MTE
    Test app from GitHub, open it in Android Studio, explore common native memory bug patterns,
    enable or disable MTE via the AndroidManifest, then build and debug the app on a connected
    Pixel 8. The path targets advanced developers and takes about 20 minutes. Prerequisites include
    a Google Pixel 8 smartphone, Android Studio on your development computer, a USB cable, and
    Android Debug Bridge (adb) installed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Pixel 8 smartphone, Android Studio on your development computer, a USB
      cable, and adb. If adb is not installed, follow the Android Debug Bridge documentation linked
      in the prerequisites.
  - question: How do I get the MTE Test app project into Android Studio?
    answer: >-
      Clone the repository from GitHub using the provided git clone command, then launch Android
      Studio and open the cloned project. The path guides you to view the project files as needed.
  - question: Which file do I edit to enable or disable MTE?
    answer: >-
      Use the AndroidManifest.xml in the app module. Switch the project view to Project Files,
      navigate to app -> src -> main -> res, and open AndroidManifest.xml to apply the settings
      shown in the steps.
  - question: How do I run and debug the app on my Pixel 8?
    answer: >-
      Connect the Pixel 8 via USB, ensure it appears in the device selector in Android Studio,
      and press the Debug button to build and start debugging. On the device, you will see a startup
      message, then the app interface appears for you to continue debugging.
  - question: What should I check if my Pixel 8 does not appear in Android Studio?
    answer: >-
      Verify the USB connection and confirm that adb is installed as listed in the prerequisites.
      Reconnect the device and reopen the project if it still does not show up.
# END generated_summary_faq

author: Roberto Lopez Mendez

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

