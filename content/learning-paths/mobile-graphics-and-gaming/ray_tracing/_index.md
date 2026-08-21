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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:26:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6895a7653dc7811c0cc58ebbac2d79a4b7408fb265ec98b20fcc7f28fff40b44
  summary_generated_at: '2026-08-21T17:26:44Z'
  summary_source_hash: 6895a7653dc7811c0cc58ebbac2d79a4b7408fb265ec98b20fcc7f28fff40b44
  faq_generated_at: '2026-08-21T17:26:44Z'
  faq_source_hash: 6895a7653dc7811c0cc58ebbac2d79a4b7408fb265ec98b20fcc7f28fff40b44
  summary: >-
    You'll add Vulkan ray tracing effects to an Android renderer. First, you'll query and enable the required
    extensions, then use a ray tracing pipeline or ray queries to traverse the scene. After that, you'll build
    acceleration structures and use bindless resources for material data. Finally, you'll implement reflections,
    shadows, and refractions, and use Arm tools to debug and optimize ray traversal.
  faqs:
  - question: How do I know my Android device can run the ray tracing steps?
    answer: >-
      Confirm that the device exposes the required Vulkan ray tracing extensions. Immortalis GPUs
      such as Immortalis‑G715, Immortalis‑G720, and Immortalis‑G925 support ray tracing, while
      some Mali G7‑series GPUs after Mali‑G715 might or might not depending on the phone model.
  - question: 'Which ray traversal option should I use: ray tracing pipeline or ray query?'
    answer: >-
      Use `VK_KHR_ray_query` for most simple effects because it lets you add traversal to existing
      shaders, and the source recommends it for simple examples. Use `VK_KHR_ray_tracing_pipeline`
      when you need its dedicated ray-tracing shader stages and driver-managed traversal.
  - question: What should exist after I build the acceleration structure?
    answer: >-
      After you build an acceleration structure, use it to represent scene geometry for fast
      ray-intersection tests. Vulkan exposes it through `VK_KHR_acceleration_structure`; the
      implementation is opaque but typically tree-like.
  - question: Do I need bindless materials to implement ray tracing effects?
    answer: >-
      No. `VK_EXT_descriptor_indexing` is independent of ray tracing. Use it when you need shaders
      to dynamically index arrays of buffers and textures, such as when accessing material data for ray hits.
  - question: Can I prototype the effects on a PC and then deploy to Android?
    answer: >-
      Yes. Vulkan uses the same API for ray tracing on PC and mobile, making it straightforward
      to implement and test effects on desktop and deploy them to supported Android devices. Porting
      existing ray tracing effects from PC to mobile should also be simple.
# END generated_summary_faq

author: Iago Calvo Lista

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
