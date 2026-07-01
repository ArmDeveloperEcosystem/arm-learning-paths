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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:48:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  summary_generated_at: '2026-06-30T21:48:05Z'
  summary_source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  faq_generated_at: '2026-06-30T21:48:05Z'
  faq_source_hash: e4eb84292a669a8d73bff4b63d2fe3f70382dd873d023fc8ff24db5ad6178ab8
  summary: >-
    You'll deploy an Arm-based Cobalt 100 virtual machine (VM) in Microsoft
    Azure using the Azure Portal, select an appropriate VM series, and prepare it for remote access
    and basic testing. First, you'll create the VM, then configure the associated Network Security
    Group to allow inbound SSH (port 22) and an application test port (8080). Then, you'll connect over SSH using the VM’s public IP address and validate external connectivity
    by running a service on the chosen port. By the end, you'll reach the VM via SSH and
    confirm that traffic to the opened port is permitted from the configured source IP range.
  faqs:
  - question: How do I choose between Dpsv6/Dplsv6 and Epsv6 when creating the VM?
    answer: >-
      Dpsv6 and Dplsv6 are general-purpose series, while Epsv6 is memory-optimized. Select a series
      that aligns with the memory needs of your workload.
  - question: Where do I find the VM’s public IP address for SSH?
    answer: >-
      Open the VM resource in the Azure Portal and copy the Public IP address from the Overview
      page. Use the admin username you set during creation (for example, azureuser) and the path
      to your SSH private key.
  - question: What should I check if SSH times out or is refused?
    answer: >-
      Verify the Network Security Group has an inbound rule allowing TCP port 22 from your client
      IP. Also confirm you’re using the correct public IP address and the admin username you chose
      during VM creation.
  - question: Which IP range should I allow when opening port 8080 in the NSG?
    answer: >-
      For testing, allow traffic from your IP to limit exposure. Adjust the source IP range or
      choose a different port if your workload requires broader access or a non-default port.
  - question: What result should I expect when verifying port 8080 connectivity?
    answer: >-
      With an application or temporary HTTP server listening on port 8080, connecting to http://[public
      IP]:8080 should return a response. If it doesn’t, re-check the NSG rule and ensure the service
      is running on the VM.
# END generated_summary_faq

author: Joe Stech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

