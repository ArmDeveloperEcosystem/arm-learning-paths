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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:13:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  summary_generated_at: '2026-07-28T16:13:33Z'
  summary_source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  faq_generated_at: '2026-07-28T16:13:33Z'
  faq_source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  summary: >-
    This Learning Path guides learners through building, configuring, and running robotics simulation
    and reinforcement learning workflows using NVIDIA Isaac Sim and Isaac Lab on an Arm-based
    DGX Spark system powered by the Grace–Blackwell architecture. Learners verify the platform
    setup, install required dependencies, and build Isaac Sim before layering Isaac Lab on top
    of that environment. A hands-on Cartpole example demonstrates how to launch a pre-built scene,
    control it with Python, and understand the simulation loop. The path then moves to training
    a Unitree H1 humanoid locomotion policy with Isaac Lab’s integration of RSL-RL (PPO), highlighting
    task selection, training parameters, and evaluation so learners can recognize when a policy
    is learning effectively on DGX Spark.
  faqs:
  - question: What should I check on my DGX Spark before starting the setup?
    answer: >-
      Verify the system configuration and confirm you have about 50 GB of free disk space. Plan
      for roughly 15–20 minutes of setup time on DGX Spark.
  - question: Which component should I install and configure first?
    answer: >-
      Build and configure Isaac Sim first, then set up Isaac Lab on top of the Isaac Sim environment.
      Isaac Lab relies on the Isaac Sim installation.
  - question: How do I confirm the installation worked before moving on to training?
    answer: >-
      Launch a pre-built sample scene from Isaac Sim and interact with it programmatically. If
      the scene runs without errors and responds to actions, the environment is ready.
  - question: What result should I expect when running the Cartpole example?
    answer: >-
      You should see a running simulation where the cart and pole respond to actions driven by
      your Python control loop. This validates the simulation loop and your ability to step and
      control the environment.
  - question: How do I know the humanoid policy is training correctly with Isaac Lab and RSL-RL?
    answer: >-
      Select the Unitree H1 task, start PPO training via Isaac Lab’s RSL-RL integration, and monitor
      training logs and evaluation outputs. Successful runs show improving evaluation results
      and stable locomotion over rough terrain in simulation.
# END generated_summary_faq

author:
    - Johnny Nunez
    - Odin Shen
    - Asier Arranz
    - Raymond Lo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

