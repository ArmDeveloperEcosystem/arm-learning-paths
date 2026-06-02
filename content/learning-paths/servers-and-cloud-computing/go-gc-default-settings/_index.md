---
title: Measure Go GC behavior on AWS Graviton with default runtime settings
description: Learn how to run a Go allocation benchmark on AWS Graviton and measure garbage collection behavior without changing Go runtime settings.

minutes_to_complete: 75

who_is_this_for: This Learning Path is for Go developers and performance engineers who want to measure garbage collection behavior on Arm servers without changing Go runtime GC settings.

learning_objectives:
    - Select an AWS Graviton instance for repeatable Go GC measurements
    - Install Go and Benchstat on an Arm Linux server
    - Confirm that Go runtime tuning variables are unset
    - Run a Go benchmark that reports allocation, GC, and pause-time metrics
    - Capture CPU and heap profiles without changing GC behavior

prerequisites:
    - An [AWS account](https://aws.amazon.com/) with permission to launch AWS Graviton EC2 instances
    - The [AWS CLI](/install-guides/aws-cli/) installed and configured on your local machine
    - An AWS Graviton instance running Ubuntu 24.04 LTS or another Arm Linux distribution
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
    - AWS
    - Go
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

## Measure default Go GC behavior on Arm servers

Go applications can spend meaningful time allocating memory and running garbage collection (GC). You should measure that behavior before you change runtime settings.

In this Learning Path, you run Go benchmarks on an AWS Graviton instance and keep the Go runtime in its default GC mode. You do not set `GOGC`, `GOMEMLIMIT`, `GODEBUG`, or `GOMAXPROCS`.

The goal is to build a clean baseline. You will measure operation time, allocation rate, GC frequency, GC pause cost, and profiles before making tuning decisions.
