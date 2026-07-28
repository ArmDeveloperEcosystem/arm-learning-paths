---
title: Install Arch Linux with the i3 window manager on a Pinebook Pro

description: Learn how to install and configure Arch Linux for Arm with the i3 window manager and Neovim editor on the Pinebook Pro laptop.

minutes_to_complete: 120 

who_is_this_for: This is an advanced topic for developers who want to use the Pinebook Pro as an Arm Linux development machine. 

learning_objectives:
    - Install and configure Arch Linux for Arm 
    - Install and configure the i3 window manager
    - Install and configure the Neovim editor

prerequisites:
    - A Pinebook Pro laptop
    - A microSD card (8GB or greater; class 10 or faster)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:23:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  summary_generated_at: '2026-07-28T16:23:29Z'
  summary_source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  faq_generated_at: '2026-07-28T16:23:29Z'
  faq_source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  summary: >-
    This Learning Path guides learners through preparing a bootable Arch Linux microSD on a Linux
    system, installing Arch Linux on a Pinebook Pro, and setting up the i3 window manager for
    day-to-day Arm Linux development. Learners use a regular user account with sudo to install
    packages and run i3, and apply a simple sysfs command to set the display to maximum brightness
    when needed. An optional section demonstrates configuring the Neovim editor to create a lightweight,
    extensible development environment that feels familiar to Vim users. By the end, the Pinebook
    Pro runs Arch Linux with i3 and an editor workflow suitable for iterative development on Arm.
  faqs:
  - question: Do I need a second computer to create the Arch Linux microSD, and which OS do the
      steps use?
    answer: >-
      Yes. The instructions use a Linux computer to write and partition the microSD card. You
      can use macOS, but the required partitioning steps differ and are not covered here.
  - question: How do I know the install media worked after booting the Pinebook Pro?
    answer: >-
      The laptop should boot Arch Linux from the microSD card. If it does not, recheck how the
      image was written and how the card was partitioned on the second computer.
  - question: Should I run the i3 installation commands as root or as my user?
    answer: >-
      Use your created user account and run commands with sudo as shown in the instructions. You
      also run the i3 window manager from your user account.
  - question: The display is too dim in i3. How can I set maximum brightness?
    answer: >-
      Use the command: echo 4095 > /sys/class/backlight/edp-backlight/brightness. Run it with
      appropriate permissions if required by your system.
  - question: Is configuring Neovim required, and what should I expect the first time it opens?
    answer: >-
      The Neovim section is optional. On first launch, Neovim looks almost exactly like Vim, adds
      Lua extensibility, and most Vim plugins work as expected.
# END generated_summary_faq

author: Gabriel Peterson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Migration to Arm
armips:
    - Cortex-A72
    - Cortex-A53
operatingsystems:
    - Linux
tools_software_languages:
    - i3
    - Alacritty
    - Neovim

further_reading:
    - resource:
        title: Arch Linux ARM
        link: https://archlinuxarm.org/
        type: documentation
    - resource:
        title: i3 windows manager documentation
        link: https://i3wm.org/docs/
        type: documentation
    - resource:
        title: Pinebook Pro Wiki
        link: https://wiki.pine64.org/wiki/Pinebook_Pro
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

