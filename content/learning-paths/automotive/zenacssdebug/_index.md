---
title: Debug Arm Zena CSS Reference Software Stack with Arm Development Studio


minutes_to_complete: 60

who_is_this_for: This introductory topic is for software developers who want to use Arm Development Studio to explore and debug the Arm Zena Compute Subsystem (CSS) Reference Software Stack on a Fixed Virtual Platform (FVP).

learning_objectives:
  - Set up and save a debug configuration for the Arm Zena CSS FVP
  - Start Runtime Security Engine (RSE) debug at reset and step through early boot
  - Attach to and debug Safety Island (SI) firmware
  - Attach to the Linux kernel on the primary compute cores and debug user space processes

prerequisites:
  - Ubuntu 22.04 host machine
  - Arm Development Studio 2024.1 or later with a valid license - for support see the [Install Guide for Arm DS](/install-guides/armds) 
  - Basic understanding of the Arm Zena CSS software stack, Armv8-A/Armv9-A cores, and Linux

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Cortex-A
  - Cortex-R
operatingsystems:
  - Linux
tools_software_languages:
  - Arm Development Studio
  - Arm Zena CSS
  - FVP

further_reading:
  - resource:
      title: Arm Zena Compute Subsystem (CSS)
      link: https://developer.arm.com/Compute%20Subsystems/Arm%20Zena%20Compute%20Subsystem
      type: website
  - resource:
      title: Arm Development Studio
      link: https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio
      type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
