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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:28:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  summary_generated_at: '2026-06-01T20:58:28Z'
  summary_source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  faq_generated_at: '2026-06-02T21:28:14Z'
  faq_source_hash: 2b758d2dcf28a683ab164e28578a736d6d730b81dfbc01a6765619052fcdebd0
  summary: >-
    This Learning Path shows how to set up a local automotive software development environment
    on the Arm-based System76 Thelio Astra and build the Arm Automotive Solutions Software Reference
    Stack. You will install Multipass on Ubuntu 24.04, create an Ubuntu 20.04 virtual machine,
    and use Yocto, Docker, and Git to build the stack from the VM. The path introduces the Arm
    Reference Design-1 AE (RD-1 AE) target, modeled by a Fixed Virtual Platform, and includes
    running example applications such as a Parsec-enabled TLS demo. By the end, you will have
    built and run the stack locally in a VM on Thelio Astra; no additional prerequisites beyond
    the host hardware are listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a System76 Thelio Astra desktop computer running Ubuntu 24.04. Before starting,
      install Multipass using the Multipass install guide for Arm Linux. The path uses Multipass,
      Yocto, Docker, and Git; no other prerequisites are explicitly listed.
  - question: Which Ubuntu version should I use inside the Multipass VM?
    answer: >-
      The build steps use an Ubuntu 20.04 Multipass virtual machine. Multipass creates a cloud-style
      VM on your desktop to isolate build and test tasks and split system resources.
  - question: How do I begin the build of the Arm Automotive Solutions Software Reference Stack?
    answer: >-
      From the Ubuntu 20.04 Multipass VM, create a working directory and clone the repository
      as shown in the steps. A successful clone without errors indicates the environment is ready
      for the Yocto-based build process.
  - question: Can I run the demos without RD-1 AE hardware?
    answer: >-
      Yes. The example applications demonstrate the software stack running on a Fixed Virtual
      Platform that models the reference hardware system.
  - question: What result should I expect from the Parsec demo?
    answer: >-
      The Parsec-enabled TLS demo illustrates an HTTPS session where a simple web page is transferred
      over a TLS connection. This demonstrates use of Parsec’s common API to access security and
      cryptographic services in the stack.
# END generated_summary_faq

author: Jason Andrews

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

