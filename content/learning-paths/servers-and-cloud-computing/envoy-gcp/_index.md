---
title:  Deploy Envoy Proxy on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Envoy proxy on Google Cloud Axion C4A Arm64 instances and benchmark HTTP proxy performance with load testing.

minutes_to_complete: 30

who_is_this_for: This introductory topic for software developers migrating Envoy Proxy workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines (VMs) built on Axion processors.

learning_objectives:
  - Provision an Arm-based C4A VM on Google Cloud Platform (GCP) 
  - Install and configure Envoy Proxy on a C4A instance
  - Validate Envoy functionality with baseline tests
  - Benchmark Envoy performance on both Arm64 (AArch64) and x86_64 architectures

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - Familiarity with networking concepts and the [Envoy architecture](https://www.envoyproxy.io/docs/envoy/latest/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:18:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b8a1d2b9e2692a7041e10223b73bc6513748f64f24c0601ab6a778323c6d410c
  summary_generated_at: '2026-08-12T20:18:28Z'
  summary_source_hash: b8a1d2b9e2692a7041e10223b73bc6513748f64f24c0601ab6a778323c6d410c
  faq_generated_at: '2026-08-12T20:18:28Z'
  faq_source_hash: b8a1d2b9e2692a7041e10223b73bc6513748f64f24c0601ab6a778323c6d410c
  summary: >-
    You'll deploy and benchmark Envoy Proxy on a Google Cloud Axion C4A VM running
    RHEL 9. First, you'll install the static Arm64 binary, configure a listener that forwards to
    `httpbin.org`, and verify responses on port `10000`. Then, you'll build and run Siege to measure
    availability, throughput, response time, and failures.
  faqs:
  - question: Which Google Cloud machine type should I choose for the example VM?
    answer: >-
      Use the C4A family with the `c4a-standard-4` machine type (four vCPUs, 16 GB memory).
  - question: How do I verify that Envoy installed correctly on the C4A VM?
    answer: >-
      Follow the verification step after installing the official static Arm64 binary to confirm
      it's present and executable. You should be able to start Envoy with the provided minimal
      configuration before continuing.
  - question: What result should I expect from the baseline Envoy test?
    answer: >-
      Requests to the listener on port `10000` should be proxied to `httpbin.org` and return HTTP
      `200 OK`. The response confirms the listener is active and routing works as configured.
  - question: When I run Siege, which endpoint should I target?
    answer: >-
      Target the Envoy listener defined in your configuration, typically the VM’s address on port
      `10000` or `localhost:10000`. Keep the same target across runs to compare results consistently.
  - question: How do I compare results between Arm64 C4A and x86_64?
    answer: >-
      Use the same Envoy version, configuration, and Siege workload on both instance types. Compare
      throughput, response time, availability, and failure rates reported by Siege.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Web
platforms:
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
