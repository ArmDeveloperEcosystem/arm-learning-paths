---
title: Learn about Neoverse Non-cache PMU events using C and Assembly Language 

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software and hardware engineers to learn about why common non-cache PMU events occur.

learning_objectives: 
    - Describe common non-cache PMU events.
    - Understand why specific code triggers specific PMU events on the Neoverse N2 Core.
   
prerequisites:
    - Some familiarity with performance analysis.
    - The ability to read Arm assembly code.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:12:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 523ff99ccb8d13543f64839fa21040191d2a9ff7ce7c78fa590e8775fac754a6
  summary_generated_at: '2026-06-02T05:21:57Z'
  summary_source_hash: 523ff99ccb8d13543f64839fa21040191d2a9ff7ce7c78fa590e8775fac754a6
  faq_generated_at: '2026-06-03T02:12:45Z'
  faq_source_hash: 523ff99ccb8d13543f64839fa21040191d2a9ff7ce7c78fa590e8775fac754a6
  summary: >-
    This advanced Learning Path shows how to describe common non-cache PMU events and understand
    why specific C and Arm assembly sequences trigger them on the Arm Neoverse N2 core. You will
    run compact examples that exercise Topdown Methodology L1 metrics, TLB effectiveness and walks,
    and operation mix groups (SIMD, scalar floating point, integer, branch, load, store), then
    examine the resulting PMU counts. The examples require a way to print to a console and can
    run in simulation or on hardware; on Linux you may see slight variations due to OS overhead.
    Prerequisites are familiarity with performance analysis and the ability to read Arm assembly.
    Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You should be comfortable with performance analysis and able to read Arm assembly. You also
      need an environment that can print to a console (printf support) to view event counts.
  - question: Which execution environment should I use for the code?
    answer: >-
      You can use any simulation environment or hardware with printf support. The provided examples
      were run bare-metal in EL3; running under Linux is also possible but may introduce slight
      variations in PMU counts.
  - question: How do I know the ITLB-related events were exercised correctly?
    answer: >-
      The ITLB example uses self-modifying code to execute an instruction from a previously unaccessed
      address, causing an ITLB miss and walk. After running it, check that counts for events such
      as PMU_EVENT_L1I_TLB, PMU_EVENT_L1I_TLB_REFILL, PMU_EVENT_L2D_TLB, PMU_EVENT_L2D_TLB_REFILL,
      PMU_EVENT_ITLB_WALK, and PMU_EVENT_INST_RETIRED increase as expected.
  - question: What result should I expect from the SIMD operation mix example?
    answer: >-
      The example demonstrates SIMD activity and, in the provided run, produced counts like INST_SPEC
      = 12, ASE_SPEC = 1, and ASE_INST_SPEC = 3. Your values may differ slightly, especially if
      running under an operating system.
  - question: Where can I find the definitions and behavior of the PMU events used here?
    answer: >-
      Refer to the Arm Neoverse N2 PMU guide for event behavior details. Additional Neoverse core
      PMU guides are available on developer.arm.com.
# END generated_summary_faq

author: Johanna Skinnider

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
operatingsystems:
    - Linux
armips:
    - Neoverse
tools_software_languages:
    - C
    - Assembly
    - Runbook



further_reading:
    - resource:
        title: Arm Neoverse N2 PMU Guide
        link: https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en
        type: documentation
    - resource:
        title: Arm CPU Telemetry Solution Topdown Methodology Specification 
        link: https://developer.arm.com/documentation/109542/0100/?lang=en
        type: documentation
    - resource:
        title: Arm Neoverse N2 Core Telemetry Specification 
        link: https://developer.arm.com/documentation/109215/0200/?lang=en
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

