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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  summary: >-
    Learn how to create a custom Azure Linux 3.0 VM image using QEMU, upload it to Azure Shared
    Image Gallery, and deploy it on Arm-based Cobalt 100 processors. It is designed for developers
    who want to run Azure Linux 3.0 on Arm-based Cobalt 100 processors in a custom virtual machine.
    By the end, you will be able to use QEMU to create a raw disk image, boot a virtual machine
    using an AArch64 ISO and install Azure Linux 3.0, and convert the raw disk image to VHD format.
    It focuses on tools and technologies such as QEMU and Azure CLI, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Microsoft Azure. The main steps cover Build
    and run Azure Linux 3.0 on an Arm-based Azure virtual machine, Create an Azure Linux image
    for Arm, Transfer the image to Azure, and Start an Azure virtual machine with the new image.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will use QEMU to create a raw disk image, boot a virtual machine using an AArch64 ISO
      and install Azure Linux 3.0, and convert the raw disk image to VHD format. Learn how to
      create a custom Azure Linux 3.0 VM image using QEMU, upload it to Azure Shared Image Gallery,
      and deploy it on Arm-based Cobalt 100 processors.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to run Azure Linux 3.0 on Arm-based Cobalt
      100 processors in a custom virtual machine.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with permission to create resources, including instances using Cobalt 100 processors;
      A Linux machine with [QEMU](https://www.qemu.org/download/) and the [Azure CLI](/install-guides/azure-cli/)
      installed and authenticated.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including QEMU and Azure CLI, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and run Azure Linux 3.0 on an Arm-based Azure
      virtual machine, Create an Azure Linux image for Arm, Transfer the image to Azure, and Start
      an Azure virtual machine with the new image.
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

