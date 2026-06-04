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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:59:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b6a9aa558ec5062c829d61b28fb92e25d5517249c011eb29f03cc36775b6f9af
  summary_generated_at: '2026-06-02T02:53:24Z'
  summary_source_hash: b6a9aa558ec5062c829d61b28fb92e25d5517249c011eb29f03cc36775b6f9af
  faq_generated_at: '2026-06-02T23:59:06Z'
  faq_source_hash: b6a9aa558ec5062c829d61b28fb92e25d5517249c011eb29f03cc36775b6f9af
  summary: >-
    This Learning Path shows how to enable Arm’s Memory Tagging Extension (MTE) on a Google Pixel
    8, trigger memory-bug crashes using a test app, and examine the resulting Android bug report.
    You will enable Developer options, turn on MTE on the device, install MTE_test.apk, and use
    the app to execute code with common memory bugs so that MTE forces a crash. You then capture
    a Bug report from the Developer options menu, unzip the generated archive on your desktop,
    and review diagnostics—especially tombstone files—to understand where and why the crash occurred.
    Prerequisites are a Pixel 8, a USB cable, and adb from Android SDK Platform Tools. Estimated
    time: about 10 minutes.
  faqs:
  - question: What do I need before enabling MTE on my Pixel 8?
    answer: >-
      You need a Google Pixel 8 smartphone, a USB cable, and Android Debug Bridge (adb) installed
      from the Android SDK Platform Tools. These are the only prerequisites explicitly listed.
  - question: How do I turn on Developer options to access MTE settings?
    answer: >-
      Go to Settings -> About phone -> Build number and tap the Build number seven times until
      you see “You are now a developer!”. Then return to System and open Developer options.
  - question: How do I confirm that MTE is active after I enable it?
    answer: >-
      Install and run MTE_test.apk and press any button in the app to execute code with a memory
      bug. If MTE is enabled, the app will crash and the bug report will include MTE-specific
      information about the violation.
  - question: How do I capture a bug report after the test app crashes?
    answer: >-
      Open Developer options and select the Bug report option, then tap Report to start generation.
      You can watch the progress on the device; the result is a zip file that you can move to
      your desktop and unzip.
  - question: Which files should I inspect in the bug report, and why might the filename include
      'husky'?
    answer: >-
      After unzipping, review the main bugreport text file and the tombstone file under FS/data/tombstones
      for detailed crash information. “Husky” is the code name for Google Pixel 8 Pro and may
      appear in the generated bug report filename.
# END generated_summary_faq

author: Roberto Lopez Mendez

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

