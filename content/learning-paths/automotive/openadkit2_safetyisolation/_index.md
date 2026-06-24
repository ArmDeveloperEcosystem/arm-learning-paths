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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-24T15:35:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  summary_generated_at: '2026-06-24T15:35:59Z'
  summary_source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  faq_generated_at: '2026-06-24T15:35:59Z'
  faq_source_hash: 92a6dac2b1674a44cd623a0c8c3189b38438124a6067ed7ca776999ff1d8b5bf
  summary: >-
    In this Learning Path, you'll learn about prototyping safety‑critical isolation for autonomous
    driving workloads on Arm Neoverse by applying functional safety concepts, ISO 26262 and ASIL
    guidance, and a safety‑island architecture. You'll understand how to separate safety‑critical control
    logic from non‑safety functions, then connect components using a publish‑subscribe model (DDS/ROS
    2) within containerized deployments or across Arm‑based instances. You'll explore lifecycle
    practices aligned with the V‑model, including clear requirements, version control, impact
    analysis, and regression testing. By the end, you'll organize simulation components into
    isolated units with defined interfaces and documentation suitable for advancing ISO 26262‑oriented
    development on Arm Neoverse.
  faqs:
  - question: How do I decide which components belong on the safety island versus the general
      ECU?
    answer: >-
      Place time‑critical, safety‑relevant control logic (for example, braking or steering) on
      the safety island, and keep non‑critical features (such as infotainment) on the general
      ECU. The goal is strong isolation, determinism, and minimized coupling for safety‑critical
      paths.
  - question: What should I verify to confirm the isolation boundaries are defined correctly?
    answer: >-
      Check that safety‑critical components run independently from non‑critical services and communicate
      only through defined publish‑subscribe interfaces. Ensure data exchanged is minimal and
      purpose‑specific so that safety logic is not impacted by unrelated functions.
  - question: How do ISO 26262 ASIL levels influence my development workflow in this prototype?
    answer: >-
      Higher ASIL targets require more rigorous processes and evidence across the V‑model. For
      example, ASIL‑D changes go through full impact analysis and regression testing to prevent
      introducing new risks.
  - question: Should I separate components using containers on one host or across multiple Arm
      Neoverse instances?
    answer: >-
      Both approaches support prototyping: containers model software isolation on one system,
      while multiple instances model stronger physical separation. Choose the option that best
      matches the isolation assumptions you want to evaluate.
  - question: What artifacts should I capture to support ISO 26262 traceability in this prototype?
    answer: >-
      Maintain clear safety requirements, rationale for the safety‑island split, defined DDS/ROS
      2 interfaces, and mapped tests to requirements. Record versioned changes, impact analyses,
      and verification results aligned to the V‑model stages.
# END generated_summary_faq

author: 
    - Odin Shen
    - Julien Jayat

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

