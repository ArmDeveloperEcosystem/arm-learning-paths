---
title: Understand Arm Pointer Authentication

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in understanding Arm Pointer Authentication.

learning_objectives:
    - Create a simple application on an Arm server with Pointer Authentication
    - Compile the application with and without Pointer Authentication to inspect the instructions generated
    - Exploit the applications with and without Pointer Authentication to demonstrate how Pointer Authentication instructions enhance security.

prerequisites:
    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If needed, review [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) to learn how to deploy Arm in the cloud. These learning paths also point to more advanced learning paths that show how to automate the deployment of Arm instances at different cloud providers.
    

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:45:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fa699cafa5c0d998a63de306371bfbe47680c7453b28fc4b35d4fe2671902b23
  summary_generated_at: '2026-06-02T04:45:16Z'
  summary_source_hash: fa699cafa5c0d998a63de306371bfbe47680c7453b28fc4b35d4fe2671902b23
  faq_generated_at: '2026-06-03T01:45:44Z'
  faq_source_hash: fa699cafa5c0d998a63de306371bfbe47680c7453b28fc4b35d4fe2671902b23
  summary: >-
    Use a Linux Arm server to explore Arm Pointer Authentication (PAC) by building and analyzing
    a small, vulnerable C program. You will compile the application with and without PAC, inspect
    the generated instructions, and use pwntools to exploit the non-PAC binary (main_nopac) to
    redirect control flow to an unintended function that launches a shell, then compare behavior
    with PAC enabled to see how the protection changes the outcome. This advanced path targets
    Arm-based instances in the cloud or on-premise and takes about 30 minutes. Prerequisite: access
    to an Arm-based instance; if needed, consult the referenced Get started with Arm-based cloud
    instances learning paths.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to a Linux Arm-based instance from a cloud provider or an on‑prem Arm server.
      No other prerequisites are explicitly listed.
  - question: Can I use any cloud provider for the Arm instance?
    answer: >-
      Yes. You can use an Arm-based instance from AWS, Microsoft Azure, Google Cloud, or Oracle,
      or use an on‑prem Arm server.
  - question: Which tools do I install to run the exploit code?
    answer: >-
      Install pwntools and its dependencies as shown in the steps. The path uses Python 3 and
      pip to set up pwntools.
  - question: Which binary should I target when running the exploit?
    answer: >-
      Target the application built without Pointer Authentication, referred to as main_nopac in
      the steps.
  - question: What result should I expect when the exploit works, and how do I compare with Pointer
      Authentication enabled?
    answer: >-
      A successful exploit will execute func2(), print "Hello from func2!", and spawn a shell.
      Then build the Pointer Authentication version and follow the steps to inspect the generated
      instructions and compare behavior.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Runbook


further_reading:
    - resource:
        title: Learn the architecture - Providing protection for complex software
        link: https://developer.arm.com/documentation/102433
        type: documentation
    - resource:
        title: Code reuse attacks - the compiler story
        link: https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/code-reuse-attacks-the-compiler-story
        type: blog
    - resource:
        title: Arm A-profile Instruction Set Architecture
        link: https://developer.arm.com/documentation/ddi0602
        type: documentation
    - resource:
        title: pwntools Documentation
        link: https://docs.pwntools.com/en/stable/
        type: documentation
    - resource:
        title: -mbranch-protection (armclang)
        link: https://developer.arm.com/documentation/101754/0620/armclang-Reference/armclang-Command-line-Options/-mbranch-protection
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

