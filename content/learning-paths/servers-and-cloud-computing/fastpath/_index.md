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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:50:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 978d3da8668e38758c138313c31809f3de5a8cefd1b7c2b47a536c0ee364b692
  summary_generated_at: '2026-06-02T03:48:10Z'
  summary_source_hash: 978d3da8668e38758c138313c31809f3de5a8cefd1b7c2b47a536c0ee364b692
  faq_generated_at: '2026-06-03T00:50:51Z'
  faq_source_hash: 978d3da8668e38758c138313c31809f3de5a8cefd1b7c2b47a536c0ee364b692
  summary: >-
    This advanced Learning Path guides you through building custom Linux kernels with tuxmake,
    provisioning Arm-based AWS EC2 instances, and benchmarking multiple kernel versions using
    Fastpath. You will set up three machines: a CPU-optimized kernel build host, a Fastpath host
    on Ubuntu 24.04 LTS to orchestrate testing, and a System Under Test (SUT) on Ubuntu 24.04
    LTS to run workloads. You will generate a YAML benchmark plan (plan.yaml), execute benchmarks,
    and analyze collected results to compare kernel performance across versions. Prerequisites
    include an AWS account with permissions to create EC2 instances and familiarity with basic
    Linux administration and SSH. The estimated time to complete is about 90 minutes.
  faqs:
  - question: What do I need before provisioning the EC2 instances?
    answer: >-
      You need an AWS account with permissions to create EC2 instances. The path assumes familiarity
      with basic Linux administration and SSH.
  - question: Which EC2 instance types and images are used for each role?
    answer: >-
      The example build host and SUT use AWS Graviton m6g.12xlarge instances. The Fastpath host
      is a separate EC2 instance using the Ubuntu 24.04 LTS (Arm) AMI, and the SUT also runs Ubuntu
      24.04 LTS; other instance details beyond these examples are not explicitly listed.
  - question: Can I use the AWS Management Console or the AWS CLI to create the instances?
    answer: >-
      You can use either the AWS Management Console or the AWS CLI to perform the EC2 instance
      creation steps. The Learning Path supports both approaches.
  - question: Where are kernels built and which tools are used?
    answer: >-
      Kernels are built on the kernel build host using tuxmake. The Learning Path then prepares
      those kernels for testing with Fastpath.
  - question: How do I generate and run the Fastpath benchmark plan, and what should I expect?
    answer: >-
      You use a provided helper script to generate a YAML plan (plan.yaml) that defines the SUT,
      kernels to deploy, and workloads to run. Executing the plan on the Fastpath host installs
      each kernel on the SUT, runs benchmarks, collects results, and enables you to compare performance
      across kernel versions; connectivity between the Fastpath host and SUT is validated during
      setup.
# END generated_summary_faq

author: Geremy Cohen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
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

