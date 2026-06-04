---
title: Get started with Trusted Firmware-M

description: Learn how to build and run the reference Trusted Firmware-M tests and example application on Arm Fixed Virtual Platforms for secure microcontroller development.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers new to Trusted
  Firmware-M.


learning_objectives:
- Build and run the reference TF-M tests and example application.

prerequisites:
- Some familiarity with embedded C programming
- A machine running Ubuntu Linux

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:43:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8d8f9df559ff1b1570dc98baf640fc2d4c4d225d69f22529e1881b62d4017752
  summary_generated_at: '2026-06-01T21:54:11Z'
  summary_source_hash: 8d8f9df559ff1b1570dc98baf640fc2d4c4d225d69f22529e1881b62d4017752
  faq_generated_at: '2026-06-02T22:43:17Z'
  faq_source_hash: 8d8f9df559ff1b1570dc98baf640fc2d4c4d225d69f22529e1881b62d4017752
  summary: >-
    This introductory Learning Path shows how to build and run the reference Trusted Firmware-M
    (TF-M) tests and example application on the Corstone-300 Fixed Virtual Platform (FVP). Working
    in a bare-metal environment for Armv8-M/Armv8.1-M, you use Arm Virtual Hardware FVP to exercise
    the Secure Processing Environment (SPE) reference implementation aligned with PSA Certified
    guidelines. The steps assume an Ubuntu 22.04 LTS (Jammy) host and basic familiarity with embedded
    C. By the end, you will have compiled the supplied TF-M tests and reference example and executed
    them on the Corstone-300 FVP, providing a practical starting point for secure microcontroller
    development with TF-M.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a machine running Ubuntu Linux and some familiarity with embedded C programming.
      No other prerequisites are explicitly listed.
  - question: Which platform should I use to run the TF-M tests and example?
    answer: >-
      Use the Corstone-300 Fixed Virtual Platform (FVP). It is available from the Arm Ecosystem
      FVP page.
  - question: Is an RTOS required or is this a bare-metal setup?
    answer: >-
      This path targets a bare-metal setup. No operating system is used on the target.
  - question: Which Ubuntu version is assumed, and what initial setup step should I run?
    answer: >-
      The instructions assume Ubuntu 22.04-LTS (jammy). Begin by updating your system package
      lists with: sudo apt update.
  - question: What result should I expect after completing the steps, and how long will it take?
    answer: >-
      You will build the supplied TF-M tests and reference example and run them on the Corstone-300
      FVP. The estimated time to complete is about 15 minutes.
# END generated_summary_faq

author: Pareena Verma

test_images:
- armswdev/arm-tools:bare-metal-compilers
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: Security
armips:
- Cortex-M
- Corstone
operatingsystems:
- Baremetal
tools_software_languages:
- Arm Virtual Hardware
- FVP
- TrustZone
- Trusted Firmware

further_reading:
    - resource:
        title: Trusted Firmware-M First Long Term Support (LTS)
        link: https://www.trustedfirmware.org/blog/tf-m-v2-1-0_lts
        type: blog
    - resource:
        title: Trusted Firmware-M
        link: https://www.trustedfirmware.org/projects/tf-m/
        type: website
    - resource:
        title: TF-M documentation
        link: https://tf-m-user-guide.trustedfirmware.org
        type: documentation
    - resource:
        title: PSA Certified
        link: https://www.psacertified.org/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

