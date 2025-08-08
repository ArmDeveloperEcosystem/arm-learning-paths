---
title: Deploy Apache Spark on Google Axion C4A virtual machine

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for the software developers who are willing to migrate their Apache Spark workloads from the x86_64 platforms to Arm-based platforms, or on Google Axion-based C4A virtual machines specifically.  

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family, and RHEL 9 as the base image.
       - Understand how to install and configure Apache Spark on Arm-based GCP C4A instances.
       - Validate the functionality of spark through baseline testing.
       - Perform benchmarking to evaluate Apache Spark’s performance on Arm.

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled.
     - Basic understanding of Linux command line.
     - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/). 

author: Jason Andrews

##### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers: Google Cloud

armips:
    - Neoverse

tools_software_languages:
  - Apache Spark
  - Python

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Google Cloud official website and documentation
        link: https://cloud.google.com/docs
        type: documentation

    - resource:
        title: Spark official website and documentation
        link: https://spark.apache.org/
        type: documentation

    - resource:
        title: The Scala programming language official website
        link: scala-lang.org
        type: website


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
