---
title: Create Linux virtual machines with Hyper-V

description: Learn how to create and manage Arm-based Linux virtual machines using Hyper-V on Windows on Arm devices.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to use Linux virtual machines (VMs) with Windows on Arm devices. 

learning_objectives:
    - Create Arm-based Linux VMs using Hyper-V.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 with [Hyper-V](/install-guides/hyper-v/) installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:18:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  summary_generated_at: '2026-07-28T16:18:42Z'
  summary_source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  faq_generated_at: '2026-07-28T16:18:42Z'
  faq_source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  summary: >-
    You'll create an Arm-based Ubuntu 24.04 VM on a Windows on Arm device with Hyper-V.
    You'll download the Arm ISO, create the VM manually, attach the ISO,
    and boot the Linux installer. You can adapt these steps as a repeatable process for other
    Arm Linux distributions.
  faqs:
  - question: Which Ubuntu image do I need to download?
    answer: >-
      Download the Ubuntu 24.04 ISO file for Arm. Use the Arm-specific ISO so the VM can boot
      and install correctly on Windows on Arm hardware.
  - question: Can I use Hyper-V Quick Create on my Windows on Arm device?
    answer: >-
      No. Don't use Quick Create with Windows on Arm devices. Instead, create the VM manually.
  - question: How do I know if I’m on a Windows version that can run Linux VMs?
    answer: >-
      You need Windows 11 version 22H2 or later. Confirm your Windows version before you start
      creating the VM.
  - question: What result should I expect when I start the VM from the ISO?
    answer: >-
      The VM should boot into the Linux installer. If it doesn't, verify you used the Arm ISO
      and created the VM manually rather than with Quick Create.
  - question: I want to use a different Linux distribution. What should I change?
    answer: >-
      Ubuntu is used in the Learning Path as an example. Use the same approach with the
      Arm ISO and documentation of the distribution of your choice as you adapt the steps.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
    - Linux
tools_software_languages:
    - Hyper-V

further_reading:
    - resource:
        title: Virtualization Documentation
        link: https://learn.microsoft.com/en-us/virtualization/ 
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
