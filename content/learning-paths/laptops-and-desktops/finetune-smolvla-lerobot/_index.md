---
title: Fine-tune SmolVLA for an SO-101 pick-and-place task

description: Record SO-101 demonstrations, fine-tune SmolVLA on an Arm-based NVIDIA DGX Spark, and evaluate the model with LeRobot.

minutes_to_complete: 1920

who_is_this_for: This is an advanced topic for robotics and AI developers who want to train a vision-language-action model from their own SO-101 demonstrations.

learning_objectives:
    - Set up a LeRobot environment for SO-101 data collection and SmolVLA training.
    - Connect, calibrate, and teleoperate an SO-101 leader-follower pair with cameras.
    - Record and inspect a pick-and-place dataset, then optionally upload it.
    - Fine-tune and physically evaluate a SmolVLA model on a NVIDIA DGX Spark.

prerequisites:
    - A NVIDIA DGX Spark with at least 30 GB of free storage.
    - An assembled SO-101 leader and follower, two USB cameras, and an unobstructed workspace.
    - A vial or similar graspable object and a stable rack for the placement target.
    - A [Hugging Face account](https://huggingface.co/join) if you want to upload the dataset.

author: Koki Mitsunami

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
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
    - PyTorch
    - LeRobot
    - SmolVLA
    - Hugging Face
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: LeRobot installation documentation
        link: https://huggingface.co/docs/lerobot/installation
        type: documentation
    - resource:
        title: LeRobot SO-101 documentation
        link: https://huggingface.co/docs/lerobot/so101
        type: documentation
    - resource:
        title: SmolVLA documentation
        link: https://huggingface.co/docs/lerobot/smolvla
        type: documentation
    - resource:
        title: SmolVLA base model card
        link: https://huggingface.co/lerobot/smolvla_base
        type: documentation
    - resource:
        title: SmolVLA research paper
        link: https://arxiv.org/abs/2506.01844
        type: website
    - resource:
        title: Train an SO-101 Robot From Sim-to-Real With NVIDIA Isaac
        link: https://docs.nvidia.com/learning/physical-ai/sim-to-real-so-101/latest/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
