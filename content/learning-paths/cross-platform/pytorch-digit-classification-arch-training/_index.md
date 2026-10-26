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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:44:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  summary_generated_at: '2026-07-29T16:44:40Z'
  summary_source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  faq_generated_at: '2026-07-29T16:44:40Z'
  faq_source_hash: 1251465f13b67ee80292b66ef22069a1b6cc2ca67bb602cdd5e393a278576ec8
  summary: >-
    You'll build and train a PyTorch feedforward neural network for MNIST digit classification, then use it
    for inference and Android deployment. You'll set up Python, prepare the dataset, and train the model. Then, you'll
    reload the model's saved parameters and apply the same preprocessing to new images. You'll quantize
    and fuse an optimized variant, integrate it into an Android application, and compare inference
    times before deployment.
  faqs:
  - question: How do I know the MNIST dataset is set up correctly before training?
    answer: >-
      Confirm that the training and test splits download without errors and that the `DataLoader`
      returns batches. With `batch_size` set to 32, the first batch contains 32 images of 28x28 pixels
      and corresponding labels from 0–9.
  - question: What should I look for during training to confirm the model is learning?
    answer: >-
      Monitor the loss and confirm that it decreases over epochs. Evaluate on the test data
      periodically to check whether predictions align with the true labels more often.
  - question: After training, what do I need to load the model for inference?
    answer: >-
      Use the model file produced during training and provide its path when loading. Recreate the
      same model architecture before loading the saved parameters.
  - question: How do I validate that inference works on new images?
    answer: >-
      Apply the training preprocessing, including normalization and tensor conversion, then run a
      prediction. The output maps to a digit from 0–9. Compare it with a known test-set label.
  - question: How do I compare unoptimized and optimized models after quantization and fusing?
    answer: >-
      Measure inference time with the original model, then repeat the measurement after quantization
      and fusing with identical inputs and conditions. Use the timings to choose the model for the
      Android application.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
