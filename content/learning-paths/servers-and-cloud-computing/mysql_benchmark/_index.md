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

author_primary: Bolt Liu

skilllevels: introductory
subjects: Databases
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
test_status:
    - passed

weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
