---
title: Build an Edge AI Reachy Mini App with Raspberry Pi, MediaPipe, and MuJoCo

draft: true
cascade:
    draft: true
    
description: Run MediaPipe gesture inference on a Raspberry Pi 5, connect to a Reachy Mini MuJoCo simulation on a development machine, and use a browser dashboard to decide Reachy's fate with a thumbs-up or thumbs-down.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers interested in edge AI, robotics simulation, and physical AI applications. You can complete the main path without owning a physical Reachy Mini.

learning_objectives:
    - Understand why simulation environments can aid Edge AI and robotics development.
    - Run a simulated Reachy Mini robot on a laptop or desktop.
    - Use MediaPipe and TensorFlow Lite gesture recognition on Raspberry Pi 5.
    - Connect an edge inference node to a robot daemon over the network.
    - Display results over a web dashboard.
    - (Optional) Extend the project toward a physical Reachy Mini, audio or multimodal interaction, or your own app.

prerequisites:
    - A Raspberry Pi 5, ideally with 16 GB RAM.
    - A USB webcam connected to the Raspberry Pi.
    - A macOS or Linux machine, or a Windows machine with WSL2, capable of running the Reachy Mini MuJoCo simulation.
    - Basic Python and Bash terminal experience.
    - (Optional) [Reachy Mini](https://huggingface.co/reachy-mini)

author: Matt Cossins

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
