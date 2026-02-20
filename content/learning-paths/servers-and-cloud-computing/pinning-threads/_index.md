---
title: Optimize application performance with CPU affinity

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, performance engineers, and system administrators looking to fine-tune the performance of their workload on many-core Arm-based systems.

learning_objectives: 
    - Pin threads to specific CPU cores using taskset and source code modifications
    - Measure cache performance improvements from thread pinning using perf
    - Evaluate performance trade-offs between throughput and latency consistency
    - Implement CPU affinity strategies for co-located workloads

prerequisites:
    - An Arm Linux system with four or more CPU cores
    - Experience with multi-threaded programming in C++ and Python
    - Understanding of build systems and computer architecture concepts
    - Familiarity with Linux command-line tools

author: Kieran Hejmadi

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - C++
    - Python
    - taskset
    - perf
    - Google Benchmark
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Taskset Manual  
        link: https://man7.org/linux/man-pages/man1/taskset.1.html
        type: documentation
    - resource:
        title: pthread_setaffinity_np Manual
        link: https://man7.org/linux/man-pages/man3/pthread_setaffinity_np.3.html
        type: documentation
    - resource:
        title: NUMA Deep Dive
        link: https://frankdenneman.nl/2016/07/07/numa-deep-dive-part-1-uma-numa/
        type: documentation
    - resource:
        title: Linux Scheduler Documentation
        link: https://www.kernel.org/doc/html/latest/scheduler/index.html
        type: documentation
    - resource:
        title: Get started with Arm-based cloud instances
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
