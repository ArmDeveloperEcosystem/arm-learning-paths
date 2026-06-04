---
title: Deploy a live sensor dashboard with TimescaleDB and Grafana on Google Cloud C4A
    
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for DevOps engineers, database engineers, and software developers who want to deploy and operate TimescaleDB on SUSE Linux Enterprise Server (SLES) Arm64, ingest live time-series sensor data, and visualize it in Grafana.

learning_objectives:
  - Install and configure TimescaleDB on Google Cloud C4A Axion processors by building from source for Arm64
  - Create a real-time sensor data ingestion pipeline using Python with hypertables, continuous aggregates, and retention policies
  - Build a live sensor dashboard with Grafana that automatically refreshes to display time-series data
  - Validate end-to-end data flow from ingestion through TimescaleDB to Grafana visualization

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with SQL, Python, and Grafana

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:10:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: edf5bebb0440c110723c87ca27e5f4b21e4da588e4208b5391f7091ae93cb73d
  summary_generated_at: '2026-06-02T05:18:38Z'
  summary_source_hash: edf5bebb0440c110723c87ca27e5f4b21e4da588e4208b5391f7091ae93cb73d
  faq_generated_at: '2026-06-03T02:10:49Z'
  faq_source_hash: edf5bebb0440c110723c87ca27e5f4b21e4da588e4208b5391f7091ae93cb73d
  summary: >-
    Deploy a live sensor dashboard on Google Cloud Axion C4A Arm instances by provisioning a c4a-standard-4
    VM running SUSE Linux Enterprise Server (SLES) Arm64, building PostgreSQL 15 with the TimescaleDB
    2.25.0 extension from source, and configuring access for Grafana on TCP port 3000. You will
    simulate real-time sensor data with a Python script using psycopg2, create a TimescaleDB hypertable
    along with continuous aggregates and retention policies, and visualize the stream in a Grafana
    dashboard that auto-refreshes. The path concludes with validating end-to-end data flow from
    ingestion through TimescaleDB to Grafana. Prerequisites: a GCP account with billing enabled
    and basic familiarity with SQL, Python, and Grafana.
  faqs:
  - question: What do I need before provisioning the VM on Google Cloud?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Basic familiarity with SQL,
      Python, and Grafana is expected.
  - question: Which Google Cloud VM and operating system are used in this path?
    answer: >-
      You will create a c4a-standard-4 instance (4 vCPUs, 16 GB memory) on Google Axion C4A. The
      VM runs SUSE Linux Enterprise Server (SLES) on Arm64.
  - question: Why does the path build TimescaleDB from source on Arm64, and which versions are
      used?
    answer: >-
      Building from source ensures the TimescaleDB extension is fully optimized for Arm64. The
      environment uses PostgreSQL 15 with the TimescaleDB 2.25.0 extension.
  - question: Which firewall port should I open, and what is it for?
    answer: >-
      Open TCP port 3000 in a Google Cloud VPC firewall rule. This exposes the Grafana interface
      used to view the time-series dashboards.
  - question: How do I know the ingestion and visualization are working?
    answer: >-
      The Python sensor script (using psycopg2) continuously writes readings into a TimescaleDB
      hypertable, and Grafana automatically refreshes to display the data. Successful completion
      shows end-to-end flow from ingestion through TimescaleDB to Grafana visualization.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - TimescaleDB
  - PostgreSQL
  - Python
  - Grafana
  - psycopg2

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: TimescaleDB official documentation
      link: https://docs.timescale.com/
      type: documentation

  - resource:
      title: PostgreSQL 15 documentation
      link: https://www.postgresql.org/docs/15/index.html
      type: documentation

  - resource:
      title: Grafana documentation
      link: https://grafana.com/docs/grafana/latest/
      type: documentation

  - resource:
      title: Python psycopg2 documentation
      link: https://www.psycopg.org/docs/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---

