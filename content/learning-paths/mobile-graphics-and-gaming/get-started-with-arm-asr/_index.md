---
title: Get started with Arm Accuracy Super Resolution 

minutes_to_complete: 40

who_is_this_for: This Learning Path is for mobile, gaming, and graphics developers who want to install and configure Arm Accuracy Super Resolution (Arm ASR) to enhance performance on complex game content without sacrificing image quality.

learning_objectives:
    - Understand what Arm Accuracy Super Resolution (Arm ASR) is.
    - Integrate Arm ASR into your game project.
    - Manage how Arm ASR upscales content.

prerequisites:
    - A game project that uses advanced rendering features (such as hardware ray tracing) that stretch the performance capabilities of everyday smartphones.
    - A development machine with Git installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:02:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2424d8faebea11359ea0330d94698187b9305dde158d5761f9942eb33e711583
  summary_generated_at: '2026-08-17T22:02:37Z'
  summary_source_hash: 2424d8faebea11359ea0330d94698187b9305dde158d5761f9942eb33e711583
  faq_generated_at: '2026-08-17T22:02:37Z'
  faq_source_hash: 2424d8faebea11359ea0330d94698187b9305dde158d5761f9942eb33e711583
  summary: >-
    You'll add Arm ASR to an Unreal Engine project or custom engine.
    You'll learn about Unreal Engine plugin and how to integrate Arm ASR with a custom engine using the standalone backend or your engine's backend. For both options, you'll learn to configure settings such as quality presets, shaders, extensions, and input resources
    to evaluate image quality and performance trade-offs on mobile devices.
  faqs:
  - question: Which Unreal Engine versions should I use for the Arm ASR plugin?
    answer: >-
      Use Unreal Engine 5.3, 5.4, or 5.5. 
  - question: Can I use Arm ASR without Unreal Engine?
    answer: >-
      Yes. You can integrate Arm ASR into a custom engine using the generic library.
  - question: Which integration method should I choose with the generic library?
    answer: >-
      You can integrate Arm ASR using the standalone backend, or your engine’s backend or renderer. 
  - question: What configuration areas do I set up when using the generic library?
    answer: >-
      Configure quality presets, shader variants and extensions, and input resources. These
      settings control how ASR processes and upscales your content.
  - question: How do I balance image quality and performance in a custom-engine integration?
    answer: >-
      Select a shader quality preset and an upscaling ratio. Use `FfxmFsr2ShaderQualityMode` and
      `FfxmFsr2UpscalingRatio` together to choose the balance that suits your application.
# END generated_summary_faq

author: Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Arm ASR on Arm Developer Hub
        link: https://www.arm.com/developer-hub/mobile-graphics-and-gaming/arm-accuracy-super-resolution
        type: website
    - resource:
        title: Arm ASR Manga Comic
        link: https://developer.arm.com/Mobile%20Graphics%20and%20Gaming/FeaturedContent/Mali%20Manga/FeaturedContent-MaliManga-Volume4
        type: website
    - resource:
        title: Arm Community Blog
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/introducing-arm-accuracy-super-resolution
        type: blog
    - resource:
        title: Arm Accuracy Super Resolution for Unreal Engine Tutorial
        link: https://developer.arm.com/documentation/109993/latest/
        type: documentation
    - resource:
        title: Arm Accuracy Super Resolution for the Generic Library Tutorial
        link: https://developer.arm.com/documentation/110404/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
