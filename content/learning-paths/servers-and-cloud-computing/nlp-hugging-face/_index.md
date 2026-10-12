---
title: Run a Natural Language Processing (NLP) model from Hugging Face on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run a natural language processing (NLP) model from Hugging Face using PyTorch on Arm based servers. 

learning_objectives:
    - Deploy a PyTorch NLP model from Hugging Face on an Arm AArch64 CPU
    - Use the PyTorch profiler to analyze the execution time of the model

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:40:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5d0c0a2a23fba1796458c60ac49fa5d4b43e0d827463e049afb0e1b79eb9292f
  summary_generated_at: '2026-10-01T19:40:33Z'
  summary_source_hash: 5d0c0a2a23fba1796458c60ac49fa5d4b43e0d827463e049afb0e1b79eb9292f
  faq_generated_at: '2026-10-01T19:40:33Z'
  faq_source_hash: 5d0c0a2a23fba1796458c60ac49fa5d4b43e0d827463e049afb0e1b79eb9292f
  summary: >-
    You'll run and profile a Hugging Face NLP model with PyTorch on an Arm
    AArch64 CPU. First, you'll prepare an Ubuntu 22.04 LTS Arm server and install PyTorch, Transformers,
    and SciPy. You'll then run a RoBERTa sentiment-analysis model and inspect its ranked labels and
    confidence scores. Finally, you'll add the PyTorch Profiler and review the CPU execution time
    for individual operators.
  faqs:
  - question: How can I analyze my own text with the example?
    answer: >-
      Replace the string assigned to `text` in `sentiment-analysis.py`, save the file, and run
      `python sentiment-analysis.py` again. The script preprocesses your text before passing it
      to the tokenizer and model.
  - question: How does the example handle usernames and links?
    answer: >-
      When you run the script, its `preprocess` function replaces words that start with `@` and
      contain more than one character with `@user`. It replaces words that start with `http`
      with `http` before tokenization.
  - question: Which Hugging Face model should I use?
    answer: >-
      Use the `cardiffnlp/twitter-roberta-base-sentiment-latest` model.
  - question: What result should I expect when I run the model?
    answer: >-
      A successful run prints three ranked sentiment labels with confidence scores. The scores
      should sum to 1. The first line is the model's strongest prediction.
  - question: How do I know that the PyTorch profiler captured my run?
    answer: >-
      You should see a table of CPU operators and their execution times before the classification
      output. The `model_inference` row summarizes the profiled inference region.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse 
operatingsystems:
    - Linux 
tools_software_languages:
    - Python
    - PyTorch
    - Hugging Face

further_reading:
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: PyTorch Inference Performance Tuning on AWS Graviton Processors
        link: https://pytorch.org/tutorials/recipes/inference_tuning_on_aws_graviton.html
        type: documentation
    - resource:
        title: ML inference on Graviton CPUs with PyTorch
        link: https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md
        type: documentation
    - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
