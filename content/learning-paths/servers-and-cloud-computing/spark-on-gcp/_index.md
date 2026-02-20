---
title: Deploy Apache Spark on Google Axion processors
   
minutes_to_complete: 60

who_is_this_for: This introductory topic is for software developers interested in migrating their Apache Spark workloads from x86_64 platforms to Arm-based platforms, specifically on Google Axion–based C4A virtual machines.  

learning_objectives:
  - Start an Arm virtual machine on Google Cloud Platform (GCP) using the C4A Google Axion instance family with RHEL 9 as the base image
  - Install and configure Apache Spark on Arm-based GCP C4A instances
  - Validate Spark functionality through baseline testing
  - Benchmark Apache Spark performance on Arm

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/)

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

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
      title: Google Cloud official documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Apache Spark documentation
      link: https://spark.apache.org/
      type: documentation

  - resource:
      title: Scala programming language official website
      link: https://scala-lang.org
      type: website

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


