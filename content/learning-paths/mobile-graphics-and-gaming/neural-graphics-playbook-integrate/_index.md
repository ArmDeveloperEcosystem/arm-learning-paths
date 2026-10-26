---
title: Arm Neural Technology Playbook - Integrate
description: Plan an NFRU or NSS integration, evaluate model work with MLIA and Streamline, and scope experimental NSSD exploration with Arm.
minutes_to_complete: 60

who_is_this_for: This Learning Path is for game developers, graphics engineers, and technical leads who understand Arm Neural Technology and want to plan an integration for a mobile game.

learning_objectives:
    - Choose the Arm Neural Technology integration route that matches your game and team.
    - Plan an Neural Frame Rate Upscaling (NFRU) evaluation using public Arm tools and representative game content.
    - Decide when advanced Neural Super Sampling and Denoising (NSSD) exploration with Arm fits your visual goals.
    - Use Model Gym, Arm ML Inference Advisor (MLIA), and Streamline to plan model development and validation for neural accelerator (NX).

prerequisites:
    - Familiarity with Arm Neural Technology and its NSS, NFRU, and NSSD use cases
    - Basic understanding of real-time rendering, motion vectors, temporal techniques, and denoising
    - Familiarity with your game's frame-rate, image-quality, power, and thermal targets

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-26T15:47:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 48fb2106c848266d9b29f50ed3d56d189b263e7946d18c4956fe172e707c780d
  summary_generated_at: '2026-10-26T15:47:56Z'
  summary_source_hash: 48fb2106c848266d9b29f50ed3d56d189b263e7946d18c4956fe172e707c780d
  faq_generated_at: '2026-10-26T15:47:56Z'
  faq_source_hash: 48fb2106c848266d9b29f50ed3d56d189b263e7946d18c4956fe172e707c780d
  summary: >-
    You'll choose an Arm Neural Technology route for your game's visual goal and engine.
    You'll examine Neural Frame Rate Upscaling (NFRU) inputs and frame pacing, then set pass
    criteria and test game content. Next, you'll decide whether NSSD merits experimental exploration with Arm. If a measured gap justifies
    model work, you'll use Model Gym, MLIA, and Streamline to assess candidates. You'll finish
    with an integration brief separating estimates from device measurements.
#   faqs:
#   - question: How do I choose between NFRU, NSS, and NSSD?
#     answer: >-
#       Start with your player-facing goal and the resources your engine can provide. Choose the public
#       NFRU route for smoother presentation or the public NSS route for neural upscaling. If your
#       lighting goals call for denoising and super sampling together, consider NSSD as an experimental
#       exploration with Arm. You can start with a published model and defer custom model work.
#   - question: What pass condition confirms NFRU is viable for my game?
#     answer: >-
#       Set your presentation, image-quality, latency, power, and thermal limits before testing.
#       Compare the same representative action with NFRU disabled and enabled under fixed conditions.
#       Continue only if your measured result meets your presentation target within those limits.
#   - question: What should I record during the NFRU test run?
#     answer: >-
#       Record render FPS, present FPS, frame-time distribution, and your image-quality observations.
#       Capture latency, power, and thermal data against the limits you set. Use the Project Moku case
#       study to establish a repeatable capture method, then apply it to representative game content.
#   - question: How should I treat desktop results from the ML Emulation Layer?
#     answer: >-
#       Use the ML Emulation Layer for desktop development and testing. Don't treat its performance
#       as representative of production hardware. Validate performance-critical decisions on an Arm
#       GPU with a neural accelerator (NX).
#   - question: Which motion data does NFRU need, and how do I check it?
#     answer: >-
#       Supply color, depth, motion vectors, camera data, and metadata from your engine. Check the
#       motion-vector format and coordinate system, and confirm that the data aligns with neighboring
#       rendered frames. NFRU uses optical flow within its motion-estimation stage; you don't supply
#       it as a separate engine input.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
tools_software_languages:
    - Unreal Engine
    - Vulkan
    - Arm Performance Studio
    - Streamline
    - MLIA
    - NX
operatingsystems:
    - Windows
    - Android

further_reading:
    - resource:
        title: Neural Network Model Development Best Practices for GPUs with Neural Accelerator
        link: https://developer.arm.com/documentation/112431/latest
        type: documentation
    - resource:
        title: Arm GPU Best Practices Developer Guide
        link: https://support.arm.com/documentation/101897/latest/
        type: documentation
    - resource:
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Get Started with profiling Arm Neural Technology workloads with Streamline
        link: /learning-paths/mobile-graphics-and-gaming/streamline-nx/
        type: learningpath
    - resource:
        title: Estimate neural accelerator (NX) performance with ML Inference Advisor
        link: /learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
