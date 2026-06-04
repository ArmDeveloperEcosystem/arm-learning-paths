---
title: Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors
description: Learn how to create a custom Azure Linux 3.0 VM image using QEMU, upload it to Azure Shared Image Gallery, and deploy it on Arm-based Cobalt 100 processors.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for developers who want to run Azure Linux 3.0 on Arm-based Cobalt 100 processors in a custom virtual machine.


learning_objectives:
  - Use QEMU to create a raw disk image
  - Boot a virtual machine using an AArch64 ISO and install Azure Linux 3.0
  - Convert the raw disk image to VHD format
  - Upload the VHD file to Azure
  - Use Azure Shared Image Gallery (SIG) to create a custom image
  - Create an Azure Linux 3.0 virtual machine on Arm using the Azure CLI and the custom image

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with permission to create resources, including instances using Cobalt 100 processors
    - A Linux machine with [QEMU](https://www.qemu.org/download/) and the [Azure CLI](/install-guides/azure-cli/) installed and authenticated
    

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:24:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  summary_generated_at: '2026-06-02T03:11:18Z'
  summary_source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  faq_generated_at: '2026-06-03T00:24:06Z'
  faq_source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  summary: >-
    This advanced Learning Path guides you through building a custom Azure Linux 3.0 image for
    Arm and deploying it on Microsoft Azure Cobalt 100 processors. You will use QEMU on a Linux
    host to create a raw disk image, install Azure Linux 3.0 from an AArch64 ISO, convert the
    disk to a fixed-size VHD, upload it to Azure, and register it in Azure Shared Image Gallery.
    Finally, you will create an Azure VM using the Azure CLI and your custom image. Prerequisites
    include an Azure account with permissions for Cobalt 100 resources and a Linux machine with
    QEMU and the Azure CLI installed and authenticated. Estimated time: about 120 minutes.
  faqs:
  - question: What do I need before running these steps?
    answer: >-
      You need a Microsoft Azure account with permission to create resources, including instances
      using Cobalt 100 processors. You also need a Linux machine with QEMU and the Azure CLI installed
      and authenticated.
  - question: Which Azure Linux ISO and architecture should I use with QEMU?
    answer: >-
      Use the Azure Linux 3.0 AArch64 (Arm64) ISO. The Learning Path points to the Azure Linux
      3.0 project README, which includes links to ISO downloads.
  - question: What artifacts should I have before uploading to Azure?
    answer: >-
      After installing Azure Linux 3.0 in QEMU, you should have a raw disk image that you convert
      to a fixed-size VHD. The VHD file is the artifact you upload to Azure.
  - question: How is the VHD registered so I can reuse it to create VMs?
    answer: >-
      You upload the VHD to Azure Blob Storage using the Azure CLI, then register it in Azure
      Shared Image Gallery. This process produces a custom image you can reference by its image
      ID.
  - question: How do I launch a VM on Cobalt 100 using my custom image?
    answer: >-
      Use az vm create with the image ID from the Shared Image Gallery and specify the VM size
      targeting Cobalt 100 Arm-based processors. Provide the resource group, VM name, image ID,
      size, admin username, and optionally generate an SSH key as shown in the example.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
  - QEMU
  - Azure CLI

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Virtual machines in Azure
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Store and share images in an Azure Compute Gallery
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/shared-image-galleries
      type: documentation
  - resource:
      title: QEMU Documentation
      link: https://wiki.qemu.org/Documentation
      type: documentation
  - resource:
      title: Upload a VHD to Azure or copy a managed disk to another region - Azure CLI
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/upload-vhd
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

