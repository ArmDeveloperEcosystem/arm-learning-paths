---
title: Deploy MySQL on an Arm-based Linux server
description: Deploy MySQL with Docker on an Arm-based Linux server, create a database, and verify that it stores and retrieves data.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to deploy MySQL on Arm.

learning_objectives: 
    - Run MySQL in a container on an Arm-based Linux server.
    - Connect to MySQL, create a database, and verify that it can store and retrieve data.

prerequisites:
    - An Arm-based Linux cloud instance or on-premises server with at least 2 GiB of available memory
    - Docker Engine [installed](/install-guides/docker/docker-engine/) and running on the server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-28T18:45:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 348a89a04baaedaf9f54c699fea0f15fd66f54aac7a68d55a65cc739b822943c
  summary_generated_at: '2026-10-28T18:45:50Z'
  summary_source_hash: 348a89a04baaedaf9f54c699fea0f15fd66f54aac7a68d55a65cc739b822943c
  faq_generated_at: '2026-10-28T18:45:50Z'
  faq_source_hash: 348a89a04baaedaf9f54c699fea0f15fd66f54aac7a68d55a65cc739b822943c
  summary: >-
    You'll deploy MySQL 8.4 on an Arm-based Linux server with Docker Engine. First, you'll check the server
    architecture and Docker connection. Then, you'll start an Arm64 MySQL container with a persistent
    volume. You'll connect to the MySQL client, create a test database, and add a sample
    table. Finally, you'll insert rows into the table and verify the stored data.
  # faqs:
  # - question: How do I check that my server is ready to run the Arm64 MySQL image?
  #   answer: >-
  #     Run `uname -m` and confirm that it prints `aarch64`. Then run `docker info` to check that
  #     your Docker client can reach Docker Engine. If it can't, use the linked Docker install guide.
  # - question: How do I keep my MySQL data when I replace the container?
  #   answer: >-
  #     Create the `mysql-data` Docker volume and mount it at `/var/lib/mysql`, as shown in the
  #     `docker run` command. Your database files then remain in the volume when you replace the
  #     container.
  # - question: What should I check if `docker exec` cannot connect to the MySQL container?
  #   answer: >-
  #     Run `docker ps --filter name=mysql-arm` to check that the container is running. Check
  #     `docker logs mysql-arm` and wait for MySQL to report that it is ready for connections.
  #     Use the container name you chose if it differs from `mysql-arm`.
  # - question: How do I connect and create the sample database?
  #   answer: >-
  #     Run `docker exec -it mysql-arm mysql -uroot -p` and enter your root password. At the
  #     `mysql>` prompt, run `CREATE DATABASE arm_test;`. You can confirm its creation with
  #     `SHOW DATABASES;`.
  # - question: How do I verify that the sample table stores data?
  #   answer: >-
  #     Select `arm_test`, create the `book` table, and insert the seven sample rows. Run
  #     `SELECT * FROM book;` and confirm that the query returns seven rows.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - SQL
    - MySQL
    - Docker

further_reading:
    - resource:
        title: MySQL Manual
        link: https://dev.mysql.com/doc/refman/8.0/en/installing.html
        type: documentation
    - resource:
        title: Tune MySQL performance on Arm-based platforms
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql_tune/
        type: learning-path
    - resource:
        title: Benchmarking MySQL with Sysbench
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql_benchmark/
        type: learning-path
    - resource:
        title: Deploy MySQL on Microsoft Azure Cobalt 100 processors
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql-azure/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
