---
title: Enable Memory Tagging Extension on Google Pixel 8

description: Learn how to enable Arm Memory Tagging Extension (MTE) on a Google Pixel 8 smartphone, trigger memory bug crashes, and interpret bug reports.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers interested in learning how to enable Arm's Memory Tagging Extension (MTE) on Google's Pixel 8 smartphone and also how to access a memory bug report.

learning_objectives: 
    - Enable MTE on your Google Pixel 8 smartphone
    - Understand how MTE works and learn how to make an application crash when it encounters a memory bug
    - Access the memory bug report
    - Interpret the memory bug report

prerequisites:
    - A Google Pixel 8 smartphone
    - A USB cable to connect your Google Pixel 8 to your desktop machine
    - Android Debug Bridge (adb) installed on your device. Follow the steps in https://developer.android.com/tools/adb to install Android SDK Platform Tools. The adb tool is included in this package.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:10:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 91c91c4f9261ad235fe22d6b03fbe967cdf536da79d67aba41e5ad12105122f9
  summary_generated_at: '2026-08-17T22:10:02Z'
  summary_source_hash: 91c91c4f9261ad235fe22d6b03fbe967cdf536da79d67aba41e5ad12105122f9
  faq_generated_at: '2026-08-17T22:10:02Z'
  faq_source_hash: 91c91c4f9261ad235fe22d6b03fbe967cdf536da79d67aba41e5ad12105122f9
  summary: >-
    You'll enable Arm Memory Tagging Extension (MTE) on a Google Pixel 8 and exercise it with
    a test app. Turn on MTE in Developer options, install `MTE_test.apk`, and capture a bug report
    after a deliberate memory violation. Then inspect the bug report and tombstone to understand
    the fault and MTE's lock-and-key model.
  faqs:
  - question: What result should I expect when I press a button in the test app?
    answer: >-
      With MTE enabled, the app triggers a memory violation and crashes. This lets you capture
      a bug report that includes MTE-specific details about the fault.
  - question: How do I capture a bug report after the crash?
    answer: >-
      Open **Developer options** and select **Bug report**, then tap **Report** to start generation. Wait
      for the progress indicator to complete, then use the resulting zip file for analysis.
  - question: Where in the bug report do I find detailed MTE diagnostics?
    answer: >-
      The zip contains a primary bugreport text file, and more detailed information is written
      to a tombstone file. Look under `FS/data/tombstones` in the unzipped folder.
  - question: My bug report filename includes “Husky.” Is that expected?
    answer: >-
      Yes. Husky is the code name for Google Pixel 8 Pro and can appear in the generated bug report
      filename.
  - question: What should I check if the test app doesn’t crash?
    answer: >-
      Verify that MTE is enabled in **Developer options** before running the app’s tests. Also confirm
      that `MTE_test.apk` installed correctly and that you are invoking one of the buttons designed
      to trigger a memory bug.
# END generated_summary_faq

author: Roberto Lopez Mendez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - MTE
    - adb
    - Google Pixel 8
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
