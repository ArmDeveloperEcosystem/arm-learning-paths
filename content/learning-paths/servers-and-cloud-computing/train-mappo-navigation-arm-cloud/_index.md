---
title: Train and export a MAPPO navigation policy on Arm cloud

draft: true
cascade:
    draft: true
    
description: Train a MAPPO navigation policy with BenchMARL and VMAS on an Arm cloud instance, evaluate it, and export an actor-only inference artifact.

minutes_to_complete: 330

who_is_this_for: This Learning Path is for cloud and machine learning developers who want to train and package multi-agent reinforcement learning navigation policies on Arm-based servers.
learning_objectives:
    - Configure a reproducible BenchMARL and VMAS workload for an Arm cloud instance.
    - Train and quantitatively evaluate a multi-agent navigation policy with MAPPO.
    - Export and validate the shared actor as a smaller inference-only artifact.

prerequisites:
    - An Arm-based Ubuntu 24.04 cloud instance with SSH access, `sudo` privileges, and internet access.
    - Familiarity with Linux, Python, PyTorch, and reinforcement learning concepts such as observations, actions, rewards, and policies.

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
        title: Load a MAPPO policy with the Arm Device Connect dashboard
        link: /learning-paths/servers-and-cloud-computing/use-mappo-device-connect-dashboard/
        type: website
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
    - resource:
        title: TorchRL documentation
        link: https://docs.pytorch.org/rl/stable/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
