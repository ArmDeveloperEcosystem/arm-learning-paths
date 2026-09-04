---
title: Detect and resolve false sharing in Java

minutes_to_complete: 30

who_is_this_for: Java developers who need to understand sub-optimal multithreaded scaling caused by cache-line contention on multi-core Arm servers.

description: Build a Java false-sharing example, identify a contended cache line with JOL and Perf C2C, apply @Contended padding, and compare runtimes.

learning_objectives:
  - Explain why independent Java fields or objects can contend for one cache line
  - Inspect adjacent Java fields with JOL and record their sharing with Perf C2C
  - Identify a highly contended cache line in Perf C2C output
  - Apply @Contended, verify the padded layout, and compare repeated runtimes

prerequisites:
  - Access to an Arm Neoverse Linux system that exposes SPE to perf
  - Familiarity with compiling and running Java applications
  - A working Java runtime installed on the target machine
  - Permission to use perf on the target system

author:
  - John O'Hara

generate_summary_faq: true
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
      title: Attribute contended cache lines to Java heap objects
      link: /learning-paths/servers-and-cloud-computing/java-attribute-cache-lines/
      type: learning-path
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
