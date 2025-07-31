---
title: Analyze Java Performance on Arm servers using FlameGraphs

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers looking to analyze the performance of their Java applications on the Arm Neoverse based servers using flame graphs. 

learning_objectives: 
    - How to set up tomcat benchmark environment
    - How to generate flame graphs for Java applications using async-profiler
    - How to generate flame graphs for Java applications using Java agent

prerequisites:
    - An Arm-based and x86 computer running Ubuntu. You can use a server instance from a cloud service provider of your choice.
    - Basic familiarity with Java applications and flame graphs

author: Ying Yu, Martin Ma

### Tags
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




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
