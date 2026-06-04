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
  - Completion of the [Get started with CCA attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison) Learning Path
  - Completion of the [Run an end-to-end attestation flow with Arm CCA](/learning-paths/servers-and-cloud-computing/cca-essentials/) Learning Path

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:31:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 563456f5d151c7ef59bf458f6ac971c321077475a0a78d3b5a3885b97157ba9e
  summary_generated_at: '2026-06-02T03:20:03Z'
  summary_source_hash: 563456f5d151c7ef59bf458f6ac971c321077475a0a78d3b5a3885b97157ba9e
  faq_generated_at: '2026-06-03T00:31:41Z'
  faq_source_hash: 563456f5d151c7ef59bf458f6ac971c321077475a0a78d3b5a3885b97157ba9e
  summary: >-
    This Learning Path shows how to run an end-to-end attestation flow using Arm Confidential
    Computing Architecture (CCA) and Trustee services. On a Linux or macOS host (AArch64 or x86_64),
    you will use an Armv9-A AEM Base Fixed Virtual Platform (FVP) with RME extensions to launch
    a Linux realm, deploy a simple workload, and connect it to Trustee services (AS, KBS, RVPS)
    with Docker. You will generate attestation evidence, see an initial secret request fail under
    policy, endorse the realm initial measurement (RIM), re-attest, and retrieve the secret. Prerequisites
    include completing the CCA attestation and Veraison and CCA end-to-end Learning Paths. Estimated
    time: 60 minutes.
  faqs:
  - question: What do I need before running the exercises?
    answer: >-
      You need an AArch64 or x86_64 computer running Linux or macOS. Complete the “Get started
      with CCA attestation and Veraison” and “Run an end-to-end attestation flow with Arm CCA”
      Learning Paths first.
  - question: Can I use a cloud instance as the host machine?
    answer: >-
      Yes. You can use cloud instances; see the Arm cloud service providers link referenced in
      the prerequisites.
  - question: Which FVP and realm environment does this path use?
    answer: >-
      You will deploy a simple workload in a CCA realm on an Armv9-A AEM Base FVP that has support
      for RME extensions. The target compute environment is a Linux realm.
  - question: Which Trustee components are started during the flow?
    answer: >-
      You will run the Trustee services: AS, KBS, and RVPS. These are used in the attestation
      flow and policy-controlled secret release.
  - question: What result should I expect when I request a secret?
    answer: >-
      The first request intentionally fails due to attestation policy. After endorsing the realm
      initial measurement (RIM) and re-attesting, the request succeeds and the secret is retrieved.
# END generated_summary_faq

author:
  - Anton Antonov

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

