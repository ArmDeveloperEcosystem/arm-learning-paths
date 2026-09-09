---
title: Deploy ML models to Arm edge devices using Edge Impulse and AWS IoT Greengrass

description: Learn how to deploy Edge Impulse ML models to Arm-based Linux edge devices using AWS IoT Greengrass custom components.

minutes_to_complete: 180

who_is_this_for: This Learning Path is for embedded and IoT engineers who want to deploy Edge Impulse ML models to Arm-based edge devices at scale using AWS IoT Greengrass.

learning_objectives:
    - Set up an Arm-based edge device for ML inference with Edge Impulse.
    - Install and configure AWS IoT Greengrass on the edge device.
    - Deploy an Edge Impulse ML model as a Greengrass custom component.
    - Verify model inference results through AWS IoT Core.

prerequisites:
    - An [Edge Impulse Studio](https://studio.edgeimpulse.com/signup) account
    - An [AWS account](https://aws.amazon.com/) with administrator access
    - A supported Arm-based edge device such as a Raspberry Pi 5, NVIDIA Jetson, Qualcomm Dragonwing QC6490, or an Arm-based Amazon EC2 instance
    - An SSH client and familiarity with the Linux command line
    - Basic understanding of ML concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-08T19:59:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f79311c5af9a429f3bcfb63f31c0e3113b392811870ae92632d90c3880f8f670
  summary_generated_at: '2026-09-08T19:59:44Z'
  summary_source_hash: f79311c5af9a429f3bcfb63f31c0e3113b392811870ae92632d90c3880f8f670
  faq_generated_at: '2026-09-08T19:59:44Z'
  faq_source_hash: f79311c5af9a429f3bcfb63f31c0e3113b392811870ae92632d90c3880f8f670
  summary: >-
    You'll deploy an Edge Impulse ML model to an Arm-based Linux edge device with AWS IoT Greengrass.
    First, you'll choose and prepare a supported device or Arm-based Amazon EC2 instance. Then, you'll
    clone and build an Edge Impulse project, install Greengrass, and store your API key in AWS
    Secrets Manager. Finally, you'll deploy the custom component and verify inference results in AWS
    IoT Core.
  faqs:
  - question: What should I use to complete the
      steps if I don't have a supported hardware board?
    answer: >-
      You can use an Arm-based Amazon EC2 instance as a local edge device and complete every step.
  - question: What do I need before running the AWS IoT Greengrass installer on the device?
    answer: >-
      Before installation, provide your AWS access credentials so you can register your device with
      AWS IoT Core and configure the required resources.
  - question: How should I store my Edge Impulse API key for the Greengrass component?
    answer: >-
      Store your Edge Impulse API key in AWS Secrets Manager with the secret ID `EI_API_KEY`. Set
      its key to `ei_api_key`.
  - question: Why does the Greengrass component need an Edge Impulse API key?
    answer: >-
      The component uses your API key to authenticate with your Edge Impulse project and download
      the model.
  - question: What result should I expect after deploying the custom component?
    answer: >-
      You can verify that your model runs on your Arm-based device and view its inference results
      in AWS IoT Core.
# END generated_summary_faq

author: Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
platforms:
    - AWS
subjects: ML
armips:
    - Cortex-M
    - Cortex-A
    - Neoverse

tools_software_languages:
    - Edge Impulse
    - AWS IoT Greengrass
    - GStreamer

operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Edge Impulse for beginners
        link: https://docs.edgeimpulse.com/docs/readme/for-beginners
        type: documentation
    - resource:
        title: AWS IoT Greengrass developer guide
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html
        type: documentation
    - resource:
        title: Edge Impulse AWS Greengrass integration
        link: https://docs.edgeimpulse.com/docs/integrations/aws-greengrass
        type: documentation
    - resource:
        title: Edge Impulse Greengrass components repository
        link: https://github.com/edgeimpulse/aws-greengrass-components
        type: website

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
