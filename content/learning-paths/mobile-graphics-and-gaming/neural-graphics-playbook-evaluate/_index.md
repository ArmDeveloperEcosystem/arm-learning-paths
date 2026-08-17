---
title: Arm Neural Technology Playbook - Evaluate
description: Evaluate whether Arm Neural Technology techniques such as NFRU and NSSD are a fit for your game.
minutes_to_complete: 45

who_is_this_for: This Learning Path is for game developers and graphics engineers evaluating Arm Neural Technology for mobile games.

learning_objectives:
    - Understand why Arm Neural Technology matters for mobile games
    - Learn what Arm built with Neural Dawn
    - Evaluate whether NFRU and NSSD are a fit for your game

prerequisites:
    - Familiarity with game development in Unreal Engine
    - Basic understanding of real-time rendering concepts (motion vectors, temporal techniques, denoising, upscaling)
    - Awareness of mobile rendering constraints (bandwidth, power efficiency, thermal management)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:11:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2448b0a37ba988434f97fe500681e7660cd9c2ad470c61a930e8c5a6f092f03d
  summary_generated_at: '2026-08-17T22:11:02Z'
  summary_source_hash: 2448b0a37ba988434f97fe500681e7660cd9c2ad470c61a930e8c5a6f092f03d
  faq_generated_at: '2026-08-17T22:11:02Z'
  faq_source_hash: 2448b0a37ba988434f97fe500681e7660cd9c2ad470c61a930e8c5a6f092f03d
  summary: >-
    You'll evaluate Arm Neural Technology for mobile games, focusing on Neural Frame Rate Upscaling
    and Neural Screen Space Denoising. Review the Neural Graphics Development Kit, including Unreal
    Engine plugins, models, and its Vulkan runtime. Then assess fit for your content, camera behavior,
    and performance targets, and begin hands-on trials with the available components.
  faqs:
  - question: How do I know if NFRU or NSSD fits my game?
    answer: >-
      Evaluate your content type, camera behavior, and performance targets. These neural techniques
      are not equally useful everywhere, so weigh visual goals and runtime constraints specific
      to your project.
  - question: Which component should I try first when starting hands-on?
    answer: >-
      NFRU is a good entry point. Integrate the Unreal Engine plugin, enable it in your project,
      and evaluate it like any other rendering feature.
  - question: What can I run today without waiting for NX hardware?
    answer: >-
      You can start with NSSD and the Neural Graphics Development Kit today. The current runtime
      path is centered on Vulkan on Arm platforms.
  - question: Where do I get the plugins and models used in this evaluation?
    answer: >-
      Arm provides Unreal Engine plugins, an SDK, prebuilt models, and tooling, along with reference
      implementations and sample content in the Neural Graphics Development Kit. Use them to integrate
      and assess the techniques in your project.
  - question: Why does the path reference Neural Dawn?
    answer: >-
      Neural Dawn is a mobile game built with Sumo Digital that showcases a rendering pipeline
      designed around neural graphics. It demonstrates high-fidelity visuals on mobile with a
      target of 60 FPS and helps set expectations for what these techniques can achieve.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Graphics
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
    - Vulkan
    - NX
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Arm Neural Technology for Mobile Games
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Enable Neural Super Sampling in Unreal Engine with ML Extensions
        link: /learning-paths/mobile-graphics-and-gaming/nss-unreal/
        type: documentation
    - resource:
        title: Arm Neural Technology Delivers Smarter, Sharper, More Efficient Mobile Graphics for Developers 
        link: https://newsroom.arm.com/news/arm-announces-arm-neural-technology
        type: blog
    - resource:
        title: Start experimenting with Neural Super Sampling for mobile graphics today
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/how-to-access-arm-neural-super-sampling
        type: blog
    - resource:
        title: New neural technologies set to join the Neural Graphics Development Kit
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/new-neural-technologies-set-to-join-the-neural-graphics-development-kit
        type: blog
    - resource:
        title: How Neural Graphics, AI, and Arm Tools Are Shaping Mobile Game Development
        link: https://newsroom.arm.com/blog/takeaways-from-gdc-festival-of-gaming-2026
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
