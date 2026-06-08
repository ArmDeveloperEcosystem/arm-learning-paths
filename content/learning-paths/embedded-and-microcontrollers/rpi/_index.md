---
title: Get started with the Raspberry Pi 4

description: Learn how to build and run multiple software examples on the Raspberry Pi 4, including TensorFlow and Docker applications, and compare its performance to Arm cloud servers.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for software developers interested in the Raspberry Pi 4.

learning_objectives: 
    - Build and run multiple software examples on the Raspberry Pi 4
    - Compare and contrast the Raspberry Pi 4 to an Arm cloud server

prerequisites:
    - A Raspberry Pi 4 board
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:39:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5e5fad1563b67ed38d1cf3399d8e0d62162e76cae8d6848c3be7638f67cd037c
  summary_generated_at: '2026-06-01T21:51:21Z'
  summary_source_hash: 5e5fad1563b67ed38d1cf3399d8e0d62162e76cae8d6848c3be7638f67cd037c
  faq_generated_at: '2026-06-02T22:39:04Z'
  faq_source_hash: 5e5fad1563b67ed38d1cf3399d8e0d62162e76cae8d6848c3be7638f67cd037c
  summary: >-
    This introductory Learning Path walks you through setting up a Raspberry Pi 4 with 64-bit
    Raspberry Pi OS and an Arm-based cloud instance, then running comparable software examples
    on both to understand relative performance. You will identify hardware characteristics with
    uname, build the Linux kernel, and install and run a TensorFlow quickstart using tensorflow-aarch64
    and tensorflow_io. The path also includes Docker applications, as indicated in the overview.
    By the end, you will have built and executed multiple examples on the Raspberry Pi 4 and contrasted
    the results with an Arm cloud server. Prerequisites are a Raspberry Pi 4 and an Arm-based
    instance from a cloud service provider. Estimated time to complete is about 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Raspberry Pi 4 and access to an Arm-based instance from a cloud service provider.
      Both systems should run 64-bit Linux for the comparisons in this path.
  - question: Which Raspberry Pi OS should I install and how?
    answer: >-
      Install the 64-bit version of Raspberry Pi OS. Use Raspberry Pi Imager on Windows, Linux,
      or macOS as recommended by the Raspberry Pi documentation.
  - question: How do I verify that both systems are 64-bit Arm and running Linux?
    answer: >-
      Run uname -a on the Raspberry Pi 4 and on the Arm cloud instance. You should see aarch64
      GNU/Linux in the output; exact kernel details may differ between systems.
  - question: How do I install and test TensorFlow in this path?
    answer: >-
      Install Python and pip with sudo apt install python-is-python3 python3-pip, then run pip
      install tensorflow-aarch64 tensorflow_io. Validate by running the TensorFlow quickstart
      code provided in the path.
  - question: What result should I expect from the Linux kernel compile comparison?
    answer: >-
      You will compile the Linux kernel on both platforms to observe relative performance. Recent
      cloud servers are faster than a Raspberry Pi 4; the goal is to understand the differences,
      not to achieve a specific metric.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Embedded Linux
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Raspberry Pi
    - TensorFlow
    - Docker

further_reading:
    - resource:
        title: Raspberry Pi OS documentation
        link: https://www.raspberrypi.com/documentation/computers/os.html
        type: documentation
    - resource:
        title: Image Classification with MobilenetV2, Arm NN, and TensorFlow Lite Delegate pre-built binaries Tutorial
        link: https://developer.arm.com/documentation/102561
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

