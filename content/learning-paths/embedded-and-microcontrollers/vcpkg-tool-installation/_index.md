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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:58:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9570302d161023bafe287a823c5268cc92a08d59399124d28b7288cf3bbfd806
  summary_generated_at: '2026-08-13T18:58:09Z'
  summary_source_hash: 9570302d161023bafe287a823c5268cc92a08d59399124d28b7288cf3bbfd806
  faq_generated_at: '2026-08-13T18:58:09Z'
  faq_source_hash: 9570302d161023bafe287a823c5268cc92a08d59399124d28b7288cf3bbfd806
  summary: >-
    You'll install and initialize vcpkg on Linux, Windows, or macOS for reproducible command-line tool
    setup for projects. First, you'll run the shell-specific initialization script and create `vcpkg-configuration.json`
    for your host. Then, you'll run `vcpkg-shell activate`, inspect installed artifacts, and activate
    a Keil MDK Community license with `armlm` for Arm tooling.
  faqs:
  - question: Do I need to run the vcpkg init script every time I open a new terminal?
    answer: >-
      Yes. Run the appropriate script from ~/.vcpkg for your shell (vcpkg-init.cmd on Windows
      cmd, vcpkg-init.ps1 in PowerShell, or vcpkg-init on Linux/macOS). Initialization is required
      in every new terminal window before using vcpkg.
  - question: What does my vcpkg-configuration.json control, and why create it before activation?
    answer: >-
      The configuration ensures consistent installation across platforms and selects the correct
      binaries for the host OS and architecture. Create it first so activation installs and exposes
      the tools defined for your environment.
  - question: How do I know that vcpkg activation worked?
    answer: >-
      After running vcpkg-shell activate, you should see a summary of artifacts with their Version
      and Status, such as installed. The listed tools come from your vcpkg-configuration.json.
  - question: I see a warning that vcpkg-artifacts is experimental. Should I worry?
    answer: >-
      The activation output can include a warning that vcpkg-artifacts is experimental and may
      change at any time. This is expected; continue with the steps as shown.
  - question: How do I activate and verify the Keil MDK Community license for Arm Compiler for
      Embedded?
    answer: >-
      Activate it using armlm activate -product KEMDK-COM0 -server https://mdk-preview.keil.arm.com,
      then optionally run armlm inspect to confirm an active product entry such as Keil MDK Community.
      Use of Arm tools is subject to the End User License Agreement located in the license_terms
      folder of the downloaded archive.
# END generated_summary_faq

author: Christopher Seidl

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
