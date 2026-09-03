---
title: Train multi-agent reinforcement learning policies with MAPPO on an Arm-based cloud instance

description: Train a MAPPO navigation policy with BenchMARL and VMAS on an Arm-based cloud instance, deploy the checkpoint to a visualization GUI, and export an actor-only inference artifact.

minutes_to_complete: 330

who_is_this_for: This Learning Path is for cloud and machine learning developers who want to train and package multi-agent reinforcement learning navigation policies on Arm-based servers.

learning_objectives:
    - Configure a vectorized BenchMARL and VMAS workload for an Arm cloud instance
    - Train and evaluate a multi-agent navigation policy with MAPPO
    - Package and validate the trained BenchMARL checkpoint when the companion cloud visualization GUI is available
    - Extract and validate the shared actor as a smaller inference-only artifact

prerequisites:
    - An `aarch64` cloud instance running Ubuntu 24.04 with SSH access, `sudo` privileges, and internet access
    - Familiarity with Linux, Python, PyTorch, and reinforcement learning concepts such as observations, actions, rewards, and policies
    - A local checkout of the companion MARL GUI containing `tools/deploy_checkpoint.py` and `tools/inspect_checkpoint.py` if you want to complete the GUI deployment section

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-03T15:27:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0633ae9c265fb42853371d59189d721c34e923ba9d337349c41dedcf8fec9923
  summary_generated_at: '2026-09-03T15:17:57Z'
  summary_source_hash: 0633ae9c265fb42853371d59189d721c34e923ba9d337349c41dedcf8fec9923
  faq_generated_at: '2026-09-03T15:27:34Z'
  faq_source_hash: 0633ae9c265fb42853371d59189d721c34e923ba9d337349c41dedcf8fec9923
  summary: >-
    You'll configure and run a vectorized MAPPO navigation workload on an Arm-based cloud instance
    with BenchMARL, VMAS, and TorchRL. First, you'll select the agent count and CPU devices for shared-actor
    training with a centralized critic. Then, you'll restore the run configuration, locate and validate
    the checkpoint, optionally deploy it to a companion GUI, and export the actor for inference.
  faqs:
  - question: How many agents should I use for the reference MAPPO run?
    answer: >-
      Use three agents by exporting `AGENTS=3` before configuring the run. With
      `share_policy_params=true`, the three agents share one actor while receiving different
      observations.
  - question: How do I restore a previous run’s configuration before validating the checkpoint?
    answer: >-
      Activate the training environment, set `RUN_DIR` to the run directory that you want to validate,
      and source `"$RUN_DIR/run.env"`. Then, change to the `BenchMARL` repository to continue
      validation.
  - question: How do I make sure sampling and training run on the CPU?
    answer: >-
      Export `SAMPLING_DEVICE=cpu` and `TRAIN_DEVICE=cpu` before you launch the experiment.
      BenchMARL configures sampling and training devices independently, and saves these choices in
      your run environment.
  - question: What should I expect from the exported actor artifact?
    answer: >-
      Your export contains only the actor policy, without the critic, replay buffer, collector
      state, or training counters. For VMAS navigation, you'll get an MLP with 18 inputs, two
      256-unit `Tanh` layers, and four outputs for a two-dimensional action.
  - question: Do I need the GUI to verify the checkpoint or export the actor?
    answer: >-
      No. You can validate the checkpoint and export the actor without the GUI. Use the
      GUI only when you have the companion checkout described in the prerequisites. Otherwise,
      skip that stage and continue with exporting the actor.
# END generated_summary_faq

author:
    - Sagar Surendran
    - Na Li
    - Masoud Koleini

generate_summary_faq: false
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
