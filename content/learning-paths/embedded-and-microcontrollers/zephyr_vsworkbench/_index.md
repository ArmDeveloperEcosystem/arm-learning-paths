---
title: Build Zephyr projects with Workbench for Zephyr in VS Code

description: Learn how to set up the Workbench for Zephyr extension in VS Code, create and build Zephyr applications for Arm Cortex-M, and debug firmware using integrated memory analysis and breakpoint debugging.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded developers targeting Arm-based platforms with the Zephyr RTOS using the Workbench for Zephyr extension for VS Code.

learning_objectives:
    - Install and configure the Workbench for Zephyr extension in VS Code
    - Set up a complete Zephyr development environment including the SDK and toolchain
    - Create, build, and debug Zephyr applications using hands-on examples
    - Perform memory usage analysis and apply basic optimization techniques
    - Apply essential debugging workflows for embedded systems

prerequisites:
    - Basic familiarity with embedded C programming
    - Visual Studio Code
    - A Cortex-M development board
    - Windows 10+ (64-bit), macOS with Homebrew, or Linux (preferably Ubuntu 20.04+)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:04:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5fb4f48c2d5ab091b58505cbe3df364173dac0e2c6a1218f9510696a74899077
  summary_generated_at: '2026-08-13T19:04:08Z'
  summary_source_hash: 5fb4f48c2d5ab091b58505cbe3df364173dac0e2c6a1218f9510696a74899077
  faq_generated_at: '2026-08-13T19:04:08Z'
  faq_source_hash: 5fb4f48c2d5ab091b58505cbe3df364173dac0e2c6a1218f9510696a74899077
  summary: >-
    You'll use Workbench for Zephyr in Visual Studio Code to set up a Zephyr RTOS environment and
    build firmware for an Arm Cortex-M board. First, you'll select a supported board and debug runner.
    Then, you'll build the project, inspect memory-usage reports, set breakpoints, and step through
    code to verify the target's behavior.
  faqs:
  - question: How do I know I installed the Workbench for Zephyr extension correctly?
    answer: >-
      The setup is correct if the extension completes SDK and toolchain configuration and you
      can create and build a Zephyr application without errors. A memory usage report generated
      after the build is another good confirmation.
  - question: Which board should I select when creating the project?
    answer: >-
      Choose your Zephyr-supported Arm Cortex-M board. NXP FRDM-MCXN947 is used as an
      example, and you can confirm other options in the [Zephyr Supported Boards list](https://docs.zephyrproject.org/latest/boards/#).
  - question: What should I check if building works but debugging doesn't start?
    answer: >-
      Verify the selected debug runner matches your board’s requirements. If the board needs a
      different runner, switch to the recommended option for that target and try again.
  - question: What result should I expect after a successful build?
    answer: >-
      Expect build artifacts for your application and a generated memory usage report from Workbench
      for Zephyr. These outputs indicate the project is ready for debugging on the selected board.
  - question: How should I use the memory usage report in this workflow?
    answer: >-
      Review the report to see how code and data are allocated and identify areas to reduce usage.
      Apply basic adjustments, rebuild, and compare reports to validate improvements before debugging.
# END generated_summary_faq

author: 
    - Ayoub Bourjilat
    - Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - RTOS
tools_software_languages:
    - Zephyr
    - C

further_reading:
    - resource:
        title: Zephyr Project Documentation
        link: https://docs.zephyrproject.org/latest/index.html
        type: documentation
    - resource:
        title: Workbench for Zephyr Official Website
        link: https://z-workbench.com/
        type: website
    - resource:
        title: AC6 Zephyr Training
        link: https://www.ac6-training.com/en/cours.php/cat_oRT/ref_oRT5/zephyr-rtos-programming
        type: website

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
