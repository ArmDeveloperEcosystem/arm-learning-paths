---
title: Build and run a native Windows on Arm Qt application 

description: Learn how to build and run Qt-based desktop applications on Windows on Arm and investigate native Arm64 performance improvements.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to use the native performance of the Qt framework for building desktop applications on Windows on Arm (WoA).

learning_objectives:
    - Build and run a Qt-based desktop application
    - Investigate performance improvements gained by running on Arm64

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - '[Qt framework](https://www.qt.io/) or [Qt for Open Source Development](https://www.qt.io/download-open-source)'

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:27:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 63389742eced4df89f85bdf56a01e489e52a9702d446b557f8f55312f9d31f20
  summary_generated_at: '2026-07-28T16:27:00Z'
  summary_source_hash: 63389742eced4df89f85bdf56a01e489e52a9702d446b557f8f55312f9d31f20
  faq_generated_at: '2026-07-28T16:27:00Z'
  faq_source_hash: 63389742eced4df89f85bdf56a01e489e52a9702d446b557f8f55312f9d31f20
  summary: >-
    You'll build and run a Qt desktop application as a native Arm64 binary on Windows on Arm. You'll
    configure the project target, compile and launch the app, then observe runtime behavior to
    investigate possible performance improvements from native execution and Qt libraries.
  faqs:
  - question: How do I know if I built a native Arm64 binary?
    answer: >-
      Confirm that your build configuration targets Arm64 for Windows on Arm, then run the
      resulting executable on the device. A successful launch without additional changes indicates
      a native build.
  - question: What should I check if my project fails to compile?
    answer: >-
      Verify that your Qt installation supports Windows on Arm; Qt 6.2 adds native Windows on Arm support.
      Also check that the required Qt modules for your project are installed.
  - question: What result should I expect when I run the application?
    answer: >-
      A Qt desktop window should launch and respond on Windows on Arm. Basic UI interactions should
      work as they do on other platforms supported by Qt.
  - question: How can I investigate performance improvements after building for Arm64?
    answer: >-
      Run the native Arm64 build and observe runtime behavior such as startup and UI responsiveness.
      Record your observations to compare how the app feels when executed natively.
  - question: Do I need to use Qt Creator to complete this Learning Path?
    answer: >-
      No. Qt Creator is available, but the you'll focus on building and running a Qt application
      on Windows on Arm. You don't need a specific IDE.
# END generated_summary_faq

author: Dawid Borycki

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
    - C
    - CPP
    - Qt    

further_reading:
    - resource:
        title: Qt for Windows on ARM
        link: https://www.qt.io/blog/qt-for-windows-on-arm
        type: blog
    - resource:
        title: Qt Examples And Tutorials
        link: https://doc.qt.io/qt-6/qtexamplesandtutorials.html
        type: documentation    

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
