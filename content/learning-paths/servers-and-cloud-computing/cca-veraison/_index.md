---
title: Get Started with CCA Attestation and Veraison
description: Learn how to inspect and verify Arm CCA attestation tokens using command-line tools and the open-source Veraison attestation verification service.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who would like to learn about attestation in confidential computing, using Arm's Confidential Computing Architecture (CCA). 

learning_objectives:
    - Describe the importance of attestation in confidential computing.
    - Understand what a CCA attestation token is, and describe its format.
    - Inspect the contents of a CCA attestation token using command-line tools.
    - Use an attestation verification service to evaluate a CCA attestation token.
    - Understand the purpose of the Open-Source Veraison project.

prerequisites:
    - An Arm-based or x86 computer running Ubuntu. You can use a server instance from a cloud service provider of your choice.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:44:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  summary_generated_at: '2026-06-30T21:44:15Z'
  summary_source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  faq_generated_at: '2026-06-30T21:44:15Z'
  faq_source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  summary: >-
    You'll learn about CCA attestation by connecting the concepts of confidential computing
    and Arm’s Realm Management Extension to practical token handling. First, you'll start with an overview
    of attestation and Veraison, then obtain an example CCA attestation token
    and set up the required tools by installing Go. You'll inspect the token’s structure using
    command-line workflows, then submit it to a Linaro-hosted verification service implemented
    with Veraison components. By the end, you'll recognize a successful verification response and be able to relate it back to the token
    contents that you inspected.
  faqs:
  - question: Should I remove an existing Go installation before setting up the tools?
    answer: >-
      Yes. The steps direct you to remove any existing Go installation before downloading and
      extracting the specified Go release and updating your PATH.
  - question: What can I verify locally before using the online verification service?
    answer: >-
      You can inspect the example CCA attestation token with command-line workflows to review
      its data and format. This helps you understand what the service will evaluate.
  - question: How do I know the token I’m using is supported by the verifier?
    answer: >-
      The verifier targets pre-silicon CCA platforms, such as emulated Arm platforms like FVP.
      The example token provided in this exercise is suitable for this service.
  - question: What result should I expect after submitting a token to the verification service?
    answer: >-
      You should receive a verification response from the Veraison-based service indicating the
      evaluation outcome. Use that result to confirm the token’s validity for the targeted pre-silicon
      environment.
  - question: Do I need access to CCA hardware to follow this Learning Path?
    answer: >-
      No. You'll use an example token and a publicly available verifier for emulated pre-silicon
      CCA platforms hosted by Linaro.
# END generated_summary_faq

author: Paul Howard

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
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

