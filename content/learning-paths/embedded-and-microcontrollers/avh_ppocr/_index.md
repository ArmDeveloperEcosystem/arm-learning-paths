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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:05:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  summary_generated_at: '2026-06-01T21:28:14Z'
  summary_source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  faq_generated_at: '2026-06-02T22:05:16Z'
  faq_source_hash: 398077be1406d0787b0a5d8dc254472da0d125b51b0907769cd4a3516ce9111b
  summary: >-
    This introductory Learning Path shows how to export a PaddlePaddle inference model for text
    recognition, compile it with TVMC, and deploy it on the Arm Corstone-300 Fixed Virtual Platform
    (FVP) with Cortex-M55 using Arm Virtual Hardware. You will work with a PaddleOCR text recognition
    model in a bare-metal target environment, using tools listed in the path such as TVMC, GCC,
    Paddle, and Arm Virtual Hardware. The steps include an OCR overview and an end-to-end workflow
    from model preparation through final execution on the FVP. Prerequisites include basic familiarity
    with embedded and AI/ML development and an AWS account to subscribe to the Arm Virtual Hardware
    AMI. Expected duration is about 30 minutes.
  faqs:
  - question: What do I need before running the workflow?
    answer: >-
      You need an AWS account to subscribe to the Arm Virtual Hardware AMI, basic familiarity
      with embedded programming, and some experience with AI/ML development. No other prerequisites
      are explicitly listed.
  - question: Do I need to train a model, or does this use a pre-trained PaddlePaddle model?
    answer: >-
      The steps deploy pre-trained PaddlePaddle models. You export a Paddle inference model and
      compile it with TVMC before deployment.
  - question: Which Arm platform and runtime does this target?
    answer: >-
      The deployment targets the Corstone-300 FVP with an Arm Cortex-M55 processor, included with
      Arm Virtual Hardware. The operating system context is bare-metal.
  - question: How do I start the environment on AWS?
    answer: >-
      Begin by launching the Arm Virtual Hardware AMI on AWS. The Learning Path then guides you
      through the end-to-end flow from model export to execution on the Corstone-300 FVP.
  - question: What result should I expect after completing the steps?
    answer: >-
      You should complete model export and TVMC compilation and see the PaddleOCR text recognition
      model execute on the Corstone-300 FVP with Cortex-M55. Successful final execution on the
      FVP indicates the deployment worked.
# END generated_summary_faq

author: Liliya Wu

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

