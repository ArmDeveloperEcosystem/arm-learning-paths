---
title: Develop Arm automotive software on the System76 Thelio Astra

description: Learn how to build and run the Arm Automotive Solutions Software Reference Stack locally on the System76 Thelio Astra desktop using Multipass virtualization and Yocto build tools.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for automotive developers interested in local development using the System76 Thelio Astra Linux desktop computer. 

learning_objectives:
    - Create an efficient automotive development environment on the System76 Thelio Astra desktop. 
    - Build and run the Arm Automotive Solutions Software Reference Stack locally.

prerequisites:
    - A System76 Thelio Astra desktop computer running Ubuntu 24.04.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-24T15:36:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  summary_generated_at: '2026-06-24T15:36:29Z'
  summary_source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  faq_generated_at: '2026-06-24T15:36:29Z'
  faq_source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  summary: >-
    In this Learning Path, you'll use a System76 Thelio Astra Arm desktop to build and run the
    Arm Automotive Solutions Software Reference Stack in a local Multipass virtual machine. You'll
    create an Ubuntu 20.04 guest, isolate builds, and compile Yocto-based
    components targeting a Fixed Virtual Platform that models the Arm Reference Design-1 AE. You'll review the Thelio Astra platform and the software stack context, then run a Parsec-enabled TLS demo that establishes an HTTPS session to transfer a web page.
  faqs:
  - question: Which Multipass install guide should I follow before creating the virtual machine?
    answer: >-
      Use the Multipass install guide for Arm Linux before starting the steps. This ensures Multipass
      is set up correctly on the Thelio Astra running Ubuntu.
  - question: Which Ubuntu release runs inside the Multipass virtual machine for this build?
    answer: >-
      The build is performed from the command line of an Ubuntu 20.04 Multipass virtual machine.
  - question: Why use a Multipass virtual machine on the Thelio Astra instead of building directly on the host?
    answer: >-
      A Multipass VM creates an isolated automotive development environment and lets you split
      the resources of the Thelio Astra between development tasks. It keeps the build and test
      process contained.
  - question: What target platform is used when running the software stack examples?
    answer: >-
      The examples run on a Fixed Virtual Platform that models the Arm Reference Design‑1 AE (RD‑1
      AE) hardware system.
  - question: What result should I expect from the Parsec-enabled TLS demo?
    answer: >-
      The demo establishes an HTTPS session and transfers a simple web page over a TLS connection.
      Parsec provides the common API to the underlying security and cryptographic services used
      by the demo.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Multipass
    - Yocto
    - Docker
    - Git

further_reading:
    - resource:
        title: Arm Automotive Solutions Documentation
        link: https://arm-auto-solutions.docs.arm.com/en/v1.1/index.html
        type: documentation
    - resource:
        title: Parsec 
        link: https://parsec.community/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

