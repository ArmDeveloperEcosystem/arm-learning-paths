---
title: Build NVIDIA JetPack Yocto images for NVIDIA Jetson Orin NX, Orin Nano, and Thor platforms
minutes_to_complete: 180 

draft: true
cascade:
    draft: true
   
description: Build a custom Yocto-based NVIDIA JetPack image on a Google Axion C4A virtual machine, then flash and run it on an NVIDIA Jetson Orin NX, Orin Nano, or Thor platform.

who_is_this_for: This is an advanced topic for embedded Linux developers familiar with Yocto and NVIDIA JetPack. You’ll build and flash custom images for NVIDIA Jetson Orin NX, Orin Nano, and Thor platforms.

learning_objectives:
  - Explain how Yocto uses OpenEmbedded, BitBake, and layers to create custom Linux distributions
  - Provision a Google Axion C4A virtual machine for Yocto image builds
  - Build a custom Yocto image for a supported NVIDIA Jetson platform
  - Flash and run the Yocto image on the NVIDIA Jetson platform


prerequisites:
  - Basic proficiency with Linux shell commands, SSH, and file transfers
  - A Google Cloud account with permission and quota to create a `c4a-standard-32` virtual machine
  - A supported NVIDIA Jetson platform
  - An Ubuntu 22.04 or later computer with USB access for flashing the image

author: Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
tools_software_languages: 
    - Yocto
    - BitBake

platforms:
  - Google Cloud

armips:
  - Neoverse
  - Cortex-A
  
operatingsystems:
  - Linux

shared_path: true
shared_between:
    - embedded-and-microcontrollers
    - automotive
    - servers-and-cloud-computing

further_reading:
  - resource:
      title: OE4T meta-tegra documentation
      link: https://oe4t.github.io/master/
      type: website
  - resource:
      title: Yocto Project Overview and Concepts Manual
      link: https://docs.yoctoproject.org/overview-manual/index.html
      type: documentation
  - resource:
      title: BitBake User Manual
      link: https://docs.yoctoproject.org/bitbake/index.html
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
