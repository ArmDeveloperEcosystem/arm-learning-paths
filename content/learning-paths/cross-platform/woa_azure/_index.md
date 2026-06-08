---
title: Deploy a Windows on Arm virtual machine on Microsoft Azure

minutes_to_complete: 15

description: Learn how to create and connect to a Windows on Arm virtual machine in Microsoft Azure using the Azure Marketplace and RDP.

who_is_this_for: This is an introductory topic for software developers interested using Windows on Arm in the Azure cloud.

learning_objectives: 
    - Start a Windows on Arm virtual machine in Azure cloud.
    - Discover all Arm-based image offerings in the Azure Image Marketplace. 

prerequisites:
    - An Azure Cloud account.
    - An RDP client to connect to your Windows on Arm instance.  For more info on RDP clients, see [Remote Desktop clients for Remote Desktop Services and remote PCs](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) to get started.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:56:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 367566dfec0a76685b1504c2c1a996e50c55e67b2f4c5515057c0f0f1384ef98
  summary_generated_at: '2026-06-01T21:23:14Z'
  summary_source_hash: 367566dfec0a76685b1504c2c1a996e50c55e67b2f4c5515057c0f0f1384ef98
  faq_generated_at: '2026-06-02T21:56:12Z'
  faq_source_hash: 367566dfec0a76685b1504c2c1a996e50c55e67b2f4c5515057c0f0f1384ef98
  summary: >-
    Learn how to deploy a Windows on Arm virtual machine in Microsoft Azure and connect to it
    using Remote Desktop. This introductory path guides you through signing in to Azure, using
    the Azure Marketplace to locate Arm-based images, creating a Windows on Arm VM, and establishing
    an RDP session. You will also see how to discover other Arm-based offerings, with a note that
    the same flow applies if you choose a Linux image instead of Windows. Prerequisites are an
    Azure Cloud account and an RDP client. By the end, you will have a running Windows on Arm
    instance in Azure.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Azure Cloud account and an RDP client. You can sign in using either your personal
      subscription or your organization’s subscription.
  - question: Where do I start creating the Windows on Arm VM in Azure?
    answer: >-
      Sign in to your Azure account and use the Azure Marketplace to select a Windows on Arm image,
      then create a virtual machine from that listing. The steps walk you through initiating the
      VM from the Marketplace.
  - question: How do I discover Arm-based image offerings in Azure?
    answer: >-
      Open the Azure Image Marketplace and review the available Arm-based listings. The path highlights
      how to locate Windows on Arm and other Arm-based images.
  - question: How do I connect to the VM after it is created?
    answer: >-
      Use your RDP client to connect to the Windows on Arm instance. The path uses RDP for access
      so you can sign in to the Windows session.
  - question: Can I use the same instructions to deploy a Linux image on Arm?
    answer: >-
      Yes. Select a Linux distribution instead of Windows during image selection, as noted in
      the path.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
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

