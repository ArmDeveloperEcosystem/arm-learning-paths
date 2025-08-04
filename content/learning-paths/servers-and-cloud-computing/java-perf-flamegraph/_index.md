---
title: Analyze Java Performance on Arm servers using FlameGraphs
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to analyze the performance of Java applications on the Arm Neoverse-based servers using FlameGraphs.

learning_objectives: 
  - Set up a benchmarking environment using Tomcat and wrk2
  - Generate FlameGraphs using async-profiler
  - Generate FlameGraphs using a Java agent

prerequisites:
  - Access to both Arm-based and x86-based computers running Ubuntu (you can use cloud-based server instances)
  - Basic familiarity with Java applications and performance profiling using FlameGraphs

author: 
  - Ying Yu
  - Martin Ma

# Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Neoverse

tools_software_languages:
  - OpenJDK-21
  - Tomcat
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
