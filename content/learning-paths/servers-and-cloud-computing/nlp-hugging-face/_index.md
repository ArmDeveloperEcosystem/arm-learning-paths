---
title: Run a Natural Language Processing (NLP) model from Hugging Face on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run a Natural Language Processing (NLP) model from Hugging Face using PyTorch on Arm based servers. 

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
    Run and profile a Hugging Face natural language processing (NLP) model with PyTorch on an Arm
    AArch64 CPU. You prepare an Ubuntu 22.04 LTS Arm server and install PyTorch, Transformers,
    and SciPy. You then run a RoBERTa sentiment-analysis model and inspect its ranked labels and
    confidence scores. Finally, you add the PyTorch Profiler and review the CPU execution time
    for individual operators.
  faqs:
  - question: Do I need a specific Linux version for these steps?
    answer: >-
      Yes. The instructions target Ubuntu 22.04 LTS on an Arm server.
  - question: How do I know I’m running on an Arm AArch64 machine before I install PyTorch?
    answer: >-
      Confirm the instance type is Arm-based in your cloud console, or use an on-premises Arm
      server. The instructions assume an Arm AArch64 CPU.
  - question: Which Hugging Face model should I pick for the tutorial?
    answer: >-
      Use the `cardiffnlp/twitter-roberta-base-sentiment-latest` model specified in the example.
      The script downloads its configuration, tokenizer, and PyTorch weights from Hugging Face.
  - question: What result should I expect when I run the model?
    answer: >-
      A successful run prints three ranked sentiment labels with confidence scores. The scores
      should sum to 1, and the first line is the model's strongest prediction.
  - question: How do I know the PyTorch profiler captured my run?
    answer: >-
      You should see a table of CPU operators and their execution times after the classification
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
