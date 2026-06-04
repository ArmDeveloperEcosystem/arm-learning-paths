---
title: Develop desktop applications with Chromium Embedded Framework on Windows on Arm

description: Learn how to create and build Chromium Embedded Framework desktop applications using CMake and web technologies on Windows on Arm.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to use web technologies for developing Desktop apps on Windows on Arm (WoA).

learning_objectives:
    - Create and build a Chromium Embedded Framework project using CMake
    - Modify and style the application

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:25:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5df8cc6d859c505ad79f8297056b06233956c92203a6d2352d9be8e498a42547
  summary_generated_at: '2026-06-01T22:15:54Z'
  summary_source_hash: 5df8cc6d859c505ad79f8297056b06233956c92203a6d2352d9be8e498a42547
  faq_generated_at: '2026-06-02T23:25:17Z'
  faq_source_hash: 5df8cc6d859c505ad79f8297056b06233956c92203a6d2352d9be8e498a42547
  summary: >-
    This introductory Learning Path guides you through creating and building a Chromium Embedded
    Framework (CEF) desktop application on Windows on Arm using CMake. Working in Visual Studio
    2022 on a Windows on Arm device or a Windows on Arm virtual machine, you will set up a C++
    CEF project and then modify and style the application using HTML, JavaScript, and CSS. The
    focus is on building the project for Arm-based Windows systems (Arm Cortex-A) and applying
    basic UI changes with familiar web technologies. Prerequisites are a Windows on Arm computer
    such as a Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm VM, and Visual Studio
    2022. Estimated time: about 30 minutes.
  faqs:
  - question: What do I need before starting this Learning Path?
    answer: >-
      You need a Windows on Arm computer such as the Lenovo ThinkPad X13s running Windows 11,
      or a Windows on Arm virtual machine, and Visual Studio 2022. These are the only explicit
      prerequisites.
  - question: Which tools and languages will I use to build the application?
    answer: >-
      You will use CMake with Visual Studio 2022 to configure and build a CEF project written
      in C++. You will also work with HTML, JavaScript, and CSS to modify and style the application.
  - question: What environment does the resulting application target?
    answer: >-
      The application targets Windows on Arm (WoA) devices. The metadata indicates an Arm Cortex-A
      CPU class for the platform.
  - question: What result should I expect when I finish the steps?
    answer: >-
      You will have created and built a CEF project on Windows on Arm and applied basic styling
      or modifications using web technologies. Expect a CEF-based desktop application that incorporates
      web content.
  - question: Is this suitable if I am new to CEF or Windows on Arm, and how long will it take?
    answer: >-
      Yes. The Learning Path is introductory and is designed to be completed in about 30 minutes.
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
    - CPP
    - CMake 
    - HTML
    - JavaScript
    - CSS

further_reading:
    - resource:
        title: CEF GitHub Repository
        link: https://github.com/chromiumembedded/cef
        type: documentation
    - resource:
        title: Chromium Embedded Framework
        link: https://en.wikipedia.org/wiki/Chromium_Embedded_Framework
        type: website   


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

