---
title: Train Multi-Agent Reinforcement Learning policies with MAPPO on Arm cloud

description: Train a MAPPO navigation policy with BenchMARL and VMAS on an Arm cloud instance, deploy the checkpoint to a visualization GUI, and export an actor-only inference artifact.

minutes_to_complete: 330

who_is_this_for: This Learning Path is for cloud and machine learning developers who want to train and package multi-agent reinforcement learning navigation policies on Arm-based servers.
learning_objectives:
    - Configure a vectorized BenchMARL and VMAS workload for an Arm cloud instance.
    - Train and evaluate a multi-agent navigation policy with MAPPO.
    - Package and validate the trained BenchMARL checkpoint for a cloud visualization GUI.
    - Extract and validate the shared actor as a smaller inference-only artifact.

prerequisites:
    - An Arm64 Ubuntu cloud instance with SSH access, `sudo` privileges, and internet access.
    - Familiarity with Linux, Python, PyTorch, and reinforcement learning concepts such as observations, actions, rewards, and policies.
    - A local checkout of the companion MARL GUI containing `tools/deploy_checkpoint.py` and `tools/inspect_checkpoint.py` if you want to complete the GUI deployment section.

author:
    - Sagar Surendran
    - Na Li
    - Masoud Koleini

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - Reinforcement Learning
    - Multi-Agent Reinforcement Learning
    - MAPPO
    - Python
    - PyTorch
    - TorchRL
    - BenchMARL
    - VMAS

operatingsystems:
    - Linux
further_reading:
    - resource:
        title: BenchMARL repository
        link: https://github.com/facebookresearch/BenchMARL
        type: website
    - resource:
        title: VMAS documentation
        link: https://vmas.readthedocs.io/en/latest/
        type: documentation
    - resource:
        title: The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games
        link: https://arxiv.org/abs/2103.01955
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
