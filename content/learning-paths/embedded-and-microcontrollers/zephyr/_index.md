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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:56:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 89f599ab33721a2d578d4fc39e505b5aed8d930aabac71f22d1ba28bfc4a5cf8
  summary_generated_at: '2026-06-01T22:00:54Z'
  summary_source_hash: 89f599ab33721a2d578d4fc39e505b5aed8d930aabac71f22d1ba28bfc4a5cf8
  faq_generated_at: '2026-06-02T22:56:13Z'
  faq_source_hash: 89f599ab33721a2d578d4fc39e505b5aed8d930aabac71f22d1ba28bfc4a5cf8
  summary: >-
    This Learning Path shows how to build and run Zephyr RTOS applications on the Arm Corstone-300
    Fixed Virtual Platform (FVP) using Arm Virtual Hardware. You will obtain the Zephyr source,
    install the Zephyr SDK, build Zephyr sample applications, and execute them on a virtual Corstone-300
    system targeting Cortex-M. This introductory path is designed for developers getting started
    with Zephyr on Arm and can be completed in about 30 minutes. Prerequisites are some familiarity
    with embedded C and either a Linux machine running Ubuntu or an AWS account to use Arm Virtual
    Hardware. By the end, you will have verified Zephyr builds running on the Corstone-300 FVP.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need some familiarity with embedded C programming and either a Linux machine running
      Ubuntu or an AWS account to use Arm Virtual Hardware. No other prerequisites are explicitly
      listed.
  - question: Do I need physical hardware for this Learning Path?
    answer: >-
      No. The applications are run on the Corstone-300 Fixed Virtual Platform using Arm Virtual
      Hardware, so no physical hardware is required.
  - question: 'Which environment should I use: local Ubuntu or Arm Virtual Hardware on AWS?'
    answer: >-
      Use a local Ubuntu machine if you prefer to run the tools on your own system, or choose
      an AWS account to access Arm Virtual Hardware in the cloud. The path supports either option
      as indicated in the prerequisites.
  - question: What will I build and run in this path?
    answer: >-
      You will get the Zephyr source, install the Zephyr SDK, build sample Zephyr applications,
      and run them on the Corstone-300 FVP.
  - question: How do I know the application ran correctly on the Corstone-300 FVP?
    answer: >-
      You should be able to launch the Corstone-300 FVP and see the sample application run without
      errors. If it fails, recheck that the Zephyr SDK is installed and the Zephyr source was
      obtained as shown in the steps.
# END generated_summary_faq

author: Pareena Verma

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

