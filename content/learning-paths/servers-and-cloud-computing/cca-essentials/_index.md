---
title: Run an end-to-end Attestation Flow with Arm CCA
description: Learn how to deploy a CCA realm on an FVP with RME support and connect it with attestation services to create an end-to-end confidential computing workflow.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers who want to learn how to run an end-to-end attestation flow with Arm's Confidential Computing Architecture (CCA).  

learning_objectives:
     - Describe how you can use attestation with Arm's Confidential Computing Architecture (CCA).
     - Deploy a simple workload in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support for RME extensions. 
     - Connect the workload with additional software services to create an end-to-end example that uses attestation to unlock the confidential processing of data.

prerequisites:
    - An AArch64 or x86_64 computer running Linux. You can use cloud instances, see this list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison) Learning Path.
    - Completion of the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:30:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b032debbdfe82cbd017812cf671907520b146fd8684afce0c45c91e7f2287e18
  summary_generated_at: '2026-06-02T03:18:08Z'
  summary_source_hash: b032debbdfe82cbd017812cf671907520b146fd8684afce0c45c91e7f2287e18
  faq_generated_at: '2026-06-03T00:30:18Z'
  faq_source_hash: b032debbdfe82cbd017812cf671907520b146fd8684afce0c45c91e7f2287e18
  summary: >-
    This advanced Learning Path guides you through running an end-to-end attestation flow with
    Arm’s Confidential Computing Architecture (CCA). You will deploy a simple workload inside
    a confidential Linux realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) with Realm
    Management Extension (RME) support, then connect it to attestation services so confidential
    data is released only after the realm’s isolation is assessed. Using Docker and Veraison,
    you will run a minimal, educational Key Broker Server (KBS) and integrate it with the realm.
    A Linux host (AArch64 or x86_64) is required, and prior completion of the CCA attestation/Veraison
    and CCA realm application Learning Paths is expected.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Linux computer on AArch64 or x86_64; cloud instances are acceptable. You must
      also complete the “Get Started with CCA Attestation and Veraison” and “Run an application
      in a Realm using the Arm Confidential Computing Architecture (CCA)” Learning Paths.
  - question: Which FVP and Arm features does the example require?
    answer: >-
      Use the Armv9-A AEM Base Fixed Virtual Platform (FVP) with support for RME extensions. The
      target compute environment is a Linux realm.
  - question: How do I run the Key Broker Server (KBS) used in this path?
    answer: >-
      A pre-built Docker container image for the KBS is provided, and you will pull the image
      and run the container. The KBS comes from the Veraison project and is intentionally minimal
      for educational use, not for production.
  - question: What result should I expect when attestation succeeds?
    answer: >-
      Attestation assesses whether the realm offers a provable level of confidential isolation.
      When it succeeds, confidential data can be released to the Linux realm for processing as
      part of the end-to-end flow.
  - question: How long does this take and which tools will I use?
    answer: >-
      The estimated time to complete is about 120 minutes. You will use GCC, FVP, RME, CCA, Docker,
      Veraison, and a runbook on a Linux host.
# END generated_summary_faq

author: 
    - Arnaud de Grandmaison
    - Paul Howard
    - Pareena Verma

### Tags
skilllevels: Advanced
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
    - Veraison
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

