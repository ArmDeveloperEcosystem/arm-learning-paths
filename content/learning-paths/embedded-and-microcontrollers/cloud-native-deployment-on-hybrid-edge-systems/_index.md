---
title: Deploy firmware on hybrid edge systems using containers

description: Learn how to deploy containerized embedded applications and firmware onto an Arm Cortex-M core from a Cortex-A core using containerd, K3s, and the hybrid-runtime on Arm Virtual Hardware.

minutes_to_complete: 20

who_is_this_for: This learning path is for developers interested in learning how to deploy software (embedded applications and firmware) onto other processors in the system, using Linux running on the application core.

learning_objectives:
    - Deploy a containerized embedded application onto an Arm Cortex-M core from an Arm Cortex-A core using containerd and K3s.
    - Build a firmware container image.
    - Build the hybrid-runtime components.


prerequisites:
    - A valid account with [Arm Virtual Hardware](https://app.avh.arm.com/login)
    - An Arm Linux host machine (if you want to build your own runtime and container image)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 3394bf994039e441d57dced2abb64d725077d4672e0e68dc71f1de50e58f0408
  summary: >-
    Learn how to deploy containerized embedded applications and firmware onto an Arm Cortex-M
    core from a Cortex-A core using containerd, K3s, and the hybrid-runtime on Arm Virtual Hardware.
    It is designed for developers interested in learning how to deploy software (embedded applications
    and firmware) onto other processors in the system, using Linux running on the application
    core. By the end, you will be able to deploy a containerized embedded application onto an
    Arm Cortex-M core from an Arm Cortex-A core using containerd and K3s, build a firmware container
    image, and build the hybrid-runtime components. It focuses on tools and technologies such
    as Docker, Arm Virtual Hardware, K3s, and Containerd, Linux environments, and Arm platforms
    including Cortex-M and Cortex-A. The main steps cover Motivation, Hybrid container runtime,
    AVH device setup, Deploy firmware container using `containerd`, and Deploy SMARTER Demo using
    K3s.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will deploy a containerized embedded application onto an Arm Cortex-M core from an Arm
      Cortex-A core using containerd and K3s, build a firmware container image, and build the
      hybrid-runtime components. Learn how to deploy containerized embedded applications and firmware
      onto an Arm Cortex-M core from a Cortex-A core using containerd, K3s, and the hybrid-runtime
      on Arm Virtual Hardware.
  - question: Who is this Learning Path for?
    answer: >-
      This learning path is for developers interested in learning how to deploy software (embedded
      applications and firmware) onto other processors in the system, using Linux running on the
      application core.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A valid account with [Arm Virtual Hardware](https://app.avh.arm.com/login);
      An Arm Linux host machine (if you want to build your own runtime and container image).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Docker, Arm Virtual Hardware, K3s, and Containerd,
      Linux environments, and Arm platforms such as Cortex-M and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Motivation, Hybrid container runtime, AVH device setup,
      Deploy firmware container using `containerd`, and Deploy SMARTER Demo using K3s.
# END generated_summary_faq

author: Basma El Gaabouri

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-M
    - Cortex-A
tools_software_languages:
    - Docker
    - Arm Virtual Hardware
    - K3s
    - Containerd
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: K3s Quick start Guide 
        link: https://docs.k3s.io/quick-start
        type: documentation
    - resource:
        title: Smarter Project GitHub page
        link: https://github.com/smarter-project/
        type: website
    - resource:
        title: Hybrid-runtime GitHub page 
        link: https://github.com/smarter-project/hybrid-runtime/tree/main
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

