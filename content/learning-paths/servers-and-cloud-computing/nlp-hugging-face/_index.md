---
title: Run a Natural Language Processing (NLP) model from Hugging Face on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run a Natural Language Processing (NLP) model from Hugging Face using PyTorch on Arm based servers. 

learning_objectives:
    - Deploy a PyTorch NLP model from Hugging Face on an Arm AArch64 CPU
    - Use the PyTorch profiler to analyze the execution time of the model

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:40:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 81bdee16a18b09da91a7514eb70368771b251ed3f8ec657ec105ca10ecead038
  summary_generated_at: '2026-06-02T04:38:40Z'
  summary_source_hash: 81bdee16a18b09da91a7514eb70368771b251ed3f8ec657ec105ca10ecead038
  faq_generated_at: '2026-06-03T01:40:53Z'
  faq_source_hash: 81bdee16a18b09da91a7514eb70368771b251ed3f8ec657ec105ca10ecead038
  summary: >-
    Learn how to run a Hugging Face Natural Language Processing (NLP) model with PyTorch on Arm
    servers. Using an Arm-based cloud instance or on-prem Arm server running Ubuntu 22.04 LTS,
    you will install PyTorch, load an NLP model from Hugging Face, execute the model on an Arm
    AArch64 CPU, and use the PyTorch profiler to analyze its execution time. The path focuses
    on practical setup and measurement using Python, PyTorch, and Hugging Face. No explicit prerequisites
    are listed beyond access to an Arm-based server. This introductory Learning Path is designed
    to be completed in about 20 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm based instance from a cloud service provider or an on-premise
      Arm server. No other explicit prerequisites are listed.
  - question: Which operating system should my server use?
    answer: >-
      The instructions are written for an Arm server running Ubuntu 22.04 LTS on Linux. Other
      operating systems are not covered in this path.
  - question: Can I use AWS, Microsoft Azure, Google Cloud, or Oracle Cloud for this?
    answer: >-
      Yes. You can use an Arm based instance from any of these cloud service providers, or an
      on-premise Arm server.
  - question: Do I need a GPU to run the model?
    answer: >-
      No. This path focuses on deploying and running the model on an Arm AArch64 CPU. GPU use
      is not covered.
  - question: How do I know the deployment and profiling worked?
    answer: >-
      You should be able to run inference on the model and collect execution-time data using the
      PyTorch profiler. Seeing profiler output for the model run indicates success.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

