---
title: Run a computer vision model on a Himax microcontroller

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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:00:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0f19a85594bbc7811f5179c0658b80a4b053bc62a8f51e874919dcd3e9cab9ec
  summary_generated_at: '2026-08-13T19:00:42Z'
  summary_source_hash: 0f19a85594bbc7811f5179c0658b80a4b053bc62a8f51e874919dcd3e9cab9ec
  faq_generated_at: '2026-08-13T19:00:42Z'
  faq_source_hash: 0f19a85594bbc7811f5179c0658b80a4b053bc62a8f51e874919dcd3e9cab9ec
  summary: >-
    You'll build and deploy a YOLO computer-vision example on a Himax WiseEye2 microcontroller with the
    Grove Vision AI Module V2. First, you'll prepare the host, clone the example repository, and build
    firmware. Then, you'll connect the camera, select an application in the makefile, flash the device,
    and verify its live feed on Cortex-M55 and Ethos-U55 hardware.
  faqs:
  - question: How do I clone the correct Himax examples and make sure submodules are included?
    answer: >-
      Run `git clone --recursive https://github.com/HimaxWiseEyePlus/Seeed_Grove_Vision_AI_Module_V2.git`,
      then change into the new directory. The `--recursive` option pulls the required third-party
      subrepositories.
  - question: Where do I change the application type and which option should I pick for YOLO object
      detection?
    answer: >-
      Go to `Seeed_Grove_Vision_AI_Module_V2/EPII_CM55M_APP_S` and open the makefile. Set `APP_TYPE`
      to a value from the provided table. For object detection, use `tflm_yolov8_od`. Then, pass the
      corresponding model argument with the `--model` option when flashing.
  - question: How do I install the Xmodem dependency before flashing?
    answer: >-
      From the repository root, run `pip install -r xmodem/requirements.txt`. This installs an
      Xmodem file transfer utility used by the flashing scripts.
  - question: How should I connect the camera module to the Grove Vision AI V2?
    answer: >-
      Insert the flexible printed circuit (FPC) cable into the module’s connector and lift the
      dark grey latch, then secure the cable. Connect the board to the host with
      a USB-C cable.
  - question: What result should I expect after flashing, and how do I know the model is running?
    answer: >-
      You should be able to view a live camera feed with the computer vision application active.
      If you selected the YOLO option, expect object detection to appear in the feed.
# END generated_summary_faq

author:
    - Chaodong Gong
    - Alex Su
    - Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
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
