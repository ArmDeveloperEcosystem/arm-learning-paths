---
title: Train Multi-Agent Reinforcement Learning policies with MAPPO on Arm cloud

draft: true
cascade:
    draft: true
    
description: Train a MAPPO navigation policy with BenchMARL and VMAS on an Arm cloud instance, deploy the checkpoint to a visualization GUI, and export an actor-only inference artifact.

minutes_to_complete: 330

who_is_this_for: This Learning Path is for cloud and machine learning developers who want to train and package multi-agent reinforcement learning navigation policies on Arm-based servers.
learning_objectives:
    - Configure a vectorized BenchMARL and VMAS workload for an Arm cloud instance.
    - Train and evaluate a multi-agent navigation policy with MAPPO.
    - Package and validate the trained BenchMARL checkpoint when the companion cloud visualization GUI is available.
    - Extract and validate the shared actor as a smaller inference-only artifact.

prerequisites:
    - An `aarch64` cloud instance running Ubuntu 24.04 with SSH access, `sudo` privileges, and internet access. The reference experiment was tested on an AWS Graviton5 `m9g.48xlarge` instance with 192 vCPUs, 768 GiB of memory, and 512 GB of EBS storage. You can use another Arm-based cloud instance, but training time and the effective environment count will differ.
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
    - resource:
        title: Amazon EC2 M9g instances
        link: https://aws.amazon.com/ec2/instance-types/m9g/
        type: documentation
    - resource:
        title: PyTorch installation guidance
        link: https://pytorch.org/get-started/locally/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
