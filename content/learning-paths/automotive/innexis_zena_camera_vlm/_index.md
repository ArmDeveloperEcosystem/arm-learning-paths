---
title: Build a Camera-to-VLM Pipeline on Arm Zena CSS

draft: true
cascade:
    draft: true
    
description: Capture a virtual camera frame in a Zena CSS Linux guest and submit it to a local vision-language model for a recorded functional check.

minutes_to_complete: 90

who_is_this_for: AI and vision developers who can access an Arm Zena CSS virtual platform in Siemens Innexis ANA.

learning_objectives:
    - Configure a reproducible video input for the Zena CSS virtual camera.
    - Capture and inspect one frame from the Linux guest's V4L2 device.
    - Prepare a vision-capable model and its matching image projector.
    - Run one local image prompt and save the input and response together.

prerequisites:
    - Access to a Zena CSS virtual platform in Siemens Innexis ANA and console or authorized SSH access to its EWAOL Linux guest after startup.
    - Complete Run Local LLM Inference with llama.cpp on Arm Zena CSS in the same Linux guest OS, so its llama-cli binary is available.
    - Permission to configure a virtual camera file input, and `ffmpeg` and `ffprobe` on your local computer to prepare video from public source media.
    - Enough guest storage and memory for a vision model; check the actual guest before downloading files.
    - A working guest file-transfer route and basic Linux command-line knowledge.

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Cortex-A
tools_software_languages:
    - Arm Zena CSS
    - Siemens Innexis ANA
    - GStreamer
    - llama.cpp
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm Zena Compute Subsystem
        link: https://www.arm.com/products/autonomous-machines/zena-compute-subsystems
        type: documentation
    - resource:
        title: llama.cpp multimodal documentation
        link: https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
