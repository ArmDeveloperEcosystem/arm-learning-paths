---
title: Learn how to create a virtual machine in a Realm using Arm Confidential Compute Architecture (CCA)

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers who want to learn about Arm Confidential Compute Architecture (CCA).

learning_objectives:
    - Understand the reference software stack used in Arm CCA
    - Build and run the software stack on an Armv-A AEM Base FVP platform with support for RME extensions
    - Create a virtual machine in a Realm running guest Linux

prerequisites:
    - An aarch64 or x86_64 computer running Ubuntu 22.04. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - If you use a client application to access your computer running Ubuntu, make sure that X11 forwarding is enabled.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:02:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 180803cf9c6e34c0dda76cafdfcd0ce67edfaca4563f57ae0c36bfefd2199ae9
  summary_generated_at: '2026-06-02T05:04:08Z'
  summary_source_hash: 180803cf9c6e34c0dda76cafdfcd0ce67edfaca4563f57ae0c36bfefd2199ae9
  faq_generated_at: '2026-06-03T02:02:26Z'
  faq_source_hash: 180803cf9c6e34c0dda76cafdfcd0ce67edfaca4563f57ae0c36bfefd2199ae9
  summary: >-
    Build and run the Arm Confidential Compute Architecture (CCA) reference software stack on
    an Armv-A AEM Base FVP with RME support, then create a guest Linux virtual machine inside
    a Realm. This introductory path targets developers exploring CCA and uses GCC, FVP, RME, CCA,
    and a Runbook. You will work on Ubuntu 22.04 on aarch64 or x86_64, including cloud instances,
    with X11 forwarding enabled if you access the machine via a client application. Allocate at
    least 30 GB of free disk space and install git, gcc, telnet, xterm, net-tools, and build-essential.
    Estimated time to complete is about two hours.
  faqs:
  - question: What do I need on my Ubuntu host before building the Arm CCA stack?
    answer: >-
      Use Ubuntu 22.04 on aarch64 or x86_64 with at least 30 GB of free disk space. Install git,
      gcc, telnet, xterm, net-tools, and build-essential before starting.
  - question: Which FVP should I use to run the CCA stack?
    answer: >-
      Use the Armv-A AEM Base FVP with support for RME extensions. The steps in the path specify
      the required FVP configuration.
  - question: Can I complete this Learning Path on a cloud instance?
    answer: >-
      Yes. Cloud instances can be used; the path links to a list of Arm cloud service providers.
  - question: Do I need to enable X11 forwarding?
    answer: >-
      Enable X11 forwarding if you use a client application to access your Ubuntu machine. This
      supports any steps that open X11 applications such as xterm.
  - question: What outcome should I expect when everything runs correctly?
    answer: >-
      You will build and run the Arm CCA reference software stack on the FVP and create a Realm
      that hosts a guest Linux virtual machine. This demonstrates the CCA flow from build to launching
      a Realm-based VM.
# END generated_summary_faq

author: Pareena Verma

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

