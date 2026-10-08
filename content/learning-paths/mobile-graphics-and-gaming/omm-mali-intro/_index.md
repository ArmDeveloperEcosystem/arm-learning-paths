---
title: Evaluate Opacity Micromaps for ray-traced game assets

draft: true
cascade:
    draft: true
    
description: Learn how Opacity Micromaps reduce opacity work during ray traversal, then choose an OMM strategy and fallback for an alpha-tested asset.

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
  - question: How do I know if my asset is a good candidate for OMM?
    answer: >-
      Look for an alpha-tested asset with a stable mask that receives repeated ray hits, such as
      static foliage or a fence. You also need to classify most of its opacity regions in advance.
      If much of the mask remains unknown, shader-side evaluation can limit the benefit.
  - question: How should I choose a subdivision level and state format?
    answer: >-
      Compare the alpha detail with the microtriangle grid and check the device's subdivision limits.
      You can use a 4-state format to leave difficult edges unknown for shader-side evaluation.
      Choose a 2-state format only if you can classify every region without changing the image.
  - question: What must I enable before my renderer traverses OMM-enabled geometry?
    answer: >-
      Check for `VK_KHR_opacity_micromap` and enable its `micromap` feature. Build and link the
      micromap to the matching triangles in the bottom-level acceleration structure. You must also
      enable OMM for your traversal path: use `VK_PIPELINE_CREATE_RAY_TRACING_OPACITY_MICROMAP_BIT_KHR`
      for a ray pipeline, or set `OpacityMicromapIdKHR` to `true` for ray queries.
  - question: What happens when a microtriangle has an unknown opacity state?
    answer: >-
      You retain shader-side opacity evaluation for the candidate hit. During normal 4-state
      traversal, you handle both unknown variants that way. Forcing 2-state evaluation with a ray
      or instance makes the variants behave differently. If OMM isn't supported, use your original
      alpha-tested path without OMM data.
  - question: How do I validate an OMM adoption decision?
    answer: >-
      Compare OMM-on, OMM-off, and reference images across shadows, reflections, levels of detail,
      and camera distances. You should also record device support, successful micromap and BLAS
      builds, triangle mapping, state ratios, and the active pipeline or shader control.
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
