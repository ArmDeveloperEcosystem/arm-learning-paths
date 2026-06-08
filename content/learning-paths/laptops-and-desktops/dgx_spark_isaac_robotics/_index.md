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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:00:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  summary_generated_at: '2026-06-01T22:02:33Z'
  summary_source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  faq_generated_at: '2026-06-02T23:00:20Z'
  faq_source_hash: eda533c727ea7094202e8784bf1ed2240cfea2573cefc73aca1a86797840778c
  summary: >-
    This advanced Learning Path shows how to build, configure, and run NVIDIA Isaac Sim and Isaac
    Lab on an Arm-based NVIDIA DGX Spark system powered by the Grace–Blackwell (GB10) architecture.
    You will verify the DGX Spark configuration, install required build dependencies, build Isaac
    Sim, and set up Isaac Lab on top. You will launch and control a sample Cartpole simulation
    using Python to understand Isaac Sim’s simulation loop. You will then train and evaluate a
    reinforcement learning policy for the Unitree H1 humanoid robot using Isaac Lab with RSL-RL
    (PPO). Prerequisites include a DGX Spark with about 50 GB free disk space, Linux command-line
    skills, experience with Python virtual environments, and a basic understanding of RL concepts.
    Estimated time to complete is 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an NVIDIA DGX Spark system with at least 50 GB of free disk space. Familiarity
      with Linux command-line tools, Python scripting and virtual environments, and basic RL concepts
      is expected.
  - question: How long does installation usually take, and how much storage is required?
    answer: >-
      The setup typically takes 15–20 minutes on a DGX Spark system. Plan for approximately 50
      GB of available disk space.
  - question: How are Isaac Sim and Isaac Lab arranged in the environment?
    answer: >-
      You first build and configure Isaac Sim, then set up Isaac Lab on top of the Isaac Sim environment.
      The path begins by verifying the DGX Spark configuration and installing required build dependencies.
  - question: Which simulation do I run first, and how do I confirm it worked?
    answer: >-
      You start with the Cartpole environment by launching a pre-built scene in Isaac Sim. Successful
      setup is indicated by the scene loading and your ability to interact with it programmatically
      using Python while exploring the simulation loop.
  - question: Which RL framework and algorithm are used for training the humanoid policy?
    answer: >-
      Training uses Isaac Lab’s integration with the RSL-RL library implementing PPO. You configure
      the task and environment for the Unitree H1 humanoid to walk over rough terrain, then train
      and evaluate the policy.
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

