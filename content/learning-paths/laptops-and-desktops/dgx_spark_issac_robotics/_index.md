---
title: Building IsaacSim and IsaacLab Robotic Workflows on DGX Spark

minutes_to_complete: 90

who_is_this_for: This advanced topic is for robotics developers, simulation engineers, and AI researchers who want to run high-fidelity robotic workloads using IsaacSim and IsaacLab on Arm-based DGX Spark platforms (Grace CPU + Blackwell GPU). It is especially useful for those evaluating ROS 2 performance on Arm Neoverse cores, developing reinforcement learning pipelines, or simulating control logic on heterogeneous CPU-GPU systems.

learning_objectives:
    - Understand the role of IsaacSim and IsaacLab in robotic workflow development
    - Set up an optimized Arm64 development environment for Isaac tools on DGX Spark
    - Simulate a robotic arm and control its motion using ROS 2 nodes on Grace CPU
    - Launch a reinforcement learning task with IsaacLab using headless execution

   
prerequisites:
    - Access to a DGX Spark platform (or equivalent Arm-based system with a discrete GPU)
    - Familiarity with ROS 2 concepts (nodes, topics, navigation stack)
    - Experience with Python scripting and Linux terminal usage
    - Basic understanding of reinforcement learning workflows

author:
    - Odin Shen
    - Asier Arranz
    - Johnny Nunez
    - Raymond Lo

### Tags
skilllevels: Advanced
subjects: physical AI
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - Python
    - ROS 2
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Isaac Sim
        link: https://developer.nvidia.com/isaac/sim
        type: website
    - resource:
        title: Isaac Lab
        link: https://developer.nvidia.com/isaac/lab
        type: website
    - resource:
        title: DGX Spark Playbook
        link: https://github.com/NVIDIA/dgx-spark-playbooks
        type: github    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---