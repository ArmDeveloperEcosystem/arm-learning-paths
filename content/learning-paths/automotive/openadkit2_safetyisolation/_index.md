---
title: Prototype safety-critical isolation for autonomous driving systems on Neoverse
description: Learn how to implement functional safety isolation for autonomous driving systems on Arm Neoverse using DDS-based communication, containerized deployment, and ISO 26262 compliance principles.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for automotive engineers developing safety-critical systems. You'll learn how to accelerate ISO 26262-compliant development workflows using Arm-based cloud compute, containerized simulation, and DDS-based communication.

learning_objectives: 
    - Apply functional safety principles, including risk prevention, fault detection, and ASIL compliance, to build robust, certifiable automotive systems
    - Use DDS and a publish-subscribe architecture for low-latency, scalable, and fault-tolerant communication in autonomous driving systems
    - Implement distributed development by separating the simulation platform into independent, safety-isolated components

prerequisites:
    - Access to two Arm-based Neoverse cloud instances, or a local Arm Neoverse Linux system with at least 16 CPUs and 32 GB of RAM
    - Completion of the [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/) Learning Path
    - Basic familiarity with Docker

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:27:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  summary_generated_at: '2026-06-01T20:57:59Z'
  summary_source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  faq_generated_at: '2026-06-02T21:27:35Z'
  faq_source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  summary: >-
    This advanced Learning Path shows automotive engineers how to prototype safety-critical isolation
    for autonomous driving workloads on Arm Neoverse running Linux. You apply ISO 26262 concepts
    (including ASIL and the V-model), use a safety island architectural approach, and separate
    a simulation platform into independent, safety-isolated components. Communication between
    components uses DDS in a publish-subscribe pattern, with containerized deployment and tooling
    that includes Docker, ROS 2, and Python. Prerequisites include two Arm-based Neoverse cloud
    instances or a local Arm Neoverse Linux system with at least 16 CPUs and 32 GB RAM, completion
    of the “Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse” Learning
    Path, and basic Docker familiarity. Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running this path?
    answer: >-
      You need either two Arm-based Neoverse cloud instances or a local Arm Neoverse Linux system
      with at least 16 CPUs and 32 GB of RAM. You must also have completed the “Deploy Open AD
      Kit containerized autonomous driving simulation on Arm Neoverse” Learning Path and be familiar
      with Docker.
  - question: Can I use a single local system instead of two cloud instances?
    answer: >-
      Yes. A local Arm Neoverse Linux system with at least 16 CPUs and 32 GB of RAM is listed
      as an alternative to two Arm-based Neoverse cloud instances.
  - question: Which technologies are used for communication and isolation?
    answer: >-
      The path uses DDS with a publish–subscribe architecture and containerized deployment to
      separate components and communicate between them. Tools referenced include Docker, ROS 2,
      DDS, and Python on Linux.
  - question: How are ISO 26262 and ASIL levels applied here?
    answer: >-
      The path introduces the ISO 26262 safety lifecycle aligned with the V-model and explains
      how ASIL levels guide design and testing. You apply prevention and detection principles
      and plan safe-state behavior as part of the workflow.
  - question: What result should I expect and how do I know I’m on track?
    answer: >-
      Expect to separate the simulation platform into independent, safety-isolated components
      that communicate via DDS. You should be able to describe a safety island architecture versus
      a non-safety ECU and relate requirements to verification activities consistent with ISO
      26262.
# END generated_summary_faq

author: 
    - Odin Shen
    - Julien Jayat

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - Python
    - Docker
    - ROS 2
    - DDS
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Functional Safety compute for the Software-defined Vehicle
        link: https://community.arm.com/arm-community-blogs/b/automotive-blog/posts/functional-safety-compute
        type: blog
    - resource:
        title: SOAFEE
        link: https://www.soafee.io/
        type: website
    - resource:
        title: V-model
        link: https://en.wikipedia.org/wiki/V-model
        type: documentation
    - resource:
        title: ISO 26262
        link: https://www.iso.org/standard/68383.html
        type: documentation
    - resource:
        title: Automotive Safety Integrity Level
        link: https://en.wikipedia.org/wiki/Automotive_Safety_Integrity_Level
        type: documentation
    - resource:
        title: What is Functional Safety?
        link: https://www.youtube.com/watch?v=R0CPzfYHdpQ
        type: video
    - resource:
        title: Eclipse Zenoh
        link: https://github.com/eclipse-zenoh/zenoh
        type: documentation
    - resource:
        title: Eclipse Cyclone DDS 
        link: https://github.com/eclipse-cyclonedds/cyclonedds
        type: documentation
    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

