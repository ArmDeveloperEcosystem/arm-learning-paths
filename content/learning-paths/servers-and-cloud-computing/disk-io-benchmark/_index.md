---
title: Microbenchmark Storage Performance with fio

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers seeking to optimize storage costs and performance, identify bottlenecks, and navigate storage considerations during application migration across platforms.

learning_objectives: 
    - Understand the flow of data for storage devices.
    - Use basic observability utilities such as iostat, iotop and pidstat.
    - Understand how to run fio for microbenchmarking a block storage device.

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an Arm Linux server.
    - Familiarity with Linux.

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - bash
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Fio documentation
        link: https://fio.readthedocs.io/en/latest/fio_doc.html#running-fio
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
