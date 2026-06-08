---
title: Install Ubuntu on ChromeOS Crostini as an LXC container

description: Learn how to create and run Ubuntu containers on ChromeOS Crostini using LXC with file sharing and GUI application support on Arm-based Chromebooks.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers who want to install Ubuntu and other Linux distributions on their Arm-based Chromebook with ChromeOS file sharing and GUI support.

learning_objectives:
  - Create and run an Ubuntu 24.04 container on ChromeOS Crostini using LXC and Termina shell
  - Set up ChromeOS integration for file sharing and GUI applications
  - Manage LXC containers on ChromeOS
  - Enable file sharing between ChromeOS and Ubuntu containers
  - Run Linux GUI applications on your Chromebook with Sommelier integration

prerequisites:
    - A ChromeOS device with the Linux development environment enabled. The Lenovo Chromebook Plus 14 is recommended. 
    - Basic knowledge of the Linux command line

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:58:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  summary_generated_at: '2026-06-01T22:01:54Z'
  summary_source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  faq_generated_at: '2026-06-02T22:58:53Z'
  faq_source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  summary: >-
    This introductory Learning Path shows how to create and run an Ubuntu 24.04 LXC container
    on ChromeOS (Crostini) from the Termina shell on an Arm-based Chromebook. You will set up
    ChromeOS integration for selective folder sharing from the Files app and enable Linux GUI
    applications through Sommelier, using a minimal desktop environment and a test app to validate.
    You will also manage the container lifecycle with common LXC commands, including start, stop,
    exec, list, info, and delete. Prerequisites are a ChromeOS device with the Linux development
    environment enabled (the Lenovo Chromebook Plus 14 is recommended) and basic Linux command-line
    familiarity. Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a ChromeOS device with the Linux development environment enabled and basic Linux
      command-line knowledge. The Lenovo Chromebook Plus 14 is recommended.
  - question: Where do I run the LXC and setup commands on ChromeOS?
    answer: >-
      Run all container management and setup commands in the Termina shell provided by the ChromeOS
      Linux development environment.
  - question: How do I start, stop, and access my Ubuntu container, and check its status?
    answer: >-
      From Termina, use lxc start u1 to start, lxc stop u1 to stop, and lxc exec u1 -- bash to
      enter the container shell. Use lxc list to view all containers and lxc info u1 for detailed
      information such as status and architecture.
  - question: How do I share folders between ChromeOS and the Ubuntu container?
    answer: >-
      In the ChromeOS Files app, right-click a folder and select Share with Linux to make it available
      to the container. Only folders (not individual files) can be shared, and access is two-way
      for Linux apps and the command line.
  - question: How do I enable and test Linux GUI applications from the container?
    answer: >-
      Install a minimal desktop environment and configure the display environment variables so
      applications use Sommelier. You can install a test GUI application (for example, a terminal
      emulator like terminator) to confirm that windows open in the ChromeOS desktop.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
  - Cortex-A
operatingsystems:
  - ChromeOS
tools_software_languages:
  - Ubuntu

further_reading:
  - resource:
      title: Official ChromeOS Linux Support
      link: https://chromeos.dev/en/linux
      type: documentation
  - resource:
      title: Linux Containers
      link: https://linuxcontainers.org/
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

