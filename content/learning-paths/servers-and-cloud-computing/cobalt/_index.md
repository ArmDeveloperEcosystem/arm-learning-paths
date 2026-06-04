---
title: Deploy a Cobalt 100 Virtual Machine on Azure
description: Learn how to deploy an Arm-based Cobalt 100 virtual machine on Azure, connect via SSH, and configure network security group rules for external connectivity.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to deploy an Arm-based virtual machine on Azure and expose an application port to the internet.

learning_objectives:
    - Deploy an Arm-based Cobalt 100 virtual machine (VM) on Microsoft Azure
    - Connect to the Cobalt 100 VM using SSH
    - Configure an inbound TCP port in the associated Network Security Group (NSG)
    - Verify external connectivity to the newly-opened port

prerequisites:
    - A Microsoft Azure subscription with permissions to create virtual machines and networking resources
    - Basic familiarity with SSH

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:35:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  summary_generated_at: '2026-06-02T03:25:26Z'
  summary_source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  faq_generated_at: '2026-06-03T00:35:17Z'
  faq_source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  summary: >-
    This Learning Path walks you through deploying a Linux-based Cobalt 100 virtual machine on
    Microsoft Azure, connecting via SSH, and configuring Network Security Group (NSG) rules to
    expose an application port for testing. Using the Azure Portal, you create an Arm-based VM
    powered by Microsoft’s Cobalt 100 (Armv9 Neoverse-N2), open inbound TCP ports 22 and 8080,
    and verify external connectivity to the newly opened port. You will copy the VM’s public IP,
    establish an SSH session, and optionally start a temporary HTTP server to confirm reachability.
    Prerequisites include an Azure subscription with permissions to create VMs and networking
    resources, and basic familiarity with SSH. Azure Portal and Azure CLI are listed tools; the
    steps focus on the Portal.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure subscription with permissions to create virtual machines and
      networking resources, and basic familiarity with SSH. No other prerequisites are explicitly
      listed.
  - question: Which Cobalt 100 VM series should I choose during creation?
    answer: >-
      Azure offers Cobalt 100–powered VMs in Dpsv6 and Dplsv6 (general-purpose) and Epsv6 (memory-optimized)
      series. Select the series that aligns with your general-purpose or memory-optimized needs.
  - question: How do I find the public IP to SSH into the VM?
    answer: >-
      Open the VM’s Overview page in the Azure Portal and copy the Public IP address. Use that
      address in your SSH command.
  - question: What SSH command and username should I use to connect?
    answer: >-
      From a terminal, run: ssh -i [path to your pem file] azureuser@[public IP], replacing the
      placeholders with your key path and the VM’s public IP. Use azureuser unless you specified
      a different admin username during VM creation.
  - question: How do I open and test an application port like 8080?
    answer: >-
      Add an inbound rule in the VM’s Network Security Group to allow TCP 8080, typically scoped
      to your IP for testing. Start your application (or a temporary HTTP server) on the VM listening
      on 8080, then access the VM on that port from your client to verify connectivity.
# END generated_summary_faq

author: Joe Stech

### Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure
armips:
    - Neoverse
tools_software_languages:
    - Azure Portal
    - Azure CLI
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Azure Cobalt 100 VM documentation
        link: https://learn.microsoft.com/azure/virtual-machines/cobalt-100
        type: Documentation
    - resource:
        title: Azure Virtual Machines overview
        link: https://learn.microsoft.com/azure/virtual-machines/
        type: Documentation
    - resource:
        title: Configure Azure network security group rules
        link: https://learn.microsoft.com/azure/virtual-network/security-overview
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

