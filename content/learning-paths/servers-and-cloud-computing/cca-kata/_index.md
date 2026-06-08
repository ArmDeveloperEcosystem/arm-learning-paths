---
title: Run Confidential Containers with encrypted images using Arm CCA and Trustee
description: Learn how to deploy Confidential Containers from encrypted images inside Arm CCA Realms using Trustee services for attestation-based authorization on an FVP with RME support.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to understand how Confidential Containers run in Arm CCA Realms.

learning_objectives:
  - Gain an overview of Confidential Containers and their role in confidential computing
  - Understand how Trustee services are used with Arm CCA attestation to authorize and unlock confidential workloads
  - Deploy a Confidential Container from an encrypted image inside an Arm CCA Realm using an Armv9-A AEM Base Fixed Virtual Platform (FVP) with RME support

prerequisites:
  - An AArch64 or x86_64 computer running Linux or macOS. Cloud-based instances can also be used; see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/)
  - Completion of the [Run an end-to-end Attestation with Arm CCA and Trustee](/learning-paths/servers-and-cloud-computing/cca-trustee) Learning Path

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:31:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  summary_generated_at: '2026-06-02T03:19:07Z'
  summary_source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  faq_generated_at: '2026-06-03T00:31:07Z'
  faq_source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  summary: >-
    Learn to deploy a Confidential Container from an encrypted image inside an Arm CCA Realm using
    Trustee for attestation-based authorization. Working on the Armv9-A AEM Base Fixed Virtual
    Platform (FVP) with RME support, you will start the Trustee services (AS, KBS, RVPS) and a
    local Docker registry, publish an encrypted image, then launch and verify the container running
    in a Realm. The path includes an overview of Confidential Containers and how Arm CCA attestation
    integrates with Trustee. Prerequisites are an AArch64 or x86_64 Linux or macOS host (cloud
    instances are acceptable) and completion of the prior CCA + Trustee attestation path. Tools
    include FVP, RME, CCA, Docker, Veraison, Trustee, and Kata Containers.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an AArch64 or x86_64 computer running Linux or macOS; a cloud-based instance is also
      acceptable. Complete the “Run an end-to-end Attestation with Arm CCA and Trustee” Learning
      Path first.
  - question: Which platform does the container run on in this workflow?
    answer: >-
      The container runs on an Armv9-A AEM Base FVP with RME support. The procedure is FVP-based
      and does not specify running on physical hardware.
  - question: Which services must be started before launching the confidential container?
    answer: >-
      Start the Trustee services (AS, KBS, RVPS) and a local Docker registry. The steps also guide
      you to install Docker if it is not already present.
  - question: How do I create and publish the encrypted container image?
    answer: >-
      Follow the steps to encrypt the image and push it to the local Docker registry. The Learning
      Path provides the exact sequence to publish the encrypted image.
  - question: How do I know the container is running inside an Arm CCA Realm?
    answer: >-
      After launching the workload, the Learning Path includes a verification step to confirm
      it is running inside an Arm CCA Realm. Follow those checks to validate success.
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
  - Confidential Containers
  - Kata Containers

further_reading:
  - resource:
      title: Arm Confidential Compute Architecture
      link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
      type: website
  - resource:
      title: Arm Confidential Compute Architecture Open-Source enablement
      link: https://www.youtube.com/watch?v=JXrNkYysuXw
      type: video
  - resource:
      title: Learn the architecture - Realm Management Extension
      link: https://developer.arm.com/documentation/den0126
      type: documentation
  - resource:
      title: Realm Management Monitor Specification
      link: https://developer.arm.com/documentation/den0137/latest/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

