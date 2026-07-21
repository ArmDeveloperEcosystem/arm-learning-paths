---
title: Tune PostgreSQL performance on Arm-based platforms
description: Learn how to tune PostgreSQL configuration, Linux memory settings, and storage options to improve database performance on Arm-based platforms.

minutes_to_complete: 150

who_is_this_for: This Learning Path is for database administrators (DBAs) and software developers who want to optimize PostgreSQL performance on Arm-based platforms.

learning_objectives:
    - Configure PostgreSQL settings that affect connection handling, memory use, write-ahead logging, query planning, and concurrency.
    - Enable huge pages for PostgreSQL and size them for the shared memory area.
    - Evaluate storage, kernel, compiler, and library choices that can affect PostgreSQL performance.

prerequisites:
    - On-prem or cloud [installation of PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql/)
    - A repeatable PostgreSQL workload or benchmark that you can run before and after tuning

author: Julio Suarez

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

test_images:
    - ubuntu:latest
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Databases
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
    - SQL
    - PostgreSQL
    - HammerDB
    - Runbook

further_reading:
    - resource:
        title: PostgreSQL documentation
        link: https://www.postgresql.org/docs/current/
        type: documentation
    - resource:
        title: PostgreSQL resource consumption settings
        link: https://www.postgresql.org/docs/current/runtime-config-resource.html
        type: documentation
    - resource:
        title: PostgreSQL write-ahead log settings
        link: https://www.postgresql.org/docs/current/runtime-config-wal.html
        type: documentation
    - resource:
        title: Linux HugeTLBpage documentation
        link: https://docs.kernel.org/admin-guide/mm/hugetlbpage.html
        type: documentation
    - resource:
        title: Migrating applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
