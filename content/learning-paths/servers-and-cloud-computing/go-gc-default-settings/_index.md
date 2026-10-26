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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:09:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8839edf689c26c8abe50094c0cfa62521b58a69c4e58a3f4c67b2e111e7d49e6
  summary_generated_at: '2026-09-10T22:09:54Z'
  summary_source_hash: 8839edf689c26c8abe50094c0cfa62521b58a69c4e58a3f4c67b2e111e7d49e6
  faq_generated_at: '2026-09-10T22:09:54Z'
  faq_source_hash: 8839edf689c26c8abe50094c0cfa62521b58a69c4e58a3f4c67b2e111e7d49e6
  summary: >-
    You'll establish a Go GC baseline on an AWS Graviton-based Arm server. First, you'll install Go and Benchstat and confirm default runtime settings. Then, you'll run a benchmark and collect allocation, pause, and GC metrics with CPU and heap profiles. You'll compare results with Benchstat before experimenting with GC behavior and measuring its impact.
  faqs:
  - question: How do I verify the instance and Go toolchain are Arm-based before benchmarking?
    answer: >-
      Run `go version` and check that it reports `linux/arm64`. Also run `go env GOOS GOARCH` and confirm
      `GOARCH` is `arm64`.
  - question: What should I check to keep the default Go GC baseline intact?
    answer: >-
      Confirm that `GOGC`, `GOMEMLIMIT`, `GODEBUG`, and `GOMAXPROCS` aren't set. Use `env | grep -E '^(GOGC|GOMEMLIMIT|GODEBUG|GOMAXPROCS)=' || true` and unset any variables that appear.
  - question: What result should I expect after the baseline benchmark run?
    answer: >-
      You should have a runtime snapshot (Go version, `GOOS/GOARCH`, CPU count, and memory) and raw
      benchmark output in `default_gc_benchmark.txt`. Run `benchstat default_gc_benchmark.txt` next to create the summary used to compare and interpret the baseline metrics.
  - question: How do I interpret the Benchstat metrics related to GC?
    answer: >-
      `ns/op` shows time per operation (lower is faster), `B/op` shows bytes allocated per operation,
      and `allocs/op` shows the number of allocations per operation—lower values generally reduce
      GC pressure. `gc/op` indicates how often GC cycles occur per operation. A lower `gc/op` means
      GC runs less frequently for the same work.
  - question: How do I capture CPU and heap profiles without changing GC behavior?
    answer: >-
      Leave `GOGC`, `GOMEMLIMIT`, `GODEBUG`, and `GOMAXPROCS` unset and run the benchmark using the profiling
      commands. The run writes CPU and heap profiles alongside the benchmark
      results while preserving default GC behavior.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
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
