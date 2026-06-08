---
title: Install tools on the command line using vcpkg 

description: Learn how to install vcpkg, initialize it, create vcpkg-configuration.json files, use vcpkg for tool management, activate tool licensing, and remove vcpkg for reproducible command-line tool installations.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers who want to create reproducible tool installations on the command line.

learning_objectives: 
    - Install vcpkg
    - Initialize vcpkg
    - Create a vcpkg-configuration.json file
    - Use vcpkg
    - Activate tool licensing
    - Remove vcpkg

prerequisites:
    - A basic understanding of the [development tools for Arm Cortex-M](https://developer.arm.com/Tools%20and%20Software/)
    - Command line access to your machine

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:49:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0c3422e1cd571e6abff676c28ec32c2ec69a626a406167f9166e57daa6829252
  summary_generated_at: '2026-06-01T21:57:53Z'
  summary_source_hash: 0c3422e1cd571e6abff676c28ec32c2ec69a626a406167f9166e57daa6829252
  faq_generated_at: '2026-06-02T22:49:26Z'
  faq_source_hash: 0c3422e1cd571e6abff676c28ec32c2ec69a626a406167f9166e57daa6829252
  summary: >-
    Use vcpkg on Linux, Windows, or macOS to create reproducible command-line installations of
    tools used in Arm Cortex-M development. You will install and initialize vcpkg in each new
    terminal session, create a vcpkg-configuration.json to ensure consistent, cross-platform tool
    setup, activate the tools defined by your configuration, and handle license activation for
    Arm tools using armlm. The path also covers removing vcpkg when you are finished. Prerequisites
    are a basic understanding of development tools for Arm Cortex-M and command-line access. After
    completing the steps, you will be able to stand up a consistent tool installation via vcpkg
    and verify that licensing is active.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a basic understanding of the development tools for Arm Cortex-M and command-line
      access to your machine. No other explicit prerequisites are listed.
  - question: Which initialization command should I use on my OS, and when should I run it?
    answer: >-
      Run the vcpkg init command in every new Terminal window: Windows (cmd): %USERPROFILE%\.vcpkg\vcpkg-init.cmd,
      Windows (PowerShell): . ~/.vcpkg/vcpkg-init.ps1, Linux/macOS: . ~/.vcpkg/vcpkg-init. This
      ensures your shell session is set up to use vcpkg.
  - question: What is the purpose of vcpkg-configuration.json?
    answer: >-
      It ensures a consistent installation of tools across all platforms by selecting the correct
      binaries for your host OS and architecture. Creating this configuration file is the first
      step before using the tools.
  - question: How do I activate the tools and confirm activation worked?
    answer: >-
      Use vcpkg-shell activate to activate the tools specified in your vcpkg-configuration.json.
      You should see a list of artifacts with their Status (for example, "installed") such as
      Arm distributed Open-CMSIS-Pack CLI tools or Arm Compiler for Embedded. A warning that vcpkg-artifacts
      is experimental may appear and is shown in the example output.
  - question: When do I need to activate a license, and how can I verify it?
    answer: >-
      Before compiling with Arm Compiler for Embedded, you must install a license. You can activate
      an MDK-Community license with: armlm activate -product KEMDK-COM0 -server https://mdk-preview.keil.arm.com.
      Verify the license with armlm inspect, which shows active products in your local cache.
# END generated_summary_faq

author: Christopher Seidl

### Tags
skilllevels: Advanced
subjects: CI-CD
armips:
    - Cortex-M
tools:
    - Arm Compiler for Embedded
    - GCC
tools_software_languages:
    - vcpkg
operatingsystems:
    - Linux
    - Windows
    - macOS


further_reading:
    - resource:
        title: vcpkg documentation
        link: https://learn.microsoft.com/en-gb/vcpkg/
        type: documentation
    - resource:
        title: User-based Licensing User Guide
        link: https://developer.arm.com/documentation/102516/latest/User-based-licensing-overview
        type: documentation
    - resource:
        title: Example projects for CMSIS-Toolbox 2.0.0
        link: https://github.com/Arm-Examples#cmsis-toolbox-2.0.0-examples
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

