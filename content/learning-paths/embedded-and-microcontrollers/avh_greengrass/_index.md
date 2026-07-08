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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:22:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  summary_generated_at: '2026-07-08T15:22:29Z'
  summary_source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  faq_generated_at: '2026-07-08T15:22:29Z'
  faq_source_hash: 85845fd4a47960bca053aed8d87c1d1442a7f5de0be5caff349fc92c6980b07e
  summary: >-
    You'll use Arm Virtual Hardware (AVH) with AWS IoT Greengrass to
    deploy IoT software to a virtual Raspberry Pi 4. First, you'll start a Raspberry Pi instance in
    AVH, then use the AWS console to create and manage a Greengrass deployment that defines pre-built
    components and their configurations. You'll walk through where to create a deployment in
    AWS IoT Core and how to adjust it by adding, removing, or reconfiguring components. By the
    end, you'll create a Greengrass deployment and apply it to the virtual device so you can iterate
    on component selection and configuration using the standard Greengrass deployment workflow.
  faqs:
  - question: What is an AWS IoT Greengrass deployment?
    answer: >-
      A deployment is a defined set of components and their configurations managed by AWS IoT
      Greengrass. You'll use it to apply or update components on your device.
  - question: Where do I create a Greengrass deployment in the AWS console?
    answer: >-
      Go to **IoT Core**, then navigate to **Manage -> Greengrass devices -> Deployments** and click **Create**.
  - question: Can I change which components are in a deployment after I create it?
    answer: >-
      Yes. You can modify a deployment to change configurations, add components, or remove components.
  - question: Which virtual device should I start in Arm Virtual Hardware?
    answer: >-
      Start a Raspberry Pi 4 virtual device to align with the steps in this Learning Path.
  - question: Will I be charged while following this Learning Path?
    answer: >-
      A new AVH account is automatically enrolled in a free 30-day trial. AWS requires a credit
      card, but the steps use free tier only and can be completed without incurring charges.
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

