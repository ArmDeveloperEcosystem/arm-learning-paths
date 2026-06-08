---
title: Use Keras Core with TensorFlow, PyTorch, and JAX backends

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for engineers who want to create a neural network model on Arm machines.

description: Create, train, and evaluate a neural network model on Arm servers using Keras Core with TensorFlow, PyTorch, and JAX backends.

learning_objectives: 
    - Create a simple neural network model using Keras Core
    - Train and evaluate your neural network model with different backends
    - Generate predictions with the trained model

prerequisites:
    - Basic Machine Learning knowledge.
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, an on-premises Arm server, or a Linux virtual machine on your Arm device. 
    - Familiarity with SSH, the Linux command line, and basic system administration tasks.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:17:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 830556dfd51aaa2dd95ee957e64306bab369297f7bc66325e7eb509f541f683c
  summary_generated_at: '2026-06-02T04:13:36Z'
  summary_source_hash: 830556dfd51aaa2dd95ee957e64306bab369297f7bc66325e7eb509f541f683c
  faq_generated_at: '2026-06-03T01:17:46Z'
  faq_source_hash: 830556dfd51aaa2dd95ee957e64306bab369297f7bc66325e7eb509f541f683c
  summary: >-
    This introductory Learning Path shows how to create, train, and evaluate a simple neural network
    on Arm servers using Keras Core with TensorFlow, PyTorch, and JAX backends. You work on Ubuntu
    22.04 LTS on an Arm-based instance or server, including cloud instances from AWS, Microsoft
    Azure, Google Cloud, or Oracle. After installing the required Python environment, you write
    and run a compact ml.py script that defines and compiles a model in Keras Core, then train,
    evaluate, and generate predictions using different backends. The path targets Linux and takes
    about 30 minutes. Prerequisites include basic machine learning knowledge and familiarity with
    SSH, the Linux command line, and basic system administration tasks.
  faqs:
  - question: What environment should I prepare before starting?
    answer: >-
      Use an Arm-based machine running Ubuntu 22.04 LTS: a cloud instance on AWS, Microsoft Azure,
      Google Cloud, or Oracle; an on-premises Arm server; or a Linux VM on your Arm device. Access
      it via SSH (for remote servers) or open a terminal locally.
  - question: Which Python version should I use on Ubuntu 22.04, and do I need pip and venv?
    answer: >-
      Ubuntu 22.04 includes Python 3.10 by default, which you can use, or you can install a newer
      Python version. In either case, install the python3-pip and python3-venv packages to manage
      dependencies and an isolated environment.
  - question: How do I switch between TensorFlow, PyTorch, and JAX backends in Keras Core?
    answer: >-
      Keras Core supports multiple backends and the Learning Path runs the same model with TensorFlow,
      PyTorch, and JAX. Follow the step that specifies how to choose the backend before executing
      the script; the exact selection method is provided there.
  - question: What script do I run, and what should I expect as output?
    answer: >-
      You will create an ml.py script that defines a simple model with Keras Core, then compile,
      train, evaluate, and generate predictions. When it runs successfully, you should see training
      progress and evaluation results, followed by prediction output.
  - question: What input shape and data type does the example model expect?
    answer: >-
      The example model uses an input shape of 784 elements with dtype float16. If your data has
      a different shape or dtype, adjust the Input layer in the script accordingly.
# END generated_summary_faq

author: 
    - Diego Russo
    - Leandro Nunes

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
tools_software_languages:
    - Python
    - Keras
    - TensorFlow
    - PyTorch
    - JAX
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Keras Documentation
        link: https://keras.io/guides/
        type: documentation
    - resource:
        title: TensorFlow Documentation
        link: https://www.tensorflow.org/api_docs
        type: documentation
    - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation
    - resource:
        title: JAX Documentation
        link: https://jax.readthedocs.io/en/latest/index.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

