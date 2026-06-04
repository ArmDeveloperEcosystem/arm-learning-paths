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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:33:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  summary_generated_at: '2026-06-02T03:23:30Z'
  summary_source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  faq_generated_at: '2026-06-03T00:33:54Z'
  faq_source_hash: e742eb44fa108bfcc4ee5a241414e6aa05e1fc0e1cceb589fb78a080f59b0d38
  summary: >-
    This Learning Path shows how to install and run Clair on Arm-based Linux servers to scan container
    images and generate vulnerability reports. You will deploy Clair using both combined (single-process)
    and distributed (separate indexer, matcher, notifier) models, then use the clairctl CLI to
    submit image manifests for static analysis. The path targets advanced developers working with
    containers on Arm infrastructure, including Arm instances from major cloud providers. Prerequisites
    are an Arm server or cloud instance running Linux with recent versions of Docker and Go installed;
    the instructions are tested on Ubuntu. By the end, you will have a running Clair deployment
    and can produce vulnerability reports from your images.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm-based instance from a cloud provider or an Arm server running Linux, with recent
      versions of Docker and Go installed. The instructions are tested on Ubuntu; other Linux
      distributions may require adjustments.
  - question: Which Clair deployment model should I use?
    answer: >-
      Use the combined deployment if you want the simplest setup, as all Clair components run
      in a single process. Choose the distributed deployment if you want to run the indexer, matcher,
      and notifier as separate services.
  - question: How do I know when Clair is ready to scan images?
    answer: >-
      Wait 5–10 minutes after starting Clair before submitting manifests so vulnerabilities can
      populate in the PostgreSQL database. Submitting too early can produce a clean (empty) report.
  - question: How do I submit a container image for scanning?
    answer: >-
      With Clair running (combined or distributed), use clairctl to submit a manifest to your
      deployment. The Learning Path steps guide you to generate a vulnerability report from this
      submission.
  - question: What result should I expect after submitting a manifest?
    answer: >-
      Clair performs static analysis of the image layers and returns a vulnerability report. It
      does not run the container image as part of the analysis.
# END generated_summary_faq

author: Jason Andrews

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

