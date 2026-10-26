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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:51:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f49cbccc2416679aa309c396a4ef464936d05941c403b2a46f064d048e8b131e
  summary_generated_at: '2026-08-13T18:51:05Z'
  summary_source_hash: f49cbccc2416679aa309c396a4ef464936d05941c403b2a46f064d048e8b131e
  faq_generated_at: '2026-08-13T18:51:05Z'
  faq_source_hash: f49cbccc2416679aa309c396a4ef464936d05941c403b2a46f064d048e8b131e
  summary: >-
    You'll profile Linux kernel code on an Arm-based system with Arm Streamline. First, you'll build
    and exercise a cache-unfriendly out-of-tree character-device module, then inspect CPU, cycle, memory,
    and cache metrics. Next, you'll profile the driver in-tree with `vmlinux` symbols and, on supported
    targets, use SPE for deeper kernel analysis.
  faqs:
  - question: Which file should I add in Streamline to analyze an in-tree driver?
    answer: >-
      Add the kernel's `vmlinux` file in the capture settings. Doing so enables analysis of function
      calls, call paths, and specific kernel code sections.
  - question: How do I know Streamline is capturing my out-of-tree module?
    answer: >-
      During the workload, expect samples attributed to your module’s functions. You should also
      see changes in metrics such as memory access and cache misses while the device is exercised.
  - question: What result should I expect when profiling the cache‑unfriendly module?
    answer: >-
      Streamline should show sampling activity during the device operations and elevated cache‑related
      metrics due to the column‑major traversal. Use these indicators to locate hotspots and costly
      memory access patterns.
  - question: Do I need to install the Buildroot dependencies on an AArch64 host?
    answer: >-
      Yes. Run the package installation on an AArch64-based Linux system
      before building.
  - question: When should I enable SPE in this workflow?
    answer: >-
      Use SPE when deeper kernel profiling insights are needed beyond regular sampling. The Learning Path
      introduces SPE on supported targets to extend kernel execution analysis.
# END generated_summary_faq

author: Yahya Abouelseoud

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
