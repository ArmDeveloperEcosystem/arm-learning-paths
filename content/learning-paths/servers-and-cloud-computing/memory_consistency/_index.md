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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:28:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6aa61de638be961339d958345225d696ff2b83b8f9cab22bf956f9bf2d15c1aa
  summary_generated_at: '2026-06-02T04:22:41Z'
  summary_source_hash: 6aa61de638be961339d958345225d696ff2b83b8f9cab22bf956f9bf2d15c1aa
  faq_generated_at: '2026-06-03T01:28:34Z'
  faq_source_hash: 6aa61de638be961339d958345225d696ff2b83b8f9cab22bf956f9bf2d15c1aa
  summary: >-
    This advanced Learning Path guides you through testing and validating thread synchronization
    in the Arm memory model on Linux using Herd7, Litmus7, and Arm hardware. You will create and
    run litmus tests, including an abbreviated MP.litmus example, to compare formal model predictions
    against observed hardware behavior. The exercises focus on Arm ISA acquire-release semantics
    with LDAR and STLR, and show how to compare results from different synchronization approaches.
    The path is intended for developers with knowledge of memory consistency models, thread synchronization,
    Arm assembly, general-purpose registers, and memory barriers (including acquire-release semantics).
    No additional prerequisites are explicitly listed beyond these skills.
  faqs:
  - question: Do I need access to Arm hardware, and what operating system is used?
    answer: >-
      Yes, testing on Arm hardware is part of the Learning Path. The target operating system is
      Linux, and no specific hardware platform or distribution is explicitly listed.
  - question: Which tools should I use for modeling versus running on hardware?
    answer: >-
      Use Herd7 to test snippets against the formal definition of the Arm memory model, and Litmus7
      to run litmus tests on Arm hardware. A Runbook structures the steps; diy7 is referenced
      only in additional resources.
  - question: How do I start with a litmus test in this path?
    answer: >-
      Follow the Herd7 and Litmus7 primer to create the provided abbreviated MP.litmus example
      as test.litmus. Run it with Herd7 to confirm the syntax is correct and to produce results
      you can later compare with hardware runs.
  - question: Which Arm synchronization instructions are covered in the examples?
    answer: >-
      The path focuses on acquire-release ordering using LDAR (load-acquire) and STLR (store-release).
      Other atomic instructions like CAS, SWP, LDADD, and STADD are mentioned but are outside
      the scope of this Learning Path.
  - question: What results should I expect to compare when I finish?
    answer: >-
      You will compare the observed outcomes of different thread synchronization approaches between
      the formal model (Herd7) and runs on Arm hardware (Litmus7). Specific expected result values
      are not listed in the context.
# END generated_summary_faq

author: Julio Suarez

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

