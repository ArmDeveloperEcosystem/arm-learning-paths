---
title: Profile the Linux kernel with Arm Streamline

description: Learn how to profile Linux kernel modules using Arm Streamline to identify performance bottlenecks, analyze both out-of-tree and in-tree modules, and use Statistical Profiling Extension (SPE) for deeper insights.


minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers and performance engineers interested in profiling Linux kernel performance.

learning_objectives: 
    - Understand why profiling Linux kernel modules is important for performance and stability
    - Set up and use Arm Streamline to profile the Linux kernel
    - Profile both out-of-tree and in-tree kernel modules on Arm-based systems
    - Analyze profiling data to find and address performance bottlenecks
    - Use the Statistical Profiling Extension (SPE) for deeper kernel profiling insights

prerequisites:
    - Basic understanding of Linux kernel development and module programming
    - Arm-based Linux target device (such as a Raspberry Pi, BeagleBone, or similar board) with Secure Shell (SSH) access
    - A host machine that meets [Buildroot system requirements](https://buildroot.org/downloads/manual/manual.html#requirement)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:41:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0b8de63a15d3d77b9c9972103b1317d6c48907875ac625c3d1c1b8db5360879a
  summary_generated_at: '2026-06-01T21:53:04Z'
  summary_source_hash: 0b8de63a15d3d77b9c9972103b1317d6c48907875ac625c3d1c1b8db5360879a
  faq_generated_at: '2026-06-02T22:41:38Z'
  faq_source_hash: 0b8de63a15d3d77b9c9972103b1317d6c48907875ac625c3d1c1b8db5360879a
  summary: >-
    This advanced Learning Path shows how to profile Linux kernel modules on Arm-based systems
    using Arm Streamline, part of Arm Performance Studio. You will prepare a Buildroot-based environment,
    implement a simple cache-unfriendly character device as an out-of-tree module, and then integrate
    the same driver in-tree to profile with the kernel’s vmlinux for symbolized analysis. The
    path explains Streamline’s sampling workflow and introduces using Statistical Profiling Extension
    (SPE) for deeper kernel insights. Prerequisites include basic Linux kernel and module development
    knowledge, an Arm-based Linux target with SSH access, and a host machine that meets Buildroot
    requirements. Expect to analyze bottlenecks in both out-of-tree and in-tree scenarios in about
    60 minutes.
  faqs:
  - question: What do I need before running the steps on hardware?
    answer: >-
      You need an Arm-based Linux target device with SSH access and a host machine that meets
      the Buildroot system requirements. A basic understanding of Linux kernel development and
      module programming is also expected.
  - question: Which system should I use to install Buildroot prerequisites and run the build steps?
    answer: >-
      Use an AArch64-based Linux system as your host and run the package installation commands
      there. The setup step shows updating package lists and installing required dependencies
      before building.
  - question: How does the example kernel module create measurable behavior for profiling?
    answer: >-
      It traverses a two-dimensional array in column-major order to induce cache misses. This
      cache-unfriendly pattern helps expose hotspots and memory access inefficiencies in Streamline.
  - question: What should I add in Streamline to profile an in-tree driver with kernel symbols?
    answer: >-
      Add the kernel’s vmlinux file in the capture settings. This enables analysis of function
      calls, call paths, and specific kernel code sections for the in-tree build.
  - question: How is the Statistical Profiling Extension (SPE) used in this path?
    answer: >-
      SPE is introduced for deeper kernel profiling insights alongside Streamline’s sampling.
      Use it when available on your Arm-based system to expand the analysis beyond basic metrics.
# END generated_summary_faq

author: Yahya Abouelseoud

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Arm Streamline
    - Arm Performance Studio
    - Linux kernel
    - Performance analysis
operatingsystems:
    - Linux



further_reading:
    - resource:
        title: Streamline user guide 
        link: https://developer.arm.com/documentation/101816/latest/Capture-a-Streamline-profile/
        type: documentation
    - resource:
        title: Arm Performance Studio Downloads
        link: https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer#Downloads
        type: website
    - resource:
        title: Streamline video tutorial
        link: https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Arm%20Mali%20GPU%20Training%20-%20EP3-3
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

