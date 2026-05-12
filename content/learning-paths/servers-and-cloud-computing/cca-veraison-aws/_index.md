---
title: Build a CCA Attestation Service on AWS with Veraison
description: Learn how to deploy a scalable Arm CCA attestation verifier service on AWS using Veraison components with platform endorsement provisioning.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for developers familiar with CCA attestation and the Veraison project. You'll learn how to deploy a scalable CCA attestation verifier service on AWS.

learning_objectives:
    - Build an attestation service on AWS using the Veraison project's components.
    - Set up Veraison as a verifier for Arm CCA attestation tokens by provisioning CCA platform endorsements.

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) with access to AWS services.
    - An x86 computer running Ubuntu or Arch Linux, authorized for AWS access. If you're using another build environment, you'll need to configure the toolchains for cross-compilation.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 55b8032ceaf735d53b1157102a3a1da5aa5cb686e9ec51cf4896ded66d9bf263
  summary: >-
    Learn how to deploy a scalable Arm CCA attestation verifier service on AWS using Veraison
    components with platform endorsement provisioning. It is designed for developers familiar
    with CCA attestation and the Veraison project. You'll learn how to deploy a scalable CCA attestation
    verifier service on AWS. By the end, you will be able to build an attestation service on AWS
    using the Veraison project's components and set up Veraison as a verifier for Arm CCA attestation
    tokens by provisioning CCA platform endorsements. It focuses on tools and technologies such
    as CCA, RME, and Runbook, Linux environments, Arm platforms including Neoverse and Cortex-A,
    and cloud platforms such as AWS. The main steps cover Overview, Prepare AWS Account, Create
    the Domain and Certificate, Create the Veraison Deployment, and Add CCA Platform Endorsements
    to Veraison.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build an attestation service on AWS using the Veraison project's components and
      set up Veraison as a verifier for Arm CCA attestation tokens by provisioning CCA platform
      endorsements. Learn how to deploy a scalable Arm CCA attestation verifier service on AWS
      using Veraison components with platform endorsement provisioning.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for developers familiar with CCA attestation and the Veraison project.
      You'll learn how to deploy a scalable CCA attestation verifier service on AWS.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/)
      with access to AWS services.; An x86 computer running Ubuntu or Arch Linux, authorized for
      AWS access. If you're using another build environment, you'll need to configure the toolchains
      for cross-compilation.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CCA, RME, and Runbook, Linux environments, Arm platforms
      such as Neoverse and Cortex-A, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Prepare AWS Account, Create the Domain and
      Certificate, Create the Veraison Deployment, and Add CCA Platform Endorsements to Veraison.
# END generated_summary_faq

author: Paul Howard

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CCA
    - RME
    - Runbook

further_reading:
    - resource:
        title: RATS architecture (RFC 9334) 
        link: https://datatracker.ietf.org/doc/rfc9334/
        type: documentation
    - resource:
        title: The Realm Management Monitor Specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation
    - resource:
        title: The Attestation Results for Secure Interactions (AR4SI) 
        link: https://datatracker.ietf.org/doc/draft-ietf-rats-ar4si/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

