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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:24:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  summary_generated_at: '2026-07-28T16:24:15Z'
  summary_source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  faq_generated_at: '2026-07-28T16:24:15Z'
  faq_source_hash: aa2a78baf3e52172e37506c3f75254968d775b4eb516f9696a0a6998aba50e97
  summary: >-
    You'll fine-tune a Llama 3.2 3B model on an Arm-based NVIDIA DGX Spark, using the Grace CPU for
    orchestration and the GPU for training. You'll configure Docker, prepare a JSONL dataset from
    Raspberry Pi datasheet content, and run supervised fine-tuning in a prebuilt PyTorch container. You'll then 
    serve both base and fine-tuned models with vLLM to compare factual responses.
  faqs:
  - question: How do I know Docker on DGX Spark is ready before pulling containers?
    answer: >-
      After configuring permissions, pull and run the pre-built PyTorch container as shown in
      the setup step. If it runs without permission errors, Docker is configured correctly.
  - question: Which Llama model variant does the training script target?
    answer: >-
      The path fine-tunes Llama 3.2 3B using `Llama3_3B_full_finetuning.py`. The
      The path uses the 8B example only to illustrate why fine-tuning improves factual responses.
  - question: What dataset format should I use for supervised fine-tuning?
    answer: >-
      Use a JSONL dataset prepared for supervised fine-tuning. Ensure its fields match what the
      script loads; check the dataset loading section in the training script to align names and
      structure.
  - question: What output indicates the fine-tuning completed successfully?
    answer: >-
      The process produces a fine-tuned Llama model that the testing step can load with vLLM.
      You should be able to serve it in the vLLM container without errors.
  - question: What result should I expect when comparing base and fine-tuned models?
    answer: >-
      On Raspberry Pi datasheet questions, the fine-tuned model should answer factual queries
      correctly. For example, it reports the RP2350 maximum clock as 150 MHz, while the base model
      may hallucinate a higher value.
# END generated_summary_faq

author: Michael Hall

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
