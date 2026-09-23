---
title: Understand Opacity Micromaps and hardware OMM on Arm Mali G2

description: Learn how OMM stores opacity data, follow that data from baking to ray traversal, and understand hardware OMM on Arm Mali G2.

minutes_to_complete: 30

who_is_this_for: Use this Learning Path if you develop game graphics and want to understand Opacity Micromaps and hardware OMM on Arm Mali G2.

learning_objectives:
    - Explain why alpha-tested geometry can require extra opacity work during ray traversal.
    - Describe microtriangles, subdivision levels, and the OMM opacity states.
    - Trace OMM data from authoring and baking through triangle links and acceleration-structure traversal.
    - Explain how Arm Mali G2 hardware OMM handles opacity decisions during ray traversal.
    - Identify the API, driver, engine, and content conditions required to use OMM.
    - Recognize OMM tradeoffs and distinguish it from general transparency acceleration.

prerequisites:
    - Basic familiarity with triangle geometry and alpha-tested materials
    - Basic familiarity with ray tracing intersections and acceleration structures

author: Patrick Wang

### Tags
skilllevels: Introductory
subjects: Gaming
armips:
    - Mali
tools_software_languages:
    - Vulkan
operatingsystems:
    - Any

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
        title: VK_KHR_opacity_micromap proposal
        link: https://docs.vulkan.org/features/latest/features/proposals/VK_KHR_opacity_micromap.html
        type: documentation
    - resource:
        title: NVIDIA Opacity MicroMap SDK
        link: https://github.com/NVIDIA-RTX/OMM
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
