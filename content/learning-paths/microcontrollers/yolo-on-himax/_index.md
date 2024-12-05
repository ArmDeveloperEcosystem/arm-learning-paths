---
title: Run a Computer Vision Model on a Himax Microcontroller
draft: true
cascade:
    draft: true
minutes_to_complete: 90

who_is_this_for: This is an introduction topic explaining how to run a computer vision application on an embedded device from Himax. The example uses an off-the-shelf Himax WiseEye2 module which is based on Arm Cortex-M55 and Ethos-U55.

learning_objectives:
    - Run a you-only-look-once (YOLO) object detection model on the Himax device.
    - Build the Himax Software Development Kit (SDK) and generate the firmware image file.
    - Update the firmware on the Himax WiseEye2.

prerequisites:
    - A [Seeed Grove Vision AI Module V2](https://www.seeedstudio.com/Grove-Vision-AI-Module-V2-p-5851.html) development board.
    - An [OV5647-62 Camera Module](https://www.seeedstudio.com/OV5647-69-1-FOV-Camera-module-for-Raspberry-Pi-3B-4B-p-5484.html) and included FPC cable.
    - A USB-C cable.
    - An x86 Linux machine or a Mac running macOS with Apple Silicon.

author_primary: Chaodong Gong, Alex Su, Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M55
    - Ethos-U55
tools_software_languages:
    - Himax SDK
    - Python
operatingsystems:
    - Linux
    - macOS

draft: true
cascade:
    draft: true


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
