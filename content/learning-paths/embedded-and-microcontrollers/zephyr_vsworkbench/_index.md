---
title: Build Zephyr projects with Workbench for Zephyr in VS Code

description: Learn how to install Workbench for Zephyr extension in VS Code, set up the complete Zephyr development environment, create and build Zephyr applications, debug embedded systems, and perform memory usage analysis.

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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:57:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 808f1c99409f9ca3bb72419eaf950bc097f1c7af6c2dcade6385be97fdbbf713
  summary_generated_at: '2026-06-01T22:01:28Z'
  summary_source_hash: 808f1c99409f9ca3bb72419eaf950bc097f1c7af6c2dcade6385be97fdbbf713
  faq_generated_at: '2026-06-02T22:57:52Z'
  faq_source_hash: 808f1c99409f9ca3bb72419eaf950bc097f1c7af6c2dcade6385be97fdbbf713
  summary: >-
    This introductory path shows how to install and configure the Workbench for Zephyr extension
    in Visual Studio Code, set up the Zephyr SDK and toolchain, and create, build, and debug Zephyr
    RTOS applications on Arm Cortex-M boards. You will follow a workflow demonstrated with an
    NXP FRDM-MCXN947 board, but the same steps apply to any Zephyr-supported Cortex-M target,
    with board-specific debug runners selected as needed. The path also covers generating memory
    usage reports to understand ROM and RAM consumption and applying basic optimization techniques.
    Prerequisites include basic embedded C skills, VS Code, a Cortex-M development board, and
    a host running Windows 10+ (64-bit), macOS with Homebrew, or Linux (preferably Ubuntu 20.04+).
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need basic familiarity with embedded C, Visual Studio Code, and access to a Cortex-M
      development board. Use Windows 10+ (64-bit), macOS with Homebrew, or Linux (preferably Ubuntu
      20.04+) as your host system.
  - question: How do I know if my Arm Cortex-M board will work for this path?
    answer: >-
      The process works for any Zephyr-supported Arm Cortex-M board. The path demonstrates with
      an NXP FRDM-MCXN947, and you can confirm your board on the Zephyr Supported Boards list.
  - question: Which debug runner should I use for my board?
    answer: >-
      The required runner depends on your board. Follow your board’s Zephyr documentation and
      the path’s guidance, as you might need to install and select a different debug tool (runner)
      in Workbench for Zephyr.
  - question: What result should I expect after I build the sample application in Workbench?
    answer: >-
      You should get a successful Zephyr build along with a memory usage report showing ROM and
      RAM consumption. You can then proceed to live debugging and memory analysis within Workbench.
  - question: What should I check if the build or debug setup fails?
    answer: >-
      Verify that the Workbench for Zephyr extension is installed and that it completed SDK and
      toolchain setup. Ensure your board is Zephyr-supported and that the appropriate debug runner
      is configured for your target.
# END generated_summary_faq

author: 
    - Ayoub Bourjilat
    - Odin Shen

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

