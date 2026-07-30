---
title: Get started with Arm-based cloud instances
description: Learn how to start an Arm-based virtual machine instance from major cloud service providers and verify the Arm architecture is being used.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:47:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  summary_generated_at: '2026-07-27T18:47:21Z'
  summary_source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  faq_generated_at: '2026-07-27T18:47:21Z'
  faq_source_hash: 9e94b69eabf35677c48db812bb85ea9cef184efc078a826b96954f540a45e915
  summary: >-
    You'll launch Arm-based virtual machines (VMs) across major cloud providers and verify that each uses
    an Arm processor. You'll use each provider's console to choose an appropriate family and instance
    type, including Amazon Elastic Compute Cloud (EC2), Azure Cobalt 100-based VMs or Ampere, Google Cloud Axion C4A, Oracle Cloud
    Ampere, and Alibaba Cloud Arm-based Elastic Compute Service (ECS) options. By the end, you'll recognize the instance details
    that confirm an Arm deployment.
  faqs:
  - question: Which option identifies an Arm-based VM on my cloud provider?
    answer: >-
      On AWS, select Graviton-based EC2 instance types. On Azure, choose Cobalt 100-based or Ampere
      VMs. On Google Cloud, use the Axion C4A series. On Oracle Cloud and Alibaba Cloud, choose
      Ampere- or Arm-based ECS options.
  - question: Where do I select the Arm series on Google Cloud, and which machine type does this
      guide use?
    answer: >-
      In the Google Cloud Console, select **Compute Engine**, **VM Instances**, and **Create**.
      Set **Series** to **C4A**, then choose the `c4a-standard-4` machine type with four vCPUs and
      16 GB of memory.
  - question: How do I confirm the instance is running on Arm after creation?
    answer: >-
      Check the instance details in your cloud console and confirm the processor family or machine
      type matches the Arm option you selected, such as Graviton, Cobalt 100, C4A, or Ampere.
      If it shows a different family, return to the creation settings and choose the Arm series.
  - question: On Microsoft Azure, should I choose Cobalt 100 or Ampere?
    answer: >-
      Both are Arm-based VM generations on Azure. The latest generation is Cobalt 100, while the
      previous generation is Ampere; choose the one that fits your needs.
  - question: What should I expect to see once provisioning finishes, and what should I verify
      before continuing?
    answer: >-
      The new VM appears in the provider console with a running status. Verify the machine type
      or series reflects the Arm-based family you selected before proceeding.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
