---
title: Benchmark Linux kernel performance on Arm servers with Fastpath
description: Learn how to build custom Linux kernels using tuxmake and Fastpath, then benchmark and compare kernel versions on Arm-based EC2 instances.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to benchmark and compare different Linux kernel versions on Arm servers.

learning_objectives:
    - Build custom Linux kernels for Arm systems using tuxmake and Fastpath
    - Configure and provision Arm-based EC2 instances for kernel testing
    - Create and execute test plans that compare kernel performance across versions
    - Analyze benchmark results to identify performance differences between kernels

prerequisites:
    - An AWS account with permissions to create EC2 instances
    - Familiarity with basic Linux administration and SSH

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:56:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a5c4bd873d7596fc2616e7a0f1d86f2a7bc3aa521e29c7f2bc7f033ca550cb9a
  summary_generated_at: '2026-09-10T21:56:23Z'
  summary_source_hash: a5c4bd873d7596fc2616e7a0f1d86f2a7bc3aa521e29c7f2bc7f033ca550cb9a
  faq_generated_at: '2026-09-10T21:56:23Z'
  faq_source_hash: a5c4bd873d7596fc2616e7a0f1d86f2a7bc3aa521e29c7f2bc7f033ca550cb9a
  summary: >-
    You'll build and benchmark Linux kernels on Arm-based Amazon EC2 instances using `tuxmake` and Fastpath. First, you'll provision a build host, Fastpath host, and system under test, then compile kernels and create a YAML benchmark plan. Fastpath installs each kernel, runs the selected workloads, and collects results so that you can compare kernel performance across versions.
  faqs:
  - question: Which EC2 instance type should I use for the kernel build host?
    answer: >-
      Use a CPU-optimized Graviton-based instance such as `m6g.12xlarge`.
  - question: Can I create the EC2 instances with the AWS console or do I need the CLI?
    answer: >-
      You can use either the AWS Management Console or the AWS CLI.
  - question: How do I know the SUT is ready for benchmarking?
    answer: >-
      Provision a Graviton-based instance running Ubuntu 24.04 LTS, configure the Fastpath software
      and user account, and validate connectivity from the Fastpath host. Proceed only
      when SSH access and required configuration are confirmed.
  - question: What does the Fastpath YAML plan include, and how is it created?
    answer: >-
      The plan defines the SUT, the kernels to deploy, and the benchmark workloads to run. The
      helper script `generate_plan.sh` gathers the required information and generates a valid `plan.yaml`.
  - question: How do I compare results between two kernels?
    answer: >-
      Use Fastpath's `result show` command with the results directory, both `--swprofile` values,
      and the `--relative` option. The output compares metrics such as the minimum, mean, maximum,
      confidence interval, coefficient of variation, and sample count for each kernel.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
  - AWS Graviton
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Fastpath
    - tuxmake
    - Linux

further_reading:
    - resource:
        title: Fastpath documentation
        link: https://fastpath.docs.arm.com/en/latest/index.html
        type: documentation
    - resource:
        title: Kernel install guide
        link: /learning-paths/servers-and-cloud-computing/kernel-build/
        type: guide
    - resource:
        title: AWS Compute Service Provider learning path
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: guide

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
