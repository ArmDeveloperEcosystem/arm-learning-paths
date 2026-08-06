---
title: Deploy a Windows on Arm virtual machine on Microsoft Azure

minutes_to_complete: 15

description: Learn how to create and connect to a Windows on Arm virtual machine in Microsoft Azure using the Azure Marketplace and RDP.

who_is_this_for: This is an introductory topic for software developers interested using Windows on Arm virtual machines (VMs) in the Azure cloud.

learning_objectives: 
    - Start a Windows on Arm virtual machine in Azure cloud.
    - Discover all Arm-based image offerings in the Azure Image Marketplace. 

prerequisites:
    - An Azure Cloud account.
    - An RDP client to connect to your Windows on Arm instance.  For more info on RDP clients, see [Remote Desktop clients for Remote Desktop Services and remote PCs](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) to get started.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T20:55:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ffcb7c740ebfdacb47349150c321972b9cf0a9b43e36592da833a588b65293f6
  summary_generated_at: '2026-08-04T20:55:10Z'
  summary_source_hash: ffcb7c740ebfdacb47349150c321972b9cf0a9b43e36592da833a588b65293f6
  faq_generated_at: '2026-08-04T20:55:10Z'
  faq_source_hash: ffcb7c740ebfdacb47349150c321972b9cf0a9b43e36592da833a588b65293f6
  summary: >-
    You'll deploy a Windows on Arm VM in Microsoft Azure using the Azure Marketplace. First, you'll configure and deploy a VM using Azure portal. After deployment, you'll connect the VM
    with a Remote Desktop Protocol (RDP) client. You can use the same workflow to launch a Linux image when you select a
    Linux distribution instead of Windows.
  faqs:
  - question: Which Azure subscription should I use to create the VM?
    answer: >-
      You can use either a personal subscription or your organization’s subscription. Sign in to
      the Azure portal with an account that has access to the chosen subscription.
  - question: Where do I start the VM creation in the Azure portal?
    answer: >-
      Sign in and use the Azure portal search bar to find **Virtual Machines**. From there, select
      **Create** and start the VM configuration flow.
  - question: How do I pick a Windows on Arm image from the Marketplace?
    answer: >-
      During VM creation, select **See all images**, search for a Windows image, and use the
      **Arm64** filter to find an Arm-based offering. For the Learning Path, select **Windows 11 Professional
      24H2 - Arm64**.
  - question: Can I use these steps to deploy a Linux image on an Arm-based VM?
    answer: >-
      Yes. Use the same process and select a Linux distribution instead of Windows during image
      selection.
  - question: How do I connect to the VM after it is created?
    answer: >-
      Copy the VM's public IP address and enter it in an RDP client. Use the username and password
      configured during VM creation. For the Learning Path, allow RDP traffic on port `3389`.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Microsoft Azure

armips:
    - Neoverse
operatingsystems:
    - Windows
tools_software_languages:

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

further_reading:
    - resource:
        title: Azure Virtual Machines with Ampere Altra Arm–based processors
        link: https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
