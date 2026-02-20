---
title: Deploy MongoDB on an Arm-based Google Axion C4A VM

minutes_to_complete: 15

who_is_this_for: This introductory topic is for software developers who want to migrate MongoDB workloads from x86_64 to Arm-based platforms, specifically on Google Axion-based C4A virtual machines.

learning_objectives:
  - Create an Arm virtual machine on Google Cloud (C4A Axion family)
  - Install and run MongoDB on the Arm-based C4A instance
  - Benchmark MongoDB performance with Yahoo Cloud Serving Benchmark (YCSB)

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
  - MongoDB
  - YCSB

operatingsystems:
    - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:
        title: YCSB
        link: https://github.com/brianfrankcooper/YCSB/wiki/
        type: documentation


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
