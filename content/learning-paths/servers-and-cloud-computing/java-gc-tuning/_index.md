---
title: Tune the performance of the Java garbage collector

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Java developers aiming to optimize application performance on Arm-based servers, especially those migrating applications from x86-based to Arm-based instances. 

description: Monitor, interpret, and optimize Java garbage collector (GC) performance on Arm servers by comparing different GCs and tuning parameters for your workload.

learning_objectives: 
    - Identify the key differences between individual Java GCs.
    - Monitor and interpret GC performance metrics.
    - Adjust core parameters to optimize performance for your specific workload.

prerequisites:
    - An Arm-based instance from a cloud service provider, or an on-premise Arm server
    - Basic understanding of Java
    - An [installation of Java](/install-guides/java/) on your machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:17:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4e044481e0de5cbc04512a181dd672f8ca753584abff4b43a6f3307980ecbc56
  summary_generated_at: '2026-09-15T21:17:09Z'
  summary_source_hash: 4e044481e0de5cbc04512a181dd672f8ca753584abff4b43a6f3307980ecbc56
  faq_generated_at: '2026-09-15T21:17:09Z'
  faq_source_hash: 4e044481e0de5cbc04512a181dd672f8ca753584abff4b43a6f3307980ecbc56
  summary: >-
    You'll evaluate and tune Java garbage collection on Arm-based servers. First, you'll verify your JDK
    and available collectors, run a compact heap-filling program, and compare common
    production GCs. Then, you'll also learn how to upgrade to a recent long-term-support (LTS) JDK before
    adjusting settings. By comparing application behavior across runs on cloud or
    on-premises Arm-based instances, you'll connect collector choices and configuration changes to
    workload needs.
  faqs:
  - question: How do I set up Java?
    answer: >-
      Install Java using the [Arm Java install guide](/install-guides/java/). After installation,
      run `java --version` to confirm it's available.
  - question: How do I check my JDK version and decide whether to upgrade?
    answer: >-
      Run `java --version` and review the reported release. Use one of the latest LTS JDKs because newer
      releases include GC improvements, such as G1GC pause time improvements from JDK 8 to JDK 11.
  - question: How can I monitor garbage collection while the Java program runs?
    answer: >-
      Run `jstat -gcutil $(pgrep java) 1000` in a second terminal while the example application runs.
      Review the `YGC`, `YGCT`, `FGC`, `FGCT`, and `GCT` columns to assess young, full, and total GC activity.
  - question: What should I expect when running the example application?
    answer: >-
      The program prints a startup message and then rapidly allocates many String objects to fill
      the heap. This makes GC behavior easier to observe so you can compare runs under different
      configurations.
  - question: How do I enable GC logging for the example application?
    answer: >-
      For JDK 11 and later, run `java -Xms512m -Xmx1024m -XX:+UseSerialGC -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java`.
      For JDK 8, use the `-Xloggc:gc.log`, `-XX:+PrintGCTimeStamps`, and `-XX:+UseGCLogFileRotation`
      options instead. Both commands create a `gc.log` file.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
