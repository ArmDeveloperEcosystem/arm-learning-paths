---
title: Analyze Java performance on Arm servers using flame graphs
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to analyze the performance of Java applications on Arm Neoverse-based servers using flame graphs.

learning_objectives: 
  - Set up a benchmarking environment using Tomcat and wrk2
  - Generate flame graphs using async-profiler
  - Generate flame graphs using a Java agent

prerequisites:
  - Access to both Arm-based and x86-based computers running Ubuntu (you can use cloud-based server instances)
  - Basic familiarity with Java applications and performance profiling using flame graphs

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
