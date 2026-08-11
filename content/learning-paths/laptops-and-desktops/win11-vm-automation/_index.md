---
title: Automate Windows on Arm virtual machine deployment with QEMU and KVM on Arm Linux

description: Learn how to automate Windows on Arm VM creation on Arm Linux systems using QEMU, KVM, and Bash scripts for development and testing.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers and system administrators who want to automate Windows on Arm virtual machine (VM) creation on Arm Linux systems using QEMU and KVM.

learning_objectives:
    - Understand the process of creating a Windows on Arm virtual machine using Bash scripts
    - Run scripts for VM creation and management
    - Troubleshoot common VM setup and runtime issues
    - Use Windows on Arm virtual machines for software development and testing

prerequisites:
    - An Arm Linux system with KVM support and a minimum of 8GB RAM and 50GB free disk space

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:17:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7b07079ab99196550519000fee60228333cc2ac721cd68b0ef2ecf411e69c08e
  summary_generated_at: '2026-08-11T16:17:24Z'
  summary_source_hash: 7b07079ab99196550519000fee60228333cc2ac721cd68b0ef2ecf411e69c08e
  faq_generated_at: '2026-08-11T16:17:24Z'
  faq_source_hash: 7b07079ab99196550519000fee60228333cc2ac721cd68b0ef2ecf411e69c08e
  summary: >-
    You'll automate a Windows 11 on Arm VM on an Arm Linux host using QEMU, KVM, and
    Bash scripts. First, you'll install prerequisite software and understand the VM creation workflow. Then, you'll create a VM with default settings, and store
    the VM files in your chosen directory. After creating the VM, you'll use a single run script to check the
    state of the VM, start it if needed, and open an RDP session with Remmina.
  faqs:
  - question: Which command should I use to create a Windows on Arm VM with default settings?
    answer: >-
      Run `./create-win11-vm.sh all <vm-directory>`. This applies the default parameters and performs
      all creation steps automatically.
  - question: Where are the VM files stored and how do I choose the location?
    answer: >-
      The VM data is stored in the directory that you pass to the creation script. For example,
      `./create-win11-vm.sh all $HOME/win11-vm` stores all VM files under `$HOME/win11-vm`.
  - question: What result should I expect during the first boot after creation?
    answer: >-
      Windows installs automatically after the VM is created. Wait for installation to finish
      before proceeding to regular use.
  - question: How do I launch the VM and connect to the desktop?
    answer: >-
      Run `./run-win11-vm.sh <vm-directory>`. The script checks if the VM is running, starts it
      in headless mode if needed, and connects over RDP using Remmina.
  - question: What should I check if the run script does not open an RDP session?
    answer: >-
      Confirm you used the same VM directory you created earlier and that the VM files exist there.
      Re-run the launch script; it detects if the VM is already running and will reconnect if
      possible.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - Windows
tools_software_languages:
    - QEMU
    - KVM
    - Bash
    - RDP

further_reading:
    - resource:
        title: Linaro Wiki - Windows on Arm
        link: https://wiki.linaro.org/LEG/Engineering/Kernel/WindowsOnArm
        type: documentation
    - resource:
        title: Botspot Virtual Machine (BVM) Project
        link: https://github.com/Botspot/bvm
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
