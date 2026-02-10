---
title: Build robotic simulation and reinforcement learning workflows with Isaac Sim and Isaac Lab on DGX Spark

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for robotics developers, simulation engineers, and AI researchers who want to run high-fidelity robotic simulations and reinforcement learning (RL) pipelines using Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark platforms powered by the Grace-Blackwell (GB10) architecture.

learning_objectives:
    - Describe the roles of Isaac Sim and Isaac Lab and explain how DGX Spark accelerates robotic simulation and learning tasks
    - Build Isaac Sim and Isaac Lab from source on an Arm-based DGX Spark system
    - Deploy a basic robot simulation in Isaac Sim and interact with it using Python
    - Train a reinforcement learning policy for a Unitree H1 humanoid robot using Isaac Lab and the RSL-RL interface
    - Scale reinforcement learning across multiple tasks and multi-agent environments using Isaac Lab

prerequisites:
    - Access to an NVIDIA DGX Spark system with at least 50 GB of available disk space
    - Familiarity with command-line interfaces and basic Linux operations
    - Experience with Python scripting and virtual environments
    - Basic understanding of reinforcement learning concepts (rewards, policies, episodes)
    - Experience building software from source using CMake and make

author:
    - Odin Shen
    - Asier Arranz
    - Johnny Nunez
    - Raymond Lo

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - Python
    - Bash
    - Isaac Sim
    - Isaac Lab
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Isaac Sim Documentation
        link: https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
        type: documentation
    - resource:
        title: Isaac Lab Documentation
        link: https://isaac-sim.github.io/IsaacLab/main/index.html
        type: documentation
    - resource:
        title: NVIDIA DGX Spark Playbooks
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: documentation
    - resource:
        title: Isaac Lab Available Environments
        link: https://isaac-sim.github.io/IsaacLab/main/source/overview/environments.html
        type: website
    - resource:
        title: DGX Spark Isaac Sim and Isaac Lab Playbook
        link: https://build.nvidia.com/spark/isaac/overview
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
