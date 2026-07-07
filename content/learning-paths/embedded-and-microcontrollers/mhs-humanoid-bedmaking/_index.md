---
title: Make a bed with two humanoid robots in NVIDIA Isaac Sim, coordinated over the Model Hardware Standard

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for robotics and edge-AI developers who want to run a physically valid, multi-robot humanoid loco-manipulation demo in NVIDIA Isaac Sim on an Arm-based NVIDIA DGX Spark, and coordinate the robots as equal peers over the Model Hardware Standard (MHS) — the open device layer that absorbed Arm Device Connect.

learning_objectives:
    - Set up NVIDIA Isaac Sim and Isaac Lab with the MHS Python SDK on an NVIDIA DGX Spark (Arm GB10)
    - Run a two-humanoid bed-making demo headless and render an MP4
    - Explain how two robots coordinate as equal peers over MHS using procedures, events, and discovery
    - Play and inspect a whole-body reinforcement-learning reach policy trained in Isaac Lab

prerequisites:
    - An NVIDIA DGX Spark (Arm GB10), or a comparable Arm plus NVIDIA GPU Linux host, able to build NVIDIA Isaac Sim 5.1 and Isaac Lab 2.3.2
    - Familiarity with the Linux command line and Python
    - No physical robot is required — everything in this Learning Path runs in simulation

author: Waheed Brown

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - NVIDIA Isaac Sim
    - NVIDIA Isaac Lab
    - Python
    - PyTorch
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Model Hardware Standard Python SDK
        link: https://github.com/modelhardwarestandard/python-sdk
        type: website
    - resource:
        title: robotics-connect — humanoid MHS connector and skills
        link: https://github.com/armwaheed/robotics-connect
        type: website
    - resource:
        title: NVIDIA Isaac Lab documentation
        link: https://isaac-sim.github.io/IsaacLab/
        type: documentation
    - resource:
        title: Unitree unitree_rl_lab (G1 velocity-walk policy)
        link: https://github.com/unitreerobotics/unitree_rl_lab
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
