---
title: Build NVIDIA JetPack Yocto images for Jetson Orin NX, Orin Nano, and Thor platforms
minutes_to_complete: 180 
   
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
  - A computer running Ubuntu 22.04 or later with USB access for flashing the image

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T16:40:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f4648abe855b5a0c8e0ac0fc8c0b8ca1e0b90b474556e34d8e0bd17eca429fa7
  summary_generated_at: '2026-08-04T16:40:49Z'
  summary_source_hash: f4648abe855b5a0c8e0ac0fc8c0b8ca1e0b90b474556e34d8e0bd17eca429fa7
  faq_generated_at: '2026-08-04T16:40:49Z'
  faq_source_hash: f4648abe855b5a0c8e0ac0fc8c0b8ca1e0b90b474556e34d8e0bd17eca429fa7
  summary: >-
    You'll use a Google Cloud C4A virtual machine powered by Google Axion to build a custom
    Yocto-based NVIDIA JetPack image. You'll configure the build with OpenEmbedded, BitBake, and
    target layers, then create a bundled flashing archive. Then, you'll transfer the archive to a
    local Ubuntu host and flash it to a supported NVIDIA Jetson platform. After the device boots,
    you'll explore the Matchbox desktop and verify the NVIDIA GPU drivers and Docker runtime.
  faqs:
  - question: Which Google Cloud machine type should I use, and how do I verify it?
    answer: >-
      Use the `c4a-standard-32` machine type, which provides 32 vCPUs and 128 GB of memory. In the
      Google Cloud console, confirm that **Series** is set to **C4A** and **Machine type** is set to
      **c4a-standard-32**.
  - question: What output should I expect after the Yocto build completes?
    answer: >-
      The build summary reports `BUILD COMPLETE` and lists the workspace, deploy directory,
      primary flashing image, and bundle archive paths. Confirm that the generated `.tar.gz`
      archive exists before continuing.
  - question: How do I transfer the build artifact from the C4A VM to my Ubuntu host?
    answer: >-
      Install the Google Cloud CLI on your Ubuntu host and authenticate with `gcloud auth login`.
      Then use `gcloud compute scp` to copy the bundled archive from the C4A VM to your host.
  - question: What do I need to install on my Ubuntu host before flashing?
    answer: >-
      Use Ubuntu 22.04 or later with USB access to the Jetson device. Install `dtc`,
      `build-essential`, `gdisk`, `gptfdisk`, `udisks2`, `bmap-tools`, `libxml2-utils`, `zstd`,
      `tar`, and `usbutils` before extracting and flashing the image.
  - question: How do I verify that the flashed Yocto image is working?
    answer: >-
      After the Matchbox desktop appears, open a terminal and run `nvidia-smi` and
      `docker --version`. Successful output confirms that the NVIDIA GPU drivers and Docker runtime
      are available.
# END generated_summary_faq

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
  - resource:
      title: Yocto on Jetson Platforms
      link: https://docs.nvidia.com/jetson/archives/r39.2/DeveloperGuide/AR/YoctoOnJetson.html
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
