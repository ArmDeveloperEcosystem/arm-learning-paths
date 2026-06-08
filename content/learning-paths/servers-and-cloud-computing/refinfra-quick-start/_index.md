---
title: Get started with the Neoverse Reference Design software stack

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in testing the Neoverse Reference Design firmware stack.

learning_objectives: 
    - Set up your environment.
    - Build the reference firmware stack.
    - Test the reference firmware stack.

prerequisites:
    - Some understanding of the [Reference Design software stack architecture](https://neoverse-reference-design.docs.arm.com/en/latest/about/software_stack.html).
    - Some understanding of the Linux command line.
    - Optionally a basic understanding of Docker and containers.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:01:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8f2515b7c416a821bd397a77297adc263397a8b3cb86e9bb34e646735a21f854
  summary_generated_at: '2026-06-02T05:02:22Z'
  summary_source_hash: 8f2515b7c416a821bd397a77297adc263397a8b3cb86e9bb34e646735a21f854
  faq_generated_at: '2026-06-03T02:01:19Z'
  faq_source_hash: 8f2515b7c416a821bd397a77297adc263397a8b3cb86e9bb34e646735a21f854
  summary: >-
    Learn how to set up a Linux host, build, and test the Neoverse Reference Design (RD-N2) firmware
    stack using containers and an Arm Ecosystem FVP. You will prepare an Ubuntu 22.04 AArch64
    or x86_64 machine, then build a busybox root filesystem and a firmware stack that includes
    TF-A, UEFI, SCP, and a lightweight OS loader to exercise the UEFI ExitBootServices transition.
    Finally, you will validate the build by booting it on the RD-N2 FVP. Tools referenced include
    Docker, Arm Ecosystem FVPs, Arm Development Studio, and Runbook. Prerequisites include familiarity
    with the Reference Design software stack architecture and the Linux command line, plus optional
    Docker basics. Expect to allocate 64GB disk and 32GB RAM (48GB recommended) and about 30 minutes
    to complete.
  faqs:
  - question: Which host platforms and OS versions can I use?
    answer: >-
      Use either an AArch64 or x86_64 host machine running Ubuntu Linux 22.04. Other host operating
      systems are not listed.
  - question: How much disk space and memory do I need to sync and build the software stack?
    answer: >-
      Allocate at least 64 GB of free disk space and 32 GB of RAM. 48 GB of RAM is recommended
      for the build.
  - question: How do I launch the build environment and start the build?
    answer: >-
      Launch the container using the provided script (for example: bash ./container-scripts/container.sh
      -v /home/ubuntu/rd-infra/ run). Then run the build script from the build-scripts/ directory
      inside the container as instructed in the steps.
  - question: Which FVP should I download for testing, and how do I install it?
    answer: >-
      Download the Neoverse N2 Reference Design FVP from Arm Ecosystem FVPs, for example with:
      wget https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Neoverse-Infrastructure/RD-N2/FVP_RD_N2_11.25_23_Linux64.tgz.
      Unpack it (tar -xf …) and run the installer with: ./FVP_RD_N2.sh --i-agree-to-the-contained-eula
      --no-interactive, then export the path to the model binary in the MODEL environment variable.
  - question: What result should I expect when I test the firmware on the FVP?
    answer: >-
      The firmware implementation should build and boot on the RD‑N2 FVP into a lightweight BusyBox
      shell. This path exercises the UEFI ExitBootServices transition to validate the firmware
      stack.
# END generated_summary_faq

author: 
    - Tom Pilar
    - Daniel Nguyen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - FVP
    - Arm Development Studio
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Neoverse Reference Design Platform Software Documentation
        link: https://neoverse-reference-design.docs.arm.com/en/latest/index.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

