---
title: Get started with object detection using a Jetson Orin Nano

description: Learn how to set up a Jetson Orin Nano with a MIPI CSI-2 camera and perform real-time object detection from live video and image files using DetectNet and TensorRT.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers interested in integrating object detection into their applications.

learning_objectives:
    - Set up a Jetson Orin Nano with a MIPI CSI-2 camera for object detection
    - Detect objects from both live video and image files

prerequisites:
    - A [Jetson Orin Nano](https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/index.html)
    - A microSD card (64GB UHS-1 or larger is recommended)
    - A MIPI CSI-2 camera, with a 22 pin connector on at least one end

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:25:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fdf582f1b54f372768a2c896e1da152c50d22c3bd238848253cdbe18cc68222d
  summary_generated_at: '2026-06-01T21:42:08Z'
  summary_source_hash: fdf582f1b54f372768a2c896e1da152c50d22c3bd238848253cdbe18cc68222d
  faq_generated_at: '2026-06-02T22:25:46Z'
  faq_source_hash: fdf582f1b54f372768a2c896e1da152c50d22c3bd238848253cdbe18cc68222d
  summary: >-
    This introductory path shows how to bring up a Jetson Orin Nano on Linux with a MIPI CSI-2
    camera and run real-time object detection using DetectNet and TensorRT. You will download
    the latest Jetson Orin Nano developer kit image from the NVIDIA site and write it to a microSD
    card with balenaEtcher, then clone and launch the jetson-inference Docker container. From
    there, you will run DetectNet on a live CSI camera stream and on image files, including adjusting
    detection thresholds. Required hardware is a Jetson Orin Nano, a 64GB (UHS-1 recommended)
    microSD card, and a MIPI CSI-2 camera with a 22‑pin connector. The estimated completion time
    is about 60 minutes.
  faqs:
  - question: What do I need before starting the setup?
    answer: >-
      You need a Jetson Orin Nano, a microSD card (64GB UHS-1 or larger is recommended), and a
      MIPI CSI-2 camera with a 22-pin connector. No other prerequisites are explicitly listed.
  - question: How do I write the Jetson image to the microSD card?
    answer: >-
      Download the Jetson Orin Nano Developer Kit image from the NVIDIA developer website (expand
      the Jetson Xavier NX & Orin Nano section, then select the Jetson Orin Nano Developer Kit).
      Use balenaEtcher, choose Flash from file, and select the downloaded zip file without unzipping
      it.
  - question: How do I download and start the jetson-inference Docker container?
    answer: >-
      Clone the repository with git clone --recursive --depth=1 https://github.com/dusty-nv/jetson-inference,
      change into the jetson-inference directory, and run docker/run.sh to download and launch
      the container.
  - question: How do I check that the Docker container is running and find its ID?
    answer: >-
      Run sudo docker ps -q to print the container ID. A hex string (for example, 174055df45cd)
      indicates the container is active.
  - question: How do I run DetectNet on the live camera and adjust sensitivity?
    answer: >-
      Inside the container, change to build/aarch64/bin and run ./detectnet csi://0 to process
      the live camera stream. Adjust sensitivity with --threshold (default 0.5). The first run
      can take longer, and you should see object labels rendered in real time.
# END generated_summary_faq

author: Gabriel Peterson

### Tags
skilllevels: Introductory

subjects: ML

armips:
    - Cortex-A

operatingsystems:
    - Linux

tools_software_languages:
    - DetectNet
    - TensorRT
    - Docker


further_reading:
    - resource:
        title: Jetson Inference
        link: https://github.com/dusty-nv/jetson-inference
        type: documentation
    - resource:
        title: Jetson Orin Nano Developer Kit User Guide
        link: https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/index.html
        type: website
    - resource:
        title: Jetson Orin Modules and Developer Kits
        link: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

