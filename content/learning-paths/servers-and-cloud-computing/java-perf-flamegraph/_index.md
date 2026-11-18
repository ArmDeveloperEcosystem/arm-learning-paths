---
title: Analyze Java performance on Arm servers using flame graphs
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to analyze the performance of Java applications on Arm Neoverse-based servers using flame graphs.

description: Profile Java applications on Arm Neoverse servers using flame graphs generated with async-profiler and Java agents to identify performance bottlenecks.

learning_objectives: 
  - Set up a benchmarking environment using Tomcat and wrk2.
  - Generate flame graphs using async-profiler.
  - Generate flame graphs using a Java agent.

prerequisites:
  - Access to both Arm-based and x86-based computers running Ubuntu, or cloud-based server instances
  - Basic familiarity with Java applications and performance profiling using flame graphs

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:18:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9c0966884bee0b120d2e71878e7db5bca6a4ce9ab12429b6950fa97f0a4a41b9
  summary_generated_at: '2026-09-15T21:18:57Z'
  summary_source_hash: 9c0966884bee0b120d2e71878e7db5bca6a4ce9ab12429b6950fa97f0a4a41b9
  faq_generated_at: '2026-09-15T21:18:57Z'
  faq_source_hash: 9c0966884bee0b120d2e71878e7db5bca6a4ce9ab12429b6950fa97f0a4a41b9
  summary: >-
    You'll profile a Java HTTP workload on an Arm Neoverse server by applying repeatable load
    with Tomcat and `wrk2`. First, you'll capture CPU samples with `async-profiler` and generate a flame
    graph. Then, you'll profile with a Java Virtual Machine Tool Interface (JVMTI) agent and the FlameGraph toolkit. You'll compare both
    views to identify the methods and call stacks that dominate execution under load.
  faqs:
  - question: Which process ID should I target when running async-profiler?
    answer: >-
      Profile the Tomcat process. Use your system’s process listing to find the PID, and start
      profiling while `wrk2` is actively generating load.
  - question: Do I need to install async-profiler on the same machine as Tomcat?
    answer: >-
      Yes. Install and run `async-profiler` on the same Arm-based Linux machine where Tomcat is
      running to ensure accurate profiling.
  - question: Where should I run wrk2 to generate load?
    answer: >-
      Run `wrk2` from an `x86_64` Ubuntu client so that it sends HTTP requests to the Tomcat server that you're
      profiling. Confirm that you can reach the Tomcat endpoint before starting the benchmark.
  - question: How do I confirm that perf is capturing Java method names with the JVMTI agent?
    answer: >-
      Check that the profile output shows Java method names rather than raw memory addresses.
      If the output doesn't, verify that `libperf-jvmti.so` is present and loaded by the JVM.
  - question: What should I look for in the generated flame graphs?
    answer: >-
      Open `profile.svg` in a browser to analyze the sampled profiling result from the benchmark. Expect a visualization of sampled stacks during the benchmark. The widest stacks indicate where time is spent, so that you can focus on the hottest Java methods and code paths.
# END generated_summary_faq

author: 
  - Ying Yu
  - Martin Ma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
