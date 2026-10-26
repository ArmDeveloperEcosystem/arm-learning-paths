---
title: Get started with Trusted Firmware-M

description: Learn how to build and run the reference Trusted Firmware-M tests and example application on Arm Fixed Virtual Platforms for secure microcontroller development.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers new to Trusted
  Firmware-M (TF-M).

learning_objectives:
- Build and run the reference TF-M tests and example application.

prerequisites:
- Some familiarity with embedded C programming
- A machine running Ubuntu Linux

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:53:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6370f213b3895fe0af0ecd4a0ba42fb0696ff93d19659875b4c4364525901aa5
  summary_generated_at: '2026-08-13T18:53:02Z'
  summary_source_hash: 6370f213b3895fe0af0ecd4a0ba42fb0696ff93d19659875b4c4364525901aa5
  faq_generated_at: '2026-08-13T18:53:02Z'
  faq_source_hash: 6370f213b3895fe0af0ecd4a0ba42fb0696ff93d19659875b4c4364525901aa5
  summary: >-
    You'll build TF-M tests and a reference example for the Corstone-300 Fixed
    Virtual Platform (FVP). First, you'll prepare an Ubuntu 22.04 LTS host and install the Corstone-300 FVP.
    Then, you'll build TF-M, launch the virtual platform, and use its console output to verify the
    tests and reference workload run successfully.
  faqs:
  - question: Which FVP should I use to complete the Learning Path?
    answer: >-
      Use the Corstone-300 FVP.
  - question: Where do I download the Corstone-300 FVP?
    answer: >-
      The Corstone-300 FVP is available from the [Arm Ecosystem FVP page](https://support.arm.com/tools-and-software/fixed-virtual-platforms).
  - question: Where can I find the TF-M test executables after a successful build?
    answer: >-
      Find the executables in `build/tests-spe` and `build/tests`. These include images for the
      MCUBoot bootloader, TF-M secure firmware, and the non-secure application, including signed
      secure and non-secure variants.
  - question: What should I check before building TF-M?
    answer: >-
      Ensure the system package lists are current by running `sudo apt update`.
  - question: What result should I expect when I run the tests and example on the FVP?
    answer: >-
      The Corstone-300 FVP should start TF-M and execute the supplied tests and the reference
      example. You should see console output indicating test progress and completion.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
