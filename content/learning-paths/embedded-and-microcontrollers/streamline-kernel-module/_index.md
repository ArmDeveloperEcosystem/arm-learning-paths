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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:16Z'
  generator: template
  source_hash: 0b8de63a15d3d77b9c9972103b1317d6c48907875ac625c3d1c1b8db5360879a
  summary: >-
    Learn how to profile Linux kernel modules using Arm Streamline to identify performance bottlenecks,
    analyze both out-of-tree and in-tree modules, and use Statistical Profiling Extension (SPE)
    for deeper insights. It is designed for developers and performance engineers interested in
    profiling Linux kernel performance. By the end, you will be able to understand why profiling
    Linux kernel modules is important for performance and stability, set up and use Arm Streamline
    to profile the Linux kernel, and profile both out-of-tree and in-tree kernel modules on Arm-based
    systems. It focuses on tools and technologies such as Arm Streamline, Arm Performance Studio,
    Linux kernel, and Performance analysis, Linux environments, and Arm platforms including Cortex-A.
    The main steps cover Profile Linux kernel modules with Arm Streamline, Set up your environment,
    Build the out-of-tree kernel module, Profile the out-of-tree kernel module, and Integrate
    a custom character device driver into the Linux kernel.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand why profiling Linux kernel modules is important for performance and
      stability, set up and use Arm Streamline to profile the Linux kernel, and profile both out-of-tree
      and in-tree kernel modules on Arm-based systems. Learn how to profile Linux kernel modules
      using Arm Streamline to identify performance bottlenecks, analyze both out-of-tree and in-tree
      modules, and use Statistical Profiling Extension (SPE) for deeper insights.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers and performance engineers interested in profiling
      Linux kernel performance.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic understanding of Linux kernel
      development and module programming; Arm-based Linux target device (such as a Raspberry Pi,
      BeagleBone, or similar board) with Secure Shell (SSH) access; A host machine that meets
      [Buildroot system requirements](https://buildroot.org/downloads/manual/manual.html#requirement).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Streamline, Arm Performance Studio, Linux kernel,
      and Performance analysis, Linux environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Profile Linux kernel modules with Arm Streamline,
      Set up your environment, Build the out-of-tree kernel module, Profile the out-of-tree kernel
      module, and Integrate a custom character device driver into the Linux kernel.
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

