---
title: Deploy MongoDB on Google Axion C4A virtual machine

minutes_to_complete: 60

who_is_this_for: This Learning Path is designed for software developers looking to migrate their MongoDB workloads from x86_64 to Arm-based platforms, specifically on Google Axion-based C4A virtual machines.

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family, and RHEL 9 as the base image.
       - Install and run MongoDB on an Arm-based GCP C4A instances.
       - Validate the functionality of MongoDB through baseline testing.
       - Benchmark the MongoDB performance on Arm using Yahoo Cloud Serving Benchmark (YCSB).

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled.
     - Basic understanding of Linux command line.
     - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms.

author: Jason Andrews

##### Tags
skilllevels: Advanced
subjects: Databases
cloud_service_providers: Google Cloud

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
