---
title: Explore thread synchronization in the Arm memory model

minutes_to_complete: 150

who_is_this_for: This is an advanced topic for developers seeking practical ways to test thread synchronization approaches in the Arm memory model.

description: Test and validate thread synchronization approaches in the Arm memory model using Herd7, Litmus7, and Arm hardware with assembly snippets.

learning_objectives:
    - Test thread synchronization assembly snippets against the formal definition of the Arm memory model.
    - Test thread synchronization assembly snippets on Arm hardware.
    - Compare the results of different thread synchronization approaches.

prerequisites:
    - An understanding of memory consistency models (such as sequential consistency, weak ordering, relaxed consistency, and processor consistency)
    - An understanding of thread synchronization
    - Familiarity with Arm assembly language, and the ability to find relevant information on Arm assembly instructions
    - Familiarity with general-purpose registers
    - Familiarity with memory barriers, including acquire and release semantics

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
    You'll examine thread synchronization on Arm systems with small concurrency litmus tests. First, you'll create
    an AArch64 MP-style test and use Herd7 to analyze outcomes allowed by the formal Arm memory
    model. You'll then run the same specification on Arm hardware with Litmus7 and compare observed
    behavior with the model. Along the way, you'll explore acquire-release ordering through `LDAR`
    and `STLR` examples.
  faqs:
  - question: Which architecture should I target when I write the litmus test?
    answer: >-
      Use AArch64 for the MP litmus test. Configure your tools and hardware runs for the
      same architecture.
  - question: Why might Litmus7 not observe an outcome that Herd7 permits?
    answer: >-
      Herd7 evaluates outcomes against the formal memory model, while Litmus7 runs the test on
      hardware. A compliant Arm CPU can exhibit stronger ordering than the formal model, and a
      finite run can miss rare outcomes. Increasing the iteration count improves your chances of
      observing rare outcomes but doesn't guarantee that every permitted outcome will occur.
  - question: How do I know I’m ready to move from Herd7 to Litmus7 on hardware?
    answer: >-
      Run the test in Herd7 and review the outcomes permitted by the formal model. After you can
      reproduce and interpret the outcomes, run the same test with Litmus7 on Arm hardware to compare
      behavior.
  - question: Which instructions should I use to demonstrate acquire-release ordering?
    answer: >-
      Use `LDAR` for load-acquire and `STLR` for store-release. Compare the examples to see how
      these instructions enforce acquire-release ordering.
  - question: How can I increase the chance of observing rare outcomes with Litmus7?
    answer: >-
      Increase the iteration count with the `-s` option. For example, run `litmus7 ./test.litmus
      -s 5000000` to execute five million iterations instead of the default one million.
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
