---
title: Learn about Neoverse Cache PMU Events using C and Assembly Language

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software and hardware engineers who want to learn about the causes of common Neoverse cache Performance Monitoring Unit (PMU) events.

learning_objectives: 
    - Describe common cache PMU events.
    - Describe why some code triggers PMU events on the Neoverse N2 core.
    - Describe the events triggered during common scenarios.

prerequisites:
    - Knowledge of performance analysis. 
    - The ability to read Arm assembly code.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:12:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1b309980bef983966d948036e309e132b56f767161967187e72c6a9f81f17dce
  summary_generated_at: '2026-06-02T05:21:26Z'
  summary_source_hash: 1b309980bef983966d948036e309e132b56f767161967187e72c6a9f81f17dce
  faq_generated_at: '2026-06-03T02:12:13Z'
  faq_source_hash: 1b309980bef983966d948036e309e132b56f767161967187e72c6a9f81f17dce
  summary: >-
    This advanced Learning Path shows how simple C and assembly code patterns trigger common cache
    Performance Monitoring Unit (PMU) events on Arm Neoverse, with a focus on the Neoverse N2
    core, in a Linux environment. You will review example snippets that issue stores to Normal
    Cacheable memory and see how they map to PMU metric groups for L1 data and instruction caches,
    the unified L2 cache, and the last-level (LL) cache. The steps explain why events such as
    L1D_CACHE_REFILL, L1D_CACHE, and INST_RETIRED are observed in common scenarios, and include
    example event counts to compare against. Prerequisites are knowledge of performance analysis
    and the ability to read Arm assembly. Estimated time to complete is 30 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You should be comfortable with performance analysis and able to read Arm assembly. The content
      targets Linux and focuses on the Neoverse N2 core. No other explicit prerequisites are listed.
  - question: Which PMU events are used to evaluate each cache level?
    answer: >-
      L1 Data Cache: PMU_EVENT_L1D_CACHE_REFILL, PMU_EVENT_L1D_CACHE, PMU_EVENT_INST_RETIRED.
      L1 Instruction Cache: PMU_EVENT_L1I_CACHE_REFILL, PMU_EVENT_L1I_CACHE, PMU_EVENT_INST_RETIRED,
      PMU_EVENT_INST_SPEC. L2 Unified Cache: PMU_EVENT_L2D_CACHE_REFILL, PMU_EVENT_L2D_CACHE,
      PMU_EVENT_L2D_CACHE_WR, PMU_EVENT_L2D_CACHE_RD, PMU_EVENT_L1D_CACHE_WR, PMU_EVENT_INST_RETIRED.
      LL Cache: PMU_EVENT_LL_CACHE_RD, PMU_EVENT_LL_CACHE_MISS_RD, PMU_EVENT_INST_RETIRED.
  - question: How do the code samples trigger the intended cache PMU events?
    answer: >-
      They execute stores to Normal Cacheable memory to allocate and access cache lines. To highlight
      L2 activity, the examples first fill the L1 D-cache with many stores; LL activity can appear
      when stores cause writebacks or involve shared cache lines.
  - question: How do I know if my run matched the expected behavior?
    answer: >-
      Compare your observed PMU event counts and relationships to the examples shown in the path.
      For instance, the L1 D-cache section provides example counts you can use as a reference.
  - question: What should I check if LL cache events remain low or zero?
    answer: >-
      LL cache activity is highlighted when excessive stores lead to writebacks into the LL cache
      or when there are shared cache lines. Ensure your workload issues enough stores, as illustrated,
      to overflow earlier cache levels and reach the LL cache.
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

