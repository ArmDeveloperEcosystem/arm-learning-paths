---
title: Migrate applications to Arm servers

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers looking to migrate applications to Arm servers.

description: Set up an Arm development environment, analyze dependencies, and understand common challenges and scenarios for migrating applications to Arm servers.

learning_objectives:
    - Set up an Arm development machine.
    - Analyze application dependencies.
    - Identify challenges and tips for application migration.
    - Understand common migration scenarios.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:49:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 22987fb68ce0a1aa0eee3b7fef785788245445837040dfaa67aeaa5d586c9554
  summary_generated_at: '2026-09-28T19:49:40Z'
  summary_source_hash: 22987fb68ce0a1aa0eee3b7fef785788245445837040dfaa67aeaa5d586c9554
  faq_generated_at: '2026-09-28T19:49:40Z'
  faq_source_hash: 22987fb68ce0a1aa0eee3b7fef785788245445837040dfaa67aeaa5d586c9554
  summary: >-
    You'll prepare a Linux development environment and plan your application migration to Arm servers.
    First, you'll review GCC and Clang choices for C and C++, Java installation options and Java Virtual Machine (JVM) flags, and
    supported Go toolchain versions. Then, you'll analyze dependencies and consult ecosystem resources
    for independent software vendor and library support. With these checks, you can evaluate build readiness,
    adjust toolchain or runtime choices, and identify gaps before moving your workload.
  faqs:
  - question: Which Arm environment should I use for my development machine?
    answer: >-
      Use an Arm-based instance from a cloud service provider. A virtual machine such as Multipass
      also works for exploration and experimentation.
  - question: How do I choose the right GCC or Clang version for C and C++ on Arm?
    answer: >-
      Check the compiler version table and choose the latest version available for your Linux
      distribution. If the table lists a newer version than the starred default, install the newer
      version.
  - question: What should I review in my Java setup when migrating to Arm?
    answer: >-
      Install Java using the [Java install guide](/install-guides/java/) for your distribution. Review JVM flags
      that impact performance and tune them for your application.
  - question: Which Go version should I install for building on Arm?
    answer: >-
      Install the latest Go toolchain available for your system. Use Go 1.18 or newer and follow
      the [Go install guide](/install-guides/go/).
  - question: How can I confirm whether my dependencies or ISV software support Arm?
    answer: >-
      Check the Software Ecosystem Dashboard for Arm and the AWS Graviton technical guide. If
      an entry is missing or incomplete, open an issue in the corresponding GitHub repository.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Libraries
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Neon
    - SVE
    - Go
    - Runbook

further_reading:
    - resource:
        title: AWS Graviton Getting Started
        link: https://github.com/aws/aws-graviton-getting-started
        type: documentation
    - resource:
        title: AWS Graviton Processors
        link: https://dev.to/aws-builders/aws-graviton-processors-3nk3
        type: blog
    - resource:
        title: NVIDIA Getting Started with HPC on Arm64
        link: https://github.com/arm-hpc-devkit/nvidia-arm-hpc-devkit-users-guide
        type: blog
    - resource:
        title: Data points you need to know about ARM for your application code migration
        link: https://dev.to/aws-builders/data-points-you-need-to-know-about-arm-for-your-application-code-migration-5c0f
        type: blog
    - resource:
        title: Making your Go workloads up to 20% faster with Go 1.18 and AWS Graviton
        link: https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
