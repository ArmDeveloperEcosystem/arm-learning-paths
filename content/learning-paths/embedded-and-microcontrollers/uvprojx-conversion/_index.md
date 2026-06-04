---
title: Convert uvprojx-based projects to csolution

description: Learn how to import, convert, and build uvprojx-based projects to csolution format using Keil Studio, µVision, and command-line tools for CMSIS-Toolbox compatibility.

minutes_to_complete: 10

who_is_this_for: This is a topic for users of µVision who want to migrate to the new project format (csolution) required by CMSIS-Toolbox.

learning_objectives:
    - Import, convert, and build uvprojx-based projects in Keil Studio.
    - Convert uvprojx-based projects in µVision.
    - Convert and build uvprojx-based projects on the command line.

prerequisites:
    - Install [Keil Studio](/install-guides/keilstudio_vs/) on your machine.
    - Install [µVision](/install-guides/mdk/) on your machine.
    - Install [uv2csolution](https://arm-software.github.io/MDK-Toolbox/01_installation/) for the command line flow.
    - The &micro;Vision project must use Arm Compiler 6 as the default toolchain. Arm Compiler 5 is not supported.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:48:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 179b0318bbef9cef31ca6bb82de853597a609f61d6868aaaa85cfb40a27a051a
  summary_generated_at: '2026-06-01T21:57:17Z'
  summary_source_hash: 179b0318bbef9cef31ca6bb82de853597a609f61d6868aaaa85cfb40a27a051a
  faq_generated_at: '2026-06-02T22:48:13Z'
  faq_source_hash: 179b0318bbef9cef31ca6bb82de853597a609f61d6868aaaa85cfb40a27a051a
  summary: >-
    This Learning Path shows how to migrate existing µVision uvprojx-based Cortex-M projects to
    the csolution format required by CMSIS-Toolbox. You will convert projects using three workflows:
    Keil Studio in VS Code, µVision’s built-in export, and the uv2csolution command-line tool
    on Windows, Linux, or macOS. The steps highlight what gets generated (for example, .csolution.yaml,
    .cproject.yaml, and a vcpkg configuration) and how to confirm a successful conversion in the
    output views. Prerequisites include installed Keil Studio, µVision, and uv2csolution for the
    CLI flow; the project must use Arm Compiler 6. After conversion, you can use the project with
    CMSIS-Toolbox or Keil Studio. Estimated time to complete is about 10 minutes.
  faqs:
  - question: What do I need installed before running the conversion?
    answer: >-
      Install Keil Studio and µVision, and install uv2csolution if you plan to use the command-line
      flow. The µVision project must use Arm Compiler 6 as the default toolchain; Arm Compiler
      5 is not supported.
  - question: How do I start and verify the conversion in Keil Studio?
    answer: >-
      In VS Code, open the folder containing the uvprojx, right-click the uvprojx file, and select
      “Convert µVision project to csolution.” The Output window shows a successful conversion,
      and the vcpkg configuration file is automatically activated so you will see “Arm Tools”
      available.
  - question: What files should I expect after a successful conversion?
    answer: >-
      You should see files such as <project>.csolution.yaml, <project>.cproject.yaml, and vcpkg-configuration.json,
      along with any related support files.
  - question: How do I export from µVision and confirm it worked?
    answer: >-
      Use Project → Export → Save Project to csolution format in µVision. The Build Output window
      will show a successful conversion, and you can then use the project with CMSIS-Toolbox or
      Keil Studio.
  - question: What should I check if my project currently uses Arm Compiler 5?
    answer: >-
      Arm Compiler 5 is not supported; set Arm Compiler 6 as the default toolchain in your µVision
      project before converting.
# END generated_summary_faq

author: Christopher Seidl

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-M
tools_software_languages:
    - Keil MDK
    - CMSIS-Toolbox
operatingsystems:
    - Windows
    - Linux
    - macOS



further_reading:
    - resource:
        title: Keil Studio User's Guide
        link: https://developer.arm.com/documentation/108029/latest/
        type: documentation
    - resource:
        title: Introducing Keil MDK Version 6
        link: https://community.arm.com/arm-community-blogs/b/internet-of-things-blog/posts/keil-mdk-version-6
        type: blog
    - resource:
        title: keil.arm.com
        link: https://keil.arm.com
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

