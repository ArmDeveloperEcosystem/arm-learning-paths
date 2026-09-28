---
title: Explore Thread Synchronization in the Arm memory model

minutes_to_complete: 150

who_is_this_for: This is an advanced topic for developers seeking practical ways to test thread synchronization approaches in the Arm memory model.

description: Test and validate thread synchronization approaches in the Arm memory model using Herd7, Litmus7, and Arm hardware with assembly snippets.

learning_objectives:
    - Test thread synchronization assembly snippets against the formal definition of the Arm memory model
    - Test thread synchronization assembly snippets on Arm hardware
    - Compare the results of different thread synchronization approaches 

prerequisites:
    - An understanding of memory consistency models (such as Sequential Consistency, Weak Ordering, Relaxed Consistency, and Processor Consistency).
    - An understanding of thread synchronization.
    - Familiarity with Arm assembly language, and the ability to find relevant information on Arm assembly instructions.
    - Familiarity with general-purpose registers.
    - Familiarity with memory barriers, including Acquire-Release Semantics.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:48:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2abd7ad08875d94c1d8ec0c42a76169447bbfb1dd5216eaf4995c97e481165d1
  summary_generated_at: '2026-09-28T19:48:28Z'
  summary_source_hash: 2abd7ad08875d94c1d8ec0c42a76169447bbfb1dd5216eaf4995c97e481165d1
  faq_generated_at: '2026-09-28T19:48:28Z'
  faq_source_hash: 2abd7ad08875d94c1d8ec0c42a76169447bbfb1dd5216eaf4995c97e481165d1
  summary: >-
    Examine thread synchronization on Arm systems with small concurrency litmus tests. You create
    an AArch64 MP-style test and use Herd7 to analyze outcomes allowed by the formal Arm memory
    model. You then run the same specification on Arm hardware with Litmus7 and compare observed
    behavior with the model. Along the way, you explore acquire-release ordering through `LDAR`
    and `STLR` examples.
  faqs:
  - question: Which architecture should I target when I write the litmus test?
    answer: >-
      Use AArch64 for the provided MP litmus test. Configure your tools and hardware runs for the
      same architecture.
  - question: What file do I need to create for the primer, and what should I put in it?
    answer: >-
      Create `test.litmus` and copy the abbreviated MP example. Preserve its thread and process
      blocks and variable declarations exactly as shown.
  - question: How do I know I’m ready to move from Herd7 to Litmus7 on hardware?
    answer: >-
      Run the test in Herd7 and review the outcomes permitted by the formal model. After you can
      reproduce and interpret them, run the same test with Litmus7 on Arm hardware to compare
      behavior.
  - question: Which instructions should I use to demonstrate acquire-release ordering in the examples?
    answer: >-
      Use `LDAR` for load-acquire and `STLR` for store-release. Compare the examples to see how
      these instructions enforce acquire-release ordering.
  - question: Can I explore other atomic instructions such as `CAS` or `SWP` here?
    answer: >-
      You’ll learn that these instructions are mandatory starting with Armv8.1, but you won’t
      explore them in detail. Use the additional resources to investigate them further.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Runbook
    - Herd7
    - Litmus7
    - Arm ISA

further_reading:
    - resource:
        title: Arm Architecture Reference Manual for A-profile architecture
        link: https://developer.arm.com/documentation/ddi0487/la
        type: documentation
    - resource:
        title: "Barriers, Learn the Architecture: Armv8-A Memory Systems."
        link: https://developer.arm.com/documentation/100941/0101/Barriers
        type: documentation
    - resource:
        title: Barrier Litmus Tests and Cookbook
        link: https://developer.arm.com/documentation/100941/0101/Barriers
        type: documentation
    - resource:
        title: diy7 documentation
        link: https://diy.inria.fr/doc/index.html
        type: documentation

weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
