---
title: Fine-tune PyTorch models on DGX Spark

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for AI developers and ML engineers who want to fine-tune large language models using PyTorch and Hugging Face on the NVIDIA DGX Spark platform.

learning_objectives: 
    - Understand how fine-tuning teaches a model domain-specific knowledge
    - Prepare a custom JSONL dataset for supervised fine-tuning
    - Fine-tune Llama 3.1 8B on Raspberry Pi datasheet content using PyTorch and Hugging Face
    - Compare base and fine-tuned model responses to verify factual accuracy improvements

prerequisites:
    - Hugging Face account and access token
    - NVIDIA DGX Spark workstation

author: Michael Hall

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Python
    - PyTorch
    - Docker
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: NVIDIA PyTorch Fine-Tuning tutorial
        link: https://build.nvidia.com/spark/pytorch-fine-tune/overview
        type: documentation
    - resource:
        title: Hugging Face SFT Trainer
        link: https://huggingface.co/docs/trl/en/sft_trainer
        type: documentation
    - resource:
        title: Hugging Face Datasets
        link: https://huggingface.co/datasets
        type: website
    - resource:
        title: Hugging Face Fine-tuning Guide
        link: https://huggingface.co/docs/transformers/training
        type: documentation
    - resource:
        title: PyTorch Training Documentation
        link: https://pytorch.org/tutorials/beginner/introyt/trainingyt.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
