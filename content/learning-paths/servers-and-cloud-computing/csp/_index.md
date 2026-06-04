---
title: Get started with Arm-based cloud instances
description: Learn how to start an Arm-based virtual machine instance from major cloud service providers and verify the Arm architecture is being used.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:38:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  summary_generated_at: '2026-06-02T03:30:48Z'
  summary_source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  faq_generated_at: '2026-06-03T00:38:48Z'
  faq_source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  summary: >-
    This introductory Learning Path shows how to launch a Linux virtual machine on Arm-based instances
    from major cloud providers and confirm that it is running on Arm architecture. You will use
    each provider’s standard VM service: AWS EC2 with Graviton, Microsoft Azure Virtual Machines
    (Azure Cobalt 100 or previous Ampere generations), Google Cloud Compute Engine with Axion
    C4A (example c4a-standard-4), Oracle Cloud Infrastructure compute with Ampere, and Alibaba
    Cloud ECS. The steps focus on selecting an Arm-based machine type and performing a brief post-launch
    verification. An active account with your chosen provider is required; no other prerequisites
    are explicitly listed. The path takes about 15 minutes to complete.
  faqs:
  - question: What do I need before starting?
    answer: >-
      You need an account with your preferred cloud service provider. The path uses provider consoles
      and documentation to guide VM creation.
  - question: Which instance types should I choose to get an Arm VM on each cloud?
    answer: >-
      Use AWS EC2 with Graviton, Azure Arm-based VMs (Cobalt 100 or Ampere generations), Google
      Cloud Axion C4A (for example c4a-standard-4), Oracle Cloud Infrastructure with Ampere, and
      Alibaba Cloud ECS with Arm-based processors.
  - question: Which operating system is used in the examples?
    answer: >-
      Linux is used for the examples in this Learning Path.
  - question: How do I verify that the VM is Arm-based once it’s running?
    answer: >-
      Follow the verification step in the path to confirm that the instance reports an Arm CPU
      architecture. The process is performed from the running Linux VM.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will have a running Linux VM on your chosen cloud that is using an Arm-based processor,
      and you will have verified the architecture on the instance.
# END generated_summary_faq

author: Ronan Synnott

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who are new to Arm-based cloud instances.

learning_objectives:
    - Start an Arm-based instance in the cloud
    - Verify that the instance is using the Arm architecture

prerequisites:
    - An account with your preferred cloud service provider.

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
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



further_reading:
    - resource:
        title: Cloud computing (arm.com)
        link: https://www.arm.com/campaigns/cloud-computing
        type: website
    - resource:
        title: Alibaba ECS Learning Path
        link: https://www.alibabacloud.com/getting-started/learningpath/ecs
        type: website
    - resource:
        title: Getting Started with AWS
        link: https://aws.amazon.com/getting-started
        type: website
    - resource:
        title: Google Cloud Training and tutorials
        link: https://cloud.google.com/compute/docs#training-and-tutorials
        type: website
    - resource:
        title: Microsoft Azure Developer resources
        link: https://learn.microsoft.com/en-us/azure/developer
        type: website
    - resource:
        title: Oracle Developer Resource Center
        link: https://developer.oracle.com/arm/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

