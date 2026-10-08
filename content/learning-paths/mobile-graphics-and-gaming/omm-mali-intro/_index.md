---
title: Evaluate Opacity Micromaps for ray-traced game assets

draft: true
cascade:
    draft: true
    
description: Evaluate an alpha-tested asset for Opacity Micromaps on Arm Mali G2-Ultra NX, then choose an OMM strategy, fallback, and validation plan.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for game graphics developers who need to evaluate whether an alpha-tested asset is suitable for Opacity Micromaps (OMM) on Arm Mali G2-Ultra NX. You can complete the Learning Path without OMM-capable hardware.

learning_objectives:
    - Classify microtriangles as opaque, transparent, or unknown from alpha-mask data.
    - Trace OMM data from baking through acceleration-structure traversal.
    - Choose an OMM format, subdivision strategy, fallback, and validation plan for an asset.
    - Identify the Vulkan enablement requirements for ray pipelines and ray queries.

prerequisites:
    - Basic familiarity with triangle geometry and alpha-tested materials
    - Basic familiarity with ray tracing intersections and acceleration structures
    - (Optional) An Arm Mali G2-Ultra NX device and Vulkan capability tools for device validation

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-08T20:44:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 62c0dbe8121bd0ff6d93cb862a5cf5235782b0f2c6e598a19ce9931bac366354
  summary_generated_at: '2026-10-08T20:44:15Z'
  summary_source_hash: 62c0dbe8121bd0ff6d93cb862a5cf5235782b0f2c6e598a19ce9931bac366354
  faq_generated_at: '2026-10-08T20:44:15Z'
  faq_source_hash: 62c0dbe8121bd0ff6d93cb862a5cf5235782b0f2c6e598a19ce9931bac366354
  summary: >-
    You'll evaluate whether an alpha-tested asset can benefit from OMM on Arm
    Mali G2-Ultra NX. First, you'll identify a suitable asset, classify microtriangle opacity states, and
    choose a format and subdivision level. Then, you'll trace baked data through Vulkan resource and
    acceleration-structure setup. You'll enable the appropriate traversal path and define an alpha-tested
    fallback. Finally, you'll compare image and runtime evidence to record an adoption decision.
  faqs:
  - question: Why should I use OMM for ray-traced assets?
    answer: >-
      Use OMM to let ray traversal resolve known opaque and transparent
      regions of an alpha-tested asset. With OMM, you can reduce repeated shader-side opacity checks when
      rays pass through assets such as foliage or fences.
  - question: What kinds of assets should I evaluate for OMM?
    answer: >-
      Start with alpha-tested assets that participate in ray tracing, have stable opacity masks,
      and receive repeated ray hits. You'll need an update policy for changing masks, while
      alpha-blended and rasterization-only assets belong on their existing paths.
  - question: Do I need OMM-capable hardware to complete this Learning Path?
    answer: >-
      No. You can work through asset decision and validation with the provided bake
      results and saved device capability report. If you have an Arm Mali G2-Ultra NX device,
      you can compare its reported capabilities with your chosen OMM strategy.
  - question: Will OMM change the geometry of my asset?
    answer: >-
      No. You keep the original mesh triangles and use OMM to describe opacity in smaller regions
      within them. You don't add polygons to the source model.
  - question: How do I know whether an OMM strategy is suitable for my asset?
    answer: >-
      Compare image quality with and without OMM, then check the asset's data cost and remaining
      shader-side work against your goals. You can use the Learning Path's sample evidence to
      practice that decision before testing it in your own renderer.
# END generated_summary_faq

author: Patrick Wang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
tools_software_languages:
    - Vulkan
operatingsystems:
    - Android

further_reading:
    - resource:
        title: VK_KHR_opacity_micromap
        link: https://registry.khronos.org/vulkan/specs/latest/man/html/VK_KHR_opacity_micromap.html
        type: documentation
    - resource:
        title: Vulkan opacity micromap chapter
        link: https://docs.vulkan.org/spec/latest/chapters/VK_KHR_opacity_micromap/micromaps.html
        type: documentation
    - resource:
        title: SPV_KHR_opacity_micromap
        link: https://github.khronos.org/SPIRV-Registry/extensions/KHR/SPV_KHR_opacity_micromap.html
        type: documentation
    - resource:
        title: GLSL opacity micromap ray query mode
        link: https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_opacity_micromap_ray_query_mode.txt
        type: documentation
    - resource:
        title: Arm Mali G2-Ultra NX
        link: https://www.arm.com/products/silicon-ip-multimedia/gpu/mali-g2-ultra-nx
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
