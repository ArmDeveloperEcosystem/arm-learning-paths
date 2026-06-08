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


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:32:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  summary_generated_at: '2026-06-02T03:20:26Z'
  summary_source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  faq_generated_at: '2026-06-03T00:32:10Z'
  faq_source_hash: 9e6dee3aef79c1c65cc1a1f4fe3528b9c5542d8046f0b059ef703079ef964d77
  summary: >-
    Learn how to work with Arm Confidential Computing Architecture (CCA) attestation by obtaining
    an example CCA attestation token, inspecting its contents with command-line tools on Ubuntu,
    and evaluating it using a publicly hosted Veraison-based verifier from Linaro. The path covers
    key concepts including Trusted Execution Environments and how Armv9 Realm Management Extension
    (RME) provides the secure boundary, then moves into hands-on token formats and workflows.
    You will install the Go language to run the required tools. No explicit prerequisites beyond
    an Arm-based or x86 Ubuntu system are listed, and a cloud instance can be used. In about 30
    minutes, you will be able to parse a CCA token and submit it to an attestation verification
    service, and understand the purpose of the open-source Veraison project.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based or x86 computer running Ubuntu. A server instance from a cloud service
      provider is acceptable. No other explicit prerequisites are listed.
  - question: How do I install Go for this Learning Path?
    answer: >-
      The steps start by removing any existing Go installation, then download and extract Go 1.23.3
      using the provided commands. You then export the installation path and add it to your PATH
      as shown in the instructions.
  - question: What is Veraison used for here?
    answer: >-
      Veraison provides the verification components and tools used to evaluate CCA attestation
      tokens. It originated within Arm and is now an open-source project within the Confidential
      Computing Consortium.
  - question: How do I obtain and inspect the example CCA attestation token?
    answer: >-
      You will obtain an example token in the steps and use command-line tools to inspect its
      contents. This gives hands-on experience with the token format and common attestation data.
  - question: Which service should I use to verify the token, and what tokens does it support?
    answer: >-
      Use the publicly hosted Linaro attestation verifier service for pre-silicon CCA platforms
      such as FVP. It verifies CCA attestation tokens from emulated Arm platforms, including the
      example token used in this exercise.
# END generated_summary_faq

author: Paul Howard

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

