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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:48:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f36b1e9a45b6ec29d8041b70997550d917322cf9cdd456db26083169d21175ed
  summary_generated_at: '2026-06-02T03:44:25Z'
  summary_source_hash: f36b1e9a45b6ec29d8041b70997550d917322cf9cdd456db26083169d21175ed
  faq_generated_at: '2026-06-03T00:48:02Z'
  faq_source_hash: f36b1e9a45b6ec29d8041b70997550d917322cf9cdd456db26083169d21175ed
  summary: >-
    This Learning Path shows how to deploy Envoy Proxy on Google Cloud Axion C4A Arm64 virtual
    machines built on Arm Neoverse V2 cores, then validate and benchmark it. You will provision
    a c4a-standard-4 instance (4 vCPUs, 16 GB) in the Google Cloud Console, install Envoy v1.30.0
    on RHEL 9 using the official static Arm64 binary, and run a minimal configuration that forwards
    traffic to httpbin.org to verify a 200 OK response on port 10000. You will also build and
    use Siege to generate HTTP load and record availability, throughput, response time, and failure
    rates, comparing results on Arm64 (AArch64) and x86_64. Prerequisites include a GCP account
    with billing enabled and familiarity with networking and Envoy architecture.
  faqs:
  - question: What do I need before provisioning the C4A VM on GCP?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, plus familiarity with networking
      concepts and the Envoy architecture. For general GCP setup assistance, see the Learning
      Path Getting started with Google Cloud Platform.
  - question: Which C4A machine type is used, and where do I create it?
    answer: >-
      The path uses c4a-standard-4 (4 vCPUs, 16 GB memory). Create it in the Google Cloud Console
      under Compute Engine > VM instances by selecting Create instance and choosing the C4A machine
      type.
  - question: What Envoy build is installed on the C4A instance?
    answer: >-
      Envoy Proxy v1.30.0 is installed on RHEL 9 using the official static Arm64 (AArch64) binary.
      You install required dependencies and then download the binary with curl to /usr/local/bin/envoy.
  - question: How do I validate Envoy after installation, and what result should I expect?
    answer: >-
      Create a minimal Envoy configuration, start Envoy with it, and issue a request using curl.
      Envoy should listen on port 10000, forward requests to httpbin.org, and return a 200 OK
      response.
  - question: How do I run the benchmarks and what metrics does Siege report?
    answer: >-
      Build Siege from source after installing Development Tools, then run load tests against
      Envoy. Siege reports availability, throughput, response time, and failure rates; repeat
      the same procedure on Arm64 and x86_64 to compare results.
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

