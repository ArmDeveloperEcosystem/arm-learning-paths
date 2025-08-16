---
title: Tune network workloads on Arm bare-metal

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers who want to tune the performance of network workloads on Arm Neoverse-based bare-metal.

learning_objectives: 
    - Set up a benchmarking environment using Tomcat and wrk2
    - Baseline of optimal performance configuration before tuning
    - Tune network workloads performance with NIC queue
    - Tune network workloads performance with local NUMA
    - Tune network workloads performance with iommu.strict and iommu.passthrough

prerequisites:
    - Access to an Arm-based bare-metal running Ubuntu-24 (you can use a Grace) (for Tomcat)
    - Access to a x86-based bare-metal running Ubuntu-24 (you can use an any x86_64 bare-metal) (for wrk2)
    - Basic familiarity with Java applications
    - Basic familiarity with computer system, network communication, etc.

author: Ying Yu, Ker Liu, Rui Chang

### Tags
skilllevels: Advanced
subjects: Performance tuning
armips:
    - Neoverse
tools_software_languages:
    - Tomcat
    - wrk2
    - OpenJDK-21
operatingsystems:
    - Linux



further_reading:
  - resource:
      title: OpenJDK Wiki 
      link: https://wiki.openjdk.org/
      type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
