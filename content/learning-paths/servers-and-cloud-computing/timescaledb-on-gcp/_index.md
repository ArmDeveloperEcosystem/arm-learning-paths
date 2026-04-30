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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: edf5bebb0440c110723c87ca27e5f4b21e4da588e4208b5391f7091ae93cb73d
  summary: >-
    Deploy a live sensor dashboard with TimescaleDB and Grafana on Google Cloud C4A walks you
    through an end-to-end Arm software workflow. It is designed for DevOps engineers, database
    engineers, and software developers who want to deploy and operate TimescaleDB on SUSE Linux
    Enterprise Server (SLES) Arm64, ingest live time-series sensor data, and visualize it in Grafana.
    By the end, you will be able to install and configure TimescaleDB on Google Cloud C4A Axion
    processors by building from source for Arm64, create a real-time sensor data ingestion pipeline
    using Python with hypertables, continuous aggregates, and retention policies, and build a
    live sensor dashboard with Grafana that automatically refreshes to display time-series data.
    It focuses on tools and technologies such as TimescaleDB, PostgreSQL, Python, Grafana, and
    psycopg2, Linux environments, Arm platforms including Neoverse, and cloud platforms such as
    Google Cloud. The main steps cover Get started with TimescaleDB on Google Axion C4A, Create
    a firewall rule for Grafana/TimescaleDB, Create a Google Axion C4A Arm virtual machine on
    GCP, Set up TimescaleDB on Arm64, and Ingest real-time sensor data on Arm64.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install and configure TimescaleDB on Google Cloud C4A Axion processors by building
      from source for Arm64, create a real-time sensor data ingestion pipeline using Python with
      hypertables, continuous aggregates, and retention policies, and build a live sensor dashboard
      with Grafana that automatically refreshes to display time-series data.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for DevOps engineers, database engineers, and software developers
      who want to deploy and operate TimescaleDB on SUSE Linux Enterprise Server (SLES) Arm64,
      ingest live time-series sensor data, and visualize it in Grafana.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with SQL, Python, and Grafana.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including TimescaleDB, PostgreSQL, Python, Grafana, and psycopg2,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with TimescaleDB on Google Axion C4A,
      Create a firewall rule for Grafana/TimescaleDB, Create a Google Axion C4A Arm virtual machine
      on GCP, Set up TimescaleDB on Arm64, and Ingest real-time sensor data on Arm64.
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

