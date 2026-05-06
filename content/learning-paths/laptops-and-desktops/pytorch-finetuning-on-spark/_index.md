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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:55Z'
  generator: template
  source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  summary: >-
    Learn how to fine-tune large language models using PyTorch and Hugging Face on NVIDIA DGX
    Spark to improve domain-specific accuracy. It is designed for AI developers and ML engineers
    who want to fine-tune large language models using PyTorch and Hugging Face on the NVIDIA DGX
    Spark platform. By the end, you will be able to understand how fine-tuning teaches a model
    domain-specific knowledge, prepare a custom JSONL dataset for supervised fine-tuning, and
    fine-tune Llama 3.2 3B on Raspberry Pi datasheet content using PyTorch and Hugging Face. It
    focuses on tools and technologies such as Python, PyTorch, Docker, and Hugging Face, Linux
    environments, and Arm platforms including Cortex-A and Neoverse. The main steps cover Set
    up your NVIDIA DGX Spark, Understand fine-tuning, Fine-tune a model with PyTorch and Hugging
    Face, and Test your fine-tuned model with vLLM.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand how fine-tuning teaches a model domain-specific knowledge, prepare a
      custom JSONL dataset for supervised fine-tuning, and fine-tune Llama 3.2 3B on Raspberry
      Pi datasheet content using PyTorch and Hugging Face. Learn how to fine-tune large language
      models using PyTorch and Hugging Face on NVIDIA DGX Spark to improve domain-specific accuracy.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for AI developers and ML engineers who want to fine-tune large
      language models using PyTorch and Hugging Face on the NVIDIA DGX Spark platform.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Hugging Face account and access token;
      NVIDIA DGX Spark workstation.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, PyTorch, Docker, and Hugging Face, Linux
      environments, and Arm platforms such as Cortex-A and Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your NVIDIA DGX Spark, Understand fine-tuning,
      Fine-tune a model with PyTorch and Hugging Face, and Test your fine-tuned model with vLLM.
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

