---
title: Run object detection with Arm Runtime for YOLO26 on Raspberry Pi 5
description: Use Arm Runtime to run YOLO26n object detection on Raspberry Pi 5, inspect the Python example, and compare CPU inference with NCNN.

minutes_to_complete: 45
who_is_this_for: Python developers who want to run object detection on Raspberry Pi 5 and understand how and why to use the custom, optimized Arm runtime for YOLO26.

learning_objectives:
  - Run YOLO26n detection on Raspberry Pi 5 using the custom Arm Runtime.
  - Explain how the Python example loads and calls the custom runtime.
  - Understand how the runtime works, and how it differs from general purpose runtimes.
  - Export YOLO26n to NCNN and compare inference latency.

prerequisites:
  - A Raspberry Pi 5 running 64-bit Raspberry Pi OS Trixie with Python 3.13
  - Basic Python and Linux command-line knowledge
  - Basic familiarity with object detection and YOLO

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-27T15:15:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bb56442e5244d969af069b65a0738b8ce53924b28c9fcdb60dcce3fd0820a09f
  summary_generated_at: '2026-10-27T15:15:41Z'
  summary_source_hash: bb56442e5244d969af069b65a0738b8ce53924b28c9fcdb60dcce3fd0820a09f
  faq_generated_at: '2026-10-27T15:15:41Z'
  faq_source_hash: bb56442e5244d969af069b65a0738b8ce53924b28c9fcdb60dcce3fd0820a09f
  summary: >-
    You'll run YOLO26n detection on Raspberry Pi 5 with Arm Runtime, inspect its
    Python example, and compare CPU inference with NCNN. You'll start with the
    supplied video. Then, you'll
    inspect how runtime setup loads converted weights and prepares XNNPACK
    operations for reuse across frames. Finally, you'll export the checkpoint to
    NCNN and compare latency with the same dataset, input size, batch, and
    system conditions.
  # faqs:
  #   - question: Does Arm Runtime use the Raspberry Pi 5 CPU or GPU?
  #     answer: >-
  #       You run inference on the Raspberry Pi 5 CPU. The runtime uses Cortex-A76
  #       cores, a fixed schedule, planned memory reuse, and fused operations.
  #   - question: How do I run detection on my own video or a PiCamera feed?
  #     answer: >-
  #       For a video with at least 200 frames, run `make example-video
  #       VIDEO=/path/to/your-video.mp4`. For a live PiCamera feed, install the
  #       camera packages and run `make example-camera`.
  #   - question: What happens when I create the detector?
  #     answer: >-
  #       When you create the detector, the Python session checks the model
  #       manifest and binary, then loads the shared library. The runtime loads
  #       the converted model and prepares XNNPACK operations; the example
  #       reuses the detector across frames.
  #   - question: Which settings should I match for a fair NCNN comparison?
  #     answer: >-
  #       Use Ultralytics 8.4.108 and the same YOLO26n checkpoint,
  #       `coco-128-by-sa` dataset, 640 × 640 input, and batch size one. Stop
  #       other CPU workloads and use the same power, cooling, and CPU settings.
  #   - question: What should I check if the runtimes report different latency or accuracy?
  #     answer: >-
  #       Confirm both runs use the same checkpoint, dataset, input size, and
  #       batch size. Stop other CPU workloads and use matching power, cooling,
  #       and CPU settings; internal precision and operation fusion can still
  #       differ between runtimes.
# END generated_summary_faq

author:
  - Austin Hill
  - Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Introductory

subjects: ML

armips:
  - Cortex-A
operatingsystems:
  - Linux
tools_software_languages:
  - Python
  - Raspberry Pi
  - YOLO26
  - AI Portal
  - Arm Runtime for YOLO26 on Raspberry Pi 5
  - XNNPACK

further_reading:
  - resource:
      title: Arm Runtime for YOLO26 on Raspberry Pi 5
      link: https://github.com/arm/Optimized-Runtimes
      type: repository
  - resource:
      title: Arm YOLO26n Python API
      link: https://github.com/arm/Optimized-Runtimes/blob/main/yolo26-raspberry-pi-5/src/runtime/api/python/arm_yolo26n/README.md
      type: documentation
  - resource:
      title: Runtime implementation
      link: https://github.com/arm/Optimized-Runtimes/blob/main/yolo26-raspberry-pi-5/src/runtime/README.md
      type: documentation
  - resource:
      title: Ultralytics on Raspberry Pi
      link: https://docs.ultralytics.com/guides/raspberry-pi/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
