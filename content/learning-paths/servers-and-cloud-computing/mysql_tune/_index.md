---
title: Tune MySQL performance on Arm-based platforms
description: Learn how to tune MySQL configuration, Linux memory settings, and storage options to improve database performance on Arm-based platforms.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for database administrators (DBAs) and software developers who want to optimize MySQL performance on Arm-based platforms.

learning_objectives:
    - Configure MySQL settings that affect connection handling, memory usage, disk flush behavior, and concurrency.
    - Enable huge pages for MySQL and size them based on the InnoDB buffer pool.
    - Evaluate storage, kernel, compiler, and library choices that can affect MySQL performance.

prerequisites:
    - On-prem or cloud [installation of MySQL](https://dev.mysql.com/doc/refman/en/)
    - A repeatable MySQL workload or benchmark that you can run before and after tuning

author: Julio Suarez

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

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
    - MySQL
    - InnoDB
    - Runbook

test_images:
    - ubuntu:latest
test_link: null
test_maintenance: true

further_reading:
    - resource:
        title: MySQL Reference Manual
        link: https://dev.mysql.com/doc/refman/en/
        type: documentation
    - resource:
        title: InnoDB configuration parameters
        link: https://dev.mysql.com/doc/refman/en/innodb-parameters.html
        type: documentation
    - resource:
        title: Optimizing InnoDB disk I/O
        link: https://dev.mysql.com/doc/refman/en/optimizing-innodb-diskio.html
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
weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
