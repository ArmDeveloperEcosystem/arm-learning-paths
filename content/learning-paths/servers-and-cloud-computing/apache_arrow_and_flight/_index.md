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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:15:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  summary_generated_at: '2026-06-02T03:04:20Z'
  summary_source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  faq_generated_at: '2026-06-03T00:15:38Z'
  faq_source_hash: 90b638385267e085ea07a70a1c23f16578aa3caaeabeca1f651bcdcac5bf38fb
  summary: >-
    This Learning Path shows how to deploy Apache Arrow and Arrow Flight on Arm-based Google Cloud
    C4A Axion instances for high-throughput columnar analytics and low-latency data transport.
    You will provision a c4a-standard-4 arm64 VM running Linux (SUSE Linux Enterprise Server),
    configure Google Cloud firewall rules for MinIO and Arrow Flight, install Arrow and MinIO,
    and assemble a single-node analytics stack. Using Python, you will read and write Parquet
    and ORC datasets stored in MinIO and explore predicate pushdown and column pruning. The path
    also integrates Arrow Flight and includes guidance to validate performance benefits on Arm-based
    infrastructure. Prerequisites include a GCP account with billing enabled and basic familiarity
    with Python, Parquet/ORC, and the Linux command line.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled, basic familiarity with
      Python, a basic understanding of Parquet or ORC, and comfort with Linux command-line operations.
      No other prerequisites are explicitly listed.
  - question: Which Google Cloud machine type and operating system are used?
    answer: >-
      You will create an Axion C4A arm64 virtual machine using the c4a-standard-4 type, which
      provides 4 vCPUs and 16 GB of memory. The environment is based on SUSE Linux Enterprise
      Server (SLES) for arm64.
  - question: Which firewall ports should I open for MinIO and Arrow Flight?
    answer: >-
      Open port 9000 for the MinIO S3 API as listed in the path. Additional ports for the MinIO
      Web UI and Arrow Flight are required; follow the port list provided in the firewall setup
      step.
  - question: How is MinIO used, and how does Apache Arrow access data?
    answer: >-
      MinIO provides S3-compatible object storage for analytical datasets. Apache Arrow uses its
      Dataset API to read and write Parquet and ORC files stored in MinIO.
  - question: What result should I expect after the analysis and Arrow Flight steps, and how can
      I validate success?
    answer: >-
      You should be able to store datasets in MinIO and use Apache Arrow to read and write Parquet
      and ORC while exploring predicate pushdown and column pruning. You also set up and run an
      Arrow Flight server for low-latency data transport, with access allowed by your firewall
      rules. The path includes validation of performance benefits on Arm-based C4A, but it does
      not provide specific metrics.
# END generated_summary_faq

author: Pareena Verma

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

