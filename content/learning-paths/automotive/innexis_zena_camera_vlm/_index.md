---
title: Build a camera-to-VLM pipeline on Arm Zena CSS
    
description: Capture a virtual camera frame in a Zena CSS Linux guest and submit it to a local vision-language model for a recorded functional check.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for AI and vision developers who can access an Arm Zena CSS virtual platform in Siemens Innexis Architecture Native Acceleration (ANA).

learning_objectives:
    - Configure a reproducible video input for the Zena CSS virtual camera.
    - Capture and inspect one frame from the Linux guest's V4L2 device.
    - Prepare a vision-capable model and its matching image projector.
    - Run one local image prompt and save the input and response together.

prerequisites:
    - Access to a Zena CSS virtual platform in Siemens Innexis ANA and console, or authorized SSH access to its EWAOL Linux guest after startup
    - Completion of [Run local LLM inference with llama.cpp on Arm Zena CSS](/learning-paths/automotive/innexis_zena_llamacpp/) in the same Linux guest OS, so its llama-cli binary is available
    - Permission to configure a virtual camera file input
    - The `ffmpeg` and `ffprobe` tools on your local computer to prepare video from public source media
    - Enough guest storage and memory for a vision model
    - A working guest file-transfer route and basic Linux command-line knowledge

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-11T19:30:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 072a3534cb7406648d21fab7f72584d36f4f8f450784bec1f35eca33ab6903cb
  summary_generated_at: '2026-11-11T19:30:59Z'
  summary_source_hash: 072a3534cb7406648d21fab7f72584d36f4f8f450784bec1f35eca33ab6903cb
  faq_generated_at: '2026-11-11T19:30:59Z'
  faq_source_hash: 072a3534cb7406648d21fab7f72584d36f4f8f450784bec1f35eca33ab6903cb
  summary: >-
    You'll build a camera-to-VLM workflow on Arm Zena CSS and check a local response to one
    captured frame. First, you'll prepare a repeatable video input in Siemens Innexis ANA. Then, you'll capture and
    inspect a JPEG from `/dev/video0`, and download a matching model and projector for
    `llama-cli`. Finally, you'll save the image-inference log and exit status. Optionally, you can capture
    frames from moving traffic and compare two model responses.
  # faqs:
  # - question: Do I need to run this in the same guest where I built llama.cpp?
  #   answer: >-
  #     Yes. You use the same Zena CSS Linux guest as the prerequisite Learning Path so your
  #     `llama-cli` binary is available.
  # - question: How do I check that the virtual camera is configured and reachable from the guest?
  #   answer: >-
  #     Check that `virtualcam-bridge@1.service` is active, the file-input command returns `OK`,
  #     and the `INPUT` readback shows your selected file. Then capture a JPEG from `/dev/video0`
  #     and inspect it to confirm that the intended image arrived.
  # - question: Which GStreamer elements should be present before I try to capture a frame?
  #   answer: >-
  #     You need `v4l2src`, `videoconvert`, `jpegenc`, `filesink`, and `waylandsink`. Check each
  #     element with `gst-inspect-1.0` before you capture a frame.
  # - question: How do I verify the model and `mmproj` files are set correctly for `llama.cpp` image
  #     inference?
  #   answer: >-
  #     You download the pinned model and matching multimodal projector (`mmproj`) from the
  #     specified revision. Check that both files pass their SHA-256 checks before inference.
  # - question: What outputs should I expect after running the final command block?
  #   answer: >-
  #     You should find `vision-run.exit` and `vision-run.log` in
  #     `/root/zena-camera-vlm/results/`. Check for exit status `0`, confirm that the log names
  #     the captured JPEG after `Loaded media from`, and compare the response with your saved image.
# END generated_summary_faq

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
