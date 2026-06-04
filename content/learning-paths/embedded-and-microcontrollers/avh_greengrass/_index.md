---
title: Deploy IoT applications with AWS IoT Greengrass and Arm Virtual Hardware

description: Learn how to set up AWS IoT Greengrass Core on Arm Virtual Hardware and deploy AWS Greengrass components to a virtual Raspberry Pi 4 device.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded software developers interested in AWS IoT Greengrass.

learning_objectives: 
    - Start a Raspberry Pi Arm Virtual Hardware instance.
    - Deploy pre-built AWS IoT Greengrass components on Arm Virtual Hardware.

prerequisites:
    - An Amazon AWS account
    - An Arm Virtual Hardware account
    - Some familiarity with embedded Linux

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:03:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  summary_generated_at: '2026-06-01T21:27:06Z'
  summary_source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  faq_generated_at: '2026-06-02T22:03:50Z'
  faq_source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  summary: >-
    This introductory Learning Path guides embedded Linux developers through running a virtual
    Raspberry Pi 4 on Arm Virtual Hardware and deploying AWS IoT Greengrass components to it.
    You will create or use existing accounts for Arm Virtual Hardware and AWS, start a Raspberry
    Pi Arm Virtual Hardware instance, set up AWS IoT Greengrass Core on the device, and use the
    AWS IoT console to define and launch a Greengrass deployment of pre-built components. The
    steps focus on essential configuration and deployment actions in a Linux environment. Prerequisites
    include an Amazon AWS account, an Arm Virtual Hardware account, and some familiarity with
    embedded Linux.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Amazon AWS account, an Arm Virtual Hardware (AVH) account, and some familiarity
      with embedded Linux. These are the only explicit prerequisites.
  - question: Will I be charged by AWS or Arm Virtual Hardware during this tutorial?
    answer: >-
      AWS requires a credit card, but this Learning Path uses free tier only and can be completed
      without incurring charges. New AVH accounts are automatically enrolled in a free 30-day
      trial.
  - question: Which virtual device does this Learning Path use?
    answer: >-
      It uses a Raspberry Pi 4 virtual device provided by Arm Virtual Hardware. You will start
      this virtual device as part of the steps.
  - question: Where do I create the AWS IoT Greengrass deployment?
    answer: >-
      In the AWS console, open the IoT Core service and navigate to Manage -> Greengrass devices
      -> Deployments. Click Create to start a new Greengrass deployment.
  - question: How do I change what runs on the device after deployment?
    answer: >-
      Modify the Greengrass deployment to change component configurations, add components, or
      remove components. Deployments are designed to be updated in place.
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
    - AWS IoT Greengrass
    - Raspberry Pi


further_reading:
    - resource:
        title: AWS IoT Greengrass CLI documentation 
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-cli-component.html
        type: documentation
    - resource:
        title: Develop AWS IoT Greengrass components
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/develop-greengrass-components.html
        type: documentation
    - resource:
        title: AWS IoT Greengrass v2 Developer Guide 
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

