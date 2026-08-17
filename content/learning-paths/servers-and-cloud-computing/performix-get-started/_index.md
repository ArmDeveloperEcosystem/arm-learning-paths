---
title: Optimize a sample C++ application on an Arm-based server with Arm Performix

description: Profile and optimize a C++ application on Arm-based servers using Arm Performix recipes, CPU microarchitecture analysis, and Neon intrinsics.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for software developers and performance engineers who want to optimize applications on Arm-based servers using Arm Performix.

learning_objectives:
    - Configure Arm Performix and use its recipes to guide performance analysis on Arm-based systems
    - Profile a C++ application with the Code Hotspots recipe to identify functions consuming the most CPU time
    - Use CPU Microarchitecture and Instruction Mix recipes to pinpoint pipeline bottlenecks and missed SIMD opportunities
    - Optimize the application with Arm Neon intrinsics and compare Performix runs to validate changes in runtime and bottleneck behavior

prerequisites:
    - SSH access to an Arm Linux server with at least three Performance Monitor Unit (PMU) counters
    - Arm Performix installed on your local machine. For installation instructions, see the [Arm Performix install guide](/install-guides/performix).
    - A C++ compiler such as GCC or Clang installed on the target Linux server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T18:29:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 28f333bdf963818feb09d60bd23a0bbe95c449c41febaa668b1f942b448dfbaf
  summary_generated_at: '2026-08-17T18:29:05Z'
  summary_source_hash: 28f333bdf963818feb09d60bd23a0bbe95c449c41febaa668b1f942b448dfbaf
  faq_generated_at: '2026-08-17T18:29:05Z'
  faq_source_hash: 28f333bdf963818feb09d60bd23a0bbe95c449c41febaa668b1f942b448dfbaf
  summary: >-
    You'll configure Arm Performix, connect it to an Arm Linux target over SSH, and build a C++
    dot-product program. First, you'll use the **Code Hotspots**, **CPU Microarchitecture**, and **Instruction Mix**
    recipes to identify CPU bottlenecks and missed SIMD use in the baseline sample program. Then, you'll vectorize the hot loop with Arm Neon
    intrinsics, rebuild, and rerun the recipes. After rerunning the recipes, you'll compare runtime, hotspots, and pipeline behavior.
  faqs:
  - question: Which path should I use for my binary when I run a recipe?
    answer: >-
      Enter the path on the target system relative to the target user's home directory. For example,
      use a path such as `performix-analysis/dot_scalar`. If Performix can't start the binary, check
      the relative path and file permissions on the target.
  - question: What result should I expect from the Code Hotspots recipe?
    answer: >-
      You should see a list of functions ranked by CPU time. Use this view to choose which functions
      to inspect or optimize first.
  - question: How do I run the CPU Microarchitecture recipe with the same parameters as before?
    answer: >-
      Specify the same binary path and arguments you used previously, for example,
      `performix-analysis/dot_scalar 16777216 2000`. Then, run the recipe to get a Topdown breakdown
      of pipeline usage.
  - question: How do I know from the Instruction Mix recipe that my run is scalar-only?
    answer: >-
      Look for results dominated by scalar operations with no SIMD usage reported. This indicates
      missed vectorization opportunities.
  - question: After I add Neon intrinsics, what should I compare between runs?
    answer: >-
      Compare total runtime, changes in hotspot rankings, and shifts in the **CPU Microarchitecture**
      breakdown. In **Instruction Mix**, check for increased SIMD usage relative to the scalar run.
# END generated_summary_faq

author: 
    - Julie Gaskin

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Arm Performix
    - C++
    - GCC

further_reading:
    - resource:
        title: Install Arm Performix
        link: https://learn.arm.com/install-guides/performix
        type: documentation
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest/
        type: documentation
    - resource:
        title: Find Code hotspots with Arm Performix
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix
        type: website
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-microarchitecture
        type: website
    - resource:
        title: Generate Arm Performix AI insights in Visual Studio Code with Codex
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/
        type: website
        
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
