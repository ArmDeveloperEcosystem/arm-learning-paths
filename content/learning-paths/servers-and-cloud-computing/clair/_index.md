---
title: Use Clair to scan container images and generate vulnerability reports
description: Learn how to install and run Clair on Arm servers using combined and distributed deployment models to scan container images and generate vulnerability reports.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in scanning container images for vulnerabilities on Arm servers.

learning_objectives:
    - Install Clair on an Arm server
    - Run Clair using combined and distributed deployment models
    - Submit container images using the Clair CLI (command-line interface) and generate vulnerability reports

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an Arm server with recent versions of Docker and Go installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:46:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  summary_generated_at: '2026-06-30T21:46:01Z'
  summary_source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  faq_generated_at: '2026-06-30T21:46:01Z'
  faq_source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  summary: >-
    You'll install and run Clair on Arm-based Linux servers using both
    combined and distributed deployment models. First, you'll set up the combined deployment to run
    all services in a single process, then explore the distributed option where the indexer, matcher,
    and notifier operate as separate services. With Clair running, you'll submit a container image manifest using `clairctl` to perform static analysis and generate a vulnerability report.
    You'll learn about timing considerations — allowing initial vulnerability data to populate
    the PostgreSQL database — so reports reflect current findings. By the end, you'll launch Clair,
    select a deployment model, and produce a report for a chosen image.
  faqs:
  - question: Which deployment model should I start with?
    answer: >-
      The combined deployment runs all Clair services in a single OS process and is the easiest
      to configure. The distributed deployment runs the indexer, matcher, and notifier as separate
      services.
  - question: How do I know Clair is ready before submitting a manifest?
    answer: >-
      Wait 5–10 minutes after starting Clair for vulnerabilities to populate in the PostgreSQL
      database. Submitting too soon can return a clean report even when issues exist. If that
      happens, wait and resubmit.
  - question: What do I submit to Clair to scan an image?
    answer: >-
      Submit the image’s manifest to your running Clair deployment using clairctl. The CLI sends
      the request and returns a vulnerability report when analysis completes.
  - question: In a distributed deployment, which services run separately?
    answer: >-
      The indexer, matcher, and notifier run as separate services in a distributed setup. The
      indexer retrieves image layers, scans them, and generates an intermediate IndexReport.
  - question: Does Clair run the container image during analysis?
    answer: >-
      No. Clair performs static analysis of container images without running them.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Docker
    - Go 
    - Clair

further_reading:
    - resource:
        title: Clair Manual
        link: https://quay.github.io/clair/
        type: documentation
    - resource:
        title: Amazon EC2 C7g Instances powered by AWS Graviton3 processors
        link: https://aws.amazon.com/blogs/aws/new-amazon-ec2-c7g-instances-powered-by-aws-graviton3-processors/
        type: Blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

