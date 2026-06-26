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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T18:40:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  summary_generated_at: '2026-06-26T18:40:27Z'
  summary_source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  faq_generated_at: '2026-06-26T18:40:27Z'
  faq_source_hash: 413467e581e3561425229d0f6118975dbb596d6a9494544a54f0b9ab22c1b89d
  summary: >-
    In this Learning Path, you build a custom Azure Linux 3.0 image for Arm and deploy it on Cobalt
    100-based virtual machines. Starting from the Azure Linux `aarch64` ISO, you use QEMU to create
    a raw disk, boot the installer, and produce a working system image. You convert the disk to
    a fixed-size VHD, upload it to Azure, and register it in Azure Shared Image Gallery using
    the Azure CLI. With the image ID, you create a new VM on Arm-based Cobalt 100 processors.
    The flow emphasizes the key decisions around image format, resource naming, and region/size
    selection, and finishes with a VM launched from the custom image.
  faqs:
  - question: Which ISO architecture should I download for the QEMU installation?
    answer: >-
      Use the Azure Linux 3.0 `aarch64` ISO referenced in the project `README`. The steps boot QEMU
      with this ISO to install the OS onto a raw disk image.
  - question: Does the VHD need to be fixed-size before uploading to Azure?
    answer: >-
      Yes. The procedure converts the installed disk to a fixed-size VHD before upload, and the
      later steps assume this format when registering the image.
  - question: What environment variables should I set before running the Azure CLI upload and
      image registration steps?
    answer: >-
      Set `RESOURCE_GROUP`, `LOCATION`, and `STORAGE_ACCOUNT` as shown in the steps. Choose a `LOCATION`
      where Cobalt 100 processors are available to your subscription.
  - question: How do I confirm that my image registration in Shared Image Gallery succeeded?
    answer: >-
      After registration, obtain an image ID from the Shared Image Gallery. You will reference
      this `IMAGE_ID` in the `az vm create` command; having and using it confirms the image is ready.
  - question: What credentials are configured when creating the VM with `az vm create`?
    answer: >-
      The example uses `--admin-username` to define the Linux user and `--generate-ssh-key` to create
      an SSH key locally. This sets up key-based SSH access for the specified admin user.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
