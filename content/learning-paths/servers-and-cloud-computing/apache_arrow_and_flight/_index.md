---
title: Deploy High-Performance Analytics with Apache Arrow and Arrow Flight on Google Cloud C4A Axion processors
description: Learn how to deploy Apache Arrow and Arrow Flight on Google Cloud Axion C4A processors for high-throughput columnar data processing and low-latency data transport with MinIO integration.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for data engineers, platform engineers, and developers who aim to build high-performance analytics pipelines on Arm64-based Google Cloud C4A Axion processors using Apache Arrow and Arrow Flight.

learning_objectives:
 - Deploy Apache Arrow–based data processing workloads on Google Cloud C4A Axion processors
 - Set up and run an Arrow Flight server for high-throughput, low-latency data transport
 - Read and write columnar data formats such as Parquet and ORC using Apache Arrow
 - Integrate Arrow with object storage (MinIO) for cloud-native analytics workflows
 - Validate performance benefits of Arrow and Arrow Flight on Arm-based infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python
  - Basic understanding of data formats such as Parquet or ORC
  - Familiarity with Linux command-line operations

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:22:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  summary_generated_at: '2026-06-26T17:22:13Z'
  summary_source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  faq_generated_at: '2026-06-26T17:22:13Z'
  faq_source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  summary: >-
    You'll set up a single-node analytics stack on Google Cloud C4A virtual machines powered by Google Axion processors. First, you'll provision an `arm64` C4A instance, configure
    Google Cloud firewall rules for MinIO and Arrow Flight, and prepare a SUSE Linux Enterprise
    Server environment with Apache Arrow. Then, you'll integrate MinIO object storage and use Apache Arrow
    to read and write Parquet and ORC datasets, highlighting predicate pushdown and column pruning
    in a practical workflow. By the end, you'll have a working setup that serves and moves columnar
    data with Arrow Flight and validates end-to-end data access using Arrow with MinIO on Arm-based
    infrastructure.
  faqs:
  - question: Which Google Cloud instance and OS image should I choose for this setup?
    answer: >-
      Use a Google Axion C4A `arm64` virtual machine; the steps use `c4a-standard-4` (4 vCPUs, 16 GB).
      Select an `arm64` SUSE Linux Enterprise Server image as shown in the Learning Path.
  - question: Which network ports must be opened for the stack to work?
    answer: >-
      Open the ports listed in the firewall step, including MinIO’s S3 API on port 9000 and the
      Arrow Flight port specified there. After creating the rule, confirm that inbound connections
      to those services succeed from allowed sources.
  - question: How do I confirm MinIO is ready before running Arrow jobs?
    answer: >-
      Verify the MinIO service is running and accessible on the configured port (including 9000
      for the S3 API). Follow the Learning Path instructions to store a test object and read it back
      to validate access.
  - question: What result should I expect when testing predicate pushdown and column pruning with
      Arrow?
    answer: >-
      Operations should return only the filtered rows and the selected columns from Parquet or
      ORC. If unfiltered rows or extra columns appear, review the dataset, filter, and projection
      arguments used in the example.
  - question: How do I know the Arrow Flight server is reachable from a client?
    answer: >-
      Use the address and port from the steps. The client should connect and list or fetch data
      without errors. Connection timeouts or refusals usually indicate a missing firewall rule
      or a server that's not running.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers: 
- Google Cloud

armips:
- Neoverse

tools_software_languages:
- Apache Arrow
- Arrow Flight
- Python
- MinIO

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
      title: Apache Arrow documentation
      link: https://arrow.apache.org/docs/
      type: documentation

  - resource:
      title: Arrow Flight documentation
      link: https://arrow.apache.org/docs/format/Flight.html
      type: documentation

  - resource:
      title: Apache Parquet documentation
      link: https://parquet.apache.org/documentation/latest/
      type: documentation

  - resource:
      title: MinIO documentation
      link: https://min.io/docs
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
