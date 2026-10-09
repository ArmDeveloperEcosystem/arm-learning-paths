---
title: Enable neural graphics using ML Extensions for Vulkan
description: Learn how to set up ML Emulation Layers for Vulkan, run sample applications with ML Extensions for Vulkan, and debug the workflow with RenderDoc.
minutes_to_complete: 30

who_is_this_for: This advanced Learning Path is for engine developers who want to create neural graphics with ML Extensions for Vulkan.

learning_objectives:
    - Explain the purpose of neural graphics and the role of ML Extensions for Vulkan
    - Set up the ML Emulation Layers for Vulkan to enable the extensions
    - Run a sample Vulkan application that uses the extensions
    - Debug the flow using RenderDoc

prerequisites:
    - Windows 11 development machine
    - Visual Studio 2022
    - Visual Studio workload - Desktop development with C++
    - Visual Studio workload - .NET desktop build tools
    - Visual Studio Code

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:33:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 789ae18c87f9bf1d4171117d7f45b54440d9ab81bc42f85ce6418b9fc4f78962
  summary_generated_at: '2026-08-21T17:33:57Z'
  summary_source_hash: 789ae18c87f9bf1d4171117d7f45b54440d9ab81bc42f85ce6418b9fc4f78962
  faq_generated_at: '2026-08-21T17:33:57Z'
  faq_source_hash: 789ae18c87f9bf1d4171117d7f45b54440d9ab81bc42f85ce6418b9fc4f78962
  summary: >-
    You'll enable neural graphics workloads with ML Extensions for Vulkan by setting up the ML Emulation
    Layers and running Vulkan Samples. First, you'll install development tools and configure the
    layers. You'll build the Simple Tensor and Data Graph sample which runs a 2D average pooling
    operation through a data graph pipeline. Then, you'll review the Scenario Runner assets for an
    inference workflow and use RenderDoc to capture frames and inspect Vulkan calls, shaders, tensors,
    and resource states.
  faqs:
  - question: Do I need native driver support for VK_ARM_data_graph and VK_ARM_tensors to run
      the samples?
    answer: >-
      No. The ML Emulation Layers for Vulkan simulate these extensions so you can build and run
      the samples during development.
  - question: How do I run the Simple Tensor and Data Graph sample after building it?
    answer: >-
      Run `build\windows\app\bin\Release\AMD64\vulkan_samples.exe sample simple_tensor_and_data_graph`
      from the `Vulkan-Samples` repository. A new window opens and visualizes the operation.
  - question: How do I run a 2D average pooling operation?
    answer: >-
      Run the Simple Tensor and Data Graph sample to execute a 2D average pooling operation through
      a data graph pipeline. Create input and output tensors, bind them with descriptor sets
      and pipeline layouts, and dispatch the SPIR-V-defined network.
  - question: What does the NSS Scenario Runner download include?
    answer: >-
      The NSS model release includes a Windows-compatible Scenario Runner binary, the VGF model,
      and one input frame with expected output data. You can use these assets to run an end-to-end
      workflow and examine the VGF model.
  - question: How do I capture a Vulkan Samples frame in RenderDoc?
    answer: >-
      Use RenderDoc when you need to diagnose unexpected visual output, examine Vulkan API calls,
      inspect resource states, or validate data graph pipeline execution. In **Launch Application**,
      set the **Executable Path**, **Working Directory**, and **Command-line Arguments**, select
      **Launch**, then press the **F12** key while the sample is active. In the capture, inspect Vulkan API
      calls, shader inputs and outputs, and resource states.
# END generated_summary_faq

author:
    - Annie Tallund
    - Joshua Marshall-Law

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - Vulkan
    - RenderDoc
    - NX
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: ML SDK for Vulkan
        link: https://github.com/arm/ai-ml-sdk-for-vulkan
        type: website
    - resource:
        title: Vulkan Samples
        link: https://github.com/ARM-software/Vulkan-Samples
        type: website
    - resource:
        title: RenderDoc for Arm GPUs
        link: https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs
        type: documentation
    - resource:
        title: How Arm Neural Super Sampling works
        link: https://community.arm.com/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-arm-neural-super-sampling-works
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
