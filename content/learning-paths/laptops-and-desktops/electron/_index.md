---
title: Develop cross-platform desktop applications with Electron on Windows on Arm

description: Learn how to develop and build cross-platform desktop applications using the Electron Framework on Windows on Arm devices.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to develop cross-platform desktop applications using the Electron Framework on Windows on Arm (WoA).

learning_objectives:
    - Implement a sample application using the electron framework on a Windows on Arm machine
    - Learn how to create a multi platform build of the application

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Node.js for Arm64. You can find the [Node.js installer](https://nodejs.org/dist/v20.10.0/node-v20.10.0-arm64.msi).
    - Any code editor; we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:04:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  summary_generated_at: '2026-06-01T22:05:20Z'
  summary_source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  faq_generated_at: '2026-06-02T23:04:46Z'
  faq_source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  summary: >-
    This Learning Path shows how to develop a simple Electron desktop application on Windows on
    Arm (Arm64) and build it for multiple architectures. You will set up a Windows on Arm device
    or virtual machine with Node.js for Arm64 and a code editor, create an Electron app using
    web technologies, and configure cross-platform builds. The steps introduce Electron Builder
    and the required changes to package.json so you can produce builds targeting Arm64 and x64.
    Designed for an introductory audience, the path takes about 30 minutes and provides a practical
    workflow for getting an Electron app running on Windows on Arm and preparing multi-architecture
    outputs.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Have a Windows on Arm computer (for example, a Lenovo ThinkPad X13s running Windows 11)
      or a Windows on Arm virtual machine, Node.js for Arm64 installed, and a code editor. Visual
      Studio Code for Arm64 is recommended.
  - question: How long should I plan to spend on this Learning Path?
    answer: >-
      The estimated time to complete is 30 minutes.
  - question: How do I add Electron Builder to my project?
    answer: >-
      From your project folder, run: npm install electron-builder --save-dev. The console output
      will be similar to the example shown in the steps and may include npm audit messages.
  - question: Where do I configure the project for cross-platform builds?
    answer: >-
      Modify the package.json file in your project folder as shown in the Learning Path to enable
      building for multiple architectures.
  - question: Which architectures will the final build target?
    answer: >-
      The build is configured to run on both Arm64 and x64.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - JavaScript
    - HTML    
    - Visual Studio Code

further_reading:
    - resource:
        title: Electron
        link: https://www.electronjs.org/blog/electron-doumentation
        type: documentation
    - resource:
        title: Awesome Electron
        link: https://github.com/sindresorhus/awesome-electron
        type: website
    - resource:
        title: Electron support for Windows on Arm
        link: https://www.electronjs.org/docs/latest/tutorial/windows-arm
        type: documentation    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

