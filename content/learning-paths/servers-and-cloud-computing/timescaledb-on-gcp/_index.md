---
title: Deploy TimescaleDB Live Sensor Dashboard on SUSE Arm64

minutes_to_complete: 45

who_is_this_for: This learning path is designed for DevOps engineers, database engineers, and software developers who want to deploy and operate TimescaleDB on SUSE Linux Enterprise Server (SLES) Arm64, ingest live time-series sensor data, and visualize it in Grafana.

learning_objectives:
  - Provision a SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud C4A Arm-based Axion processors
  - Install PostgreSQL 15 and build TimescaleDB from source for Arm64
  - Initialize and configure TimescaleDB for time-series workloads
  - Ingest live sensor data using Python with `psycopg2` (SUSE package)
  - Create hypertables, continuous aggregates, retention policies, and indexes in TimescaleDB
  - Install Grafana on SUSE Arm64
  - Configure PostgreSQL (TimescaleDB) as a Grafana data source
  - Build a live sensor dashboard with automatic refresh
  - Validate end-to-end data flow from ingestion → TimescaleDB → Grafana visualization
  - Apply basic production hardening for TimescaleDB and Grafana users

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with SQL, Python, and Grafana

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Google Cloud

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
