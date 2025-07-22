---
title:  Create Azure Linux 3.0 custom Arm VM

draft: true
cascade:
    draft: true

minutes_to_complete: 120  

who_is_this_for: This Learning Path helps developers create a custom Azure Linux 3.0 virtual machine for Arm and utilize the default software stack provided by Microsoft.


learning_objectives:
    - Use the qemu-img utility to create a raw disk image, boot a VM with Aarch64 ISO to install the OS onto that disk, and convert the raw disk image into VHD
    - Upload the VHD to Azure and use the Azure Shared Image Gallery to create a custom image.
    - Use Azure CLI to create Azure Linux 3.0 VM for Arm, using the custom image from Azure SIG.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with permission to create resources, including Cobalt 100 (Arm64) instances (Dpsv6).
    - A local Linux machine with [QEMU](https://www.qemu.org/download/) installed to emulate Aarch64.
    - An [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and authenticated on your local machine.
    
author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
  - QEMU
  - Azure CLI

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Shared Image Gallery documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/shared-image-galleries
      type: documentation
  - resource:
      title: QEMU User Documentation
      link: https://wiki.qemu.org/Documentation
      type: documentation
  - resource:
      title: Upload a VHD to Azure and create an image
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/upload-vhd
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

