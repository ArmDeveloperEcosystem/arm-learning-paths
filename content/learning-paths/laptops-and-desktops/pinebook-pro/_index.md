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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:10:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  summary_generated_at: '2026-06-01T22:08:50Z'
  summary_source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  faq_generated_at: '2026-06-02T23:10:51Z'
  faq_source_hash: e1befed4cafab0eaee29a31c2f259a6a90a14d9f8230c570b6c10a9840b761d5
  summary: >-
    This advanced Learning Path shows how to install and configure Arch Linux for Arm on a Pinebook
    Pro, then set up the i3 window manager and optionally configure Neovim for development. You
    will prepare a bootable microSD card from a second computer (instructions target Linux), install
    Arch Linux on the Pinebook Pro, and perform user-level i3 configuration, including practical
    tweaks like setting display brightness. An optional section demonstrates a Neovim-based editing
    workflow. The focus is turning the Pinebook Pro into an Arm Linux development machine. Prerequisites
    are a Pinebook Pro and a class‑10 or faster microSD card (8GB or larger); no other explicit
    prerequisites are listed.
  faqs:
  - question: Do I need a second computer to prepare the microSD card, and which OS is covered?
    answer: >-
      Yes. You will write the Arch Linux image to the microSD card from a second computer, and
      the instructions are written for Linux. You can use macOS, but the partitioning steps differ
      and are not included here.
  - question: What hardware do I need before starting?
    answer: >-
      You need a Pinebook Pro laptop and a microSD card that is at least 8GB and class 10 or faster.
      These are required to install Arch Linux for Arm.
  - question: Which account should I use when installing and running the i3 window manager?
    answer: >-
      Use your created user account, not root. The instructions use sudo for package installation,
      and you will run i3 from your user account.
  - question: How do I set the Pinebook Pro display to maximum brightness under i3?
    answer: >-
      Run the command: echo 4095 > /sys/class/backlight/edp-backlight/brightness. This sets the
      laptop display to maximum brightness.
  - question: Is the Neovim setup required, and what should I expect the first time I open it?
    answer: >-
      The Neovim section is optional. On first launch it looks much like vim, but it is more customizable
      with Lua extensibility and still supports Vimscript; the majority of vim plugins work as
      expected.
# END generated_summary_faq

author: Gabriel Peterson

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

