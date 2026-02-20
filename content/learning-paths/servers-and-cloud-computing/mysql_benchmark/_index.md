---
title: Benchmarking MySQL with Sysbench

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for performance engineers who want to benchmark MySQL using Sysbench and optimize performance on Arm Linux systems.

learning_objectives:
    - Run Sysbench to benchmark a MySQL database server
    - Enable profile-guided optimization (PGO) for MySQL and examine the performance improvements

prerequisites:
    - Basic knowledge of [MySQL databases](https://www.mysql.com/)
    - Two Arm servers running Ubuntu 22.04, one for the MySQL server and the other for the Sysbench client

author: Bolt Liu

skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - MySQL
    - Sysbench

test_images:
    - ubuntu:22.04
test_link: null
test_maintenance: false

further_reading:
    - resource:
        title: MySQL documentation
        link: https://www.mysql.com/
        type: documentation
    - resource:
        title: Running MySQL on ARM
        link: https://mysqlonarm.github.io/Running-MySQL-on-ARM/
        type: documentation
    - resource:
        title: Learn how to deploy MySQL
        link: /learning-paths/servers-and-cloud-computing/mysql/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
