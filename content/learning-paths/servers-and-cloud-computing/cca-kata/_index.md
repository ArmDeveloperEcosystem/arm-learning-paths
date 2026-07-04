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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:42:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  summary_generated_at: '2026-06-30T21:42:36Z'
  summary_source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  faq_generated_at: '2026-06-30T21:42:36Z'
  faq_source_hash: 649957b07b2bde05bc11047bd12bfc4f697c1a55eef1c3a25b5fafc95cda893d
  summary: >-
    You'll deploy a confidential container from an encrypted
    image inside an Arm CCA Realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) with Realm Management Extension (RME) support.
    First, you'll learn about the Confidential Containers design, understand which components run inside the
    Trusted Execution Environment, and see how Trustee services use Arm CCA
    attestation to authorize decryption. Then, you'll start the Trustee services and a local Docker
    registry, publish an encrypted image, and launch the container on the FVP. By the end, you'll confirm attestation, key release, and that the workload runs in a Realm only
    after authorization.
  faqs:
  - question: How do I know the Trustee services are ready before pushing the image?
    answer: >-
      Confirm that the AS, KBS, and RVPS processes have started and are listening. Check their
      startup logs for ready or healthy messages before continuing.
  - question: Which registry should I use when publishing the encrypted image?
    answer: >-
      Use the local Docker registry started as part of this Learning Path. Tag the encrypted image
      for that registry and push, and proceed only after the push completes without errors.
  - question: What result should I expect when launching the confidential container on the FVP?
    answer: >-
      The runtime pulls the encrypted image from the local registry, performs Arm CCA attestation
      via Trustee, obtains decryption keys, and starts the workload inside an Arm CCA Realm. Expect
      logs indicating successful attestation or authorization and that the container is running.
  - question: How can I verify the container is actually running inside an Arm CCA Realm?
    answer: >-
      Follow the verification step to check Realm-specific output from the launch. Validation
      relies on Trustee accepting CCA attestation evidence; without acceptance, the image remains
      locked and the workload does not start.
  - question: What should I check if the encrypted image fails to pull or decrypt during launch?
    answer: >-
      Verify the local registry is running and reachable and that the image was pushed with the
      expected tag. Confirm AS, KBS, and RVPS are up and that attestation evidence is available
      so the KBS can release keys after authorization.
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

