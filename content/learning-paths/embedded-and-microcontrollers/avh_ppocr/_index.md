---
title: Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware

description: Learn how to export and compile a PaddleOCR text recognition model using TVMC and deploy it on the Arm Corstone-300 FVP with Cortex-M55 processors.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in using PaddlePaddle for Arm Cortex-M processors.

learning_objectives: 
    - Export Paddle inference model
    - Compile Paddle inference model with TVMC
    - Deploy on the AVH Corstone-300 platform with Arm Cortex-M55

prerequisites:
    - Some familiarity with embedded programming 
    - Some familiarity with AI/ML software development 
    - An Amazon Web Services(AWS) [account](https://aws.amazon.com/) to subscribe [Arm Virtual Hardware](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g) Amazon Machine Image(AMI)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:23:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  summary_generated_at: '2026-07-08T15:23:39Z'
  summary_source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  faq_generated_at: '2026-07-08T15:23:39Z'
  faq_source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  summary: >-
    You'll export a PaddlePaddle OCR text recognition inference
    model, compile it with TVMC, and deploy the result to the Arm Corstone-300 Fixed Virtual
    Platform (FVP) with Cortex-M55 processors using Arm Virtual Hardware. You'll follow an end-to-end
    flow that starts with a pre-trained PaddlePaddle model, produces a TVMC-compiled output for
    the target, and runs the workload in a bare-metal environment on the FVP. Along the way, you'll
    make the key export, compilation, and deployment choices required for Cortex-M, then validate
    the workflow by executing the model on the virtual platform.
  faqs:
  - question: Do I need to train an OCR model for this workflow?
    answer: >-
      No. The steps use a pre-trained PaddlePaddle model for text recognition, so you export and
      deploy the inference model without training.
  - question: What is exported from PaddlePaddle before compilation?
    answer: >-
      You'll export a Paddle inference model that TVMC can compile.
  - question: Which target should I choose when running TVMC?
    answer: >-
      Compile the model for the Arm Corstone-300 Fixed Virtual Platform with Cortex-M55 processors.
      The workflow prepares an output intended for that target.
  - question: Where does the compiled model run?
    answer: >-
      It runs on the Corstone-300 FVP included with Arm Virtual Hardware. You'll begin by launching
      the Arm Virtual Hardware Amazon Machine Image (AMI) on AWS.
  - question: Does this Learning Path cover text detection or only recognition?
    answer: >-
      The Learning Path focuses on text recognition, the stage after text detection that converts an image region
      into text. Text detection and model training are out of scope.
# END generated_summary_faq

author: Liliya Wu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Corstone
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
    - GCC
    - Paddle
    - TVMC

further_reading:
    - resource:
        title: AVH Product Overview
        link: https://arm-software.github.io/AVH/main/overview/html/index.html
        type: documentation
    - resource:
        title: PaddleOCR
        link: https://github.com/PaddlePaddle/PaddleOCR
        type: website
    - resource:
        title: Paddle examples for AVH
        link: https://github.com/ArmDeveloperEcosystem/Paddle-examples-for-AVH/tree/main/Object-Detection-example
        type: website
    - resource:
        title: Arm and Baidu PaddlePaddle blog
        link: https://www.arm.com/blogs/blueprint/baidu-paddlepaddle
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
