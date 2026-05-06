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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 6aa61de638be961339d958345225d696ff2b83b8f9cab22bf956f9bf2d15c1aa
  summary: >-
    Test and validate thread synchronization approaches in the Arm memory model using Herd7, Litmus7,
    and Arm hardware with assembly snippets. It is designed for developers seeking practical ways
    to test thread synchronization approaches in the Arm memory model. By the end, you will be
    able to test thread synchronization assembly snippets against the formal definition of the
    Arm memory model, test thread synchronization assembly snippets on Arm hardware, and compare
    the results of different thread synchronization approaches. It focuses on tools and technologies
    such as Runbook, Herd7, Litmus7, and Arm ISA, Linux environments, and Arm platforms including
    Neoverse. The main steps cover Thread Synchronization, Arm Memory Model, and Tools, Herd7
    and Litmus7 Test Primer, Thread Synchronization Examples, and Additional Resources.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will test thread synchronization assembly snippets against the formal definition of
      the Arm memory model, test thread synchronization assembly snippets on Arm hardware, and
      compare the results of different thread synchronization approaches. Test and validate thread
      synchronization approaches in the Arm memory model using Herd7, Litmus7, and Arm hardware
      with assembly snippets.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers seeking practical ways to test thread synchronization
      approaches in the Arm memory model.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An understanding of memory consistency
      models (such as Sequential Consistency, Weak Ordering, Relaxed Consistency, and Processor
      Consistency).; An understanding of thread synchronization.; Familiarity with Arm assembly
      language, and the ability to find relevant information on Arm assembly instructions.; Familiarity
      with general-purpose registers.; Familiarity with memory barriers, including Acquire-Release
      Semantics.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Runbook, Herd7, Litmus7, and Arm ISA, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Thread Synchronization, Arm Memory Model, and Tools,
      Herd7 and Litmus7 Test Primer, Thread Synchronization Examples, and Additional Resources.
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

