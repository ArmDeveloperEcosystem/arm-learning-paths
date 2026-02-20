---
title: Deploy a live sensor dashboard with TimescaleDB and Grafana on Google Cloud C4A

draft: true
cascade:
    draft: true
    
minutes_to_complete: 45

who_is_this_for: This learning path is for DevOps engineers, database engineers, and software developers who want to deploy and operate TimescaleDB on SUSE Linux Enterprise Server (SLES) Arm64, ingest live time-series sensor data, and visualize it in Grafana.

learning_objectives:
  - Install and configure TimescaleDB on Google Cloud C4A Axion processors by building from source for Arm64
  - Create a real-time sensor data ingestion pipeline using Python with hypertables, continuous aggregates, and retention policies
  - Build a live sensor dashboard with Grafana that automatically refreshes to display time-series data
  - Validate end-to-end data flow from ingestion through TimescaleDB to Grafana visualization

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with SQL, Python, and Grafana

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

TimescaleDB is a high-performance, open-source time-series database built on PostgreSQL that provides powerful features for storing, querying, and analyzing time-series data efficiently. When you deploy TimescaleDB on Google Cloud C4A Axion Arm-based processors, you can achieve high-throughput time-series ingestion and query processing with optimized performance per watt and lower infrastructure costs. This Learning Path shows you how to build a complete time-series data pipeline with live sensor ingestion and real-time visualization using Grafana.

