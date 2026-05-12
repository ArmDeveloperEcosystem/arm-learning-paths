---
title:  Deploy Node.js on Google Cloud C4A Arm-based Axion VMs



minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Node.js workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server virtual machine on Google Cloud C4A instances with Axion processors
  - Install and configure Node.js on a SUSE Arm64 (C4A) instance
  - Validate Node.js functionality with baseline HTTP server tests
  - Benchmark Node.js performance using Autocannon on Arm64 (AArch64) architecture 


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with networking concepts and [Node.js event-driven architecture](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 800eed835763098d4b369789d10de642bbdbaa390e8bfe0cb6ea2c4c78f7ecbd
  summary: >-
    Deploy Node.js on Google Cloud C4A Arm-based Axion VMs walks you through an end-to-end Arm
    software workflow. It is designed for software developers migrating Node.js workloads from
    x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion
    processors. By the end, you will be able to provision an Arm-based SUSE Linux Enterprise Server
    virtual machine on Google Cloud C4A instances with Axion processors, install and configure
    Node.js on a SUSE Arm64 (C4A) instance, and validate Node.js functionality with baseline HTTP
    server tests. It focuses on tools and technologies such as Node.js, npm, and Autocannon, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as Google Cloud.
    The main steps cover Getting started with Node.js on Google Axion C4A (Arm Neoverse-V2), Create
    a Google Axion C4A Arm virtual machine on GCP, Install Node.js using Node Version Manager,
    Validate Node.js baseline on Google Axion C4A Arm virtual machine, and Benchmark Node.js performance
    with Autocannon.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server virtual machine on Google Cloud
      C4A instances with Axion processors, install and configure Node.js on a SUSE Arm64 (C4A)
      instance, and validate Node.js functionality with baseline HTTP server tests.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers migrating Node.js workloads from x86_64
      to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Familiarity with networking concepts and [Node.js event-driven
      architecture](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Node.js, npm, and Autocannon, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Getting started with Node.js on Google Axion C4A (Arm
      Neoverse-V2), Create a Google Axion C4A Arm virtual machine on GCP, Install Node.js using
      Node Version Manager, Validate Node.js baseline on Google Axion C4A Arm virtual machine,
      and Benchmark Node.js performance with Autocannon.
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
  - Node.js
  - npm
  - Autocannon

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
      title: Node.js documentation
      link: https://nodejs.org/en
      type: documentation

  - resource:
      title: Autocannon documentation
      link: https://www.npmjs.com/package/autocannon/v/5.0.0
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

