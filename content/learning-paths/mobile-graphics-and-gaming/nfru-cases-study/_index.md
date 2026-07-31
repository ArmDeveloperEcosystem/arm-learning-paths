---
title: Analyze Neural Frame Rate Upscaling using Project Moku

description: Learn how Project Moku uses Neural Frame Rate Upscaling to improve presented smoothness, then enable, evaluate, and tune NFRU in Unreal Engine using Arm ML Extensions for Vulkan.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for game and graphics developers who want to evaluate Neural Frame Rate Upscaling (NFRU) in Unreal Engine using Arm ML Extensions for Vulkan.

learning_objectives:
    - Understand how NFRU generates intermediate frames for smoother motion.
    - Evaluate NFRU visual quality across occlusion, particle, and lighting-change scenarios.
    - Measure NFRU performance and tune frame pacing with Unreal Engine console variables.
    - Analyze generated frames with RenderDoc for Arm GPUs.


prerequisites:
    - (Recommended) Complete [Enable Neural Frame Rate Upscaling in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/)
    - Windows 11
    - Unreal Engine 5.4 or 5.6 with Templates and Feature Pack enabled
    - Visual Studio with Desktop Development with C++ and .NET desktop build tools
    - Familiarity with Unreal Engine project setup and rendering settings

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  summary: >-
    You will use Project Moku, an Arm Unreal Engine sample, to evaluate Neural Frame Rate
    Upscaling (NFRU) on mobile GPUs. You will enable the Arm Neural Graphics Plugin, create
    repeatable reference cuts, and use Streamline and RenderDoc to validate frame generation,
    inspect visual differences, and measure render FPS, present FPS, neural workload, and frame
    pacing. You will analyze occlusion, particle, and lighting-change scenarios before tuning
    NFRU for your own Unreal Engine content.
  faqs:
  - question: What is Project Moku used for?
    answer: >-
      Project Moku is an Arm Unreal Engine sample that provides a controlled environment for
      evaluating NFRU and related neural rendering techniques on supported mobile GPUs.
  - question: How does NFRU improve perceived smoothness?
    answer: >-
      NFRU generates an intermediate frame between rendered frames, increasing the presentation
      cadence without requiring the engine to render every displayed frame.
  - question: Which tools validate NFRU?
    answer: >-
      Use Streamline to confirm NFRU activity and measure GPU and neural workload. Use RenderDoc
      to inspect frame-generation events, inputs, intermediate resources, and generated output.
  - question: Which scenes are useful for evaluating NFRU visual quality?
    answer: >-
      Test repeatable scenes with occlusion changes, alpha-blended particles, and lighting changes.
      These scenarios expose differences around visibility, disocclusion, transparency, and
      screen edges.
  - question: How should NFRU performance be measured?
    answer: >-
      Compare render FPS with present FPS, then check GPU and neural workload, display limits,
      and frame-pacing gaps. Use the pace adjuster to select a presentation target the workload
      can sustain.
# END generated_summary_faq

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

author: Powen Yang

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
    - Vulkan SDK
    - Visual Studio
    - Arm Performance Studio
    - NX
operatingsystems:
    - Windows



further_reading:
    - resource:
        title: Enable NFRU in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/nfru-unreal/
        type: learning path
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: RenderDoc for Arm GPUs
        link: https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs
        type: documentation
    - resource:
        title: Streamline Performance Analyzer
        link: https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer
        type: documentation
    - resource:
        title: Neural Graphics Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learning path
    - resource:
        title: Fine-tune neural graphics models using Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym/
        type: learning path
    - resource:
        title: Generate neural graphics datasets with Neural Graphics Data Capture in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/
        type: learning path



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
