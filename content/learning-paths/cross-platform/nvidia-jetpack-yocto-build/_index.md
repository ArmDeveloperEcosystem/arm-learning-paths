---
title: Build Nvidia Jetpack Yocto Images for Nvidia Orin NX/Orin Nano/Thor platforms
minutes_to_complete: 180 

description: Learn how to utilize the new yocto support in Nvidia Jetpack to build a custom linux image for the Jetson Orin NX, Orin Nano, and Thor platforms.

who_is_this_for: This is a moderately advanced topic for engineers who want to construct a highly customizable Jetpack image for the Jetson platforms via Yocto build processes. 

learning_objectives:
  - Learn about the Yocto custom linux distro creation process and platform
  - Utilize scripting to initiate a Yocto build for a give targeted Jetson platform
  - Flash and run the custom build on the Jetson platform


prerequisites:
  - Experience using Linux on embedded or SBC platforms
  - Experience with the Yocto build system
  - Experience with Nvidia Jetpack and the Jetson platforms (Orin NX, Orin Nano, and Thor)

author: Doug Anson

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
tools_software_languages: 
    - Yocto
    - C

cloud_service_providers:
  - AWS

armips:
  - Neoverse
  
operatingsystems:
  - Linux

shared_path: true
shared_between:
    - embedded-and-microcontrollers
    - automotive

further_reading:
  - resource:
      title: OE4T
      link: https://oe4t.github.io/master/
      type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
