---
title: Build Robot Simulation and Reinforcement Learning Workflows with Isaac Sim and Isaac Lab on DGX Spark

description: Learn how to build and deploy high-fidelity robotic simulations and reinforcement learning pipelines using Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark with Grace-Blackwell architecture.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for robotics developers, simulation engineers, and AI researchers who want to run high-fidelity robotic simulations and reinforcement learning (RL) pipelines using NVIDIA Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark system powered by the Grace–Blackwell (GB10) architecture.

learning_objectives:
    - Describe the roles of Isaac Sim and Isaac Lab within a robotics simulation and RL pipeline
    - Build and configure Isaac Sim and Isaac Lab on an Arm-based DGX Spark system
    - Launch and control a robot simulation in Isaac Sim using Python
    - rain and evaluate a reinforcement learning policy for the Unitree H1 humanoid robot using Isaac Lab and RSL-RL

prerequisites:
    - A NVIDIA DGX Spark system with at least 50 GB of free disk space
    - Familiarity with Linux command-line tools
    - Experience with Python scripting and virtual environments
    - Basic understanding of reinforcement learning concepts (rewards, policies, episodes)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:55Z'
  generator: template
  source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  summary: >-
    Learn how to build and deploy high-fidelity robotic simulations and reinforcement learning
    pipelines using Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark with Grace-Blackwell
    architecture. It is designed for robotics developers, simulation engineers, and AI researchers
    who want to run high-fidelity robotic simulations and reinforcement learning (RL) pipelines
    using NVIDIA Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark system powered by the Grace–Blackwell
    (GB10) architecture. By the end, you will be able to describe the roles of Isaac Sim and Isaac
    Lab within a robotics simulation and RL pipeline, build and configure Isaac Sim and Isaac
    Lab on an Arm-based DGX Spark system, and launch and control a robot simulation in Isaac Sim
    using Python. It focuses on tools and technologies such as Python, Bash, IsaacSim, and IsaacLab,
    Linux environments, and Arm platforms including Cortex-X and Cortex-A. The main steps cover
    Explore Isaac Sim and Isaac Lab for robotic workflows on DGX Spark, Set up Isaac Sim and Isaac
    Lab on DGX Spark, Run and Understand a Sample Robot Simulation with Isaac Sim, and Train a
    Humanoid Locomotion Policy with Isaac Lab on DGX Spark.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe the roles of Isaac Sim and Isaac Lab within a robotics simulation and
      RL pipeline, build and configure Isaac Sim and Isaac Lab on an Arm-based DGX Spark system,
      and launch and control a robot simulation in Isaac Sim using Python. Learn how to build
      and deploy high-fidelity robotic simulations and reinforcement learning pipelines using
      Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark with Grace-Blackwell architecture.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for robotics developers, simulation engineers, and AI researchers
      who want to run high-fidelity robotic simulations and reinforcement learning (RL) pipelines
      using NVIDIA Isaac Sim and Isaac Lab on Arm-based NVIDIA DGX Spark system powered by the
      Grace–Blackwell (GB10) architecture.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A NVIDIA DGX Spark system with at least
      50 GB of free disk space; Familiarity with Linux command-line tools; Experience with Python
      scripting and virtual environments; Basic understanding of reinforcement learning concepts
      (rewards, policies, episodes).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, Bash, IsaacSim, and IsaacLab, Linux environments,
      and Arm platforms such as Cortex-X and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore Isaac Sim and Isaac Lab for robotic workflows
      on DGX Spark, Set up Isaac Sim and Isaac Lab on DGX Spark, Run and Understand a Sample Robot
      Simulation with Isaac Sim, and Train a Humanoid Locomotion Policy with Isaac Lab on DGX
      Spark.
# END generated_summary_faq

author:
    - Johnny Nunez
    - Odin Shen
    - Asier Arranz
    - Raymond Lo

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

