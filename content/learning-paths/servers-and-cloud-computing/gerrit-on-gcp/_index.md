---
title: Deploy Gerrit on a Google Cloud C4A instance 

description: Deploy Gerrit on an Ubuntu 24.04 arm64 Google Cloud C4A virtual machine powered by Google Axion processors, verify web access, and benchmark baseline performance.
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying Gerrit in Arm Linux environments, specifically using Google Cloud C4A virtual machines (VM) powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based Ubuntu 24.04 LTS virtual machine on Google Cloud (C4A with Axion processors)
  - Install Gerrit Server on the Ubuntu arm64 (C4A) instance
  - Verify Gerrit deployment by accessing the web console
  - Benchmark Gerrit by measuring operations per second (ops/sec), memory utilization, and disk performance on the Arm platform

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [Gerrit](https://gerrit-review.googlesource.com/Documentation/intro-gerrit-walkthrough-github.html)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-29T15:40:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7b4d6c5bb04f6ab123243d184e404c074a68440084fd8b9100b2536db2e56a46
  summary_generated_at: '2026-06-29T15:40:39Z'
  summary_source_hash: 7b4d6c5bb04f6ab123243d184e404c074a68440084fd8b9100b2536db2e56a46
  faq_generated_at: '2026-06-29T15:40:39Z'
  faq_source_hash: 7b4d6c5bb04f6ab123243d184e404c074a68440084fd8b9100b2536db2e56a46
  summary: >-
    You'll deploy Gerrit on an Ubuntu 24.04 LTS `arm64` virtual
    machine (VM) in Google Cloud using the C4A instance family powered by Google Axion processors (Arm
    Neoverse-V2). First, you'll enable external access by creating a Google Cloud firewall
    rule for TCP port 8080. Then, you'll provision a `c4a-standard-4` VM, and install Gerrit with the required
    packages. You'll confirm a successful setup by loading the Gerrit web console, then establish
    a baseline by running a benchmarking script that exercises common Gerrit operations.
    The result is a functional Arm-based Gerrit deployment on Google Cloud with initial performance
    data suitable for comparison and follow-up analysis.
  faqs:
  - question: Which Google Cloud port must be open to access the Gerrit web console?
    answer: >-
      Open TCP port `8080`. Create a firewall rule in the Google Cloud console to allow incoming
      traffic on port `8080` so the Gerrit web interface is reachable.
  - question: What virtual machine configuration should I use for this deployment?
    answer: >-
      Use a Google Axion C4A instance with the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory).
      The VM runs Ubuntu 24.04 LTS on arm64.
  - question: What packages should I install before setting up Gerrit?
    answer: >-
      Update the system and install `wget`, `default-jdk`, `git`, and `net-tools`. The steps show running
      apt update and apt upgrade before installing these tools.
  - question: How do I verify that Gerrit is running after installation?
    answer: >-
      Confirm that the Gerrit web console loads on port `8080` after completing the install steps.
      If it doesn't load, review the command outputs from the installation for errors.
  - question: How do I run the benchmark and what should I expect?
    answer: >-
      Clone the `gerrit_test` repository into your VM and run the provided script with `SYNTH_PROFILE=production_like`
      and `REQUIRE_GERRIT_METRICS=true`. The script exercises Gerrit functions and captures timing
      and performance data for baseline measurement.
# END generated_summary_faq

author: Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Gerrit

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation for C4A VMs
      link: https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series
      type: documentation

  - resource:
      title: Gerrit documentation
      link: https://gerrit-review.googlesource.com/Documentation/
      type: documentation

  - resource:
      title: Getting started with Google Cloud Platform
      link: /learning-paths/servers-and-cloud-computing/csp/google/
      type: website

  - resource:
      title: Gerrit 3.14 release notes
      link: https://www.gerritcodereview.com/3.14.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

