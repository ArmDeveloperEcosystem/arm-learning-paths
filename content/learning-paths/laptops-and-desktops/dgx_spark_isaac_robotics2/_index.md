---
title: Advance Robotics Reinforcement Learning Workflows to Manipulation and Multi-Agent Tasks with IsaacLab

draft: true
cascade:
    draft: true
    
minutes_to_complete: 120

who_is_this_for: This advanced topic is intended for robotics software architects, simulation engineers, and AI researchers who want to orchestrate high-fidelity robotic simulations and reinforcement learning (RL) pipelines. It specifically targets those leveraging Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark systems powered by the Grace–Blackwell (GB10) architecture.

learning_objectives:
    - Describe the roles of Isaac Sim and Isaac Lab.
    - Train a reinforcement learning policy for simulations of the Franka robotic arm and Unitree H1 humanoid robot using the RSL-RL and skrl interface.
    - Train reinforcement learning policies in multi-agent environments for cooperative robotic systems.
    - Use Adversarial Motion Priors (AMP) to enable natural humanoid locomotion.

prerequisites:
    - Access to an NVIDIA DGX Spark system with at least 50 GB of free disk space
    - Completion of the previous Isaac Sim / Isaac Lab setup on Arm-based systems
    - Experience with Python scripting
    - Basic understanding of reinforcement learning concepts (rewards, policies, etc.)

author:
    - Johnny Nunez
    - Kieran Hejmadi
    - Odin Shen


### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
tools_software_languages:
    - Python
    - Bash
    - IsaacSim
    - IsaacLab
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
        title: Isaac Sim and Isaac Lab learning path
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/
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
