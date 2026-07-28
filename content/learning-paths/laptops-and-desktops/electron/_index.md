---
title: Develop cross-platform desktop applications with Electron on Windows on Arm

description: Learn how to develop and build cross-platform desktop applications using the Electron Framework on Windows on Arm devices.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to learn how to develop cross-platform desktop applications using the Electron Framework on Windows on Arm (WoA).

learning_objectives:
    - Implement a sample application using the electron framework on a Windows on Arm machine
    - Learn how to create a multi platform build of the application

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Node.js for Arm64. You can find the [Node.js installer](https://nodejs.org/dist/v20.10.0/node-v20.10.0-arm64.msi).
    - Any code editor; we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:17:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  summary_generated_at: '2026-07-28T16:17:03Z'
  summary_source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  faq_generated_at: '2026-07-28T16:17:03Z'
  faq_source_hash: 8491a5e83e9e6436721f6078085e9b367121d19fdf228634dba859b3e1a0802a
  summary: >-
    You'll create an Electron desktop application on Windows on Arm and configure cross-platform
    packaging. You'll add project code, install Electron Builder with `npm`, update `package.json`, and
    target Arm64 and x64 from one codebase. You'll build both Arm64 and x64 variants, inspect console output, and
    identify where to change future packaging settings.
  faqs:
  - question: Which installation scope should I use for Electron Builder?
    answer: >-
      Install Electron Builder as a development dependency.
      This keeps the build tool in your project’s `devDependencies`.
  - question: What should I look for after running `npm install electron-builder --save-dev`?
    answer: >-
      A successful install reports that packages were added and might include funding and vulnerability
      notices. Use this as confirmation to continue to the `package.json` changes.
  - question: Where do I configure builds for Arm64 and x64?
    answer: >-
      Edit the `package.json` file in your project folder. Add or update the Electron Builder configuration
      so it includes both Arm64 and x64 targets as described.
  - question: How do I know the build includes both architectures?
    answer: >-
      After updating `package.json`, run your build and check that artifacts are generated for both
      Arm64 and x64. If only one appears, review the targets configured in `package.json`.
  - question: The install output lists vulnerabilities and suggests `npm audit`. Do I need to fix
      this before proceeding?
    answer: >-
      The log might show vulnerability notices and recommend running `npm audit`. To complete the Learning Path, continue with configuration and application builds. 
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
