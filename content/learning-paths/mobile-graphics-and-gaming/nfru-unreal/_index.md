---
title: Enable Neural Frame Rate Upscaling in Unreal Engine
description: Configure Neural Frame Rate Upscaling (NFRU) in Unreal Engine with ML extensions for Vulkan, then validate, tune, debug, and analyze frame generation.

minutes_to_complete: 30

who_is_this_for: This Learning Path is designed for developers interested in exploring neural frame generation techniques in Unreal Engine® using ML extensions for Vulkan®.

learning_objectives:
    - Understand the fundamentals of neural graphics in game development
    - Set up and use ML extensions for Vulkan emulation
    - Set up Neural Frame Rate Upscaling (NFRU) in Unreal Engine
    - Visualize neural frame generation result
    - Set available console variables for tuning NFRU performance and quality


prerequisites:
    - Windows 11
    - Unreal Engine 5.4 or 5.6, with the Templates and Feature Pack enabled
    - Visual Studio, with Desktop Development with C++ and .NET desktop build tools
    - Git Large File Storage (LFS) downloaded and installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-20T21:53:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 58ca900e7970e8d2d3dded0aacca94ff1c237ef3881005d422ba95f3f1d8f9b9
  summary_generated_at: '2026-07-20T21:53:46Z'
  summary_source_hash: 58ca900e7970e8d2d3dded0aacca94ff1c237ef3881005d422ba95f3f1d8f9b9
  faq_generated_at: '2026-07-20T21:53:46Z'
  faq_source_hash: 58ca900e7970e8d2d3dded0aacca94ff1c237ef3881005d422ba95f3f1d8f9b9
  summary: >-
    You’ll configure NFRU in Unreal Engine using Arm’s Neural Graphics
    Development Kit and ML Extensions for Vulkan. You’ll build the Neural Graphics SDK, enable the
    Vulkan ML emulation layers, and add the Neural Rendering plugin to a C++ project. After configuring
    Vulkan as the rendering hardware interface, you’ll validate NFRU in **Standalone Game** mode and
    inspect frame-generation statistics and intermediate buffers. You’ll then learn to adjust NFRU settings with
    console variables, visualize NFRU intermediate buffers, and inspect frames with RenderDoc for Arm GPUs
    to examine Vulkan events, resources, and pipeline stages. By the end, you’ll have a working NFRU
    project and a repeatable workflow for validation and debugging.
  faqs:
  - question: Which Unreal Engine project type should I create to use NFRU?
    answer: >-
      Create a **Third Person** template project using the **C++** option. A C++ project is required
      to build the Neural Graphics for Unreal plugin.
  - question: Why doesn’t NFRU work in the standard Unreal Editor viewport?
    answer: >-
      NFRU isn’t supported in the standard viewport. Use **Standalone Game** mode or create a packaged
      build to run and validate NFRU.
  - question: Where should I place the Neural Graphics plugin in my project?
    answer: >-
      Create a `Plugins` directory in the project's root directory to place the plugin. Then, create a symbolic link to the plugin folder for your Unreal Engine version. You need administrator permissions to create the symbolic link.
  - question: Which Vulkan SDK version do I need for ML extension emulation?
    answer: >-
      Install Vulkan SDK version `1.4.321.0` or newer. Use Vulkan Configurator to enable the emulation
      layers for running ML workloads through Vulkan ML extensions.
  - question: How do I tune or debug NFRU while testing?
    answer: >-
      Adjust NFRU console variables, such as `r.NFRU.Enable`, `r.NFRU.ShowDebugView`, and `r.NFRU.DataGraphFrameGeneration`, in **Standalone Game** mode to control enablement, debugging, performance tuning, and
      frame generation modes.
# END generated_summary_faq

author: Powen Yang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
    - Vulkan SDK
    - Visual Studio
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: RenderDoc for Arm GPUs
        link: https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs
        type: documentation
    - resource:
        title: Get started with neural graphics using ML extensions for Vulkan
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath
    - resource:
        title: Train and evaluate Neural Frame Rate Upscaling models using Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym-nfru/
        type: learningpath



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
