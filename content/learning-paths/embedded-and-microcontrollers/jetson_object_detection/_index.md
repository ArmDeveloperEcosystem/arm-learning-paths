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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:07:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7fb5ed9785035997a9f31381c71fd8b02dd3c4b4afb1e9e5c0989b41a0034aa9
  summary_generated_at: '2026-08-12T20:07:54Z'
  summary_source_hash: 7fb5ed9785035997a9f31381c71fd8b02dd3c4b4afb1e9e5c0989b41a0034aa9
  faq_generated_at: '2026-08-12T20:07:54Z'
  faq_source_hash: 7fb5ed9785035997a9f31381c71fd8b02dd3c4b4afb1e9e5c0989b41a0034aa9
  summary: >-
    You'll prepare a Jetson Orin Nano for object detection with a microSD image and MIPI CSI-2
    camera. First, you'll clone `jetson-inference`, launch its Docker container, and run TensorRT-accelerated
    DetectNet on live camera input and image files. Then, you'll adjust the detection threshold and
    verify labeled objects in the resulting video and images.
  faqs:
  - question: Which image should I download for the microSD card?
    answer: >-
      On the NVIDIA developer website, expand **JETSON XAVIER NX DEVELOPER KIT & ORIN NANO DEVELOPER
      KIT**, then select **JETSON Orin Nano DEVELOPER KIT** to download the latest
      image.
  - question: Where should I run the Docker commands, and how do I get the container ID?
    answer: >-
      Run the Docker commands in a terminal on the host, not from inside the running container.
      To print the container ID, use `sudo docker ps -q`.
  - question: How do I start DetectNet on the live camera, and from which directory?
    answer: >-
      Change into the binaries directory with `cd build/aarch64/bin`. Start the live camera feed
      with `./detectnet csi://0`.
  - question: How can I adjust detection sensitivity, and what is the default?
    answer: >-
      Use the `--threshold` option to change sensitivity. For example, run
      `./detectnet csi://0 --threshold=0.25`. The default is `0.5`.
  - question: How do I run DetectNet on an image and save the annotated output?
    answer: >-
      From `build/aarch64/bin`, run `./detectnet --network=ssd-mobilenet-v2 images/peds_0.jpg`
      followed by your output path, such as `images/test/output.jpg`. The `--network` option is
      optional, and you can use `docker cp` to add your own images to the container.
# END generated_summary_faq

author: Gabriel Peterson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
