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

author: Patrick Wang

generate_summary_faq: true
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
