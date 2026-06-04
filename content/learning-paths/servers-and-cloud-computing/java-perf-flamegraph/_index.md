---
title: Analyze Java performance on Arm servers using flame graphs
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to analyze the performance of Java applications on Arm Neoverse-based servers using flame graphs.

description: Profile Java applications on Arm Neoverse servers using flame graphs generated with async-profiler and Java agents to identify performance bottlenecks.

learning_objectives: 
  - Set up a benchmarking environment using Tomcat and wrk2
  - Generate flame graphs using async-profiler
  - Generate flame graphs using a Java agent

prerequisites:
  - Access to both Arm-based and x86-based computers running Ubuntu (you can use cloud-based server instances)
  - Basic familiarity with Java applications and performance profiling using flame graphs

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:14:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 655180d91bb9b9cf571840b59d8943c1d2c73d8f8aea647db57dc2704ede3af8
  summary_generated_at: '2026-06-02T04:10:23Z'
  summary_source_hash: 655180d91bb9b9cf571840b59d8943c1d2c73d8f8aea647db57dc2704ede3af8
  faq_generated_at: '2026-06-03T01:14:15Z'
  faq_source_hash: 655180d91bb9b9cf571840b59d8943c1d2c73d8f8aea647db57dc2704ede3af8
  summary: >-
    Learn how to analyze Java application performance on Arm Neoverse-based Linux servers by benchmarking
    a Tomcat deployment and generating flame graphs. You will set up Apache Tomcat, drive HTTP
    load with wrk2, and profile on the same Arm machine using two approaches: async-profiler and
    a perf-based Java agent (libperf-jvmti) with the FlameGraph toolkit. The path uses OpenJDK
    21 and focuses on producing actionable flame graphs to help identify bottlenecks under load.
    Prerequisites include access to Arm- and x86-based Ubuntu systems (cloud instances are acceptable)
    and basic familiarity with Java applications and flame graph profiling. Estimated time to
    complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to both Arm-based and x86-based computers running Ubuntu (cloud instances
      are acceptable) and basic familiarity with Java applications and flame-graph-based profiling.
      The path uses OpenJDK 21, Apache Tomcat, async-profiler, FlameGraph, and wrk2.
  - question: Can I perform the steps on an x86 server?
    answer: >-
      The procedures target an Arm Neoverse-based Linux server for profiling. Access to an x86
      Ubuntu system is listed as a prerequisite, but the profiling steps in this path are executed
      on the Arm machine.
  - question: Where should I run async-profiler relative to Tomcat?
    answer: >-
      Install and run async-profiler on the same Arm-based Linux machine where Tomcat is running
      to ensure accurate profiling.
  - question: How are flame graphs generated with the Java agent approach?
    answer: >-
      Configure Tomcat to load the libperf-jvmti.so JVMTI agent so perf can record stacks with
      Java method names, then use the FlameGraph toolkit to build the flame graph. This complements
      the async-profiler method provided earlier in the path.
  - question: Do I need to generate load during profiling, and how should I do that?
    answer: >-
      Yes. The path sets up a Tomcat benchmark and uses wrk2 to simulate HTTP load while you collect
      profiles, so the flame graphs reflect realistic request handling.
# END generated_summary_faq

author: 
  - Ying Yu
  - Martin Ma

# Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Neoverse

tools_software_languages:
  - OpenJDK 21
  - Apache Tomcat
  - async-profiler
  - FlameGraph
  - wrk2

operatingsystems:
  - Linux

further_reading:
  - resource:
      title: OpenJDK Wiki 
      link: https://wiki.openjdk.org/
      type: documentation
  - resource:
      title: Java FlameGraphs
      link: https://www.brendangregg.com/flamegraphs.html
      type: website

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

