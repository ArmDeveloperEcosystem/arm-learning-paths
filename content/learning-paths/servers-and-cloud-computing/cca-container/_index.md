---
title: Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)
description: Learn how to run the Arm CCA reference software stack on an FVP with RME support, create a Realm virtual machine, and obtain attestation tokens for confidential computing.

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers who want to learn how to run their applications in a Realm using the Arm Confidential Compute Architecture (CCA).

learning_objectives:
    - Run the Arm reference CCA software stack on an Armv-A AEM Base FVP (Fixed Virtual Platform) with support for RME extensions.
    - Create a virtual machine in a Realm running guest Linux using a pre-built docker container.
    - Run a simple application in a Realm running guest Linux.
    - Obtain a CCA attestation token from the virtual guest in a Realm.
    - Run the CCA software stack using MEC (Memory Encryption Contexts)

prerequisites:
    - An AArch64 or x86_64 computer running Linux or macOS. You can use cloud instances, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:28:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  summary_generated_at: '2026-06-02T03:16:50Z'
  summary_source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  faq_generated_at: '2026-06-03T00:28:52Z'
  faq_source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  summary: >-
    This Learning Path shows how to bring up the Arm Confidential Compute Architecture (CCA) reference
    software stack on an Armv-A AEM Fixed Virtual Platform (FVP) with Realm Management Extension
    (RME) support using a pre-built Docker image (armswdev/cca-learning-path:cca-simulation-v3).
    You will create a Realm that runs a guest Linux virtual machine, inject and run a simple application
    inside that Realm, and obtain a CCA attestation token from the guest. You also run the CCA
    stack with Memory Encryption Contexts (MEC). The path targets developers on AArch64 or x86_64
    hosts running Linux or macOS and is introductory, with an estimated completion time of about
    120 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an AArch64 or x86_64 computer running Linux or macOS and install Docker Engine. You
      can use cloud instances; a list of Arm cloud service providers is referenced.
  - question: Which Docker image should I pull, and how do I verify it downloaded?
    answer: >-
      Pull armswdev/cca-learning-path:cca-simulation-v3. Verify with docker image list and check
      that the image appears with its ID and sizes.
  - question: What runs inside the Realm, and what result should I expect regarding attestation?
    answer: >-
      A guest Linux virtual machine runs inside the Realm. As part of the steps, you will obtain
      a CCA attestation token from the virtual guest.
  - question: How do I run my own application inside the Realm in this example?
    answer: >-
      Inject the application into the guest filesystem of the Realm. The path demonstrates this
      with a simple hello application that runs under the Realm’s protections.
  - question: When do I use Memory Encryption Contexts (MEC), and what does it change?
    answer: >-
      The MEC section shows how to run the CCA software stack using MEC after downloading the
      same container. MEC extends RME to support multiple encryption contexts in the Realm Physical
      Address Space, with each access tagged by a MECID.
# END generated_summary_faq

author:
    - Pareena Verma
    - Arnaud de Grandmaison

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
    - Docker
    - Runbook


further_reading:
    - resource:
        title: Learn the architecture - Introducing Arm Confidential Compute Architecture
        link: https://developer.arm.com/documentation/den0125
        type: documentation
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
    - resource:
        title: Realm Management Monitor specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

