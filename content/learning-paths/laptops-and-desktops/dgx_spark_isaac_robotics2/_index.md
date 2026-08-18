---
title: Advance Robotics Reinforcement Learning with Isaac Lab on DGX Spark

draft: true
cascade:
    draft: true
    
minutes_to_complete: 120

who_is_this_for: This advanced topic is for robotics developers and AI researchers who want to extend an existing Isaac Sim and Isaac Lab setup on DGX Spark to manipulation, multi-agent training, and motion imitation.

learning_objectives:
    - Train Franka manipulation policies with RSL-RL and RL Games
    - Compare MAPPO and IPPO in a two-agent Shadow Hand task
    - Train humanoid motion policies with Adversarial Motion Priors
    - Select an RL library that has a registered configuration for a task

prerequisites:
    - Access to an NVIDIA DGX Spark system with at least 50 GB of free disk space
    - Completion of the previous Isaac Sim and Isaac Lab Learning Path on DGX Spark
    - Experience with Python scripting
    - Basic understanding of reinforcement learning concepts such as rewards and policies

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
        title: Isaac Lab 2.3.2 Documentation
        link: https://isaac-sim.github.io/IsaacLab/v2.3.2/index.html
        type: documentation
    - resource:
        title: Isaac Lab 3.0 Beta 2 Documentation
        link: https://isaac-sim.github.io/IsaacLab/release/3.0.0-beta2/index.html
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
