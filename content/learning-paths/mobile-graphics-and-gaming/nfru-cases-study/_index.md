---
title: Analyze Neural Frame Rate Upscaling using Project Moku

description: Learn how Project Moku uses Neural Frame Rate Upscaling (NFRU) to improve presented smoothness, then enable, evaluate, and tune NFRU in Unreal Engine using Arm ML Extensions for Vulkan.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for game and graphics developers who want to evaluate Neural Frame Rate Upscaling (NFRU) in Unreal Engine using Arm ML Extensions for Vulkan.

learning_objectives:
    - Understand how NFRU generates intermediate frames for smoother motion.
    - Evaluate NFRU visual quality during camera movement, object movement, occlusion, particles, and lighting changes.
    - Measure NFRU performance and tune frame pacing with Unreal Engine console variables.
    - Analyze generated frames with RenderDoc for Arm GPUs.


prerequisites:
    - (Recommended) Complete [Enable Neural Frame Rate Upscaling in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/)
    - Windows 11
    - For Android captures, a device and driver meeting the current plugin requirements in the NFRU integration guide
    - A compatible Unreal Engine C++ project, as described in the NFRU integration guide
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
    You'll inspect NFRU results from Project Moku, Arm's internal Unreal Engine project, and apply the
    evaluation workflow to your own content. You'll enable the Arm Neural Graphics Plugin and prepare
    repeatable scenes. With Streamline and RenderDoc, you'll validate frame generation, inspect camera
    and object motion, and analyze occlusion, particles, and lighting changes. You'll then measure
    performance and tune presentation pacing.
  faqs:
  - question: What is Project Moku used for?
    answer: >-
      You can inspect the captured scenarios from Project Moku, Arm's internal Unreal Engine project,
      to understand NFRU behavior. You don't need access to Moku; apply the validation and profiling
      workflow to repeatable scenes in your own Unreal Engine project.
  - question: How does NFRU improve perceived smoothness?
    answer: >-
      You can use NFRU to generate an intermediate frame between rendered frames, increasing presentation
      cadence without rendering every displayed frame.
  - question: Which tools validate NFRU?
    answer: >-
      Use Streamline to confirm NFRU activity and measure GPU and neural workload. Use RenderDoc
      to inspect frame-generation events, inputs, intermediate resources, and generated output.
  - question: Which scenes are useful for evaluating NFRU visual quality?
    answer: >-
      You can compare fast camera turns and continuous object movement to inspect scene continuity
      and object silhouettes. You can then test occlusion changes, alpha-blended particles, and lighting
      changes to inspect visibility, transparency, and screen edges.
  - question: How should NFRU performance be measured?
    answer: >-
      Compare render FPS with the plugin's present FPS counter, then check GPU and neural workload
      and frame-pacing gaps. Verify physical display cadence separately. Use the pace adjuster
      to select a presentation target your workload can sustain.
# END generated_summary_faq

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

author: Powen Yang

### Tags
skilllevels: Advanced
subjects: AI/ML
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
        title: Enable Neural Frame Rate Upscaling in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/nfru-unreal/
        type: learningpath
    - resource:
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Train and evaluate Neural Frame Rate Upscaling models using Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym-nfru/
        type: learningpath
    - resource:
        title: Arm Neural Frame Rate Upscaling model on Hugging Face
        link: https://huggingface.co/Arm/neural-frame-rate-upscaling
        type: code
    - resource:
        title: RenderDoc for Arm GPUs
        link: https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs
        type: documentation
    - resource:
        title: Streamline Performance Analyzer
        link: https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer
        type: documentation
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
