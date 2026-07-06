---
title: Build an edge AI Reachy Mini app with Raspberry Pi, MediaPipe, and MuJoCo

description: Run MediaPipe gesture inference on a Raspberry Pi 5, connect to a Reachy Mini MuJoCo simulation on a development machine, and use a browser dashboard to decide Reachy's fate with a thumbs-up or thumbs-down.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers interested in edge AI, robotics simulation, and physical AI applications. You can complete the main path without owning a physical Reachy Mini.

learning_objectives:
    - Understand why simulation environments can aid Edge AI and robotics development.
    - Run a simulated Reachy Mini robot on a laptop or desktop.
    - Use MediaPipe and TensorFlow Lite gesture recognition on Raspberry Pi 5.
    - Connect an edge inference node to a robot daemon over the network.
    - Display results over a web dashboard.
    - Optionally extend the project toward a physical Reachy Mini, audio or multimodal interaction, or your own app.

prerequisites:
    - A Raspberry Pi 5, ideally with 16 GB RAM.
    - A USB webcam connected to the Raspberry Pi.
    - A macOS or Linux machine, or a Windows machine with WSL2, capable of running the Reachy Mini MuJoCo simulation.
    - Basic Python and Bash terminal experience.
    - (Optional) [Reachy Mini](https://huggingface.co/reachy-mini)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:04:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d021122b9217e2326e98d45aeffccb742357e77a7774f9c469d2c73285ca91a9
  summary_generated_at: '2026-07-02T19:04:59Z'
  summary_source_hash: d021122b9217e2326e98d45aeffccb742357e77a7774f9c469d2c73285ca91a9
  faq_generated_at: '2026-07-02T19:04:59Z'
  faq_source_hash: d021122b9217e2326e98d45aeffccb742357e77a7774f9c469d2c73285ca91a9
  summary: >-
    You'll build a distributed edge AI application that runs MediaPipe
    gesture inference on a Raspberry Pi 5 and drives a Reachy Mini robot in a MuJoCo simulation.
    First, you'll start the simulator on a development machine, prepare the Pi with Raspberry Pi OS and
    Git LFS so the gesture model downloads correctly, then run the app and open a browser dashboard
    to monitor the camera feed and verdicts. A thumbs-up or thumbs-down from the webcam triggers
    victory or defeat motions in the simulated robot. You'll also learn about the project layout
    so you can locate perception, app logic, motion, and dashboard components in the codebase to iterate on.
  faqs:
  - question: Which address should I open to view the dashboard?
    answer: >-
      If you use VS Code Remote SSH port forwarding, open `http://localhost:8042` on your laptop.
      Otherwise, browse to `http://<pi-ip-address>:8042` from any machine on the same network.
  - question: How do I find the Raspberry Pi IP address for the dashboard?
    answer: >-
      Run `hostname -I` on the Raspberry Pi to print its IP address. Then use that address with
      port `8042` in your browser.
  - question: How do I confirm the gesture model downloaded correctly with Git LFS?
    answer: >-
      Check that `assets/gesture_recognizer.task` exists as a real model file, not a tiny pointer
      file. If you cloned before enabling Git LFS, enable LFS and re-clone the repository.
  - question: The dashboard loads but the MuJoCo simulation doesn't move—what should I check?
    answer: >-
      Verify the MuJoCo simulation is running on your development machine and that the Pi can
      reach it over the network. Also review `main.py` because it contains the settings used for
      the distributed simulation route.
  - question: What result should I expect when a thumbs-up or thumbs-down is detected?
    answer: >-
      You should see the simulated Reachy Mini play a victory or defeat motion, and the web dashboard
      should reflect the verdict. This indicates the camera, inference, network, and simulator
      are connected end to end.
# END generated_summary_faq

author: Matt Cossins

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Raspberry Pi
    - Reachy Mini
    - Python
    - MediaPipe
    - FastAPI
    - MuJoCo
operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers
    - laptops-and-desktops

further_reading:
    - resource:
        title: Make and publish your Reachy Mini app
        link: https://huggingface.co/blog/pollen-robotics/make-and-publish-your-reachy-mini-apps
        type: blog
    - resource:
        title: Reachy Mini Python SDK documentation
        link: https://pollen-robotics.github.io/reachy-mini-sdk/
        type: documentation
    - resource:
        title: Reachy Mini project examples
        link: https://github.com/pollen-robotics/reachy-mini-sdk/tree/main/examples
        type: website
    - resource:
        title: MediaPipe Gesture Recognizer guide
        link: https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
