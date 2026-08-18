---
title: Advance robotics reinforcement learning with Isaac Lab on DGX Spark

description: Extend an Isaac Lab setup on an Arm-based DGX Spark by training manipulation, multi-agent, and natural-motion reinforcement learning policies.
    
minutes_to_complete: 120

who_is_this_for: This advanced topic is for robotics developers and AI researchers who want to extend an existing Isaac Sim and Isaac Lab setup on DGX Spark to manipulation, multi-agent training, and motion imitation.

learning_objectives:
    - Train Franka manipulation policies with RSL-RL and RL Games
    - Compare Multi-Agent Proximal Policy Optimization (MAPPO) and Independent PPO (IPPO) in a two-agent Shadow Hand task
    - Train humanoid motion policies with Adversarial Motion Priors (AMP)
    - Select a reinforcement learning (RL) library that has a registered configuration for a task

prerequisites:
    - Access to an NVIDIA DGX Spark system with at least 50 GB of free disk space
    - Completion of the previous [Isaac Sim and Isaac Lab Learning Path](/learning-paths/laptops-and-desktops/dgx_spark_isaac_robotics/) on DGX Spark
    - Experience with Python scripting
    - Basic understanding of reinforcement learning concepts such as rewards and policies

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-18T19:30:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d5ac46a2a572810f399e4d453a17ac025149c9eb8c5faa4b1c89f38aa86dea39
  summary_generated_at: '2026-08-18T19:30:49Z'
  summary_source_hash: d5ac46a2a572810f399e4d453a17ac025149c9eb8c5faa4b1c89f38aa86dea39
  faq_generated_at: '2026-08-18T19:30:49Z'
  faq_source_hash: d5ac46a2a572810f399e4d453a17ac025149c9eb8c5faa4b1c89f38aa86dea39
  summary: >-
    You'll extend your Isaac Sim and Isaac Lab setup on DGX Spark to train increasingly complex reinforcement
    learning policies. First, you'll train a Franka arm for manipulation and contact-rich tasks. Then,
    you'll coordinate two Shadow Hands with MAPPO and IPPO, train humanoid motion with AMP, and select an RL library based on its registered task configuration and algorithm support.
  faqs:
  - question: How do I choose and stick to compatible Isaac Lab, Isaac Sim, and Python versions?
    answer: >-
      Use one compatible API set throughout training. Choose either Isaac Lab `v2.3.2` with Isaac
      Sim `5.1.0` and Python `3.11`, or Isaac Lab `v3.0.0-beta2.patch1` with Isaac Sim `6.0.0`
      or `6.0.1` and Python `3.12`.
  - question: How do I know the task and RL library I picked are supported?
    answer: >-
      Check the Isaac Lab environment list for supported task–library combinations. Start with
      a library that provides an upstream agent configuration for your task.
  - question: How do I verify that the trained policy opens the drawer?
    answer: >-
      Confirm that the arm aligns with the handle, moves the drawer along its rail after contact,
      and keeps the opening motion stable without slipping or shaking.
  - question: What changes when I switch between MAPPO and IPPO for the two Shadow Hands?
    answer: >-
      With MAPPO, the critic uses shared state during training while each hand acts from its own
      observations. With IPPO, each agent learns independently in the same environment.
  - question: What result should I expect from AMP training?
    answer: >-
      AMP uses reference motion‑capture data to guide learning toward smoother, more humanlike
      motion. Successful training produces trajectories that track the reference motions more
      closely than a standard RL policy.
# END generated_summary_faq

author:
    - Johnny Nunez
    - Kieran Hejmadi
    - Odin Shen

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
