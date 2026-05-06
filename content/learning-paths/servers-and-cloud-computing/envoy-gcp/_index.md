---
title:  Deploy Envoy Proxy on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Envoy proxy on Google Cloud Axion C4A Arm64 instances and benchmark HTTP proxy performance with load testing.

minutes_to_complete: 30

who_is_this_for: This introductory topic for software developers migrating Envoy Proxy workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based C4A VM on Google Cloud Platform (GCP) 
  - Install and configure Envoy Proxy on a C4A instance
  - Validate Envoy functionality with baseline tests
  - Benchmark Envoy performance on both Arm64 (AArch64) and x86_64 architectures

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with networking concepts and the [Envoy architecture](https://www.envoyproxy.io/docs/envoy/latest/)

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: f36b1e9a45b6ec29d8041b70997550d917322cf9cdd456db26083169d21175ed
  summary: >-
    Learn how to install and configure Envoy proxy on Google Cloud Axion C4A Arm64 instances and
    benchmark HTTP proxy performance with load testing. It is designed for This introductory topic
    for software developers migrating Envoy Proxy workloads from x86_64 to Arm-based servers,
    specifically on Google Cloud C4A virtual machines built on Axion processors. By the end, you
    will be able to provision an Arm-based C4A VM on Google Cloud Platform (GCP), install and
    configure Envoy Proxy on a C4A instance, and validate Envoy functionality with baseline tests.
    It focuses on tools and technologies such as Envoy, Siege, Networking, and Service Mesh, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as Google Cloud.
    The main steps cover Get started with Envoy Proxy on Google Axion C4A (Arm Neoverse V2), Create
    a Google Axion C4A Arm virtual machine on GCP, Deploy Envoy on Google Axion C4A Arm virtual
    machines, Run baseline Envoy testing on a Google Axion C4A Arm VM, and Benchmark Envoy on
    Google Cloud for Arm64 and x86_64 with Siege.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based C4A VM on Google Cloud Platform (GCP), install and configure
      Envoy Proxy on a C4A instance, and validate Envoy functionality with baseline tests. Learn
      how to install and configure Envoy proxy on Google Cloud Axion C4A Arm64 instances and benchmark
      HTTP proxy performance with load testing.
  - question: Who is this Learning Path for?
    answer: >-
      This introductory topic for software developers migrating Envoy Proxy workloads from x86_64
      to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en)
      account with billing enabled; Familiarity with networking concepts and the [Envoy architecture](https://www.envoyproxy.io/docs/envoy/latest/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Envoy, Siege, Networking, and Service Mesh, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Envoy Proxy on Google Axion C4A (Arm
      Neoverse V2), Create a Google Axion C4A Arm virtual machine on GCP, Deploy Envoy on Google
      Axion C4A Arm virtual machines, Run baseline Envoy testing on a Google Axion C4A Arm VM,
      and Benchmark Envoy on Google Cloud for Arm64 and x86_64 with Siege.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Envoy
  - Siege
  - Networking
  - Service Mesh

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Envoy documentation
      link: https://www.envoyproxy.io/docs/envoy/latest/about_docs
      type: documentation

  - resource:
      title: Siege documentation
      link: https://www.joedog.org/siege/manual/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

