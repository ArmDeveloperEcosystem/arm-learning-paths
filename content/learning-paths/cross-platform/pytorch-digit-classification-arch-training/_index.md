---
title: Create and train a PyTorch model for digit classification using the MNIST dataset

minutes_to_complete: 160

description: Learn how to create and train a PyTorch neural network for MNIST digit classification, optimize it with quantization and fusing, and deploy it in an Android application with performance measurement.

who_is_this_for: This is an advanced topic for software developers interested in learning how to use PyTorch to create and train a feedforward neural network for digit classification, and also software developers interested in learning how to use and apply optimizations to the trained model in an Android application.

learning_objectives:
    - Prepare a PyTorch development environment.
    - Download and prepare the MNIST dataset.
    - Create and train a neural network architecture using PyTorch.
    - Create an Android app and load the pre-trained model.
    - Prepare an input dataset.
    - Measure the inference time.
    - Optimize a neural network architecture using quantization and fusing.
    - Deploy an optimized model in an Android application.

prerequisites:
    - A machine that can run Python3, Visual Studio Code, and Android Studio. 
    - For the OS, you can use Windows, Linux, or macOS.
  

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:48:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  summary_generated_at: '2026-06-01T21:14:41Z'
  summary_source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  faq_generated_at: '2026-06-02T21:48:30Z'
  faq_source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  summary: >-
    This advanced Learning Path guides you through preparing a PyTorch development environment,
    downloading and organizing the MNIST dataset, and creating, training, and saving a feedforward
    neural network for digit classification. You then create an Android application that loads
    the pre-trained model, prepares input data consistently with training, and measures inference
    time. The path also shows how to apply quantization and fusing to optimize the network and
    deploy the optimized model in the app. You need a machine capable of running Python3, Visual
    Studio Code, and Android Studio on Windows, Linux, or macOS. Estimated time to complete is
    about 160 minutes.
  faqs:
  - question: What do I need installed before running the training and Android steps?
    answer: >-
      You need a machine that can run Python3, Visual Studio Code, and Android Studio. You can
      use Windows, Linux, or macOS.
  - question: How do I download MNIST and create DataLoaders in this path?
    answer: >-
      Use torchvision.datasets.MNIST with download=True and transforms.ToTensor, then create DataLoader
      objects for the training and test sets. The example shows a batch size of 32 and uses a
      data/ folder as the root.
  - question: How do I know the training step worked and the model is saved?
    answer: >-
      The training step saves the trained model to a file that you load later for inference. After
      saving, proceed to the inference step to validate loading and predictions.
  - question: During inference, how should I preprocess inputs so they match training?
    answer: >-
      Apply the same preprocessing used during training, such as tensor conversion and normalization.
      Ensure inputs are formatted like MNIST (28x28) before feeding them to the model.
  - question: When do I apply quantization and fusing, and what gets deployed to Android?
    answer: >-
      Apply quantization and fusing after training to produce an optimized model. The Learning
      Path then deploys this optimized model in an Android application and measures inference
      time.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Windows
    - Linux
    - macOS
tools_software_languages:
    - Android Studio
    - Visual Studio Code
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: PyTorch
        link: https://pytorch.org
        type: documentation    
    - resource:
        title: MNIST
        link: https://en.wikipedia.org/wiki/MNIST_database
        type: website
    - resource:
        title: Visual Studio Code
        link: https://code.visualstudio.com
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

