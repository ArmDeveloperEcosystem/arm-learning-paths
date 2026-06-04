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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:15:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 915f6eb5e95bd42ed09b727b4599855d965125e67a8761fbd48a124e9e74b1bc
  summary_generated_at: '2026-06-01T22:11:02Z'
  summary_source_hash: 915f6eb5e95bd42ed09b727b4599855d965125e67a8761fbd48a124e9e74b1bc
  faq_generated_at: '2026-06-02T23:15:47Z'
  faq_source_hash: 915f6eb5e95bd42ed09b727b4599855d965125e67a8761fbd48a124e9e74b1bc
  summary: >-
    This introductory path shows how to install and run Windows 11 on Arm virtual machines on
    an Arm Linux system using QEMU, KVM, and two Bash automation scripts. You will clone a GitHub
    project, understand the script structure to customize options, and create a complete VM with
    a single command that stores its data in a directory you choose. You will then launch the
    VM with a run script that checks status, starts headless when needed, and connects over RDP
    using Remmina. The path is intended for developers and system administrators building or testing
    on Windows on Arm. Prerequisite: an Arm Linux host with KVM support, at least 8 GB RAM and
    50 GB free disk space.
  faqs:
  - question: What do I need before running the VM automation scripts?
    answer: >-
      An Arm Linux system with KVM support and at least 8GB RAM and 50GB free disk space. This
      path assumes you will run QEMU/KVM on that host.
  - question: How do I get the automation scripts onto my Arm Linux system?
    answer: >-
      Clone the GitHub repository and change into the project directory: git clone https://github.com/jasonrandrews/win11arm.git;
      cd win11arm.
  - question: Which command should I use to create a new Windows on Arm VM quickly?
    answer: >-
      Run: ./create-win11-vm.sh all $HOME/win11-vm. This uses default values for all configurable
      parameters and stores the VM data in $HOME/win11-vm while Windows installs automatically.
  - question: How do I start and connect to the VM after it is created?
    answer: >-
      Run: ./run-win11-vm.sh $HOME/win11-vm. The script checks if the VM is already running, starts
      it in headless mode if needed, and connects via RDP using Remmina.
  - question: What should I check if VM creation or startup fails?
    answer: >-
      Confirm your system meets the prerequisites and that KVM is available on your Arm Linux
      host. Verify the VM directory path you pass to the scripts is correct, then re-run the command;
      the Learning Path includes guidance for troubleshooting common setup and runtime issues.
# END generated_summary_faq

author: Jason Andrews

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

