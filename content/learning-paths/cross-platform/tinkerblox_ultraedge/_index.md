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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:52:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 09142517ecc64fba821062e1af4db3ac9d72f9adcd3f10c12d6fd5a4cf3daaf4
  summary_generated_at: '2026-06-01T21:20:11Z'
  summary_source_hash: 09142517ecc64fba821062e1af4db3ac9d72f9adcd3f10c12d6fd5a4cf3daaf4
  faq_generated_at: '2026-06-02T21:52:57Z'
  faq_source_hash: 09142517ecc64fba821062e1af4db3ac9d72f9adcd3f10c12d6fd5a4cf3daaf4
  summary: >-
    This Learning Path shows how to deploy Tinkerblox UltraEdge HPC-I on Arm for AI and mixed
    workloads. You start by understanding the UltraEdge layered architecture (core, boost, prime),
    then provision a Google Axion C4A VM on Google Cloud to build a Yocto image targeting the
    NXP S32G‑VNP‑GLDBOX3. You install UltraEdge on Debian or Ubuntu by registering a device in
    the Uncloud dashboard, and use the Tinkerblox CLI to deploy MicroPacs, inspect system state,
    and observe runtime behavior. By the end, you can build with the UltraEdge MicroStack, deploy
    MicroPacs on Linux-based compute, and prepare edge–cloud data flows. This advanced path assumes
    Linux, container runtime/CNI, protocol, and edge‑cloud orchestration knowledge.
  faqs:
  - question: What do I need before running the Yocto image build steps?
    answer: >-
      Provision a Google Axion C4A VM on Google Cloud using the c4a-standard-32 type (16 vCPUs,
      128 GB memory). An Ubuntu 22.04 environment with about 100 GB of disk space works well for
      this Learning Path, and supported host architectures include AArch64 (arm64) and ARMv7.
  - question: Which Ubuntu releases are supported as Yocto build hosts right now?
    answer: >-
      Tested build hosts include Ubuntu 20.04 LTS (AArch64) and Ubuntu 22.04 LTS (AArch64). As
      of publication, Ubuntu 24.04 LTS is not a supported Yocto build host OS.
  - question: How do I register a Debian or Ubuntu device for UltraEdge?
    answer: >-
      Log in to the Uncloud Dashboard and navigate to Device Management, then choose New Device.
      This initializes and registers your edge device in the Uncloud ecosystem for subsequent
      UltraEdge installation and management.
  - question: How do I deploy and validate a sample microservice on UltraEdge?
    answer: >-
      Download a sample MPAC file from the Tinkerblox support repository and install it on your
      device using the Tinkerblox CLI. Use the CLI to inspect system state and observe the microservice’s
      runtime behavior.
  - question: Do I need Docker or Kubernetes to run workloads in this Learning Path?
    answer: >-
      No. UltraEdge uses a lean, deterministic execution stack, and the procedures use the Tinkerblox
      CLI rather than Docker or Kubernetes.
# END generated_summary_faq

author: Tinkerblox

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
tools_software_languages:
  - Tinkerblox

cloud_service_providers:
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

