---
title: Control a game using motion; vision inference on Arm using Cairn SDK
description: Deploy a Cairn perception workflow on Raspberry Pi 5, consume live object detections with Python, and use detection events to control a browser game.

minutes_to_complete: 45

who_is_this_for: Python developers who want to build vision edge AI applications on Arm Linux devices using reusable runtime services.

learning_objectives:
  - Deploy a camera-to-inference workflow and verify live detections
  - Explain the roles of Cairn's Media Service, Perception Service, and Messaging Service
  - Explain how the example uses the Python SDK to deploy a workflow and receive detection results
  - Run a detection-driven browser application

prerequisites:
  - A Raspberry Pi 5 running Raspberry Pi OS 64-bit Trixie, reachable over SSH
  - A USB webcam or Raspberry Pi Camera Module 3 connected to the Pi
  - A Linux, macOS, or Windows development machine with Git, Topo 14.4.1, and Docker available; use WSL 2 on Windows for the Bash commands
  - Docker installed on the Pi and a Compose version that supports image-backed volumes
  - Internet access for container images and Hugging Face model downloads
  - Basic Python, Linux command-line, and container knowledge
  
author:
- Matt Cossins
- Luke Parkin

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Introductory
subjects: AI/ML
armips:
  - Cortex-A
tools_software_languages:
  - Cairn
  - OPK
  - Raspberry Pi
  - Python
  - Topo
  - Docker
operatingsystems:
  - Linux
further_reading:
  - resource:
      title: Composable AI Runtimes overview and compatibility
      link: https://github.com/arm/composable-ai-runtimes
      type: documentation
  - resource:
      title: Open Perception Kit overview and browser viewer
      link: https://github.com/arm/open-perception-kit
      type: documentation
  - resource:
      title: Cairn Rust and Python client libraries
      link: https://github.com/arm/composable-ai-runtimes/blob/main/lib/README.md
      type: documentation
  - resource:
      title: Object-detection example
      link: https://github.com/Arm-Examples/composable-ai-perception-object-detection
      type: documentation
  - resource:
      title: Acorn Attack example
      link: https://github.com/Arm-Examples/composable-ai-perception-acorn-attack
      type: documentation
  - resource:
      title: Deploy containerized workloads with Topo
      link: /learning-paths/cross-platform/deploy-containerized-workloads-with-topo/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
