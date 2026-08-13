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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:47:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f1cee48b7e94775896f620329ce3036dacb2399115be2974d92880f47bd58dca
  summary_generated_at: '2026-08-13T18:47:42Z'
  summary_source_hash: f1cee48b7e94775896f620329ce3036dacb2399115be2974d92880f47bd58dca
  faq_generated_at: '2026-08-13T18:47:42Z'
  faq_source_hash: f1cee48b7e94775896f620329ce3036dacb2399115be2974d92880f47bd58dca
  summary: >-
    You'll use an Arm Linux server to build MXNet in a Raspberry Pi OS file system before deploying
    it to a Raspberry Pi. First, you'll install build dependencies, switch to the `pi` user, and
    compile MXNet inside the target file system. Then, you'll retrieve the updated image, write it
    to an SD card, and start it on a Raspberry Pi 3 or 4.
  faqs:
  - question: How do I know I’m working inside the Raspberry Pi OS file system before building?
    answer: >-
      You should have a root (#) prompt within the Raspberry Pi OS environment and be able to
      switch to the `pi` user.
  - question: Which user should I use to build MXNet?
    answer: >-
      Switch from root to the `pi` user before building. Run `su pi` and work from the `pi` user's home
      directory.
  - question: What packages do I need to install before cloning and building MXNet?
    answer: >-
      Install `git`, `cmake`, `ninja-build`, `gfortran`, `lapack/blas`, OpenCV, OpenBLAS, `python3-dev`,
      `python3-pip`, `python-dev`, and `virtualenv` with `apt`. Then, install Cython with `pip3`.
  - question: Which file should I copy from the server to write to the SD card?
    answer: >-
      Copy the Raspberry Pi OS image you built on the server with `scp` using your server's IP address and SSH key.
  - question: Can I complete this Learning Path without a physical Raspberry Pi?
    answer: >-
      Yes. The Raspberry Pi deployment step is optional, so you can stop after producing the Raspberry
      Pi OS image with MXNet built on the Arm server.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
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
