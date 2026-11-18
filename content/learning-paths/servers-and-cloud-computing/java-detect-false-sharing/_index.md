---
title: Detect and resolve false sharing in Java on Arm Neoverse

minutes_to_complete: 30

who_is_this_for: Java developers who need to understand sub-optimal multithreaded scaling caused by cache-line contention on multi-core Arm servers.

description: Build a Java false-sharing example, identify a contended cache line with JOL and Perf C2C, apply @Contended padding, and compare runtimes.

learning_objectives:
  - Identify why independent Java fields or objects can contend for one cache line.
  - Inspect adjacent Java fields with Java Object Layout (JOL) and record their sharing with Perf C2C.
  - Identify a highly contended cache line in Perf C2C output.
  - Apply @Contended, verify the padded layout, and compare repeated runtimes.

prerequisites:
  - Access to an Arm Neoverse-based Linux system with Arm Statistical Profiling Extension (SPE) enabled and exposed to Perf
  - Familiarity with compiling and running Java applications
  - Permission to use Perf on the target system

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-22T15:35:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a7d9ee57f6fed816df5d122b1e51d0aeb7e7f4190b7ef5e01d110a16c5cf566f
  summary_generated_at: '2026-09-22T15:35:52Z'
  summary_source_hash: a7d9ee57f6fed816df5d122b1e51d0aeb7e7f4190b7ef5e01d110a16c5cf566f
  faq_generated_at: '2026-09-22T15:35:52Z'
  faq_source_hash: a7d9ee57f6fed816df5d122b1e51d0aeb7e7f4190b7ef5e01d110a16c5cf566f
  summary: >-
    You'll detect and mitigate Java false sharing on Arm Neoverse with JOL, Perf C2C, SPE, and HotSpot's
    `@Contended` padding. First, you'll learn how independent fields can contend for one cache line. Then, you'll build the baseline, inspect its layout, and record it. Next, you'll identify the highest-ranked
    shared line, add padding, and compare the reports. Finally, you'll collect repeated timing pairs to
    assess runtime impact and measurement variability.
  faqs:
  - question: How do I know Arm SPE is available to Perf before I start profiling?
    answer: >-
      Run the `/sys/bus/event_source/devices` check from the profiling instructions and confirm that
      it lists at least one SPE performance monitoring unit, usually `arm_spe_0`. If you get no output,
      follow the [SPE enablement instructions](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/) and repeat the check before you run `perf c2c record`.
  - question: Which Java binaries should I use to compile and run the example?
    answer: >-
      Resolve the absolute path to the Java executable and derive the matching `javac` from the
      same Java Development Kit (JDK). Use the same terminal so that compiler and runtime versions stay consistent across
      steps.
  - question: What should I look for in the Perf C2C report to find the strongest candidate cache line?
    answer: >-
      Confirm that the report is sorted by `Peer Snoop`, then inspect the line with the largest absolute
      peer-snoop count. Look for accesses from two or more CPUs, repeated loads and stores at offsets
      within the line, and activity while `left-writer` and `right-writer` run. Treat the line as a
      candidate because Perf C2C alone can't prove that its address belongs to `BaselineCounters`.
  - question: How do I confirm that @Contended padding is active?
    answer: >-
      Compile with the required package export, and run the padded mode and JOL with `-XX:-RestrictContended`.
      In the JOL output, verify that padding separates `left` and `right` into different contention
      groups. Keep `-XX:-RestrictContended` on every padded run because HotSpot otherwise ignores this
      application annotation.
  - question: What result should I expect when comparing baseline and padded modes?
    answer: >-
      Expect the padded mode to show lower absolute peer-hit counts and often a lower median worker-phase
      runtime than the baseline. Don't expect the representative values to match your system. Collect
      several alternating pairs, compare their medians, and examine variability before you conclude that
      padding helped. Also weigh any runtime improvement against the larger object size.
# END generated_summary_faq

author:
  - John O'Hara

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: Performance and Architecture
armips:
  - Neoverse

tools_software_languages:
  - OpenJDK
  - Perf
  - Java Object Layout

operatingsystems:
  - Linux

further_reading:
  - resource:
      title: JEP 142 - Reduce cache contention on specified fields
      link: https://openjdk.org/jeps/142
      type: documentation
  - resource:
      title: OpenJDK Java Object Layout
      link: https://github.com/openjdk/jol
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
