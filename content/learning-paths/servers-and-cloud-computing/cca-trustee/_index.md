---
title: Run an end-to-end attestation flow with Arm CCA and Trustee
description: Learn how to deploy a CCA realm workload on an FVP and connect it with Trustee services to enable attestation-based confidential data processing.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers who want to run an end-to-end attestation flow using Arm Confidential Compute Architecture (CCA) and Trustee services.

learning_objectives:
  - Describe how you can use attestation with Arm's Confidential Computing Architecture (CCA) and Trustee services
  - Deploy a simple workload in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support for RME extensions
  - Connect the workload with Trustee services to create an end-to-end example that uses attestation to unlock the confidential processing of data

prerequisites:
  - An AArch64 or x86_64 computer running Linux or macOS; you can use cloud instances - see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/)
  - Completion of the [Get started with CCA attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/) Learning Path
  - Completion of the [Run an end-to-end attestation flow with Arm CCA](/learning-paths/servers-and-cloud-computing/cca-essentials/) Learning Path

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:43:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7046b0fb5519afea3a779675c948ef0b423678c1feff23be2bd4ba37c19698e8
  summary_generated_at: '2026-06-30T21:43:12Z'
  summary_source_hash: 7046b0fb5519afea3a779675c948ef0b423678c1feff23be2bd4ba37c19698e8
  faq_generated_at: '2026-06-30T21:43:12Z'
  faq_source_hash: 7046b0fb5519afea3a779675c948ef0b423678c1feff23be2bd4ba37c19698e8
  summary: >-
    You'll complete an end-to-end confidential computing attestation
    flow on an Arm Fixed Virtual Platform using Arm Confidential Compute Architecture and Trustee
    services. First, you'll start the Trustee components, launch a Linux realm on an
    Armv9-A FVP with Realm Management Extension (RME), and generate attestation evidence from the realm. After intentionally
    denying the first secret request to see how policy-based gating works, you'll endorse the
    realm initial measurement (RIM), repeat attestation, and retrieve the secret after the environment
    proves its isolation properties. By the end, you'll exercise and validate the complete path from evidence generation to
    policy-controlled secret release.
  faqs:
  - question: What result should I expect from the first secret request?
    answer: >-
      The initial request is expected to fail. The attestation policy blocks secret release until
      the realm initial measurement (RIM) is endorsed.
  - question: How do I know the Trustee services are running correctly before launching the realm?
    answer: >-
      Check the Docker container status and logs for the Trustee services. They should
      start without errors and be ready to accept requests.
  - question: When should I endorse the RIM, and how do I confirm it worked?
    answer: >-
      Endorse the RIM after the first secret request is denied. After endorsement, re-run attestation
      and expect the secret request to succeed.
  - question: How can I verify that the realm generated attestation evidence?
    answer: >-
      The realm run produces evidence that the Attestation Service (AS) processes. Check the output
      and logs for evidence generation and a corresponding response from the AS.
  - question: How do I know the FVP realm is ready before requesting a secret?
    answer: >-
      The Linux realm should complete boot on the FVP and be able to produce attestation evidence.
      If evidence generation fails, resolve that before proceeding to secret requests.
# END generated_summary_faq

author:
  - Anton Antonov

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
  - Neoverse
  - Cortex-A
operatingsystems:
  - Linux
  - macOS
tools_software_languages:
  - FVP
  - RME
  - CCA
  - Docker
  - Veraison
  - Trustee

further_reading:
  - resource:
      title: Arm Confidential Compute Architecture
      link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
      type: website
  - resource:
      title: Arm Confidential Compute Architecture open-source enablement
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

