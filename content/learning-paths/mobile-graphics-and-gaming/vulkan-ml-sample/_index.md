---
title: Enable neural graphics using ML Extensions for Vulkan
description: Learn how to set up ML Emulation Layers for Vulkan, run sample applications using ML extensions, and debug the flow with RenderDoc.
minutes_to_complete: 30

who_is_this_for: This is an advanced topic for engine developers interested in learning about neural graphics using ML Extensions for Vulkan.

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



generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:13:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: af4f1c8964e0970c187643bcd0330a63a6ce66c38a2e6b4d2fc17857a12a3d7f
  summary_generated_at: '2026-06-02T03:03:08Z'
  summary_source_hash: af4f1c8964e0970c187643bcd0330a63a6ce66c38a2e6b4d2fc17857a12a3d7f
  faq_generated_at: '2026-06-03T00:13:13Z'
  faq_source_hash: af4f1c8964e0970c187643bcd0330a63a6ce66c38a2e6b4d2fc17857a12a3d7f
  summary: >-
    This Learning Path shows how to enable neural graphics workflows on Windows by using ML Extensions
    for Vulkan. You install the ML Emulation Layers to simulate VK_ARM_data_graph and VK_ARM_tensors,
    set up build tools (CMake, Python 3, Git), and use Visual Studio 2022 on a Windows 11 development
    machine. You then build and run the Vulkan Samples fork, starting with the Simple Tensor and
    Data Graph example that executes a 2D average pooling operation via a data graph pipeline.
    You also run an end-to-end inference test with the Scenario Runner from Arm’s ML SDK for Vulkan,
    and debug or inspect frames with RenderDoc. By the end, you can run sample workloads using
    the ML extensions and analyze their execution.
  faqs:
  - question: What do I need installed before building and running the samples?
    answer: >-
      Use a Windows 11 development machine with Visual Studio 2022 and the Desktop development
      with C++ and .NET desktop build tools workloads. Install CMake (3.12+), Python 3, and Git,
      then download the ML Emulation Layers for Vulkan. You can verify tools with commands like
      cmake --version and python3 --version.
  - question: Which Vulkan ML extensions does this path use, and how are they enabled?
    answer: >-
      The path uses VK_ARM_data_graph and VK_ARM_tensors. These are enabled on your machine by
      installing the ML Emulation Layers for Vulkan, which simulate the extensions so the samples
      can run.
  - question: How do I get and build the first sample?
    answer: >-
      Clone Arm’s fork of Vulkan Samples on the tensor_and_data_graph branch with submodules as
      shown in the steps. Build it with the tools you installed; the Simple Tensor and Data Graph
      sample demonstrates a 2D average pooling operation via a data graph pipeline.
  - question: How do I run a complete inference test beyond the simple sample?
    answer: >-
      Use the Scenario Runner from Arm’s ML SDK for Vulkan. The Learning Path points to Arm’s
      Hugging Face page where you can download binaries and assets that demonstrate the ML extensions
      in action.
  - question: When should I use RenderDoc with these samples, and what can I inspect?
    answer: >-
      Use RenderDoc to capture frames when you need to visualize and debug ML-integrated rendering.
      You can step through frames, inspect Vulkan API calls, view shader inputs and outputs, examine
      tensors, and review GPU resource states and memory usage.
# END generated_summary_faq

author: Annie Tallund

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

