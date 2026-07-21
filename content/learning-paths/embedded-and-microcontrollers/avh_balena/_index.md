---
title: Deploy IoT applications with Balena Cloud and Arm Virtual Hardware

description: Learn how to create a custom Balena OS image, run it on Arm Virtual Hardware, and deploy IoT applications to a virtual Raspberry Pi 4 device.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers interested in Balena OS.

learning_objectives: 
    - Start a Raspberry Pi Arm Virtual Hardware instance
    - Create a Balena OS image for Arm Virtual Hardware
    - Deploy a pre-built Balena Hub application 

prerequisites:
    - A Balena Cloud account
    - An Arm Virtual Hardware account
    - A Linux machine with root access
    - Some familiarity with embedded Linux

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:21:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  summary_generated_at: '2026-07-08T15:21:56Z'
  summary_source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  faq_generated_at: '2026-07-08T15:21:56Z'
  faq_source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  summary: >-
    You'll prepare a BalenaOS image for Arm Virtual Hardware,
    provisioning a virtual Raspberry Pi 4, and deploy a pre-built application from Balena Hub.
    First, you'll create a Balena Cloud account and fleet to organize deployments. Then, you'll start an Arm Virtual
    Hardware device and upload the custom BalenaOS firmware. With the device running, you'll navigate
    from the Balena Cloud dashboard to Balena Hub and select a ready-made application to deploy.
    You'll then deploy an example app that uses the `balena-app` Grafana dashboard to visualize the device state, providing
    a quick way to validate that the virtual Raspberry Pi 4 is up, connected, and receiving an
    application from Balena Cloud.
  faqs:
  - question: What device type should I select in Arm Virtual Hardware?
    answer: >-
      Choose **Raspberry Pi 4** when creating the device in Arm Virtual Hardware.
  - question: Which firmware option and file do I use when creating the AVH device?
    answer: >-
      Use the **Upload your own firmware** option and select the `balenaos_rpi4b.zip` file.
  - question: How do I access Balena Hub from the Balena Cloud dashboard?
    answer: >-
      Click the **Balena Hub** button in the top right corner of the Balena Cloud dashboard.
  - question: Which example application should I deploy from Balena Hub?
    answer: >-
      Open **Apps** on Balena Hub and search for `balena-app`. This example provides a Grafana dashboard.
  - question: What result should I expect after deploying the Grafana example?
    answer: >-
      The Grafana dashboard displays the state of your BalenaOS device, confirming that the application
      deployed to the virtual Raspberry Pi 4.
# END generated_summary_faq

author: Michael Hall

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory

subjects: Embedded Linux

armips:
    - Cortex-A

operatingsystems:
    - Linux

tools_software_languages:
    - Arm Virtual Hardware
    - balenaCloud
    - Raspberry Pi
    - BalenaOS

further_reading:
    - resource:
        title: Balena OS 
        link: https://www.balena.io/os
        type: website
    - resource:
        title: Package Custom U-Boot Firmware for AVH
        link: https://intercom.help/arm-avh/en/articles/7851972-package-custom-u-boot-firmware-for-avh
        type: blog
    - resource:
        title: Balena Hub 
        link: https://hub.balena.io/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

