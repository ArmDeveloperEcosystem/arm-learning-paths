---
title: Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors

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

