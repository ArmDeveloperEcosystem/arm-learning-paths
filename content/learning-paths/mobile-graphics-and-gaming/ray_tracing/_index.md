---
title: Implement ray tracing effects with Vulkan on Android
description: Learn how to use the Vulkan ray tracing API to implement realistic shadows, reflections, and refractions in Android applications.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for Vulkan developers who are familiar with rendering and are interested in deploying ray tracing in their applications.

learning_objectives:
    - Describe how the Vulkan ray tracing API works.
    - Describe how to use ray tracing to implement realistic shadows, reflections, and refractions.
    - Implement basic ray tracing effects in a Vulkan renderer.

prerequisites:
    - An appropriate Android device that supports the required Vulkan extensions (for example, Vivo X100).
    - Knowledge of the Vulkan API.
    - A Vulkan renderer. Most code is generic and should be easy to incorporate into any deferred PBR renderer.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:05:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 78f862a7c46fd4591fec45f91d040eb3f1093291c0a7328dddd2203dad72db3f
  summary_generated_at: '2026-06-02T02:57:13Z'
  summary_source_hash: 78f862a7c46fd4591fec45f91d040eb3f1093291c0a7328dddd2203dad72db3f
  faq_generated_at: '2026-06-03T00:05:48Z'
  faq_source_hash: 78f862a7c46fd4591fec45f91d040eb3f1093291c0a7328dddd2203dad72db3f
  summary: >-
    Learn how to add ray tracing to Android renderers using the Vulkan ray tracing API. This Learning
    Path explains core concepts, compares the ray tracing pipeline and ray query approaches, shows
    how to create acceleration structures, and uses bindless materials to access hit data efficiently.
    You will implement basic effects for realistic shadows, reflections, and refractions in an
    existing Vulkan renderer. The target is Android devices that support the required Vulkan extensions;
    Immortalis GPUs (such as Immortalis-G715, Immortalis-G720, and Immortalis-G925) support ray
    tracing, while support on some Mali G7-series devices varies by phone model. Prerequisites
    include a compatible Android device (for example, Vivo X100), knowledge of the Vulkan API,
    and access to a renderer, ideally a deferred PBR design.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an appropriate Android device that supports the required Vulkan extensions (for
      example, a Vivo X100), prior knowledge of the Vulkan API, and a Vulkan renderer. The material
      is written so most code can be integrated into a deferred PBR renderer.
  - question: How do I know if my Android device or GPU supports Vulkan ray tracing?
    answer: >-
      Immortalis GPUs such as Arm Immortalis-G715, Immortalis-G720, and Immortalis-G925 support
      ray tracing. Some Arm Mali G7‑series GPUs after Mali‑G715 may or may not support it, depending
      on the phone model. Vulkan uses the same ray tracing API on PC and mobile, so you can prototype
      on PC and deploy to Android.
  - question: Which Vulkan approach should I use to launch rays?
    answer: >-
      The path introduces two options: the ray tracing pipeline (VK_KHR_ray_tracing_pipeline)
      and ray queries. The ray tracing pipeline is a more driver‑managed approach with dedicated
      shader stages such as Ray Generation and Intersection. Choose the approach that best fits
      your renderer; the path covers them conceptually.
  - question: What acceleration structures will I build for ray tracing?
    answer: >-
      You will represent the scene using VK_KHR_acceleration_structure. These implementation‑defined,
      typically tree‑like structures accelerate intersection tests, and the API provides options
      to control topology and balancing. Constructing them is the first step before launching
      rays.
  - question: Are bindless materials required for the examples?
    answer: >-
      No. VK_EXT_descriptor_indexing (a core feature since Vulkan 1.2) is independent of ray tracing,
      but it simplifies accessing data for intersected objects by letting shaders index arrays
      of buffers and textures with dynamic, non‑uniform indices. It helps organize resources in
      lookup tables.
# END generated_summary_faq

author: Iago Calvo Lista

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
    - Immortalis
operatingsystems:
    - Android
tools_software_languages:
    - Vulkan


further_reading:
    - resource:
        title: "Arm GPU Best Practices Developer Guide: Ray Tracing"
        link: https://developer.arm.com/documentation/101897/latest/Ray-tracing
        type: documentation
    - resource:
        title: "Ray Tracing: delivering immersive gaming experiences on mobile (Vulkanised 2023)"
        link: https://www.youtube.com/watch?v=K19LttE67uQ
        # link: https://www.vulkan.org/user/pages/09.events/vulkanised-2023/vulkanised_2023_ray_tracing_delivering_immersive_gaming_experiences_on_mobile.pdf
        type: video
    - resource:
        title: "Realistic Graphics with Ray Tracing on Mobile (Vulkanised 2024)"
        link: https://www.youtube.com/watch?v=jJyHzkWXEfY
        # link: https://www.vulkan.org/user/pages/09.events/vulkanised-2024/vulkanised-2024-Iago-calvo-lista-arm-2.pdf
        type: video
    - resource:
        title: "Realistic Mobile Graphics with Optimized Ray Tracing (GDC 2024)"
        link: https://www.youtube.com/watch?v=OPLTK7RB7co
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

