---
title: Build embedded Linux applications on an Arm server

description: Learn how to reduce compile time for embedded Linux projects by installing a Raspberry Pi OS file system on an Arm server, building the MXNet machine learning framework, and transferring it to a Raspberry Pi.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to reduce compile time for embedded Linux software projects.

learning_objectives:
    - Install a Raspberry Pi OS file system on an Arm server
    - Reduce compile time for a Linux application, the MXNet machine learning framework
    - Transfer the compiled MXNet application to a Raspberry Pi and test it
    - Utilize an Arm server to reduce compile time for your own embedded Linux projects

prerequisites:
    - An Arm computer running Linux. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - A Raspberry Pi 3 or 4 board


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:40:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 17721158fe10e97314af364f138c32b7bcf53fdc88fe11fffeb5765f11e26b79
  summary_generated_at: '2026-06-01T21:52:22Z'
  summary_source_hash: 17721158fe10e97314af364f138c32b7bcf53fdc88fe11fffeb5765f11e26b79
  faq_generated_at: '2026-06-02T22:40:08Z'
  faq_source_hash: 17721158fe10e97314af364f138c32b7bcf53fdc88fe11fffeb5765f11e26b79
  summary: >-
    This advanced Learning Path shows how to cut compile time for embedded Linux work by building
    the MXNet machine learning framework on an Arm Linux server using a Raspberry Pi OS file system,
    then deploying the result to a Raspberry Pi. You will set up an Arm server (Ubuntu 22.04 was
    tested), enter the Raspberry Pi OS environment, install build dependencies, and compile MXNet
    as the pi user. The steps cover exporting the resulting Raspberry Pi image from the server
    via scp, writing it to an SD card, and testing on a Raspberry Pi 3 or 4. Prerequisites include
    an Arm computer running Linux (on-premises or cloud) and, optionally, a Raspberry Pi board
    for testing.
  faqs:
  - question: What do I need on the Arm server before starting?
    answer: >-
      An Arm Linux server or an Arm cloud instance running Ubuntu is required; the instructions
      were tested on Ubuntu 22.04. Verify you can use SSH to connect. A Raspberry Pi 3 or 4 is
      only needed to test the compiled application, and that step is optional if a board is not
      available.
  - question: How do I know I am inside the Raspberry Pi OS file system before installing dependencies?
    answer: >-
      Proceed when you have a root shell inside the Raspberry Pi OS file system; the prompt appears
      as #. The steps then run apt to update and install packages in that environment.
  - question: Which user should compile MXNet, and where should I run the build?
    answer: >-
      After installing packages as root, switch to user pi (su pi). Use the pi home directory
      ($HOME) to build the application.
  - question: Which packages are required to build MXNet in this path?
    answer: >-
      Run apt update/upgrade and install: git, cmake, ninja-build, gfortran, liblapack*, libblas*,
      libopencv*, libopenblas*, python3-dev, python3-pip, python-dev, and virtualenv. Then install
      Cython with pip3.
  - question: How do I transfer the built image and deploy it on a Raspberry Pi?
    answer: >-
      From your local machine, use scp with your SSH key and server IP to download the image (for
      example: scp -i <your-key.pem> ubuntu@<your-ip-addr>:~/2023-02-21-raspios-bullseye-arm64-lite.img
      .). Write the image to an SD card and insert it into a Raspberry Pi 3 or 4 to test.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A72
operatingsystems:
    - Linux
tools_software_languages:
    - Raspberry Pi
    - MXNet

further_reading:
    - resource:
        title: MXNet tutorials
        link: https://mxnet.apache.org/versions/1.2.1/tutorials/index.html 
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

