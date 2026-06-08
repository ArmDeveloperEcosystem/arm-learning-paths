---
title: Tune the Performance of the Java Garbage Collector

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Java developers aiming to optimize application performance on Arm-based servers, especially those migrating applications from x86-based to Arm-based instances. 

description: Monitor, interpret, and optimize Java Garbage Collector performance on Arm servers by comparing different GCs and tuning parameters for your workload.

learning_objectives: 
    - Describe the key differences between individual Java Garbage Collectors (GCs)
    - Monitor and interpret Garbage Collector performance metrics
    - Adjust core parameters to optimize performance for your specific workload

prerequisites:
    - An Arm-based instance from a cloud service provider, or an on-premise Arm server.
    - Basic understanding of Java.
    - An [installation of Java](/install-guides/java/) on your machine.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:11:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f57dd99bad280f64f53071373519e2d3ba8ae50b94fe1ad0a9cc40d02b458b9b
  summary_generated_at: '2026-06-02T04:08:34Z'
  summary_source_hash: f57dd99bad280f64f53071373519e2d3ba8ae50b94fe1ad0a9cc40d02b458b9b
  faq_generated_at: '2026-06-03T01:11:10Z'
  faq_source_hash: f57dd99bad280f64f53071373519e2d3ba8ae50b94fe1ad0a9cc40d02b458b9b
  summary: >-
    Learn to monitor, interpret, and tune Java Garbage Collection on Arm-based Linux servers.
    Using an Arm instance on AWS, Microsoft Azure, Google Cloud, Oracle, or an on‑premise Arm
    server, you will verify your JDK with java --version, review the differences among commonly
    used production collectors, and run a small Java program that rapidly fills the heap to expose
    GC behavior. The path shows how to select a collector for your application and adjust core
    parameters, with guidance on updating to a recent LTS JDK. Prerequisites include basic Java
    knowledge and a working Java installation. Estimated time: 45 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an Arm-based instance from a cloud provider (or an on-premise Arm server), a basic
      understanding of Java, and a working Java installation. Linux is the target operating system.
  - question: How do I check which JDK version I am using?
    answer: >-
      Run the command: java --version. The output shows your JDK release and build details so
      you can proceed with the appropriate GC options.
  - question: How do I find which Garbage Collectors are available with my JDK?
    answer: >-
      Different JDK versions ship with different collectors, so first confirm your version with
      java --version. Then follow the identification step in the path to see which collectors
      your JDK includes.
  - question: How do I use the example application to observe GC behavior?
    answer: >-
      Create the provided HeapUsageExample.java file and run it to allocate a large number of
      objects and fill the heap. This makes GC activity easy to observe while you vary GC choices
      and tuning parameters.
  - question: What should I do if I’m on an older JDK release?
    answer: >-
      Update to a recent long-term-support JDK, because newer releases include GC improvements.
      Use java --version to verify the upgrade before repeating your measurements.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Java
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: OpenJDK Wiki 
        link: https://wiki.openjdk.org/
        type: documentation
    - resource:
        title: G1GC Tuning 
        link: https://www.oracle.com/technical-resources/articles/java/g1gc.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

