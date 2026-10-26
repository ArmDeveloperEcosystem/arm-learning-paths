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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:11:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  summary_generated_at: '2026-07-28T16:11:59Z'
  summary_source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  faq_generated_at: '2026-07-28T16:11:59Z'
  faq_source_hash: 137e974aee0ccba78e3375a1c8179af392e54a0304cfecdcd53cf4ac5c38917b
  summary: >-
    You'll set up an Ubuntu 24.04 container on an Arm-based Chromebook with ChromeOS Crostini and
    LXC from the Termina shell. You'll create and manage the container, share ChromeOS folders with
    Linux, configure Sommelier, and install a minimal desktop stack. You'll then launch a GUI test app and use `lxc` commands to inspect, stop, and remove the container.
  faqs:
  - question: How do I know the Ubuntu container started correctly?
    answer: >-
      Run `lxc list` to confirm the container appears with `Status` set to `RUNNING`. Use `lxc info` for
      details such as Architecture, PID, and creation time that match the example output.
  - question: How do I share a ChromeOS folder with the Ubuntu container?
    answer: >-
      In the ChromeOS Files app, right-click a folder and choose **Share with Linux**. The folder
      becomes available to Linux apps and the command line inside the container. If the folder doesn't
      appear, ensure the container is running.
  - question: How do I launch and verify a Linux GUI app from the container?
    answer: >-
      After enabling Sommelier and installing the minimal desktop packages, start a test application
      such as `terminator` from the container shell. A window should open on the ChromeOS desktop. If a window doesn't open, revisit the display configuration steps.
  - question: Which command opens a shell inside the container for installs and configuration?
    answer: >-
      From the Termina shell, run `lxc exec <container> -- bash` (for example, `lxc exec u1 -- bash`).
      This places you in the container’s shell to install packages and run commands.
  - question: How do I stop and remove the container when I am done?
    answer: >-
      Use `lxc stop <container>` to stop the container, then `lxc delete <container>` to remove it. Deletion
      is permanent, so run the delete command only when you no longer need the container.
# END generated_summary_faq
 
author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
