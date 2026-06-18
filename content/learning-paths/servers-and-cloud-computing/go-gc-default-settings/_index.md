---
title: Measure and modify Go garbage collection behavior on AWS Graviton-based compute

description: Learn how to run Go benchmarks on AWS Graviton-based compute, capture GC metrics and pprof profiles with Benchstat, establish a reproducible default garbage collection baseline for memory-intensive workloads on Arm, and experiment with modifying garbage collection behavior.

minutes_to_complete: 75

who_is_this_for: This Learning Path is for engineers interested in learning more about Go garbage collection (GC) behavior on Arm.

learning_objectives:
    - Select an AWS Graviton-based instance for repeatable Go GC measurements
    - Install Go and Benchstat on an Arm Linux server
    - Run a Go benchmark that reports allocation, GC, and pause-time metrics
    - Capture CPU and heap profiles without changing GC behavior
    - Interpret benchmarking results and experiment with changing GC behavior

prerequisites:
    - An [AWS account](https://aws.amazon.com/) with permission to launch an AWS Graviton-based Amazon EC2 instance running Ubuntu 24.04 LTS or another Arm Linux distribution
    - The [AWS CLI](/install-guides/aws-cli/) installed and configured on your local machine
    - Basic familiarity with Go benchmarks and Linux shell commands

author: Geremy Cohen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - Go
    - Benchstat
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Amazon EC2 M8g instances
        link: https://aws.amazon.com/ec2/instance-types/m8g/
        type: documentation
    - resource:
        title: Go GC guide
        link: https://go.dev/doc/gc-guide
        type: documentation
    - resource:
        title: Go runtime package
        link: https://pkg.go.dev/runtime
        type: documentation
    - resource:
        title: Go testing package
        link: https://pkg.go.dev/testing
        type: documentation
    - resource:
        title: Graviton Performance Runbook
        link: https://github.com/aws/aws-graviton-getting-started/blob/main/perfrunbook/README.md
        type: documentation
    - resource:
        title: Benchmark Go performance with Sweet and Benchstat
        link: /learning-paths/servers-and-cloud-computing/go-benchmarking-with-sweet/
        type: learning path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
