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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:02:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  summary_generated_at: '2026-06-01T21:26:34Z'
  summary_source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  faq_generated_at: '2026-06-02T22:02:28Z'
  faq_source_hash: 983afd3fcc565266c8f12588086e36d736540e23d0e748c94b5d2a45ab53d6ab
  summary: >-
    This introductory Learning Path shows how to prepare a custom Balena OS image, run it on Arm
    Virtual Hardware as a virtual Raspberry Pi 4, and deploy a pre-built IoT application from
    Balena Hub. Working from a Linux machine with root access, you create a Balena Cloud fleet,
    start a Raspberry Pi 4 instance in Arm Virtual Hardware, and upload the balenaos_rpi4b.zip
    firmware. You then deploy a Grafana dashboard from Balena Hub to view the state of your device.
    Prerequisites include a Balena Cloud account, an Arm Virtual Hardware account, and some familiarity
    with embedded Linux. By the end, you will have a managed virtual device and a running application
    in about 30 minutes.
  faqs:
  - question: What do I need before I start?
    answer: >-
      You need a Balena Cloud account, an Arm Virtual Hardware account, and a Linux machine with
      root access. A free Balena Cloud account supports up to 10 devices, and this path uses one
      device. If you create a new AVH account, you are automatically enrolled in a free 30-day
      trial.
  - question: When and why do I create a fleet in Balena Cloud?
    answer: >-
      After signing up for Balena Cloud, create a fleet. A fleet groups devices and acts as the
      single deployment target for your applications.
  - question: In Arm Virtual Hardware, which device should I select and how do I provide the OS
      image?
    answer: >-
      From the AVH dashboard, click Create Device and select Raspberry Pi 4. When prompted for
      firmware, choose Upload your own firmware and provide the balenaos_rpi4b.zip image you prepared.
  - question: How do I open Balena Hub and which example application should I deploy?
    answer: >-
      Use the Balena Hub button in the top right of the Balena Cloud dashboard to open Balena
      Hub. Go to Apps and search for balena-app, which deploys a Grafana dashboard showing the
      state of your Balena OS device.
  - question: Can I follow this path without using the hosted Balena Cloud service?
    answer: >-
      OpenBalena can deploy Balena applications without the hosted service, but this Learning
      Path uses Balena Cloud. Follow the steps as written to use the hosted workflow.
# END generated_summary_faq

author: Michael Hall

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

