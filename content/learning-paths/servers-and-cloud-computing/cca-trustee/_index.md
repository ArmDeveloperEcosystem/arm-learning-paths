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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 563456f5d151c7ef59bf458f6ac971c321077475a0a78d3b5a3885b97157ba9e
  summary: >-
    Learn how to deploy a CCA realm workload on an FVP and connect it with Trustee services to
    enable attestation-based confidential data processing. It is designed for software developers
    who want to run an end-to-end attestation flow using Arm Confidential Compute Architecture
    (CCA) and Trustee services. By the end, you will be able to describe how you can use attestation
    with Arm's Confidential Computing Architecture (CCA) and Trustee services, deploy a simple
    workload in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support
    for RME extensions, and connect the workload with Trustee services to create an end-to-end
    example that uses attestation to unlock the confidential processing of data. It focuses on
    tools and technologies such as FVP, RME, CCA, Docker, and Veraison, Linux and macOS environments,
    and Arm platforms including Neoverse and Cortex-A. The main steps cover Architecture overview
    for Arm CCA Attestation with Trustee and Run an end-to-end Attestation with Arm CCA and Trustee.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe how you can use attestation with Arm's Confidential Computing Architecture
      (CCA) and Trustee services, deploy a simple workload in a CCA realm on an Armv9-A AEM Base
      Fixed Virtual Platform (FVP) that has support for RME extensions, and connect the workload
      with Trustee services to create an end-to-end example that uses attestation to unlock the
      confidential processing of data. Learn how to deploy a CCA realm workload on an FVP and
      connect it with Trustee services to enable attestation-based confidential data processing.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for software developers who want to run an end-to-end attestation
      flow using Arm Confidential Compute Architecture (CCA) and Trustee services.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AArch64 or x86_64 computer running
      Linux or macOS; you can use cloud instances - see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/);
      Completion of the [Get started with CCA attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison)
      Learning Path; Completion of the [Run an end-to-end attestation flow with Arm CCA](/learning-paths/servers-and-cloud-computing/cca-essentials/)
      Learning Path.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including FVP, RME, CCA, Docker, and Veraison, Linux and macOS
      environments, and Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Architecture overview for Arm CCA Attestation with
      Trustee and Run an end-to-end Attestation with Arm CCA and Trustee.
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

