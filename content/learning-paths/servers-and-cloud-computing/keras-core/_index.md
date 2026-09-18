---
title: Use Keras Core with TensorFlow, PyTorch, and JAX backends

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for engineers who want to create a neural network model on Arm machines.

description: Create, train, and evaluate a neural network model on Arm servers using Keras Core with TensorFlow, PyTorch, and JAX backends.

learning_objectives: 
    - Create a simple neural network model using Keras Core.
    - Train and evaluate your neural network model with different backends.
    - Generate predictions with the trained model.

prerequisites:
    - Basic Machine Learning knowledge
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, an on-premises Arm server, or a Linux virtual machine on your Arm device
    - Familiarity with SSH, the Linux command line, and basic system administration tasks

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:21:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 801a833c43823e5cb293569489ff5c563b983a3e3b1a86952f54ee1db906d741
  summary_generated_at: '2026-09-15T21:21:29Z'
  summary_source_hash: 801a833c43823e5cb293569489ff5c563b983a3e3b1a86952f54ee1db906d741
  faq_generated_at: '2026-09-15T21:21:29Z'
  faq_source_hash: 801a833c43823e5cb293569489ff5c563b983a3e3b1a86952f54ee1db906d741
  summary: >-
    You'll build and run a compact neural network with Keras Core on an Arm-based Ubuntu
    server. First, you'll prepare Python and define and execute a model that trains, evaluates, and
    predicts. Then, you'll switch among the TensorFlow, PyTorch, and JAX backends. You'll validate the
    complete workflow either locally or on an Arm-based instance over SSH by checking the printed
    training, evaluation, and prediction outputs.
  faqs:
  - question: How do I know which Keras Core backend is active when the script runs?
    answer: >-
      After selecting a backend, start the run and check the initial console
      output to confirm that the chosen backend is in use. If it's not the expected backend, repeat
      backend selection before training.
  - question: Where should I save ml.py, and how do I run it?
    answer: >-
      Create and activate the virtual environment that you
      prepared during dependency setup. Within the activated environment, save the script as `ml.py` in a working directory. To run the script, run `python ml.py`.
  - question: What result should I expect after training and evaluation?
    answer: >-
      The run prints training progress and evaluation metrics, then shows predictions from the
      trained model. Seeing metrics and prediction values confirms that the end-to-end workflow completed.
  - question: What should I check if importing keras_core fails?
    answer: >-
      Confirm that `keras_core` is installed in your active Python environment and that the environment
      is activated. On Ubuntu 22.04, also verify that `python3-pip` and `python3-venv` are installed
      if you use the system Python.
  - question: Can I use a different Python version than the system default?
    answer: >-
      Use a Python version supported by the required dependencies. To stay consistent with the Learning Path, use Python
      3.10 or 3.11. If you want to use a newer version such as Python 3.12, check package support because TensorFlow and PyTorch might not provide packages for it.
# END generated_summary_faq

author: 
    - Diego Russo
    - Leandro Nunes

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
