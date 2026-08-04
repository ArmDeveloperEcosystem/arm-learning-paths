---
title: Deploy Tinkerblox UltraEdge HPC-I for AI and mixed workloads on Arm
minutes_to_complete: 60 

description: Learn how to deploy Tinkerblox UltraEdge HPC-I for edge AI and mixed workloads on Arm platforms, including installation and configuration on Debian, Ubuntu, and Yocto systems.

who_is_this_for: This is an advanced topic for business, R&D, and engineering teams seeking to optimize CPU and GPU infrastructure utilization while reducing total cost of ownership on edge and constrained environments. It's ideal for innovation and development teams building next-generation AI workloads using alternative runtime environments and packaging technologies.

learning_objectives:
  - Understand the layered architecture of UltraEdge core, boost, and prime
  - Build applications using the UltraEdge MicroStack
  - Deploy the MicroPacs on Linux-based compute systems and scale to cloud or data-center environments
  - Optimize performance for edge-cloud scenarios, enabling near real-time data flows

prerequisites:
  - Experience using Linux on embedded or SBC platforms
  - Understanding of container runtimes (containerd) and CNI networking
  - Basic knowledge of communication protocols (MQTT, HTTP, and others)
  - Familiarity with edge-cloud architectures and data-flow orchestration

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T21:10:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5e3e7ecd4c814788ad8a58d3019e0838c61acde90e56172965aa3bcda65b74e1
  summary_generated_at: '2026-08-04T21:10:00Z'
  summary_source_hash: 5e3e7ecd4c814788ad8a58d3019e0838c61acde90e56172965aa3bcda65b74e1
  faq_generated_at: '2026-08-04T21:10:00Z'
  faq_source_hash: 5e3e7ecd4c814788ad8a58d3019e0838c61acde90e56172965aa3bcda65b74e1
  summary: >-
    This Learning Path introduces Tinkerblox UltraEdge as an edge-native execution fabric
    for AI and mixed workloads on Arm platforms. You review the UltraEdge architecture,
    provision a Google Axion C4A virtual machine for arm64 Yocto builds, and install the UltraEdge
    agent and MicroPac tooling on Debian or Ubuntu. You then build and deploy MicroPac workloads,
    create a Yocto image for an NXP S32G-VNP-GLDBOX3 board, and use the Tinkerblox CLI to install,
    monitor, and troubleshoot services. The path covers both Linux package-based and Yocto-based
    deployment workflows.
  faqs:
  - question: What is the purpose of UltraEdge in this Learning Path?
    answer: >-
      UltraEdge provides an edge-native execution fabric for AI and mixed workloads. You review
      its layered architecture and see how MicroStack and MicroPac support workload packaging and
      deployment on Arm-based systems.
  - question: Why is a Google Axion C4A virtual machine used for the Yocto build?
    answer: >-
      The workflow provisions a C4A VM with 16 vCPUs and 128 GB of memory. It runs Ubuntu 22.04
      and provides the environment for building the image for the target NXP board.
  - question: Can UltraEdge be installed on Debian or Ubuntu?
    answer: >-
      Yes. You install and activate the UltraEdge agent on Debian or Ubuntu, then use MicroPac
      tooling to define, build, validate, and install workloads.
  - question: What is required to build the Yocto image for the NXP board?
    answer: >-
      Use the NXP S32G-VNP-GLDBOX3 platform with BSP 38.0, an AArch64 Ubuntu build host, the
      required Yocto layers, and the `meta-edgeblox.zip` layer requested from Tinkerblox support.
      Yocto builds can take several hours depending on the available resources.
  - question: How do I manage workloads after installing UltraEdge?
    answer: >-
      Use the Tinkerblox CLI or MicroBoost CLI to install, start, stop, monitor, and diagnose
      MicroPac-based workloads on the UltraEdge-enabled device. You also inspect system state and
      troubleshoot common connection and architecture issues.
# END generated_summary_faq

author: Tinkerblox

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
tools_software_languages:
  - Tinkerblox

platforms:
  - Google Cloud

armips:
  - Neoverse

operatingsystems:
  - Linux
  - other

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - automotive

further_reading:
  - resource:
      title: Tinkerblox
      link: https://tinkerblox.io 
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
