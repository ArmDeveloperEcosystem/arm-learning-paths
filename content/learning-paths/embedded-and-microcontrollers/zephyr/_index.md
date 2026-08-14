---
title: Run the Zephyr RTOS on Arm Corstone-300

description: Learn how to build and run Zephyr RTOS applications on the Arm Corstone-300 Fixed Virtual Platform using Arm Virtual Hardware.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers getting started
  with the Zephyr RTOS.

learning_objectives:
- Build and run Zephyr applications on the Corstone-300

prerequisites:
- Some familiarity with embedded C programming
- A Linux machine running Ubuntu, or an AWS account to use [Arm Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:01:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0fc448627f05a68c8b785f8ca0cb2b7e8c7c0fb5a9686140bcbbb3dd9f24b061
  summary_generated_at: '2026-08-13T19:01:39Z'
  summary_source_hash: 0fc448627f05a68c8b785f8ca0cb2b7e8c7c0fb5a9686140bcbbb3dd9f24b061
  faq_generated_at: '2026-08-13T19:01:39Z'
  faq_source_hash: 0fc448627f05a68c8b785f8ca0cb2b7e8c7c0fb5a9686140bcbbb3dd9f24b061
  summary: >-
    You'll prepare a Zephyr workspace, install the Zephyr SDK, and build samples for a Cortex-M-based
    Corstone-300 target. First, you'll obtain the Zephyr source and configure your development environment.
    Then, you'll build the application and run its binary on the Corstone-300 Fixed Virtual Platform (FVP)
    through Arm Virtual Hardware, locally or in the cloud.
  faqs:
  - question: Can I complete the Learning Path without physical hardware?
    answer: >-
      Yes. You build Zephyr sample applications and run them on the Arm Corstone-300 FVP provided by Arm Virtual Hardware.
  - question: Which environment should I use to run the simulator?
    answer: >-
      Use a Linux machine or Linux-based Arm Virtual Hardware.
  - question: How do I know the Zephyr build worked?
    answer: >-
      The build completes without errors and generates the application artifacts for the Corstone-300
      target. Proceed when the build finishes cleanly.
  - question: What console output should I expect from the Corstone-300 FVP?
    answer: >-
      The FVP opens telnet terminal windows that show a Zephyr boot message followed by
      `Hello World! mps3_an547`.
  - question: Where can I find the built Zephyr application?
    answer: >-
      You'll find the application binaries in `~/zephyrproject/zephyr/build/zephyr/`. Use the
      `zephyr.elf` file from this directory when you run the application on the Corstone-300 FVP.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- amd64/ubuntu:latest
test_link: null
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
- Cortex-M
operatingsystems:
- RTOS
tools_software_languages:
- Zephyr
- Arm Virtual Hardware
- FVP

further_reading:
    - resource:
        title: Zephyr Project Documentation
        link: https://docs.zephyrproject.org/latest/index.html
        type: documentation
    - resource:
        title: Zephyr Sample applications and Demo
        link: https://docs.zephyrproject.org/latest/samples/index.html
        type: documentation
    - resource:
        title: List of Arm boards and platforms supported by Zephyr
        link: https://docs.zephyrproject.org/latest/boards/arm/index.html
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
