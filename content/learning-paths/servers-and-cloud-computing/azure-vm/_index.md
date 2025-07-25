---
title: Create an Azure Linux 3.0 virtual machine with Cobalt 100 processors

draft: true
cascade:
    draft: true

minutes_to_complete: 120  

who_is_this_for: This Learning Path explains how to create a virtual machine on Azure running Azure Linux 3.0 on Cobalt 100 processors.


learning_objectives:
    - Use QEMU to create a raw disk image, boot a VM using an Aarch64 ISO, install the OS, and convert the raw disk image to VHD format.
    - Upload the VHD file to Azure and use the Azure Shared Image Gallery (SIG) to create a custom image.
    - Use the Azure CLI to create an Azure Linux 3.0 VM for Arm, using the custom image from the Azure SIG.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with permission to create resources, including instances using Cobalt 100 processors. 
    - A local Linux machine with [QEMU](https://www.qemu.org/download/) and the [Azure CLI](/install-guides/azure-cli/) installed and authenticated.
    
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

