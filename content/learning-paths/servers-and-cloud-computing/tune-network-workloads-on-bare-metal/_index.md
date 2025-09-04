---
title: Tune network workloads on Arm-based bare-metal instances

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers who want to tune the performance of network workloads on Arm Neoverse-based bare-metal instances.

learning_objectives: 
    - Set up a benchmarking environment using Apache Tomcat and wrk2 on an Arm Neoverse bare‑metal host
    - Establish a reproducible baseline performance configuration (throughput and latency) before tuning
    - Tune NIC multi‑queue, RSS/RPS/XPS, and IRQ affinity to increase throughput and stabilize latency
    - Optimize NUMA locality by pinning Tomcat workers and interrupts to local CPUs and memory
    - Evaluate IOMMU configuration options and select the setting that maximizes networking performance

prerequisites:
    - An Arm Neoverse-based bare-metal server running Ubuntu 24.04 to run Apache Tomcat (this Learning Path was tested with an AWS c8g.metal-48xl instance)
    - Access to an x86_64 bare-metal server running Ubuntu 24.04 to run wrk2
    - Basic familiarity with Java applications

author: Ying Yu, Ker Liu, Rui Chang

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Tomcat
    - wrk2
    - OpenJDK 21
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: OpenJDK Wiki 
      link: https://wiki.openjdk.org/
      type: documentation

  - resource:
      title: Apache Tomcat documentation
      link: https://tomcat.apache.org/tomcat-11.0-doc/index.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
