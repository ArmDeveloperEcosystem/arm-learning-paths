---
title: Characterize system performance with Arm Performix

description: Learn how to run the Arm Performix System Characterization recipe to benchmark memory latency and bandwidth on Arm hardware and interpret the generated results.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers and performance engineers who want to characterize the hardware performance of Arm-based Linux systems using Arm Performix.

learning_objectives:
    - Run the Arm Performix System Characterization recipe to understand hardware configuration and performance.
    - Interpret memory latency and bandwidth benchmark results.
    - Locate and interpret the generated plots and raw benchmark data in the output directory.

prerequisites:
    - An Arm Linux target machine to characterize, that you can access using SSH

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:23:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7dd0078146532b90ffb079d1b792537c985ac343918bac46ad9c84a4f1967130
  summary_generated_at: '2026-11-18T20:23:22Z'
  summary_source_hash: 7dd0078146532b90ffb079d1b792537c985ac343918bac46ad9c84a4f1967130
  faq_generated_at: '2026-11-18T20:23:22Z'
  faq_source_hash: 7dd0078146532b90ffb079d1b792537c985ac343918bac46ad9c84a4f1967130
  summary: >-
    You'll characterize an Arm-based Linux system with the Arm Performix System Characterization
    recipe. First, you'll connect a target and choose default, static, or individual benchmarks.
    Then, you'll install collection tools if needed and run the recipe. Finally, you'll review memory
    latency and bandwidth in Performix, and inspect generated plots and data files.
  faqs:
  - question: Which benchmark option should I choose when running System Characterization?
    answer: >-
      Use the default set for a broad overview. Choose the static configuration option to gather
      only system details. Select individual benchmarks if you want to target specific tests.
  - question: What should I do on a first run if the target isn't ready for collection?
    answer: >-
      Select **Install Tools** in the Performix interface to copy the collection tools to the
      target. After the tools are installed, start the run again.
  - question: How do I know if the run completed, and where do I see results in Performix?
    answer: >-
      Check the **Summary** page and benchmark views for populated results. You can open the
      output directory from Performix to inspect generated files.
  - question: Where can I find the raw data and generated plots for my run?
    answer: >-
      On the **Summary** page, select **Open Run Directory**. You can inspect `.png` plots and
      `.json` files produced by the Arm System Characterization Tool.
  - question: What should I look for in the Idle latency view?
    answer: >-
      Use the **Idle latency** view to compare memory latency across NUMA nodes while the system
      is idle. Look for differences that can affect where you place a workload.
# END generated_summary_faq

author:
    - Brendan Long
    - David Wong

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - Arm System Characterization Tool
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Find CPU Cycle Hotspots with Arm Performix"
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: website
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
