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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:40:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  summary_generated_at: '2026-06-30T21:40:49Z'
  summary_source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  faq_generated_at: '2026-06-30T21:40:49Z'
  faq_source_hash: 3947ebbac742399e70001e41ac5face92819bed0deb55aba3e2414f98432023e
  summary: >-
    You'll run the Arm Confidential Compute Architecture (CCA) reference
    software stack on an Armv‑A AEM Base FVP with Realm Management Extension (RME) support using
    a pre-built Docker image. First, you'll boot a guest Linux virtual machine as a Realm, then inject
    and run a simple application inside that Realm so the program inherits the Realm’s confidential
    protections. You'll also obtain a CCA attestation token from the Realm guest and learn about Memory Encryption Contexts (MEC) and how the CCA stack can
    run with multiple encryption contexts in the Realm Physical Address Space. By the end, you'll
    see the Realm guest launch, run the injected app, and produce an attestation token.
  faqs:
  - question: Which Docker image does this path use, and how do I confirm it downloaded?
    answer: >-
      Pull `armswdev/cca-learning-path:cca-simulation-v3`. Run `docker image list` and check that
      this repository and tag appear in the output.
  - question: What result should I expect when the Realm guest virtual machine starts?
    answer: >-
      The guest virtual machine (VM) should boot as a Realm and run guest Linux. Continue when the
      VM is up and ready for the application injection step.
  - question: How do I place the sample application inside the Realm?
    answer: >-
      Inject the application into the guest filesystem as shown in the steps. Verify inside the
      guest that the file exists and is executable, then run it to confirm expected output.
  - question: Where do I retrieve the CCA attestation token in this workflow?
    answer: >-
      Request the token from inside the virtual guest running in the Realm. Follow the path step
      to capture the token and confirm that a token is returned.
  - question: What changes when running with Memory Encryption Contexts (MEC)?
    answer: >-
      Use the MEC section to run the CCA stack with multiple encryption contexts in the Realm
      Physical Address Space, identified by a MECID. The example follows the same Realm guest
      and application flow while enabling MEC.
# END generated_summary_faq

author:
    - Pareena Verma
    - Arnaud de Grandmaison

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

