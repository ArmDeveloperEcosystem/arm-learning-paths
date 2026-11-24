---
title: Create a Realm VM with Arm Confidential Compute Architecture

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers who want to learn about Arm Confidential Compute Architecture (CCA).

learning_objectives:
    - Identify the reference software stack used in Arm CCA.
    - Build and run the software stack on an Armv-A AEM Base Fixed Virtual Platform (FVP) with support for Realm Management Extension (RME) extensions.
    - Create a virtual machine in a Realm running guest Linux.

prerequisites:
    - An aarch64 or x86_64 computer running Ubuntu 22.04, or a [cloud instance](/learning-paths/servers-and-cloud-computing/csp/)
    - X11 forwarding enabled, if you use a client application to access your computer running Ubuntu

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:56:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1b33ce1d5faf924adbda49326317102c8b45c03a63937bb7a19b661cda2439b8
  summary_generated_at: '2026-11-23T20:56:20Z'
  summary_source_hash: 1b33ce1d5faf924adbda49326317102c8b45c03a63937bb7a19b661cda2439b8
  faq_generated_at: '2026-11-23T20:56:20Z'
  faq_source_hash: 1b33ce1d5faf924adbda49326317102c8b45c03a63937bb7a19b661cda2439b8
  summary: You'll build the Arm CCA reference stack and create a Realm
    guest on an Arm FVP. First, you'll prepare the build environment and compile
    the stack. You'll then launch the model and connect to its consoles to inspect the host software.
    Finally, you'll create the Realm and boot a Linux guest inside it.
  faqs:
  - question: Does starting the FVP also start the Realm guest?
    answer: No. Starting the Fixed Virtual Platform (FVP) boots the host software stack. After it's running, use `lkvm
      run --realm` in the model environment to create a Realm and boot its Linux guest.
  - question: Which packages are needed for the build and model consoles?
    answer: Install `git`, `gcc`, `telnet`, and `xterm`, as well as `net-tools` and `build-essential`. They supply source control, build tools, and console utilities.
  - question: How much free disk space should I have before building?
    answer: Check that you have at least 30 GB of free disk space before starting the build.
  - question: Which model variant do I need for Realm features?
    answer: Use the Armv-A AEM Base FVP variant with Realm Management Extension support.
  - question: What if I use SSH and no console windows appear?
    answer: Reconnect with X11 forwarding enabled. X11 forwarding is required for displaying the model
      console windows.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse 
operatingsystems:
    - Linux 
tools_software_languages:
    - GCC
    - FVP
    - RME
    - CCA
    - Runbook

further_reading:
    - resource:
        title: Arm Confidential Compute Architecture
        link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
        type: website
    - resource:
        title: Arm Confidential Compute Architecture open source enablement
        link: https://www.youtube.com/watch?v=JXrNkYysuXw
        type: video
    - resource:
        title: Learn the architecture - Realm Management Extension
        link: https://developer.arm.com/documentation/den0126
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

