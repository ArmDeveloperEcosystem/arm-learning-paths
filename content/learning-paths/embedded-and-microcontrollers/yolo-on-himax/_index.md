---
title: Run a Computer Vision Model on a Himax Microcontroller

description: Learn how to run a YOLO object detection model on the Himax WiseEye2 module, build the Himax SDK, update firmware, and connect to the Grove Vision AI module for computer vision applications.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who would like to learn about how to run a computer vision application on an embedded device from Himax.

learning_objectives:
    - Run a You-Only-Look-Once (YOLO) object detection model on a Himax WiseEye2 module.
    - Build the Himax Software Development Kit (SDK) and generate a firmware image file.
    - Update firmware on the Himax WiseEye2.
    - Connect to and use Grove Vision AI module.

prerequisites:
    - A [Seeed Grove Vision AI Module V2](https://www.seeedstudio.com/Grove-Vision-AI-Module-V2-p-5851.html) development board.
    - An [OV5647-62 Camera Module](https://www.seeedstudio.com/OV5647-69-1-FOV-Camera-module-for-Raspberry-Pi-3B-4B-p-5484.html).
    - A Flexible Printed Circuit (FPC) cable.
    - A USB-C cable.
    - An x86 Linux machine, or a Mac running macOS.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:54:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b0cb917bdcfb601c054e6cac93b2d04aca3ffe84b5a1963288fd7b89dd9bad3b
  summary_generated_at: '2026-06-01T22:00:17Z'
  summary_source_hash: b0cb917bdcfb601c054e6cac93b2d04aca3ffe84b5a1963288fd7b89dd9bad3b
  faq_generated_at: '2026-06-02T22:54:16Z'
  faq_source_hash: b0cb917bdcfb601c054e6cac93b2d04aca3ffe84b5a1963288fd7b89dd9bad3b
  summary: >-
    Build and deploy a YOLO object detection application on the Himax WiseEye2 platform (Arm Cortex-M55
    with Ethos-U55) using the Seeed Grove Vision AI Module V2. You will prepare a Linux or macOS
    host, install Python, clone the Himax examples repository, build the Himax SDK to generate
    a firmware image, and flash the microcontroller using Xmodem. After connecting the OV5647
    camera via the FPC cable and USB-C, you will run the firmware to view a live camera feed and
    explore additional models by editing a makefile and selecting a model in the web toolkit.
    Prerequisites include the Grove Vision AI Module V2, OV5647 camera, FPC and USB-C cables,
    and an x86 Linux machine or a Mac. Estimated time: 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Seeed Grove Vision AI Module V2, an OV5647-62 camera module, a Flexible Printed
      Circuit (FPC) cable, a USB-C cable, and an x86 Linux machine or a Mac running macOS.
  - question: Which operating systems are supported, and can I use Windows?
    answer: >-
      The path has been validated on Ubuntu 22.04 LTS and macOS. If you use Windows, you can run
      Ubuntu through Windows Subsystem for Linux 2 (WSL2).
  - question: How do I clone the Himax project with all required submodules?
    answer: >-
      Clone the repository recursively so that subrepositories are included: git clone --recursive
      https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git. Then change into
      the cloned directory to proceed with the build steps.
  - question: How do I install Xmodem for flashing the firmware?
    answer: >-
      From the repository root, run: cd $HOME/Seeed_Grove_Vision_AI_Module_V2 and pip install
      -r xmodem/requirements.txt. Xmodem is used to transfer the compiled firmware image to the
      microcontroller.
  - question: How do I select and run different models, such as YOLO object detection?
    answer: >-
      Edit the makefile in $HOME/Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S/ and set APP_TYPE
      (for example, tflm_yolov8_od for object detection). Use the corresponding model argument
      with the --model option in the Xmodem command; after flashing, you will view a live camera
      feed with the application running.
# END generated_summary_faq

author:
    - Chaodong Gong
    - Alex Su
    - Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M55
    - Ethos-U55
tools_software_languages:
    - Himax SDK
    - Python
    - Hugging Face

operatingsystems:
    - Linux
    - macOS




further_reading:
    - resource:
        title: Grove Vision AI Module V2 User Documentation
        link: https://wiki.seeedstudio.com/grove_vision_ai_v2/
        type: documentation
    - resource:
        title: WiseEye2 HX6538 processor blog (SoC powering Grove Vision AI Module V2) 
        link: https://www.himax.com.tw/products/wiseeye-ai-sensing/wiseeye2-ai-processor/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

