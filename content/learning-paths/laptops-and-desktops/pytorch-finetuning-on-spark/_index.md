---
title: Fine-tune PyTorch models on DGX Spark

description: Learn how to fine-tune large language models using PyTorch and Hugging Face on NVIDIA DGX Spark to improve domain-specific accuracy.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for AI developers and ML engineers who want to fine-tune large language models using PyTorch and Hugging Face on the NVIDIA DGX Spark platform.

learning_objectives: 
    - Understand how fine-tuning teaches a model domain-specific knowledge
    - Prepare a custom JSONL dataset for supervised fine-tuning
    - Fine-tune Llama 3.2 3B on Raspberry Pi datasheet content using PyTorch and Hugging Face
    - Compare base and fine-tuned model responses to verify factual accuracy improvements

prerequisites:
    - Hugging Face account and access token
    - NVIDIA DGX Spark workstation

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:11:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  summary_generated_at: '2026-06-01T22:09:20Z'
  summary_source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  faq_generated_at: '2026-06-02T23:11:51Z'
  faq_source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  summary: >-
    Learn how to fine-tune the Llama 3.2 3B language model on domain data using PyTorch and Hugging
    Face on an NVIDIA DGX Spark with an Arm-based Grace CPU and a Blackwell GPU. You will configure
    Docker on Linux, pull a pre-built PyTorch container, prepare a JSONL dataset from Raspberry
    Pi datasheet content for supervised fine-tuning, and run a provided PyTorch script to train
    the model. Finally, you will serve the base and fine-tuned models using a vLLM container to
    compare responses and confirm factual accuracy improvements. Prerequisites are a Hugging Face
    account with access token and access to a DGX Spark workstation.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Hugging Face account with an access token and an NVIDIA DGX Spark workstation.
      The Learning Path targets a Linux environment.
  - question: Do I need to install Docker on DGX Spark?
    answer: >-
      No. Docker is pre-installed on the DGX Spark, and you only need to configure permissions
      as described in the setup step.
  - question: Which model and dataset format are used for fine-tuning?
    answer: >-
      You will fine-tune Llama 3.2 3B. The workflow expects a custom JSONL dataset prepared for
      supervised fine-tuning.
  - question: Which containers are used for training and serving?
    answer: >-
      You pull a pre-built PyTorch container to run fine-tuning. For inference and comparison,
      you use an NVIDIA-provided vLLM container.
  - question: How do I know the fine-tuned model improved factual accuracy?
    answer: >-
      Serve both the base and fine-tuned models with vLLM and compare answers to domain questions.
      For example, after fine-tuning on Raspberry Pi datasheets, the model should answer that
      the RP2350 supports up to 150 MHz instead of the incorrect 1.8 GHz.
# END generated_summary_faq

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
    - Hugging Face
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
    - resource:
        title: Build a serverless LLM inference application with AWS Lambda and Arm processors
        link: /learning-paths/servers-and-cloud-computing/llama-cpu/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

