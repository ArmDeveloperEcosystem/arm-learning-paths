---
title: Run Java applications on Google Axion processors

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to run their Java-based applications on Arm-based Google Axion processors in Google Cloud. Most Java applications will run on Axion with no changes needed, but there are optimizations that can help improve application performance on Axion.

learning_objectives: 
    - Create an Arm-based VM instance with Google Axion CPU
    - Deploy a Java application on Axion
    - Understand Arm performance for different JDK versions
    - Test common performance optimization flags

prerequisites:
    - A [Google Cloud](https://cloud.google.com/) account with access to Axion based instances (C4A).

author: Joe Stech

### Tags
skilllevels: Introductory
cloud_service_providers:
  - Google Cloud
subjects: Performance and Architecture
armips:
    - Neoverse V2
tools_software_languages:
    - Java
    - Google Axion
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Exploring JVM Tuning Flags
        link: https://www.baeldung.com/jvm-tuning-flags
        type: blog
    - resource:
        title: The java Command 
        link: https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
