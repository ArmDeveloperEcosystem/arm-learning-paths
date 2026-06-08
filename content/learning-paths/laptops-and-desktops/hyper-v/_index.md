---
title: Create Linux virtual machines with Hyper-V

description: Learn how to create and manage Arm-based Linux virtual machines using Hyper-V on Windows on Arm devices.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to use Linux virtual machines with Windows on Arm devices. 

learning_objectives:
    - Create Arm-based Linux virtual machines using Hyper-V.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 with [Hyper-V](/install-guides/hyper-v/) installed.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:07:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  summary_generated_at: '2026-06-01T22:06:03Z'
  summary_source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  faq_generated_at: '2026-06-02T23:07:08Z'
  faq_source_hash: 829130636ec6969f791826ef731b38f7bb87c025d910218822a113ecdef62306
  summary: >-
    This introductory Learning Path shows how to create and manage Arm-based Linux virtual machines
    using Hyper-V on Windows on Arm devices. Working on Windows 11 version 22H2 or newer with
    Hyper-V installed, you will use an Ubuntu 24.04 ISO image for Arm as the example Linux distribution,
    with guidance that can be applied to other distributions. The steps call out a key requirement
    specific to Windows on Arm: do not use Hyper-V Quick Create. By the end, you will have created
    a Linux virtual machine in Hyper-V on your Windows on Arm computer (for example, a Lenovo
    Thinkpad X13s). Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer with Hyper-V installed and Windows 11 version 22H2 or
      newer. A device such as the Lenovo Thinkpad X13s meets the requirement.
  - question: Which Ubuntu image should I download for this setup?
    answer: >-
      Download the Ubuntu 24.04 ISO file for Arm. Make sure you select the Arm build, not an x86
      image.
  - question: Can I use Hyper-V Quick Create on Windows on Arm?
    answer: >-
      No. Do not use Quick Create with Windows on Arm devices; follow the manual creation steps
      described in the path.
  - question: How do I proceed if I want a different Linux distribution?
    answer: >-
      Use the same process shown for Ubuntu and obtain the Arm ISO for your chosen distribution.
      The instructions indicate you can follow the Ubuntu steps for other distributions.
  - question: How long will this take and what result should I expect?
    answer: >-
      Plan for about 60 minutes. You will create an Arm-based Linux virtual machine running under
      Hyper-V on your Windows on Arm device.
# END generated_summary_faq

author: Jason Andrews

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

