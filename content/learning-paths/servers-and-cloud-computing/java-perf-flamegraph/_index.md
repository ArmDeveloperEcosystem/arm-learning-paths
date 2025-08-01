---
title: Analyze Java Performance on Arm servers using FlameGraphs
minutes_to_complete: 30

who_is_this_for: "This is an introductory topic for software developers looking to analyze the performance of their Java applications on the Arm Neoverse based servers using flame graphs."

learning_objectives: 
  - Set up a Tomcat benchmarking environment
  - Generate flame graphs using async-profiler
  - Generate flame graphs using a Java agent

prerequisites:
  - "An Arm-based and x86 computer running Ubuntu. You can use a server instance from a cloud service provider of your choice."
  - Basic familiarity with Java applications and flame graphs

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
  - Async-profiler
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
